import openai
import torch
from .gan import Generator, generate_synthetic_data
from decouple import config

api_key = config("OPENAI_API_KEY")

def generate_meal_plan(user_profile):
    prompt = f"Create a meal plan for a user with the following profile: {user_profile}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text

def generate_workout_routine(user_profile):
    prompt = f"Create a workout routine for a user with the following profile: {user_profile}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text

# Load the trained generator model
def load_generator_model():
    generator = Generator()
    generator.load_state_dict(torch.load('path_to_generator.pth'))
    generator.eval()
    return generator

generator_model = load_generator_model()

# Function to get synthetic data
def get_synthetic_data(num_samples=100):
    synthetic_data = generate_synthetic_data(generator_model, num_samples)
    return synthetic_data.tolist()
