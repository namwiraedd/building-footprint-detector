4. POST AOI + date to `/api/detect/` (see docs/usage.md)

## Plugins
- `plugins/cloud_free.py` — implement `generate_cloud_free(aoi, date)` -> path to composite (tif)
- `plugins/superres.py` — implement `super_resolve(input_tif, tile)` -> path to SR tile (COG)

## Output
A GeoJSON file with features:
```json
{
"id": "...",
"properties": {"confidence": 0.92, "area_m2": 34.2},
"geometry": { ... polygon ... }
}
