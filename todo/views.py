from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from .models import Project
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def home(request):
    projects = Project.objects.all()
    return render(request, 'todo/home.html', {'projects': projects})
    
def en(request):
    projects = Project.objects.all()
    return render(request, 'todo/en.html', {'projects': projects})

# def signupuser(request):
#     if request.method =='GET':
#         return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
#     else:
#         # Create a new user
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'] , password=request.POST['password1'])
#                 user.save()
#                 login(request , user)
#                 return redirect('currenttodos')
#             except IntegrityError:
#                 return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'That username is already taken. Please choose a new username!'})
#         else:
#             return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match!'})
            
            
            
# def signupuserEn(request):
#     if request.method =='GET':
#         return render(request, 'todo/signupuserEn.html', {'form': UserCreationForm()})
#     else:
#         # Create a new user
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'] , password=request.POST['password1'])
#                 user.save()
#                 login(request , user)
#                 return redirect('currenttodosEn')
#             except IntegrityError:
#                 return render(request, 'todo/signupuserEn.html', {'form': UserCreationForm(), 'error': 'That username is already taken. Please choose a new username!'})
#         else:
#             return render(request, 'todo/signupuserEn.html', {'form': UserCreationForm(), 'error': 'Passwords did not match!'})
            



# def loginuser(request):
#     if request.method =='GET':
#         return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'username and password did not match!'})
#         else:
#             login(request , user)
#             return redirect('currenttodos')
            
            
            
            
# def loginuserEn(request):
#     if request.method =='GET':
#         return render(request, 'todo/loginuserEn.html', {'form': AuthenticationForm()})
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'todo/loginuserEn.html', {'form': AuthenticationForm(), 'error': 'username and password did not match!'})
#         else:
#             login(request , user)
#             return redirect('currenttodosEn')
            
            
            
            
def contact(request):
    if request.method == "POST":
        message_fname = request.POST['name']
        #message_lname = request.POST['surname']
        message_number = request.POST['phone']
        message_email = request.POST['email']
        message = request.POST['message']

        # Sending EMAIL
        send_mail(
        "Email from: " + message_fname , #Subject
        "Email from: " + message_fname + " " + 
        "\n" + "Email Address: " + message_email + "\n" +
        "Contact Number: " + message_number + "\n" + message,  #Message
        message_email, #from Email
        ['info@pythonclub.ir'], # To Email
        )
        return render(request, 'todo/contact.html',{'message_fname': message_fname})
    else:
        return render(request, 'todo/contact.html', {})
            




def contactEn(request):
    if request.method == "POST":
        message_fname = request.POST['name']
        #message_lname = request.POST['surname']
        message_number = request.POST['phone']
        message_email = request.POST['email']
        message = request.POST['message']

        # Sending EMAIL
        send_mail(
        "Email from: " + message_fname , #Subject
        "Email from: " + message_fname + " " + 
        "\n" + "Email Address: " + message_email + "\n" +
        "Contact Number: " + message_number + "\n" + message,  #Message
        message_email, #from Email
        ['info@pythonclub.ir'], # To Email
        )
        return render(request, 'todo/contactEn.html',{'message_fname': message_fname})
    else:
        return render(request, 'todo/contactEn.html', {})






# @login_required
# def logoutuser(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('home')
        
        
        
# @login_required
# def logoutuserEn(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('en')
        
        

@login_required
def createtodo(request):
    if request.method =='GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(), 'error':'Bad Data Passed in!'})




@login_required
def createtodoEn(request):
    if request.method =='GET':
        return render(request, 'todo/createtodoEn.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodosEn')
        except ValueError:
            return render(request, 'todo/createtodoEn.html', {'form': TodoForm(), 'error':'Bad Data Passed in!'})





@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos':todos})



