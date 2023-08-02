from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('problemList', views.problemList, name='problemList'),
    path('problemList/problem/<int:problem_id>', views.problem, name='problem'),
    path('problemList/problem/<int:problem_id>/verdict', views.verdict, name='submit'),
    path('submissions', views.sub, name='submissions'),
    path('problemList/problem/customTc', views.customTc, name='customTc'),

]