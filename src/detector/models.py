from django.db import models
import uuid

class Job(models.Model):
    JOB_STATUS = [
        ("PENDING", "Pending"),
        ("RUNNING", "Running"),
        ("FAILED", "Failed"),
        ("DONE", "Done"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    input_aoi = models.JSONField()
    reference_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=JOB_STATUS, default="PENDING")
    output_geojson = models.FilePathField(null=True, blank=True)
    log = models.TextField(blank=True)
