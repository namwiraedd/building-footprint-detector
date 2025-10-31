from celery import shared_task
from .models import Job
import json, os, tempfile, traceback
from django.conf import settings
from plugins import cloud_free, superres
from .utils.raster_io import tile_iterator
from .utils.inference import run_inference_on_tile
from .utils.vectorize import vectorize_masks_to_geojson

@shared_task(bind=True)
def run_detection_job(self, job_id: str, bands: str = "RGB"):
    job = Job.objects.get(id=job_id)
    job.status = "RUNNING"
    job.save()
    try:
        aoi = job.input_aoi
        date = job.reference_date.isoformat()
        # 1. Cloud-free composite (standard res)
        composite_tif = cloud_free.generate_cloud_free(aoi, date)
        # 2. Tile loop (10x10 km tiles)
        out_geojsons = []
        for tile_bbox in tile_iterator(composite_tif, tile_size_m=10000):
            sr_tile = superres.super_resolve(composite_tif, tile_bbox)
            # run inference -> produce segmentation mask path
            mask_path = run_inference_on_tile(sr_tile, settings.MODEL_PATH)
            # vectorize mask -> list of features
            features = vectorize_masks_to_geojson(mask_path, tile_bbox)
            out_geojsons.extend(features)
        # 3. merge and save GeoJSON
        out_path = os.path.join(settings.DEFAULT_OUTPUT_DIR, f"job_{job_id}.geojson")
        with open(out_path, "w") as f:
            json.dump({"type": "FeatureCollection", "features": out_geojsons}, f)
        job.output_geojson = out_path
        job.status = "DONE"
        job.save()
    except Exception as e:
        job.status = "FAILED"
        job.log += traceback.format_exc()
        job.save()
        raise
