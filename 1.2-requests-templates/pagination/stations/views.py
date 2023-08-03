import os
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    csv_file_path = 'data-398-2018-08-30.csv'

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations = list(reader)

    paginator = Paginator(stations, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page_number,
        'has_previous': page.has_previous,
        'has_next': page.has_next,
    }
    return render(request, 'stations/index.html', context)
