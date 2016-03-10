from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
	# http://127.0.0.1:8000/polls/
	#url(r'^$', views.index, name='index'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	
	# http://127.0.0.1:8000/polls/1/
	#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	
	# http://127.0.0.1:8000/polls/1/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	
	# http://127.0.0.1:8000/polls/1/results/
	#url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
]