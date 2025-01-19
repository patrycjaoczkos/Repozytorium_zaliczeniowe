from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/update/<int:pk>/', views.person_update),
    path('persons/delete/<int:pk>/', views.person_delete),
    path('osoby/', views.OsobaList.as_view(), name='osoba_list'),
    path('osoby/<int:pk>/', views.OsobaDetail.as_view(), name='osoba_detail'),
    path('osoby/search/<str:substring>/', views.osoba_search),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
    path("welcome/", views.welcome_view),
    path("persons_html/", views.person_list_html),
    path("persons_html/<int:id>/", views.person_detail_html),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
    path("teams_html/", views.team_list_html),
    path("teams_html/<int:id>/", views.team_detail_html),
    path('stanowisko/<int:id>/members/', views.StanowiskoMemberView.as_view(), name='stanowisko_members'),
    path('team/<int:pk>/', views.TeamDetail.as_view(), name='team_detail'),

]

