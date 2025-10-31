from rest_framework import serializers
class DetectSerializer(serializers.Serializer):
    aoi = serializers.JSONField()
    reference_date = serializers.DateField()
    bands = serializers.ChoiceField(choices=["RGB", "ALL"], default="RGB")
