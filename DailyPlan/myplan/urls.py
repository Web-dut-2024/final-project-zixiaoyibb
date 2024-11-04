from django.urls import path
from .views import plan_view, finish_view, delete_plan, add_plan, complete_plan

urlpatterns = [
    path('plans/', plan_view, name='plan'),
    path('finish/', finish_view, name='finish'),
    path('delete/<int:plan_id>/', delete_plan, name='delete_plan'),
    path('add/', add_plan, name='add_plan'),  # 添加计划的路由
    path('complete/<int:plan_id>/', complete_plan, name='complete_plan'),  # 完成计划的路由

]
