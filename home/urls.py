from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index), # ,name="home"  -->path name = home
    path("ind_as_list",views.ind_as_list),
    path("Ind_AS_1",views.Ind_AS_1), # ,name="home"  -->path name = home
    path("Ind_AS_2",views.Ind_AS_2), # ,name="home"  -->path name = home
    path("Ind_AS_7",views.Ind_AS_7), # ,name="home"  -->path name = home
    path("Ind_AS_19",views.Ind_AS_19), # ,name="home"  -->path name = home
    path("Ind_AS_37",views.Ind_AS_37), # ,name="home"  -->path name = home
    path("Ind_AS_41",views.Ind_AS_41), # ,name="home"  -->path name = home
    path("Ind_AS_101",views.Ind_AS_101), # ,name="home"  -->path name = home
    path("Ind_AS_102",views.Ind_AS_102), # ,name="home"  -->path name = home
    path("Ind_AS_113",views.Ind_AS_113), # ,name="home"  -->path name = home
    path("Ind_AS_115",views.Ind_AS_115), # ,name="home"  -->path name = home
    path("static/INDAS7 mca.pdf",views.Ind_AS_7_pdf),
    path("skreachpad",views.skreachpad,name="skreachpad"), # ,name="skreachpad"  -->path name = home
    path('game', views.game_view, name='game'),
    path('game2', views.game_view2, name='game2'),
    path('calc', views.calc, name='calc'),
    path('tools', views.tools, name='tools'),
    path('it_basic', views.it_basic, name='it_basic'),
]
