from mongo_crud_app import models, serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class CreateView( GenericAPIView ):
    serializer_class = serializers.ProductSerializer

    def post(self, request, **kwargs):
        try:
            serializer = self.serializer_class( data=request.data )
            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data )
        except Exception as e:
            print( "Error:", e )
            return Response( {"error": str( e )} )


class GetView( GenericAPIView ):
    queryset = models.Product.objects.all()

    def get(self, request, **kwargs):
        try:
            serializer_class = serializers.ProductSerializer( self.queryset, many=True )
            return Response( serializer_class.data )
        except Exception as e:
            print( "Error:", e )
            return Response( {"error": str( e )} )


class GetByID( GenericAPIView ):
    serializer_class = serializers.ProductSerializer

    def get(self, request, pk, **kwargs):
        model = models.Product.objects.get( pk=pk )
        serializer_class = self.serializer_class( model )
        return Response( serializer_class.data )


class Put( GenericAPIView ):
    serializer_class = serializers.ProductSerializer

    def put(self, request, name):
        try:

            query_set = models.Product.objects.get( name=name )
            serializer = serializers.ProductSerializer( instance=query_set, data=request.data )

            if serializer.is_valid():
                serializer.save()
                return Response( serializer.data )
        except models.Product.DoesNotExist:
            return Response( {"error": f"Product with name '{name}' does not exist."}, status=404 )
        except Exception as e:
            print( "Error:", e )
            return Response( {"error": str( e )} )


class DeleteID( GenericAPIView ):
    def delete(self, request, pk):
        try:
            mongo_delete = models.Product.objects.get( pk=pk )
            mongo_delete.delete()
            return Response( {"message": "deleted"} )
        except Exception as e:
            print( "invalid", e )
            return Response( {"error": str( e )} )
