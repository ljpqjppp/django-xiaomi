from django.shortcuts import render, HttpResponse, redirect
from xiaomi_users.forms import UserLogin,RegForm,UserPhoneCommentForm
from xiaomi_users.models import PhoneDetail
from xiaomi_views.models import PhoneCart



def index(request):

    star_phones = PhoneDetail.objects.filter(kind__name='star').order_by('-hits')
    dajiadian = PhoneDetail.objects.filter(kind__name='dajiadian')
    xiaojiadian = PhoneDetail.objects.filter(kind__name='xiaojiadian')
    CommentModel = UserPhoneCommentForm.Meta.model
    comments = CommentModel.objects.all()
    di_dajiadian = {}
    di_xiaojiadian = {}

    for i,k in zip(dajiadian,comments[0:4]):
        di_dajiadian[i]=k
    for i,k in zip(xiaojiadian, comments[4:7]):
        di_xiaojiadian[i]=k


    return render(request, 'index.html', {
                                            'star_phones':star_phones,
                                            'dajiadian': di_dajiadian,
                                            'xiaojiadian': di_xiaojiadian,
                                          })


def login(request):
    longin_form = UserLogin()
    register_form = RegForm()
    return render(request, 'login.html', {'login_form':longin_form,
                                          'reg_form':register_form
                                          })


def register(request):
    longin_form = UserLogin()
    register_form = RegForm()
    return render(request, 'register.html', {'login_form':longin_form,
                                          'reg_form':register_form
                                          })


def dingdan(request):
    return render(request, 'dingdanzhongxin.html')


def liebiao(request):
    xiaomi_phones = PhoneDetail.objects.filter(kind__name='xiaomi')
    hongmi_phones = PhoneDetail.objects.filter(kind__name='hongmi')
    return render(request, 'liebiao.html',{'xiaomi':xiaomi_phones,
                                           'hongmi':hongmi_phones})


def self_info(request):
    return render(request, 'self_info.html')

def index1(request, phone_id):
    try:
        phone = PhoneDetail.objects.filter(pk=phone_id)[0]
                                    # pk = pramary key = 主键 =id path是上面传入的参数
                                    # 因为pk=movie_id查询出来只会有一天数据 所以切片只能为[0]，不切片他不会查询
    except Exception:
        return HttpResponse('找不到')
    n = phone.hits
    PhoneDetail.objects.filter(pk=phone_id).update(hits=n+1)

    print(phone.hits)




    # login_form = UserLogin()
    # register_form = RegForm()
    comment_form = UserPhoneCommentForm()
    # CommentModel = UserPhoneCommentForm.Meta.model
    # comments = CommentModel.objects.filter(phone_id=phone_id).order_by('-id')
    return render(request, 'xiangqing.html', {'phone': phone,
                                              'conmment_form':comment_form})


def search(request):
    phone_name = request.POST['phone_name']
    try:
        phone = PhoneDetail.objects.filter(title=phone_name)[0]
    except Exception:
        return HttpResponse('找不到')
    return render(request, 'xiangqing.html', {'phone': phone})

def addgouwuche(request):
    http1 = request.META['HTTP_REFERER']
    id = int(http1.split('/', -1)[-1])
    ids = []
    phone_ids = PhoneCart.objects.all().values('phone_id')
    for i in phone_ids:
        id1 = i['phone_id']
        ids.append(id1)
    if id not in ids:
        num = 1
        PhoneCart.objects.create(phone_id=id, number=num)
    else:
        n = PhoneCart.objects.get(phone_id=id).number
        PhoneCart.objects.filter(phone_id=id).update(number=n + 1)
    return render(request, 'tijiao_gouwuche.html')


def showgouwuche(request):
    gouwuche = PhoneCart.objects.all()
    prices = []
    numbers = []
    totle = 0
    for i in gouwuche:
        prices.append(i.phone.price)
    nums = PhoneCart.objects.all().values('number')
    for num in nums:
        num1 = num['number']
        numbers.append(num1)

    print(prices)
    print(numbers)
    for i,j in zip(prices, numbers):
        one = i * j
        totle = totle + one
    print(totle)

    return render(request, 'gouwuche.html', {'mygouwuche': gouwuche,
                                             'totle': totle})




