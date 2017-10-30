from django.conf.urls import url
from . import views

urlpatterns = [
    # /menu/
    url(r'^$', views.menu, name='index'),

    # /menu/712/
    url(r'^(?P<personaje_id>[0-9]+)/$', views.detalle, name='detalle'),

    # seleccion de personaje
    url(r'^seleccion_personaje/$', views.seleccion_personaje, name='seleccion'),
]