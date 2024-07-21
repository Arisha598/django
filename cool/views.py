from django.shortcuts import render

def swag(request):
    return render(request, "main/swag.html")

def swagme2(request):
    return render(request, "main/swagme.html")

def swagmeandyou3(request):
    return render(request, "main/swagmeandyou.html")

peoples = [
    {'name' : 'arisha chaudhary', 'age' : 2},
    {'name' : 'aryan chaudhary', 'age' : 16},
    {'name' : 'arjun chaudhary', 'age' : 56},
    {'name' : 'kunal', 'age' : 61},
    {'name' : 'mariyam', 'age' : 78},
    {'name' : 'krishna', 'age' : 16},
]
def home(request):
    return render(request, "main/index.html" , context={'peoples' : peoples})
for people in peoples:
    print(people)


def customFilter(request):
    return render(request, 'main/customFilter.html')
 