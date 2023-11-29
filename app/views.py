from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(req):
    items = Tovar.objects.all()
    data = {'tovari': items}
    return render(req, 'index.html', context=data)


def buy(req, id):
    item = Tovar.objects.get(id=id)
    if Korzina.objects.filter(tovar_id=id):
        selected = Korzina.objects.get(tovar_id=id)
        selected.count += 1
        selected.summa = selected.calcSumma()
        selected.save()
    else:
        Korzina.objects.create(count=1, tovar=item, summa=item.price)
    return redirect('home')


def cart(req):
    items = Korzina.objects.all()
    summa = 0
    for i in items:
        summa += i.summa
    data = {'items': items, 'summa': summa}
    return render(req, 'cart.html', context=data)


def delete(req, id):
    Korzina.objects.get(id=id).delete()
    return redirect('cart')


def plus(req, id):
    item = Korzina.objects.get(id=id)
    item.count += 1
    item.summa = item.calcSumma()
    item.save()
    return redirect('cart')


def minus(req, id):
    item = Korzina.objects.get(id=id)
    if item.count > 1:
        item.count -= 1
        item.summa = item.calcSumma()
        item.save()
    else:
        item.delete()
    return redirect('cart')


def cartcomplete(req):
    return HttpResponse('<h1>спасибо за заказ</h1>')

