
from django.http import HttpResponse
from datetime import date, datetime
from django.template import Template, Context
from AppCoder.models import Curso
#from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django -Coder")

    
def otra_vista(request):
    return HttpResponse ("<h1>¡Esto es un titulo!</h1><p>y este es un parrafo.</p>")

def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")

def mi_cumpleaños(request):
    return HttpResponse("Mi cumpleaños en el 5 de junio!")

def muestra_nombre(self,nombre):
    return HttpResponse(f"Buenos dias {nombre}, bienvenido a Coder")

def comi(self,comida):
    return HttpResponse(f"Hoy comi {comida}")

def despedira(request):
    return HttpResponse ("Adios panas!!")

def probando_template(request):

    nom = "Eleonora"
    ap = "Sosa"
    ed = "23"
    ciu = "Còrdoba"

    lista_notas = [1,2,3,4,5,6,7,8,9]

    diccionario = {"nombre":nom, "apellido":ap, "edad":ed, "hoy": datetime.now(), "notas":lista_notas, "ciudad":ciu}

    mi_html = open ("C:/Users/eleonora/OneDrive/Imágenes/OneDrive/Escritorio/Python Proyrcto1/Proyecto1/plantilla/template1.html")

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context( diccionario)

    #plantilla = loader.get_template('template1.html')

    documento = plantilla.render(mi_contexto)


    return HttpResponse(documento)

def agregar_curso(request, nom, cam):
    curso = Curso(nombre=nom, camada=cam)
    curso.save()

    return HttpResponse("Curso agregado!!")    