from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from time import gmtime, strftime
from .models import Users, Businesses, data, Retirement
import bcrypt
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='dda6728a056040faa317235048c946d7')



def index(request):
    return render(request, "user_app/index.html")

def sign_in(request):
    return render(request, "user_app/login.html")

def create(request):
    return render(request, 'user_app/create.html')


def user(request):
    y = request.session['email']
    x = Users.objects.get(email = y)
    context = {
        'user': Users.objects.get(email = y),
        'biz': Businesses.objects.filter(user = x),
        'port': Retirement.objects.get(user = x),
        'news': newsapi.get_everything(q='stock market',
                                      sources='cnn',
                                      domains='cnn.com',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
    }
    return render(request, 'user_app/user.html', context)

def create_user(request):
    if request.method == 'POST':
        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/create')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            Users.objects.create(first_name = first_name, last_name = last_name, email = email, password= password) 
            request.session['email'] = request.POST['email'] 
            print(request.session['email'])
            request.session['email'] = request.POST['email']
            return redirect('/input_first_time')

def login(request):
    if request.method == 'POST':
            if len(Users.objects.filter(email = request.POST['emaillog'])) > 0:
                user = Users.objects.get(email = request.POST['emaillog'])

                if bcrypt.checkpw(request.POST['passlog'].encode(), user.password.encode()) and len(Users.objects.filter(email = request.POST['emaillog'])) > 0:
                    request.session['email'] = request.POST['emaillog']
                    request.session['save'] = request.POST['emaillog']
                    return redirect('/user')
                else: 
                    messages.warning(request, 'Incorrect email or password')
                    return redirect('/sign_in')
            else:
                messages.warning(request, 'Incorrect email or password')
                return redirect('/sign_in')
            

def create_biz(request):
    if request.method == "GET":
        return redirect('/')
    if request.method == "POST":
        biz_title = request.POST['biz_title']
        print(request.POST['biz_title'])
        biz_email = request.POST['biz_email']
        biz_label = request.POST['biz_label']
        market = request.POST['market']
        user = Users.objects.get(id = request.POST['user_id'] )
        Businesses.objects.create(name = biz_title, email = biz_email, user = user, stock_code = biz_label, listing= market)
        return redirect('/user')

def biz_dashboard(request, x):
    z = Businesses.objects.get(id = x)
    context = {
        'stock': Businesses.objects.get(id = x),
        'data': data.objects.filter(business = z),
    }
    return render(request, 'user_app/dashboard.html', context)

def delete(request, y):
    account_to_delete = Businesses.objects.get(id = y)
    account_to_delete.delete()
    return redirect('/user')

def logout(request):
    request.session.clear()
    return redirect('/')

def data_page(request, y):
    z = Businesses.objects.get(id = y)
    context = {
        'stock': Businesses.objects.get(id = y),
        'data': data.objects.filter(business = z)
    }
    return render(request, 'user_app/data.html', context)

def input_data(request, y):
    if request.method == 'POST':
        sales = request.POST['sales']
        products = request.POST['products']
        employees = request.POST['employees']
        busy = request.POST['busy']
        biz = Businesses.objects.get(id = busy)
        data.objects.create(sales = sales, products = products, employees = employees, business = biz)
        return redirect('/business_dashboard/' + str(y))

def retirement_data(request, y):
    context = {
        'user': Users.objects.get(id = y)
    }
    print(z.id)
    return render(request, 'user_app/retire_data.html', context)

def input_retire_data(request):
    if request.method == "POST":
        asset_type_one = request.POST['asset_one']
        per_one = request.POST['percent_one']
        asset_type_two = request.POST['asset_two']
        per_two = request.POST['percent_two']
        asset_type_three = request.POST['asset_three']
        per_three = request.POST['percent_three']
        x = request.POST['busy']
        user = Users.objects.get(id = x)
        print(x)
        Retirement.objects.create(asset_one = asset_type_one, asset_two = asset_type_two, asset_three = asset_type_three, asset_one_percentage = per_one, asset_two_percentage = per_two, asset_three_percentage = per_three, user = user)
        return redirect('/user')

def change_retire_data(request, y):
    z = Users.objects.get(id = y)
    context = {
        'user': Users.objects.get(id = y)
    }
    return render(request, 'user_app/change_retire.html', context)

def change_retirement_plan(request):
    y = Users.objects.get(email = request.session['email'])
    if request.method == 'POST':
        change_to_update = Retirement.objects.get(user = y)
        change_to_update.asset_one = request.POST['asset_one']
        change_to_update.asset_one_percentage = request.POST['percent_one']
        change_to_update.asset_two = request.POST['asset_two']
        change_to_update.asset_two_percentage = request.POST['percent_two']
        change_to_update.asset_three = request.POST['asset_three']
        change_to_update.asset_three_percentage = request.POST['percent_three']
        change_to_update.save()
        return redirect('/user')

def first_time_data(request):
    y = request.session['email']
    context = {
        'user': Users.objects.get(email = y)

    }
    return render(request, 'user_app/first_time_retire.html', context)

def input_new(request):
    if request.method == "POST":
        asset_type_one = request.POST['asset_one']
        per_one = request.POST['percent_one']
        asset_type_two = request.POST['asset_two']
        per_two = request.POST['percent_two']
        asset_type_three = request.POST['asset_three']
        per_three = request.POST['percent_three']
        x = request.POST['busy']
        user = Users.objects.get(id = x)
        print(x)
        Retirement.objects.create(asset_one = asset_type_one, asset_two = asset_type_two, asset_three = asset_type_three, asset_one_percentage = per_one, asset_two_percentage = per_two, asset_three_percentage = per_three, user = user)
        return redirect('/user')