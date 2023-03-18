from django.shortcuts import render


from marketplace.models import ProductoFijo

# Create your views here.
def home(request):
    objetos = ProductoFijo.objects.all()[:8]

    context = {'items':objetos}
    return render(request,'sp/index.html',context)


def acerca(request):

    return render(request,'sp/acerca.html')
    