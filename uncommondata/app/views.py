from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.models import User 
from django.contrib.auth import login
from django.views.decorators.http import require_http_methods
from datetime import datetime, timezone, timedelta
from decimal import Decimal
from app.models import UserProfile
# Add these two new functions to your views.py:

def new(request):
    """
    Display the signup form page.
    Only accepts GET requests.
    """
    if request.method == 'POST':
        return HttpResponseNotAllowed(['GET'])
    
    return render(request, 'uncommondata/new.html')


@require_http_methods(["POST"])
def createUser(request):
    try:
        # Get form data
        username = request.POST.get('user_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        is_curator = request.POST.get('is_curator', '0')
        
        # Validate
        if not username or not email or not password:
            return HttpResponse("Missing required fields", status=400)
        
        if is_curator not in ['0', '1']:
            return HttpResponse("Invalid account type", status=400)
        
        # Check duplicates
        if User.objects.filter(email=email).exists():
            return HttpResponse(f"email {email} already in use", status=400)
        
        if User.objects.filter(username=username).exists():
            return HttpResponse(f"username {username} already in use", status=400)
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Create profile
        UserProfile.objects.create(
            user=user,
            is_curator=(is_curator == '1')
        )
        
        # Login
        login(request, user)
        
        # Success - add content_type!
        return HttpResponse("success", status=201, content_type='text/plain')
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return HttpResponse(f"Error creating user: {str(e)}", status=500)
    
def time(request):
     CST = timezone(timedelta(hours=-6))
     now = datetime.now(timezone.utc).astimezone(CST)
     return HttpResponse(now.strftime("%H:%M"), content_type="text/plain")

def sum(request):
     n1 = request.GET.get("n1", "0")
     n2 = request.GET.get("n2", "0")
     sum= Decimal(n1) + Decimal(n2)
     return HttpResponse(str(sum), content_type="text/plain")

def index(request):
    """
    View function for the home page.
    Displays team bio, current user info, and current time.
    """
    # Get current time formatted as a string
    CST = timezone(timedelta(hours=-6))
    current_time = datetime.now(timezone.utc).astimezone(CST).strftime("%B %d, %Y at %I:%M:%S %p")
    
    # Create context dictionary with the current time
    context = {
        'current_time': current_time,
    }
    
    return render(request, 'uncommondata/index.html', context)
# Create your views here.
