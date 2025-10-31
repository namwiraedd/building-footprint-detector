from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DetectSerializer
from .models import Job
from .tasks import run_detection_job

class DetectAPIView(APIView):
    def post(self, request):
        ser = DetectSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        job = Job.objects.create(input_aoi=ser.validated_data["aoi"],
                                 reference_date=ser.validated_data["reference_date"])
        # enqueue Celery task
        run_detection_job.delay(str(job.id), ser.validated_data["bands"])
        return Response({"job_id": str(job.id)}, status=status.HTTP_202_ACCEPTED)

    def get(self, request, job_id=None):
        if job_id:
            try:
                job = Job.objects.get(id=job_id)
            except Job.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response({
                "job_id": str(job.id),
                "status": job.status,
                "output": job.output_geojson
            })
        return Response(status=status.HTTP_400_BAD_REQUEST)
