from django.conf.urls import url

from .views import ContractList, contract_list, ContractInfo

app_name = 'contracts'
urlpatterns = [
    # url(r'^$', ContractList.as_view(), name='list'),
    url(r'^$', contract_list, name='list'),
    url(r'^(?P<pk>[0-9]+)$', ContractInfo.as_view(), name='detail'),
    #url(r'^message$', views.MessageView.as_view(), name='message'),
    # url(r'^messages$', views.IndexView.as_view(), name='messages'),
    #url(r'^messages$', views.index, name='messages'),
    #url(r'^user_info$', views.user_info, name='user_info'),
    #url(r'^msg/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^new_message$', MessageWizard.as_view(MessageWizard.form_list), name='new_message'),
    #url(r'^webcam_upload$', views.webcam_upload, name='webcam_upload'),
]
