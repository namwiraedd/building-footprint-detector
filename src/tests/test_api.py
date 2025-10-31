from django.test import Client
import json
def test_post_detect():
    c = Client()
    payload = {"aoi": {"type":"FeatureCollection","features":[]}, "reference_date": "2025-01-01"}
    r = c.post("/api/detect/", json.dumps(payload), content_type="application/json")
    assert r.status_code in (202, 400)
