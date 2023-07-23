from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('problem/<int:problem_id>', views.problem, name='problem'),
    path('problem/<int:problem_id>/verdict', views.verdict, name='submit'),
    path('submissions', views.sub, name='submissions'),
    path('problem/customTc', views.customTc, name='customTc'),
    path('submissions/<int:submission_id>', views.sub_display_code, name='submissions'),

]