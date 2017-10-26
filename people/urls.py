from django.conf.urls import url
from django.views.generic import TemplateView

from .views import PeopleList, PeopleInfo

app_name = 'people'
urlpatterns = [
    url(r'^$', PeopleList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)$', PeopleInfo.as_view(), name='detail'),
    #url(r'^message$', views.MessageView.as_view(), name='message'),
    # url(r'^messages$', views.IndexView.as_view(), name='messages'),
    #url(r'^messages$', views.index, name='messages'),
    #url(r'^user_info$', views.user_info, name='user_info'),
    #url(r'^msg/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^new_message$', MessageWizard.as_view(MessageWizard.form_list), name='new_message'),
    #url(r'^webcam_upload$', views.webcam_upload, name='webcam_upload'),
]
