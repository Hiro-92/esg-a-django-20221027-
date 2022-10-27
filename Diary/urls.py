from django.urls import path
from Diary import views

urlpatterns = [
    path('<int:pk>/',views.memory_detail),
    path('',views.memory_list),
    path('new/', views.diary_new), 
]