from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import random
from.forms import *



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


# def buy(req, id):
#     item = Tovar.objects.get(id=id)
#     user = req.user
#     # if not user.username:
#     #     newuser = User.objects.create_user(username='Tempuser')
#     #
#     if user.username:
#         if Korzina.objects.filter({'tovar_id': id, 'user_id': user.id}):
#             selected = Korzina.objects.get(tovar_id=id)
#             selected.count += 1
#             selected.summa = selected.calcSumma()
#             selected.save()
#         else:
#             Korzina.objects.create(count=1, tovar=item, summa=item.price, user_id=user.id)
#     # else:
#     #     newuser = User.objects.create_user(username='Tempuser')
#     #
#     #     Korzina.objects.create(count=1, tovar=item, summa=item.price)
#     return redirect('home')


def cart(req):
    items = Korzina.objects.filter(user_id=req.user.id)
    myform = MyForm()
    summa = 0
    for i in items:
        summa += i.summa
    if req.POST:
        myform = MyForm(req.POST)
        if myform.is_valid():
            print('valid')
    data = {'items': items, 'summa': summa, 'form': myform}
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


def cart_to_order(Korzina_model, Zakaz_model, address, name, phone):
    zakaz = Zakaz_model.objects.create(address=address, name=name, phone=phone, total=0)
    zakazitemsstr = ''
    for i in Korzina_model.objects.all():
        Zacazitems.objects.create(tovar=i.tovar, count=i.count, zakaz=zakaz)
        zakaz.total += i.summa
        zakaz.save()
        zakazitemsstr += str(i.tovar.opis) + ' ' + str(i.count) + '\n'
        i.delete()
    return zakazitemsstr, zakaz.total


def pobeda(req):
    print('pobeda')
    if req.body:
        data = json.loads(req.body.decode("UTF-8"))
        address = data['address']
        name = data['name']
        phone = data['phone']
        zakazitemsstr, total = cart_to_order(Korzina, Zakaz, address, name, phone)
        print(zakazitemsstr, total)
    return JsonResponse({'mes': 'data success', 'link': '/'})


@method_decorator(csrf_exempt, name='dispatch')
def cartcomplete(req):
    print('run')
    if req.POST:
        address = req.POST.get('address')
        name = req.POST.get('name')
        phone = req.POST.get('phone')
        zakazitemsstr, total = cart_to_order(Korzina, Zakaz, address, name, phone)
        ####################################################################
        TOKEN = "6169999140:AAFzZpas7wx-gQsuFRZ0puhLNcPMYNSxsL8"
        chat_id = "50853567"
        message = zakazitemsstr + address + ' ' + name + ' ' + phone + ' ' + str(total)
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())  # Эта строка отсылает сообщение
        #######################################################################
        return JsonResponse({'mes': 'data success', 'link': '../'})
    return redirect('home')
    # return HttpResponse('<h1>спасибо за заказ</h1>')

# https://api.telegram.org/bot6169999140:AAFzZpas7wx-gQsuFRZ0puhLNcPMYNSxsL8/getUpdates   - открыть в браузере чтобы узнать chat_id


def cartcount(req, num, id):
    tovar = Korzina.objects.get(id=id)
    if tovar.count == 0 and int(num) < 0:
        tovar.delete()
    else:
        tovar.count += int(num)
        tovar.summa = tovar.calcSumma()
        tovar.save()
    return redirect('cart')
