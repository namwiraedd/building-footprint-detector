import rasterio
from typing import Iterator, Tuple
from rasterio.windows import from_bounds

def tile_iterator(tif_path: str, tile_size_m: int = 10000) -> Iterator[Tuple[float,float,float,float]]:
    """
    Yields tile bboxes in tif CRS as (minx,miny,maxx,maxy).
    Simple placeholder: in production handle CRS transforms and exact tile math.
    """
    with rasterio.open(tif_path) as src:
        bounds = src.bounds
        # naive grid: split into N x M tiles based on degree approximation or use rasterio.warp
        nx = max(1, int((bounds.right - bounds.left) / tile_size_m))
        ny = max(1, int((bounds.top - bounds.bottom) / tile_size_m))
        # fallback: single tile
        yield (bounds.left, bounds.bottom, bounds.right, bounds.top)
