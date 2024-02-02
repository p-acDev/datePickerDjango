from django.shortcuts import render
from json import dumps


# Create your views here.
def index(request):
    
    context = {}
    context["datesNonDispo"] = dumps(["2024-02-08", "2024-02-09"])
    
    return render(request, "resa/resa.html", context)
