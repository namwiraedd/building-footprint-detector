Stack summary:

Backend: Django + Django REST Framework

Async jobs: Celery + Redis (task queue)

Storage: Local filesystem (S3-compatible optional), Postgres for metadata

ML: PyTorch (model code & inference), optional TorchScript/ONNX export

Geospatial: rasterio, GDAL, shapely, geopandas

Vector output: GeoJSON (CRS: EPSG:4326)

Container: Docker Compose (app, worker, redis, postgres)

CI: GitHub Actions (pytest)

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
