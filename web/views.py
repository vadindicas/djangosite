from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from web.models import Journal
from web.models import Student
from web.models import Disciplines
from web.models import Specialty
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

def getJournal(request):
    info = Journal.objects.select_related('student').all()
    return render_to_response('web/home.html', {'data': info})

@csrf_exempt
def getDisp(request):
    if 'add' in request.GET:
        if 'submit' in request.POST:
            disp = Disciplines(
                specialty = Specialty.objects.get_or_create(specialty_id=request.POST['spec'])[0],
                disciplines_name = request.POST['name'],
                hours = request.POST['hour'],
                form = request.POST['form'],
              )
            disp.save()
        fields = Specialty.objects.all()
        return render_to_response('web/disp_add.html',{'field': fields})
    info = Disciplines.objects.all()
    return render_to_response('web/disciplines.html', {'data': info})

@csrf_exempt
def getSpec(request):
    if 'add' in request.GET:
        if 'submit' in request.POST:
            spec = Specialty(
                specialty_name = request.POST['name'],
              )
            spec.save()
        return render_to_response('web/spec_add.html')
    info = Specialty.objects.all()
    return render_to_response('web/spec.html', {'data': info})


@csrf_exempt
def addJournal(request):
    if 'submit' in request.POST:
      journal = Journal(
            j_year = request.POST['year'],
            student = Student.objects.get_or_create(student_id=request.POST['students'])[0],
            disciplines = Disciplines.objects.get_or_create(disciplines_id=request.POST['disp'])[0],
            rate = request.POST['rate'],
          )
      journal.save()
    student = Student.objects.all()
    disp = Disciplines.objects.all()
    return render_to_response('web/jouranl_edit.html', {'data': student,'disp': disp})

@csrf_exempt
def add(request):
    if 'submit' in request.POST:
        student = Student(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            middle_name = request.POST['middle_name'],
            year = request.POST['year'],
            form_training = request.POST['form_training'],
            group = request.POST['group'])
        student.save()
    return render_to_response('web/add.html', {'data': 1})

@csrf_exempt
def students(request):
    if 'delete' in request.GET:
        Student.objects.filter(student_id = request.GET['delete']).delete()
    if 'edit' in request.GET:
        if 'submit' in request.POST:
            Student.objects.filter(student_id = request.GET['edit']).update(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                middle_name = request.POST['middle_name'],
                year = request.POST['year'],
                form_training = request.POST['form_training'],
                group = request.POST['group'])
        fields = Student.objects.get(student_id=request.GET['edit'])
        return render_to_response('web/students_edit.html', {'item': fields})


    info = Student.objects.all()
    return render_to_response('web/students.html', {'data': info})

def main(request):
    return render_to_response('web/main.html')
