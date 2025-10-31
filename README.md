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
