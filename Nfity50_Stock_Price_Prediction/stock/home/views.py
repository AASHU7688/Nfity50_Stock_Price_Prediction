from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.core.exceptions import ValidationError
import numpy as np
import joblib
from django.contrib.auth import authenticate, login as auth_login
# Load your model
# Load your model
model = joblib.load('static/Stock_Price_Prediction')

def prediction(request):
    output = None 

    if request.method == 'POST':
        try:
            # Fetching form values safely and converting them to the required data types
            opening_time = float(request.POST.get('Open', 0))  # Opening time as float
            highest_value = float(request.POST.get('High', 0))  # Highest value as float
            lowest_value = float(request.POST.get('Low', 0))  # Lowest value as float
            volume = float(request.POST.get('Vol.', 0))  # Volume as float

            # Ensure input values are within a reasonable range
            opening_time = max(0, min(opening_time, 1000))  # Realistic range for opening time
            highest_value = max(0, min(highest_value, 1000))  # Realistic range for highest value
            lowest_value = max(0, min(lowest_value, 1000))  # Realistic range for lowest value
            volume = max(0, min(volume, 1000000))  # Realistic range for volume

            # Normalize input values if model expects them in a certain range (e.g., 0 to 1)
            opening_time_normalized = (opening_time - 0) / (1000 - 0)  # Example normalization
            highest_value_normalized = (highest_value - 0) / (1000 - 0)  # Example normalization
            lowest_value_normalized = (lowest_value - 0) / (1000 - 0)  # Example normalization
            volume_normalized = (volume - 0) / (1000000 - 0)  # Example normalization

            # Combine all normalized inputs into a single array for model prediction
            input_data = np.array([[opening_time_normalized, highest_value_normalized,
                                    lowest_value_normalized, volume_normalized]])

            # Log the prepared input data
            print(f"Input data for model prediction: {input_data}")

            # Predicting using the model
            pred = model.predict(input_data)
            output = f"Prediction: {pred[0]}"

        except ValueError as e:
            output = f"Error: {str(e)}"
            print(f"Error encountered: {str(e)}")

        except Exception as e:
            output = f"Unexpected error occurred: {str(e)}"
            print(f"Unexpected error: {str(e)}")

    return render(request, 'prediction.html', {'output': output})

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use Django's login function
            return redirect('home')  # Redirect to home page or any desired page
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email_or_phone')  # Adjusted field name to match the form
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'signup.html')

        # Check if username is alphanumeric and not purely numeric
        if not username.isalnum() or username.isnumeric():
            messages.error(request, "Username must contain both letters and numbers, and it can't be purely numeric.")
            return render(request, 'signup.html')

        # Create the user and set additional fields
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name  # Set first name
            user.last_name = last_name  # Set last name
            user.save()

            messages.success(request, "Account created successfully.")
            return redirect('login')  # Redirect to login page after successful signup
        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'signup.html')

    return render(request, 'signup.html')




def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('login')  # Redirect to login if not authenticated
