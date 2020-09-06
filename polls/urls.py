
from django.urls import include, path
from rest_framework import routers
from posts import views as post_views
from .apiviews import ChoiceList, CreateVote
from .apiviews import PollList, PollDetail

#from django.views.generic import DetailView, ListView
router = routers.DefaultRouter()
#router.register(r'', post_views.PostsFeedView )



urlpatterns = [
	path("polls/", PollList.as_view(), name="polls_list"),
	path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),

	path("choices/", ChoiceList.as_view(), name="choice_list"),
	path("vote/", CreateVote.as_view(), name="create_vote"),

]
