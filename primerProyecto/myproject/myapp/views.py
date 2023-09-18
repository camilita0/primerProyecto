from django.shortcuts import render

#Create your views here.
from django.http import HttpResponse

#def index ( request ):
#      return HttpResponse( "¡Hola, mundo!" ) #va a levantar en el navegador ¡Hola, mundo! 

def index( request ): 
      return render( request,"index.html" )

