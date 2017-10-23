from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]

## el (?P<pk>\d+) hace que se guarde cualquier numero en esa posicion en una variable llamada
## pk, la cual se le pasara a la funcion del views llamada post_detail con ese mismo nombre.
## post_detail en views debe agarrar la variable, poniendola como uno de sus parametros.