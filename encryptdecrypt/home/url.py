from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('question1/',views.question1,name="question1"),
    path('question2/',views.question2,name="question2"),
    path('question3/',views.question3,name="question3"),
    path('question4/',views.question4,name="question4"),
    path('question5/',views.question5,name="question5"),
    path('question6/',views.question6,name="question6"),
    path('question7/',views.question7,name="question7"),
    path('leader/',views.leaderboard,name="leaderboard")
]