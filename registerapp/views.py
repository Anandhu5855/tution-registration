
from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')

        print(f"Name: {name}, Email: {email}, Phone: {phone}, Course: {course}")
        return HttpResponse(f"Thanks for registering, {name}!")

    return render(request, 'registerapp/form.html')
# Create your views here.
