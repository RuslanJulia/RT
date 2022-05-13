import email
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, FormView, CreateView
import locale
from main.models import *
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Count
import simplejson
from django.core.mail import BadHeaderError, send_mail
import random

locale.setlocale(locale.LC_ALL, '')


class Main_Page(View):
    form_class = Login_Form
    success_url = reverse_lazy('Main_Page')
    template_name = 'main_page.html'

    def get(self, request, *args, **kwargs):
        sorted_recepts = Recepts.objects.filter().order_by('-date')[:4]
        form = self.form_class(request.POST)
        context = {
            'sorted_recepts': sorted_recepts,
            'form': form,
        }
        return render(
            request,
            'main_page.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Second_Budes_With_Photos(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=5)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'Second_budes_with_photos.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Second_Budes_List(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=5)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'second_budes_list.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Desserts_With_Photos(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=7)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'desserts_with_photos.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Desserts_List(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=7)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'desserts_list.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Salads_With_Photos(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=6)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'salads_with_photos.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Salads_List(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=6)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'salads_list.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Soups_With_Photos(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=4)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'soups_with_photos.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Soups_List(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=4)
        sub_category = Sub_Category.objects.all().filter(category=category.id)
        form = self.form_class(request.POST)
        recepts = []
        for i in sub_category:
            recepts1 = Recepts.objects.all().filter(subcategory=i.id).order_by(
                '-date')
            recepts.append(recepts1)
        context = {
            'recepts': recepts,
            'sub_category': sub_category,
            'form': form,
        }
        return render(
            request,
            'soups_list.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Contacts(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        return render(
            request,
            'contacts.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Help(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        return render(
            request,
            'help.html',
            context=context,
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password1']
                if '@' in uname:
                    username = User.objects.filter(email=uname)
                    name = []
                    for i in username:
                        name.append(i.username)
                    user = authenticate(username=name[0], password=upass)
                else:
                    user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponse(simplejson.dumps({'result': 'success'}))
                else:
                    response = {'error': '1'}
                    for k in form.errors:
                        response[k] = form.errors[k][0]
                    return HttpResponse(simplejson.dumps({'response': response, 'result': 'error'}))
        else:
            form = AuthenticationForm()
        return render(request, 'main_page.html', {'form': form})


class Recipe(View):
    form_class = Login_Form

    def get(self, request, pk, *args, **kwargs):
        recipe = Recepts.objects.get(pk=pk)

        enumerated_cooking_method = []
        enumerated_ingredients = []

        ingredients = recipe.ingredients.split(',')
        cooking_method = recipe.cooking_method.split(';')

        for ingredients_en, enu_1 in enumerate(ingredients):
            enumerated_ingredients.append([ingredients_en + 1, enu_1])
        enumerated_ingredients_dict = {
            x[1]: x[0] for x in enumerated_ingredients
        }

        for cooking_method_en, enu in enumerate(cooking_method):
            enumerated_cooking_method.append([cooking_method_en + 1, enu])
        enumerated_cooking_method_dict = {
            x[1]: x[0] for x in enumerated_cooking_method
        }

        comment = Comments.objects.filter(recept_id=pk)
        form = self.form_class(request.POST)

        context = {
            'recipe': recipe,
            'ingredients': ingredients,
            'enumerated_cooking_method_dict': enumerated_cooking_method_dict,
            'enumerated_ingredients_dict': enumerated_ingredients_dict,
            'comments': comment,
            'form': form,
        }
        return render(
            request,
            'recipe.html',
            context=context,
        )

    def post(self, request, pk, *args, **kwargs):
        if request.POST.get('comment'):
            form = self.form_class(request.POST)
            recipe = Recepts.objects.get(pk=pk)
            user = User.objects.get(username=request.user)
            sub_category = Recepts.objects.get(pk=pk)
            Comments.objects.get_or_create(
                recept_id=sub_category,
                user=user,
                comment_date=datetime.now().date(),
                comment=request.POST.get('comment')
            )
            recipe = Recepts.objects.get(pk=pk)
            user = User.objects.get(username=request.user)
            user.recept_id.add(recipe)
            enumerated_cooking_method = []
            enumerated_ingredients = []
            ingredients = recipe.ingredients.split(',')
            cooking_method = recipe.cooking_method.split(';')

            for ingredients_en, enu_1 in enumerate(ingredients):
                enumerated_ingredients.append([ingredients_en + 1, enu_1])
            enumerated_ingredients_dict = {
                x[1]: x[0] for x in enumerated_ingredients
            }

            for cooking_method_en, enu in enumerate(cooking_method):
                enumerated_cooking_method.append([cooking_method_en + 1, enu])
            enumerated_cooking_method_dict = {
                x[1]: x[0] for x in enumerated_cooking_method
            }
            comment = Comments.objects.filter(recept_id=pk)
            users = User.objects.annotate(ratings=Count('comments'))
            for user_count in users:
                User.objects.filter(username=user_count.username).update(count_comments=user_count.ratings)
            context = {
                'recipe': recipe,
                'ingredients': ingredients,
                'enumerated_cooking_method_dict': enumerated_cooking_method_dict,
                'enumerated_ingredients_dict': enumerated_ingredients_dict,
                'comments': comment,
                'form': form,
            }
            return render(
                request,
                'recipe.html',
                context=context,
            )
        recipe = Recepts.objects.get(pk=pk)
        user = User.objects.get(username=request.user)
        user.recept_id.add(recipe)
        enumerated_cooking_method = []
        enumerated_ingredients = []
        form = self.form_class(request.POST)
        ingredients = recipe.ingredients.split(',')
        cooking_method = recipe.cooking_method.split(';')

        for ingredients_en, enu_1 in enumerate(ingredients):
            enumerated_ingredients.append([ingredients_en + 1, enu_1])
        enumerated_ingredients_dict = {
            x[1]: x[0] for x in enumerated_ingredients
        }

        for cooking_method_en, enu in enumerate(cooking_method):
            enumerated_cooking_method.append([cooking_method_en + 1, enu])
        enumerated_cooking_method_dict = {
            x[1]: x[0] for x in enumerated_cooking_method
        }
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
            'enumerated_cooking_method_dict': enumerated_cooking_method_dict,
            'enumerated_ingredients_dict': enumerated_ingredients_dict,
            'form': form,
        }
        return render(
            request,
            'recipe.html',
            context=context,
        )


class New_Recipe(View):
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        current_date = datetime.now().date()
        category = Category.objects.all()
        sub_category = Sub_Category.objects.all()
        context = {
            'date': current_date,
            'categoryes': category,
            'sub_categoryes': sub_category,
        }
        return render(
            request,
            'new_recipe.html',
            context=context
        )

    def post(self, request, *args, **kwargs):
        if request.POST.get('add_subcategory'):
            category_id = Category.objects.get(name=request.POST.get('category'))
            category = Category.objects.get(pk=category_id.id)
            Sub_Category.objects.get_or_create(
                name=request.POST.get('add_subcategory'),
                category=category
            )
        elif request.POST.get('category') == 'Супы':
            category = Category.objects.get(pk=4)
            sub_category_id = Sub_Category.objects.get(name=request.POST.get('subcategory1'))
            sub_category = Sub_Category.objects.get(pk=sub_category_id.id)
            Recepts.objects.get_or_create(
                name=request.POST.get('name'),
                photo=request.FILES['photo'],
                category=category,
                subcategory=sub_category,
                description=request.POST.get('description'),
                ingredients=request.POST.get('ingredients'),
                cooking_method=request.POST.get('cooking_method'),
                date=datetime.now().date()
            )
        elif request.POST.get('category') == 'Вторые блюда':
            category = Category.objects.get(pk=5)
            sub_category_id = Sub_Category.objects.get(name=request.POST.get('subcategory2'))
            sub_category = Sub_Category.objects.get(pk=sub_category_id.id)
            Recepts.objects.create(
                name=request.POST.get('name'),
                photo=request.FILES['photo'],
                category=category,
                subcategory=sub_category,
                description=request.POST.get('description'),
                ingredients=request.POST.get('ingredients'),
                cooking_method=request.POST.get('cooking_method'),
                date=datetime.now().date()
            )
        elif request.POST.get('category') == 'Салаты':
            category = Category.objects.get(pk=6)
            sub_category_id = Sub_Category.objects.get(name=request.POST.get('subcategory3'))
            sub_category = Sub_Category.objects.get(pk=sub_category_id.id)
            Recepts.objects.create(
                name=request.POST.get('name'),
                photo=request.FILES['photo'],
                category=category,
                subcategory=sub_category,
                description=request.POST.get('description'),
                ingredients=request.POST.get('ingredients'),
                cooking_method=request.POST.get('cooking_method'),
                date=datetime.now().date()
            )
        elif request.POST.get('category') == 'Десерты':
            category = Category.objects.get(pk=7)
            sub_category_id = Sub_Category.objects.get(name=request.POST.get('subcategory4'))
            sub_category = Sub_Category.objects.get(pk=sub_category_id.id)
            Recepts.objects.create(
                name=request.POST.get('name'),
                photo=request.FILES['photo'],
                category=category,
                subcategory=sub_category,
                description=request.POST.get('description'),
                ingredients=request.POST.get('ingredients'),
                cooking_method=request.POST.get('cooking_method'),
                date=datetime.now().date()
            )
        return HttpResponseRedirect('/Главная страница/')


class Register(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('confirmation')
    template_name = 'register.html'
    verification_code = random.randint(1000, 9999)

    def form_valid(self, form: form_class):
        try:
            send_mail(
                'Подтверждение на сайте (Здесь напишешь название сайта)',
                'Код подтверждения: {}'.format(self.verification_code),
                'recipetens@gmail.com',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            instance = form.save(commit=False)
            instance.verification_code = self.verification_code
            instance.save()
        except:
            return HttpResponseRedirect('/Главная страница/')
        return super().form_valid(form)

    def form_invalid(self, form: form_class):
        print(form)
        return super().form_invalid(form)


class Confirmation_Of_Registration(View):
    form_class = Confirmation
    success_url = reverse_lazy('Main_Page')
    template_name = 'confirmation_of_registration.html'
    user = User.objects.all().order_by('-id')[:1]

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'users': self.user,
            'form': form,
        }
        return render(
            request,
            self.template_name,
            context=context
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        message = 'Введен неверный код подтверждения'
        context = {
            'users': self.user,
            'form': form,
            'message': message,
        }

        if form.is_valid():
            for activate in self.user:
                if int(request.POST.get('verification_code')) == activate.verification_code:
                    activate.is_active = True
                    activate.save()
                    return redirect(self.success_url)
        return render(
            request,
            self.template_name,
            context=context,
        )


class Profile(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        recepts = user.recept_id.all()
        context = {
            'recepts': recepts,
        }
        return render(
            request,
            'profile.html',
            context=context
        )
