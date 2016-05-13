from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import ToDoItemSerializer
from models import ToDoItem

# Create your views here.

class Index(TemplateView):
	template_name = "index.html"
	def get_context_data(self,**kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		return context


class ToDoItemViewSet(viewsets.ModelViewSet):
	queryset = ToDoItem.objects.all()
	serializer_class = ToDoItemSerializer

class ToDoItemList(APIView):
	
	def get(self, request, format=None):
		items = ToDoItem.objects.all()
		serializer = ToDoItemSerializer(items, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ToDoItemSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoItemDetail(APIView):

	def get_object(self, pk):
		try:
			return ToDoItem.objects.get(pk=pk)
		except ToDoItem.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		items = self.get_object(pk)
		serializer = ToDoItemSerializer(items)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		items = self.get_object(pk)
		serializer = ToDoItemSerializer(items, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		items = self.get_object(pk)
		items.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
