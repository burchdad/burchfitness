import React, { useState } from 'react';
import { View, Text, Button, TextInput, ScrollView } from 'react-native';
import { generateMealPlan, generateWorkoutRoutine } from '../services/api';

const GeneratePlansScreen = () => {
    const [userProfile, setUserProfile] = useState('');
    const [mealPlan, setMealPlan] = useState('');
    const [workoutRoutine, setWorkoutRoutine] = useState('');

    const handleGenerateMealPlan = async () => {
        const plan = await generateMealPlan(userProfile);
        setMealPlan(plan);
    };

    const handleGenerateWorkoutRoutine = async () => {
        const routine = await generateWorkoutRoutine(userProfile);
        setWorkoutRoutine(routine);
    };

    return (
        <ScrollView>
            <View>
                <Text>Enter Your Profile:</Text>
                <TextInput
                    value={userProfile}
                    onChangeText={setUserProfile}
                    placeholder="Describe your fitness goals, dietary restrictions, etc."
                />
                <Button title="Generate Meal Plan" onPress={handleGenerateMealPlan} />
                <Button title="Generate Workout Routine" onPress={handleGenerateWorkoutRoutine} />
            </View>
            <View>
                <Text>Meal Plan:</Text>
                <Text>{mealPlan}</Text>
            </View>
            <View>
                <Text>Workout Routine:</Text>
                <Text>{workoutRoutine}</Text>
            </View>
        </ScrollView>
    );
};

export default GeneratePlansScreen;
