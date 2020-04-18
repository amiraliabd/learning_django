from models import Status
from serializers import StatusSerializer
from cfeapi import settings
import json

def get():
    qs = Status.objects.all()
    serializer_data = StatusSerializer(qs, many=True)
    print(f'serializer_data = {serializer_data}')


get()