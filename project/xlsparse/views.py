# coding: utf8

from django.shortcuts import render, redirect
from models import Book, File
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import UploadFileForm
import xlrd
import django_rq

def index(request):
    objects = Book.objects.all()
    file = File.objects.all()
    return render(request, 'xlsparse/index.html', {'file': file})


def parser_list(request):
    objects = Book.objects.all()
    paginator = Paginator(objects, 25)
    page = request.GET.get('page')
    try:
        list_objects = paginator.page(page)
    except PageNotAnInteger:
        list_objects = paginator.page(1)
    except EmptyPage:
        list_objects = paginator.page(paginator.num_pages)
    return render(request, 'xlsparse/list.html', {'list': list_objects})


def upload_file(request):
    file = UploadFileForm()
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('xlsparse:index')

    return render(request, 'xlsparse/form.html', {'form': form})


def parser(file_id):
    rb = xlrd.open_workbook(file_id, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        title = sheet.row_values(i)[0]
        price = sheet.row_values(i)[1]
        if price:
            kg = price * 68
            obj = Book.objects.get_or_create(title=title, usd=price, kgs=kg)



def get_parser(request, file_id):
    is_file = File.objects.get(pk=file_id)
    queue = django_rq.get_queue()
    queue.enqueue(parser, is_file.xls.url, timeout=720)

    return redirect('xlsparse:list_parser')