from django.conf.urls import url
from searcher import views

urlpatterns = [
    url(r'^$', views.get_results_table, name='get_results_table'),
    url(r'^exploit_view/(?P<exploit_id>\d+)', views.view_exploit_code, name='view_exploit_code'),
    url(r'^shellcode_view/(?P<shellcode_id>\d+)', views.view_shellcode_code, name='view_shellcode_code'),
]