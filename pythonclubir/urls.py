"""pythonclubir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
   
    # Todos
    path('', views.home , name='home'),
    path('en/', views.en , name='en'),
    path('contact/', views.contact , name='contact'),
    path('contactEn/', views.contactEn , name='contactEn'),
    path('create/', views.createtodo , name='createtodo'),
    path('current/', views.currenttodos , name='currenttodos'),
    path('completed/', views.completedtodos , name='completedtodos'),
    path('todo/<int:todo_pk>', views.viewtodo , name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo , name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo , name='deletetodo'),
    
    
    path('createEn/', views.createtodoEn , name='createtodoEn'),
    path('currentEn/', views.currenttodosEn , name='currenttodosEn'),
    path('completedEn/', views.completedtodosEn , name='completedtodosEn'),
    path('todo/en/<int:todo_pk>', views.viewtodoEn , name='viewtodoEn'),
    path('todo/<int:todo_pk>/completeEn', views.completetodoEn , name='completetodoEn'),
    path('todo/<int:todo_pk>/deleteEn', views.deletetodoEn , name='deletetodoEn'),
    
    
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    
    
    # Liraries
    path('PythonProjects/', views.PythonProjects , name='PythonProjects'),
    path('pytorch/', views.pytorch , name='pytorch'),
    path('scikitlearn/', views.scikitlearn , name='scikitlearn'),
    path('tenforflow/', views.tenforflow , name='tenforflow'),
    path('opencv/', views.opencv , name='opencv'),
    path('flask/', views.flask , name='flask'),
    path('django/', views.django , name='django'),
    path('numpy/', views.numpy , name='numpy'),
    path('pandas/', views.pandas , name='pandas'),
    path('scipy/', views.scipy , name='scipy'),
    path('matplotlib/', views.matplotlib , name='matplotlib'),
    path('wxpython/', views.wxpython , name='wxpython'),
    path('gtk/', views.gtk , name='gtk'),
    path('pyqt/', views.pyqt , name='pyqt'),
    path('tkinter/', views.tkinter , name='tkinter'),
    path('pyside/', views.pyside , name='pyside'),
    path('sqlite/', views.sqlite , name='sqlite'),
    path('pygame/', views.pygame , name='pygame'),
    path('oop/', views.oop , name='oop'),
    path('designpattern/', views.designpattern , name='designpattern'),
    
    
    path('PythonProjectsEn/', views.PythonProjectsEn , name='PythonProjectsEn'),
    path('pytorchEn/', views.pytorchEn , name='pytorchEn'),
    path('scikitlearnEn/', views.scikitlearnEn , name='scikitlearnEn'),
    path('tenforflowEn/', views.tenforflowEn , name='tenforflowEn'),
    path('opencvEn/', views.opencvEn , name='opencvEn'),
    path('flaskEn/', views.flaskEn , name='flaskEn'),
    path('djangoEn/', views.djangoEn , name='djangoEn'),
    path('numpyEn/', views.numpyEn , name='numpyEn'),
    path('pandasEn/', views.pandasEn , name='pandasEn'),
    path('scipyEn/', views.scipyEn , name='scipyEn'),
    path('matplotlibEn/', views.matplotlibEn , name='matplotlibEn'),
    path('wxpythonEn/', views.wxpythonEn , name='wxpythonEn'),
    path('gtkEn/', views.gtkEn , name='gtkEn'),
    path('pyqtEn/', views.pyqtEn , name='pyqtEn'),
    path('tkinterEn/', views.tkinterEn , name='tkinterEn'),
    path('pysideEn/', views.pysideEn , name='pysideEn'),
    path('sqliteEn/', views.sqliteEn , name='sqliteEn'),
    path('pygameEn/', views.pygameEn , name='pygameEn'),
    path('oopEn/', views.oopEn , name='oopEn'),
    path('designpatternEn/', views.designpatternEn , name='designpatternEn'),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
