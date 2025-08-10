class UnderAgeError(Exception):
    def __init__(self, age, message="User is under the required age limit."):
        self.age = age
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message} (Entered age: {self.age})"
def register_user(age):
    if age < 18:
        raise UnderAgeError(age)
    print("Registration successful!")

try:
    user_age = int(input("Enter your age: "))
    register_user(user_age)
except UnderAgeError as e:
    print("Registration failed:", e)
except ValueError:
    print("Please enter a valid number.")