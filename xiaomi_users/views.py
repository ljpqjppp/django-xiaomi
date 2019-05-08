from django.shortcuts import render,HttpResponse,redirect
from xiaomi_users.models import MyUsers
from xiaomi_users.forms import UserLogin,RegForm,UserPhoneCommentForm
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password,make_password
from copy import deepcopy

def user_login(request):
    if request.method == 'POST':
        # refer_url = request.META['HTTP_REFERER']
        userlogin = UserLogin(request.POST)
        if not userlogin.is_valid():
            return HttpResponse('无效')
        data = userlogin.cleaned_data
        try:
            user = MyUsers.objects.filter(username=data['name'])[0]
        except Exception:
            return HttpResponse('用户不存在!')
        encode_pwd = user.password
        is_true = False
        if check_password(data['pwd'], encode_pwd):
            is_true = True
        if is_true:
            login(request, user)
            return redirect('/index/')
        else:
            return HttpResponse('密码错误')


def user_logout(request):
    # refer_url = request.META['HTTP_REFERER']
    logout(request)
    return redirect('/index/')


def user_register(request):
    form = RegForm(request.POST)
    if not form.is_valid():
        return HttpResponse("请检查提交的参数")
    form.instance.password = make_password(form.instance.password)
    user = form.save()
    login(request, user)
    # refer_url = request.META['HTTP_REFERER']

    return redirect('/index/')


def user_comment(request, phone_id):
    refer_url = request.META['HTTP_REFERER']
    data = deepcopy(request.POST)
    try:
        data['user'] = request.user.pk
    except Exception:
        data['user'] = 0
    data['phone'] = phone_id
    res_data = UserPhoneCommentForm(data)
    if not res_data.is_valid():
        # return redirect(refer_url)
        return redirect(refer_url)
    res_data.save()
    # return redirect(refer_url)
    return redirect(refer_url)
