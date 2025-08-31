import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

class WorkoutRecommender:
    """
    A class to recommend personalized workout plans using a RandomForestClassifier.
    Handles data creation, preprocessing, model training, prediction, and user interaction.
    """

    def __init__(self):
        self.model = None
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.detailed_plans = {
            "HIIT + Cardio": [
                "Warm-up: 5 min jogging",
                "Burpees: 3 sets of 15",
                "Jumping Jacks: 3 sets of 30",
                "Mountain Climbers: 3 sets of 20",
                "Cool down: 5 min stretching"
            ],
            "Strength Training": [
                "Warm-up: 10 min jogging",
                "Push-ups: 3 sets of 12",
                "Squats: 3 sets of 15",
                "Dumbbell Curls: 3 sets of 10",
                "Cool down: 5 min stretching"
            ],
            "Yoga + Stretching": [
                "Warm-up: Deep breathing 5 min",
                "Sun Salutation: 5 rounds",
                "Cobra Pose: Hold 30 sec",
                "Child Pose: Hold 1 min",
                "Cool down: Meditation 5 min"
            ]
        }

    def create_dataset(self):
        """
        Creates a small synthetic dataset for demonstration purposes.
        """
        data = {
            'Age': [20, 25, 30, 35, 40, 22, 28, 26],
            'BMI': [22.5, 24.1, 29.0, 31.2, 26.8, 21.7, 27.3, 23.4],
            'Goal': ['weight_loss', 'muscle_gain', 'endurance', 'flexibility',
                     'weight_loss', 'muscle_gain', 'endurance', 'flexibility'],
            'Level': ['beginner', 'intermediate', 'advanced', 'beginner',
                      'intermediate', 'beginner', 'advanced', 'intermediate'],
            'Time': [30, 45, 60, 40, 50, 30, 55, 35],
            'Workout_Plan': [
                'HIIT + Cardio',
                'Strength Training',
                'HIIT + Cardio',
                'Yoga + Stretching',
                'Strength Training',
                'HIIT + Cardio',
                'Strength Training',
                'Yoga + Stretching'
            ]
        }
        return pd.DataFrame(data)

    def preprocess_data(self, df):
        """
        Preprocesses the dataset: label encodes categorical columns, scales numerical features.
        """
        df_processed = df.copy()

        # Encode categorical features
        for column in ['Goal', 'Level']:
            le = LabelEncoder()
            df_processed[column] = le.fit_transform(df_processed[column])
            self.label_encoders[column] = le

        # Encode target variable
        target_encoder = LabelEncoder()
        df_processed['Workout_Plan'] = target_encoder.fit_transform(df_processed['Workout_Plan'])
        self.label_encoders['Workout_Plan'] = target_encoder

        # Separate features and target
        X = df_processed[['Age', 'BMI', 'Goal', 'Level', 'Time']]
        y = df_processed['Workout_Plan']

        # Scale numerical features (avoid SettingWithCopyWarning)
        X.loc[:, ['Age', 'BMI', 'Time']] = self.scaler.fit_transform(X[['Age', 'BMI', 'Time']])

        return X, y

    def train_model(self, X, y):
        """
        Trains the RandomForestClassifier on the given features and target.
        """
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X, y)
        print("✅ Model trained successfully on full dataset")

    def save_model(self, filename='workout_recommender.joblib'):
        """
        Saves the model, label encoders, and scaler to disk.
        """
        try:
            model_data = {
                'model': self.model,
                'label_encoders': self.label_encoders,
                'scaler': self.scaler
            }
            joblib.dump(model_data, filename)
        except Exception as e:
            print(f"Error saving model: {e}")

    def load_model(self, filename='workout_recommender.joblib'):
        """
        Loads the model, label encoders, and scaler from disk if available.
        """
        if os.path.exists(filename):
            try:
                model_data = joblib.load(filename)
                self.model = model_data['model']
                self.label_encoders = model_data['label_encoders']
                self.scaler = model_data['scaler']
                return True
            except Exception as e:
                print(f"Error loading model: {e}")
        return False

    def get_user_input(self):
        """
        Collects and validates user input for workout recommendation.
        """
        print("\n=== Personalized Workout Recommendation ===")
        name = input("Enter your name: ").strip()

        # Age validation
        while True:
            try:
                age = int(input("Enter your age: "))
                if 10 <= age <= 100:
                    break
                else:
                    print("Please enter a realistic age between 10 and 100.")
            except ValueError:
                print("Please enter a valid integer.")

        # Height validation
        while True:
            try:
                height = float(input("Enter your height in cm: "))
                if 100 <= height <= 250:
                    break
                else:
                    print("Please enter a realistic height in cm (100-250).")
            except ValueError:
                print("Please enter a valid number.")

        # Weight validation
        while True:
            try:
                weight = float(input("Enter your weight in kg: "))
                if 30 <= weight <= 250:
                    break
                else:
                    print("Please enter a realistic weight in kg (30-250).")
            except ValueError:
                print("Please enter a valid number.")

        bmi = weight / ((height / 100) ** 2)

        # Goal validation
        valid_goals = ['weight_loss', 'muscle_gain', 'endurance', 'flexibility']
        while True:
            goal = input("Enter your goal (weight_loss/muscle_gain/endurance/flexibility): ").lower().strip()
            if goal in valid_goals:
                break
            else:
                print("Invalid goal. Please choose from:", ", ".join(valid_goals))

        # Level validation
        valid_levels = ['beginner', 'intermediate', 'advanced']
        while True:
            level = input("Enter your fitness level (beginner/intermediate/advanced): ").lower().strip()
            if level in valid_levels:
                break
            else:
                print("Invalid level. Please choose from:", ", ".join(valid_levels))

        # Time validation
        while True:
            try:
                time = int(input("Enter available workout time in minutes: "))
                if 10 <= time <= 180:
                    break
                else:
                    print("Please enter a realistic workout time in minutes (10-180).")
            except ValueError:
                print("Please enter a valid number.")

        return {
            'name': name,
            'age': age,
            'bmi': bmi,
            'goal': goal,
            'level': level,
            'time': time
        }

    def predict_workout(self, user_data):
        """
        Predicts the recommended workout plan given the user's data.
        """
        try:
            goal_encoded = self.label_encoders['Goal'].transform([user_data['goal']])[0]
            level_encoded = self.label_encoders['Level'].transform([user_data['level']])[0]

            features = np.array([[user_data['age'], user_data['bmi'], goal_encoded, level_encoded, user_data['time']]])
            features[:, [0, 1, 4]] = self.scaler.transform(features[:, [0, 1, 4]])

            prediction = self.model.predict(features)[0]
            workout_plan = self.label_encoders['Workout_Plan'].inverse_transform([prediction])[0]
            return workout_plan
        except Exception as e:
            print(f"Prediction error: {e}")
            return None

    def bmi_category(self, bmi):
        """
        Returns a string category for the given BMI.
        """
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def display_recommendation(self, user_data, workout_plan):
        """
        Displays the recommendation to the user.
        """
        bmi_status = self.bmi_category(user_data['bmi'])
        print(f"\nHello {user_data['name']}! Your BMI is {user_data['bmi']:.2f} ({bmi_status})")
        if workout_plan:
            print(f"✅ Recommended Workout Plan: {workout_plan}\n")
            if workout_plan in self.detailed_plans:
                print("Here’s your detailed workout routine:")
                for step in self.detailed_plans[workout_plan]:
                    print("- " + step)
            else:
                print("Sorry, no detailed plan found for this workout type.")
        else:
            print("Sorry, we could not generate a recommendation. Please try again.")

def main():
    recommender = WorkoutRecommender()

    if not recommender.load_model():
        df = recommender.create_dataset()
        X, y = recommender.preprocess_data(df)
        recommender.train_model(X, y)
        recommender.save_model()

    user_data = recommender.get_user_input()
    workout_plan = recommender.predict_workout(user_data)
    recommender.display_recommendation(user_data, workout_plan)

if __name__ == "__main__":
    main()