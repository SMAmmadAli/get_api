from rest_framework import serializers

class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    device_id = serializers.IntegerField()
    sim_id = serializers.IntegerField()