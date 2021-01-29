from django.http import HttpResponse
from django.template import Template, Context

def home(request):

    doc_externo=open("C:/Users/josue/Desktop/webframework/ambientelaboral/ambientelaboral/templates/index.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)

def encuesta(request):
    return 0

def resultados(request):
    return 0