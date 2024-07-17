from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import generate_meal_plan, generate_workout_routine

class GenerateMealPlanView(APIView):
    def post(self, request):
        user_profile = request.data.get('user_profile')
        meal_plan = generate_meal_plan(user_profile)
        return Response({'meal_plan': meal_plan}, status=status.HTTP_200_OK)

class GenerateWorkoutRoutineView(APIView):
    def post(self, request):
        user_profile = request.data.get('user_profile')
        workout_routine = generate_workout_routine(user_profile)
        return Response({'workout_routine': workout_routine}, status=status.HTTP_200_OK)
