from django.urls import path

from . import views

app_name = 'website'         #permettra de différencier l'application utilisé lorsqu'on utilise {% url inside:detail %}
                            #dans le cas ou on aurais une autre application avec une vue nommé 'detail'
urlpatterns = [
    # / -> redirect to homepage
    path ('', views.home, name = 'home'),
    path ('hidden/', views.hidden, name='hidden')
    # /inside/5/
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ]