from django.conf.urls import url

from .views import SystemList, SystemInfo, ISReport7117, ISReportShorts#, is_report_7117_csv, is_report_shorts_csv

app_name = 'isystems'
urlpatterns = [
    url(r'^$', SystemList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)$', SystemInfo.as_view(), name='detail'),
    url(r'^report_7117$', ISReport7117.as_view(), name='is_report_71-17'),
    # url(r'^report_7117/csv$', is_report_7117_csv, name='is_report_71-17_csv'),
    url(r'^report_shorts$', ISReportShorts.as_view(), name='is_report_shorts'),
    # url(r'^report_shorts/csv$', is_report_shorts_csv, name='is_report_shorts_csv'),
    #url(r'^message$', views.MessageView.as_view(), name='message'),
    # url(r'^messages$', views.IndexView.as_view(), name='messages'),
    #url(r'^messages$', views.index, name='messages'),
    #url(r'^user_info$', views.user_info, name='user_info'),
    #url(r'^msg/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^new_message$', MessageWizard.as_view(MessageWizard.form_list), name='new_message'),
    #url(r'^webcam_upload$', views.webcam_upload, name='webcam_upload'),
]
