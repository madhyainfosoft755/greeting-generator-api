from rest_framework import serializers
from .models import Client, Festival, Template, Quotation

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'  # You can specify fields here or use '__all__' to include all fields

class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = '__all__'  # Here, you are including all fields as well

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['greeting_cards', 'festival']  # Manually list fields you want to include

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = '__all__'  # Including all fields for this model
