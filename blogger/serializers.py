from . import models

from rest_framework import serializers


class BloggerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BloggerProfile
        fields = (
            'pk', 
            'name', 
            'blogger_id', 
            'email', 
            'phone', 
            'city', 
            'state', 
            'pin', 
            'image', 
            'claps', 
            'birthdate', 
            'bio', 
            'created', 
            'portfolio', 
            'journ_with_us', 
            'business_rate', 
            'net_business', 
        )


