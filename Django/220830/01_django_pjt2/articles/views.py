from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    names = ['Eunkyung', 'Hyoungkyu']
    info = {
        'name': 'Hyoungkyu',
        'sur_name': 'Choi'
    }
    context = {
        'names': names,
        'info' : info,
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['파스타', '스테이크', '스시', '불고기']
    pick = random.choice(foods)
    context = {
        'pick':pick,
        'foods':foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    print("message=",message)
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)

def num(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'num.html', context)