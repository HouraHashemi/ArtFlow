from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin 
from rest_framework.viewsets import GenericViewSet
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from Users.permissions import ViewCustomerChangeArtworkPermission, FullDjangoModelPermissions

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # permission_classes = [FullDjangoModelPermissions]
    permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAdminUser]

    # overwriting the permission_classes
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAuthenticated()]
    
    # adding url that inherit all the actions and overwrite them
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    

    # def get_serializer_context(self):
    #     return {'u_id': self.kwargs['u_pk']}
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def add_artwork(self, request):
        # Customer.objects.get(user_id=self.kwargs['u_pk'])
        pass


    @action(detail=True, permission_classes=[ViewCustomerChangeArtworkPermission])
    def change_artwork(self, request, pk):
        return Response("ok")