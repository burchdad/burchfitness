from django.urls import path
from .views import GenerateMealPlanView, GenerateWorkoutRoutineView, GenerateSyntheticDataView

urlpatterns = [
    path('meal-plan/', GenerateMealPlanView.as_view(), name='generate-meal-plan'),
    path('workout-routine/', GenerateWorkoutRoutineView.as_view(), name='generate-workout-routine'),
    path('synthetic-data/', GenerateSyntheticDataView.as_view(), name='generate-synthetic-data'),
]
