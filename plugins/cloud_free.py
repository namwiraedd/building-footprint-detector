"""
Adapter for cloud-free composite generation.

Replace the stub with your provided cloud-free module or import the module and adapt.
Expected function:

def generate_cloud_free(aoi_geojson: dict, reference_date: str) -> str:
    # returns path to cloud-free raster (standard resolution, GeoTIFF)
"""
import os
from typing import Dict

def generate_cloud_free(aoi_geojson: Dict, reference_date: str) -> str:
    # STUB: integration point for your provided cloud-free routine
    # Example return: '/srv/app/data/cloudfree_<jobid>.tif'
    raise NotImplementedError("Plug your cloud-free composite generator here.")
