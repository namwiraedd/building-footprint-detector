import geopandas as gpd
from shapely.geometry import shape, mapping
import rasterio.features
import json
from affine import Affine

def vectorize_masks_to_geojson(mask_tif: str, tile_bbox) -> list:
    """
    Convert binary mask to GeoJSON features (with area + centroid + confidence placeholder)
    """
    import rasterio
    features = []
    with rasterio.open(mask_tif) as src:
        mask = src.read(1)
        transform = src.transform
        for geom, val in rasterio.features.shapes(mask, transform=transform):
            if val == 0:
                continue
            geom_shape = shape(geom)
            area = geom_shape.area  # note: area in CRS units; reproject to EPSG:3857 for sqm if needed
            centroid = geom_shape.centroid
            feat = {
                "type": "Feature",
                "geometry": mapping(geom_shape),
                "properties": {
                    "confidence": 0.9,
                    "area": float(area),
                    "centroid": [centroid.x, centroid.y]
                }
            }
            features.append(feat)
    return features
