import axios from 'axios';

const API_URL = 'http://your-django-backend-url/api';

export const generateMealPlan = async (userProfile) => {
    try {
        const response = await axios.post(`${API_URL}/generate-meal-plan/`, { user_profile: userProfile });
        return response.data.meal_plan;
    } catch (error) {
        console.error(error);
        throw error;
    }
};

export const generateWorkoutRoutine = async (userProfile) => {
    try {
        const response = await axios.post(`${API_URL}/generate-workout-routine/`, { user_profile: userProfile });
        return response.data.workout_routine;
    } catch (error) {
        console.error(error);
        throw error;
    }
};
