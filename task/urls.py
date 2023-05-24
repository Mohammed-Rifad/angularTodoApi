from django.urls import path
from . import views

urlpatterns = [
     
    path('add',views.add_task),
    path('list/<str:status>',views.task_list),
    path('remove/<int:id>',views.delete_task),
    path('update/<int:id>',views.update_task),
    path('filter/task',views.filter_task),
    path('search',views.search_task),
    
     
    
]
