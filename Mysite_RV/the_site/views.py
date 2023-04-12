from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .functions import handle_uploaded_file
from .forms import StudentForm

from pyresparser import ResumeParser





def the_site(request):
    template = loader.get_template('myfirst.html')
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            data = ResumeParser('the_site/upload/'+request.FILES['file'].name).get_extracted_data()
            return render(request, 'results.html', {'d': data})
    else:
        student = StudentForm()
        return render(request, "myfirst.html", {'form': student})

