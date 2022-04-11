from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from elements.models import *
from elements.functions import *

# Create your views here.
def elements(request, *args, **kwargs):
    my_dict = {}
    elements = Element.objects.all()
    if elements.count() < 115:
        print('')
        print('Please wait, your database is being populated.')
        print('')
        populate_db()
        elements = Element.objects.all()
    for n in range(1, 6):
        for m in range (1, 19):
            element = Element.objects.filter(period=n).filter(group=m)
            if element.count() > 0:
                element = element.first()
                print(element.symbol, element.name)
                key = str(n) + "_" + str(m)
                print(element.cpx_hex_color)
                my_dict.update({key:element})
    print(my_dict)
    return render(request, 'elements/elements.html', context=my_dict)


def element_detail(request, symbol, *args, **kwargs):
    my_dict = {}
    element = Element.objects.get(symbol__iexact=symbol)
    print(element)
    my_dict.update({'element':element})
    return render(request, 'elements/element_detail.html', context=my_dict)
