
from rest_framework import generics
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework.reverse import reverse

class PollList(generics.ListCreateAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse

class PollList(APIView):
	def get(self, request):
		polls = Poll.objects.all()[:20]
		data = PollSerializer(polls, many=True).data
		return Response(data)


class PollDetail(APIView):
	def get(self, request, pk):
		poll = get_object_or_404(Poll, pk=pk)
		data = PollSerializer(poll).data 
		return Response(data)

class ChoiceList(generics.ListCreateAPIView):
	def get(self, request):
		queryset = Choice.objects.all()
		serializer_class = ChoiceSerializer
		return HttpResponseRedirect('/')

class CreateVote(generics.CreateAPIView):
	serializer_class = VoteSerializer
	#def get(self, request, pk):
		#data= VoteSerializer.data
		#return HttpResponseRedirect('posts:index')





