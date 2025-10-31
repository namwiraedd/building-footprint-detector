"""
Adapter for super-resolution.

Expected function:
def super_resolve(input_tif: str, tile_bbox: tuple) -> str:
    # input_tif: path to standard-res GeoTIFF
    # tile_bbox: (minx, miny, maxx, maxy) in same CRS
    # returns path to SR tile (COG or GeoTIFF)
"""
from typing import Tuple

def super_resolve(input_tif: str, tile_bbox: Tuple[float,float,float,float]) -> str:
    raise NotImplementedError("Plug your super-resolution routine here.")