@login_required
def currenttodosEn(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodosEn.html', {'todos':todos})




@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completedtodos.html', {'todos':todos})




@login_required
def completedtodosEn(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completedtodosEn.html', {'todos':todos})





@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method =='GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form, 'error':'Bad Info!'})






@login_required
def viewtodoEn(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method =='GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodoEn.html', {'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodosEn')
        except ValueError:
            return render(request, 'todo/viewtodoEn.html', {'todo':todo, 'form':form, 'error':'Bad Info!'})






@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method =='POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')





@login_required
def completetodoEn(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method =='POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodosEn')





@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method =='POST':
        todo.delete()
        return redirect('currenttodos')
        




@login_required
def deletetodoEn(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method =='POST':
        todo.delete()
        return redirect('currenttodosEn')

 
        

def PythonProjects(request):
    return render(request, 'library/PythonProjects.html', {})
    
def pytorch(request):
    return render(request, 'library/pytorch.html', {})
    
def scikitlearn(request):
    return render(request, 'library/scikitlearn.html', {})
    
def tenforflow(request):
    return render(request, 'library/tenforflow.html', {})
    
def opencv(request):
    return render(request, 'library/opencv.html', {})
    
def flask(request):
    return render(request, 'library/flask.html', {})
    
def django(request):
    return render(request, 'library/django.html', {})
    
def numpy(request):
    return render(request, 'library/numpy.html', {})
    
def pandas(request):
    return render(request, 'library/pandas.html', {})
    
def scipy(request):
    return render(request, 'library/scipy.html', {})
    
def matplotlib(request):
    return render(request, 'library/matplotlib.html', {})
    
def wxpython(request):
    return render(request, 'library/wxpython.html', {})
    
def gtk(request):
    return render(request, 'library/gtk.html', {})
    
def pyqt(request):
    return render(request, 'library/pyqt.html', {})
    
def tkinter(request):
    return render(request, 'library/tkinter.html', {})
    
def pyside(request):
    return render(request, 'library/pyside.html', {})
    
def sqlite(request):
    return render(request, 'library/sqlite.html', {})
    
def pygame(request):
    return render(request, 'library/pygame.html', {})
    
def oop(request):
    return render(request, 'library/oop.html', {})    
    
def designpattern(request):
    return render(request, 'library/designpattern.html', {})    





def PythonProjectsEn(request):
    return render(request, 'library/PythonProjectsEn.html', {})

def pytorchEn(request):
    return render(request, 'library/pytorchEn.html', {})
    
def scikitlearnEn(request):
    return render(request, 'library/scikitlearnEn.html', {})
    
def tenforflowEn(request):
    return render(request, 'library/tenforflowEn.html', {})
    
def opencvEn(request):
    return render(request, 'library/opencvEn.html', {})
    
def flaskEn(request):
    return render(request, 'library/flaskEn.html', {})
    
def djangoEn(request):
    return render(request, 'library/djangoEn.html', {})
    
def numpyEn(request):
    return render(request, 'library/numpyEn.html', {})
    
def pandasEn(request):
    return render(request, 'library/pandasEn.html', {})
    
def scipyEn(request):
    return render(request, 'library/scipyEn.html', {})
    
def matplotlibEn(request):
    return render(request, 'library/matplotlibEn.html', {})
    
def wxpythonEn(request):
    return render(request, 'library/wxpythonEn.html', {})
    
def gtkEn(request):
    return render(request, 'library/gtkEn.html', {})
    
def pyqtEn(request):
    return render(request, 'library/pyqtEn.html', {})
    
def tkinterEn(request):
    return render(request, 'library/tkinterEn.html', {})
    
def pysideEn(request):
    return render(request, 'library/pysideEn.html', {})
    
def sqliteEn(request):
    return render(request, 'library/sqliteEn.html', {})
    
def pygameEn(request):
    return render(request, 'library/pygameEn.html', {})
    
def oopEn(request):
    return render(request, 'library/oopEn.html', {})    
    
def designpatternEn(request):
    return render(request, 'library/designpatternEn.html', {})    
    
    
    
    
    
    
    
    
    
    
    
    
    







