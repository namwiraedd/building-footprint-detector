Stack summary:

-Backend: Django + Django REST Framework

-Async jobs: Celery + Redis (task queue)

-Storage: Local filesystem (S3-compatible optional), Postgres for metadata

-ML: PyTorch (model code & inference), optional TorchScript/ONNX export

-Geospatial: rasterio, GDAL, shapely, geopandas

-Vector output: GeoJSON (CRS: EPSG:4326)

-Container: Docker Compose (app, worker, redis, postgres)

-CI: GitHub Actions (pytest)


Hook points: plugins/cloud_free.py and plugins/superres.py (place your provided modules here)

# Building Footprint Detector

Automated pipeline to detect building footprints from Sentinel-2 imagery using cloud-free composites, super-resolution, and deep learning detection. Given an AOI and a reference date, the system returns a GeoJSON with detected building polygons, centroids, area (sqm) and confidence scores.

## Features
- Accept AOI (GeoJSON / WKT / KML) + reference date
- Produce cloud-free Sentinel-2 composite (adapter)
- Tile-based super-resolution (adapter)
- PyTorch-based building detection + vectorization to GeoJSON
- Async job processing via Celery + Redis
- Containerized with Docker Compose
- Extensible plugin slots for cloud-free & superres modules

## Quickstart (local dev)
1. Copy `config/example.env` → `config/.env` and edit.
2. `docker-compose up --build` (from `/docker`)
3. Create migrations and superuser:

   docs/usage.md (quick API guide)

Explain POST /api/detect/ with sample AOI and how to poll /api/detect/{job_id}. (Include sample cURL).

How to integrate your provided modules:

1. Copy your cloud-free generator module to plugins/cloud_free.py. Implement generate_cloud_free(aoi_geojson, reference_date) -> path_to_tif.

2. Copy your super-resolution module to plugins/superres.py. Implement super_resolve(input_tif, tile_bbox) -> path_to_sr_tile.

3. Ensure both modules return absolute paths accessible by Docker containers (mount host dirs).

Local dev & testing

1. cd docker && docker-compose up --build -d

2. Ensure config/.env exists (copy config/example.env and edit)

Create DB migrations:

docker exec -it building-footprint-detector_app python manage.py migrate


Run a test job: POST AOI to /api/detect/ (use Django admin or Postman)

Check Celery worker logs; output GeoJSON will appear in DEFAULT_OUTPUT_DIR

Notes, caveats & production recommendations

CRS and area calculation: area in vectorize is in raster CRS units. For correct square meters compute reproject to EPSG:3857 before geom.area. I left placeholders for you to adjust to your CRS pipeline.

COG: ensure superres writes COG tiles (GDAL –co flags) for efficient cloud serving.

Scaling: for large AOIs, use chunked tasks (map-reduce style); store intermediate masks in S3 and stream vectorized features to DB.

Accuracy: tune the model on building polygon datasets (SpaceNet, OpenBuildings, local labeled data).

Legal / license: Sentinel-2 data is Copernicus — free but follow license & attribution rules.
