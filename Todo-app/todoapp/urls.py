from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.home,name=""),
    path('addtask/', views.addtask, name='addtask'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('update/<int:id>/', views.Update, name='update'),

]
