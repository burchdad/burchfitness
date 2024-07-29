from django.contrib import admin
from django.urls import path
from .views import home, GenerateMealPlanView, GenerateWorkoutRoutineView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/meal-plan/', GenerateMealPlanView.as_view(), name='generate-meal-plan'),
    path('api/workout-routine/', GenerateWorkoutRoutineView.as_view(), name='generate-workout-routine'),
]
