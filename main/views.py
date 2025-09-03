from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406396956',
        'name': 'Chris Darren Imanuel',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)