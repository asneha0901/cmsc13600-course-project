from django.http import HttpResponse
from datetime import datetime, timezone, timedelta
from decimal import Decimal
from django.shortcuts import render

def dummypage(request):
     if request.method == "GET": 
         return HttpResponse("No content here, sorry!")
     
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

