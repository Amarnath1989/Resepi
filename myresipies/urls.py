from django.conf.urls import url,include
from.import views

urlpatterns = [
    url(r'^', views.index, name = 'index'),
    url(r'^create/', views.create_resepi, name = 'create'),
    url(r'^detail/',views.detail, name='detail'),
    url(r'^detail_new/(?P<id>\d+)/$',views.detail_new, name='detail_new'),
    url(r'accounts/',include('django.contrib.auth.urls'))



]