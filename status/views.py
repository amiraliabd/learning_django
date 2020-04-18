from django.shortcuts import render
from rest_framework.response import Response
from .models import Status
from .serializers import StatusSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins, permissions
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication
# Create your views here.


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self,request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)




class StatusAPIView(generics.ListAPIView,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication] # jwt Oauth
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, **kwargs):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return super().retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def put(self,request):
        return super().update(request)

    def patch(self,request):
        return super().update(request)

    def delete(self, request):
        return super().destroy(request)




class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    #lookup_field = 'id'
    '''
    you can set lookup_field or using get_object method
    '''
    def get_object(self, *args, **kwargs):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Status.objects.get(id=kw_id)


class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
