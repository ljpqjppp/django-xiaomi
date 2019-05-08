from django.shortcuts import render, HttpResponse
from xiaomi_users.forms import UserLogin,RegForm,UserPhoneCommentForm
from xiaomi_users.models import PhoneDetail


def index(request):
    # longin_form = UserLogin()
    # register_form = RegForm()
    star_phones = PhoneDetail.objects.filter(kind__name='star')
    return render(request, 'index.html', {
                                            'star_phones':star_phones
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


def gouwuche(request):
    return render(request, 'gouwuche.html')


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
    # return HttpResponse(movie.title)
    login_form = UserLogin()
    register_form = RegForm()
    comment_form = UserPhoneCommentForm()
    CommentModel = UserPhoneCommentForm.Meta.model
    comments = CommentModel.objects.filter(phone_id=phone_id).order_by('-id')
    return render(request, 'xiangqing.html', {'login_form': login_form,
                                           "reg_form": register_form, 'phone': phone, "comment_form": comment_form,
                                           "comments": comments})

