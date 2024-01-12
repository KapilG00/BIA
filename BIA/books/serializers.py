import json
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ["id"]
        
    @staticmethod
    def get_Serialized_JSON(obj):
        try:
            obj.exists()
            serialized_data = BookSerializer(obj, many=True).data
        except Exception as e:
            serialized_data = BookSerializer(obj).data    
        return json.loads(JSONRenderer().render(serialized_data))