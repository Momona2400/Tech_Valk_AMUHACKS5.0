from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import QuestionnaireResponse
from django.contrib import messages
from django.contrib.auth import logout

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        login(request, user)

        return redirect('questionnaire')

    return render(request, 'signup.html')

def home(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.profile.questionnaire_completed:
                return redirect('dashboard')
            else:
                return redirect('questionnaire')

        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')

def signup_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Basic validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Create user
        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('questionnaire')

    return render(request, 'signup.html')


@login_required
def questionnaire(request):

    if request.user.profile.questionnaire_completed:
        return redirect('dashboard')

    if request.method == "POST":

        response = QuestionnaireResponse.objects.filter(
            user=request.user
        ).first()

        if not response:
            response = QuestionnaireResponse(user=request.user)

        # Assign all values BEFORE saving
        response.school_language = request.POST.get('q1')
        response.stage_activity = request.POST.get('q2')
        response.teaching_pace = request.POST.get('q3')
        response.doubt_clearing = request.POST.get('q4')

        response.extempore_comfort = int(request.POST.get('q5', 3))
        response.public_speaking_confidence = int(request.POST.get('q6', 3))
        response.help_seeking_comfort = int(request.POST.get('q7', 3))
        response.group_discussion_confidence = int(request.POST.get('q8', 3))
        response.adaptability = int(request.POST.get('q9', 3))

        response.academic_pressure = request.POST.get('q10')
        response.course = request.POST.get('q11')
        response.specialization = request.POST.get('q12')

        response.save()
        response.calculate_score()

        profile = request.user.profile
        profile.questionnaire_completed = True
        profile.save()

        return redirect('dashboard')

    return render(request, 'questionnaire.html')

@login_required
def dashboard(request):

    response = QuestionnaireResponse.objects.filter(
        user=request.user
    ).first()

    if not response:
        return redirect('questionnaire')

    score = response.total_score

    MIN_SCORE = 8
    MAX_SCORE = 34
    MIN_FUEL = 20
    MAX_FUEL = 80

    fuel_percentage = MIN_FUEL + round(
        ((score - MIN_SCORE) / (MAX_SCORE - MIN_SCORE)) 
        * (MAX_FUEL - MIN_FUEL)
    )

    fuel_percentage = max(MIN_FUEL, min(MAX_FUEL, fuel_percentage))

    # 🔥 ADD THIS
    if fuel_percentage < 40:
        encouragement = "🌱 Building your foundation!"
    elif fuel_percentage < 65:
        encouragement = "🏹 Keep going!"
    else:
        encouragement = "🚀 You're ready to launch!"

    return render(request, 'dashboard.html', {
        'score': score,
        'fuel_percentage': fuel_percentage,
        'encouragement': encouragement
    })
