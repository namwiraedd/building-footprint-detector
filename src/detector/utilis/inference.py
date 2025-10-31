import torch
import rasterio
import numpy as np
import os
from typing import List

def load_model(model_path: str):
    model = torch.jit.load(model_path) if model_path.endswith(".pt") else torch.load(model_path, map_location="cpu")
    model.eval()
    return model

def run_inference_on_tile(tile_tif: str, model_path: str) -> str:
    """
    Runs model on tile, returns path to binary mask (e.g., single-band GeoTIFF)
    Placeholder: implement tiling + batching + normalization appropriate to your model.
    """
    model = load_model(model_path)
    with rasterio.open(tile_tif) as src:
        img = src.read([1,2,3])  # assuming RGB; adjust for n bands
        # normalize
        arr = np.transpose(img, (1,2,0)) / 255.0
    # dummy: threshold on mean brightness to create fake mask
    mask = (arr.mean(axis=2) > 0.5).astype("uint8") * 255
    mask_path = tile_tif.replace(".tif", "_mask.tif")
    # write mask (match src profile)
    profile = src.profile.copy()
    profile.update(count=1, dtype="uint8")
    with rasterio.open(mask_path, "w", **profile) as dst:
        dst.write(mask, 1)
    return mask_path
