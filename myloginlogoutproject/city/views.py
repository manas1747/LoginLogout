from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import City

CityForm = modelform_factory(City, fields=("name", "country"))


@login_required
def city_list(request):
    context = {
        "city_list": City.objects.filter(user=request.user),
    }
    return render(request, "city/city_list.html", context)


@login_required
def create_city(request):
    if request.method == "GET":
        return render(request, "city/create_city.html", {"form": CityForm})
    elif request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.user = request.user
            city.save()
            return redirect("city_list")
    else:
        return HttpResponse("Method not supported.")
