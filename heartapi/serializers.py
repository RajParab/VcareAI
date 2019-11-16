from rest_framework import serializers
from .models import Test

class TestSerializers(serializers.ModelSerializer):
	class Meta:
		model = Test
		fields='__all__'