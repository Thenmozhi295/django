from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import forms
from django.core.files import File
from bloom_filter import BloomFilter

def home(request):
    return render(request,'form.html')

def tamilword(request):
    val1=request.POST['num1']
    
    if request.POST.get('add'):
        b=BloomFilter(max_elements=2600000,error_rate=0.1)
        file=open(r'D:\python\unique_sorted_words_in_all_words_20200604-133955.txt',encoding='utf8')
        b=file.read()
        if val1 in b:
           res='true'
           
        else:
           res='false'

   
      
    return render(request,'result.html',{'data':res})