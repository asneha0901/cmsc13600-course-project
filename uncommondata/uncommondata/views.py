from django.http import HttpResponse
from datetime import datetime, timezone, timedelta
from decimal import Decimal
from django.shortcuts import render

def dummypage(request):
     if request.method == "GET": 
         return HttpResponse("No content here, sorry!")
     


