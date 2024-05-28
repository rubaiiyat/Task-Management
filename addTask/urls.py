from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.addTask,name='addTask'),
    path('delete/<int:id>',views.deleteTask,name='deleteTask'),
    path('edit/<int:id>',views.editPost,name='editPost'),
]
