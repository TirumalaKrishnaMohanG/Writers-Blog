#!/usr/bin/env python
# Headers
from .models import comment as article
from rest_framework import serializers

# Create a serializers
class storyseriesapiserializerarticle(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = article
		fields = '__all__'