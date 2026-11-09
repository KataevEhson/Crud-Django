from django.urls import path
from .views import *


urlpatterns = [
    path('', add_tasks, name='home'),
    path('show_tasks', get_products, name='show_tasks'),
path('show_task_id/<int:id>', get_task_id_id, name='show_task_by_id'),
    path('delete_task/<int:id>', get_task_id_id, name='task_delete'),

]  