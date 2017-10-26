from django.conf.urls import url

from .views import ScheduleList, ScheduleInfo, StepsList

app_name = 'schedule_charts'
urlpatterns = [
    url(r'^$', ScheduleList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)$', ScheduleInfo.as_view(), name='detail'),
    url(r'^steps$', StepsList.as_view(), name='stepslist'),
    #url(r'^message$', views.MessageView.as_view(), name='message'),
    # url(r'^messages$', views.IndexView.as_view(), name='messages'),
    #url(r'^messages$', views.index, name='messages'),
    #url(r'^user_info$', views.user_info, name='user_info'),
    #url(r'^msg/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^new_message$', MessageWizard.as_view(MessageWizard.form_list), name='new_message'),
    #url(r'^webcam_upload$', views.webcam_upload, name='webcam_upload'),
]
