from django.conf.urls import url
from xiaomi_users.views import user_login, user_logout, user_register, user_comment

urlpatterns = [
    url(r'^login$', user_login, name='user_login'),
    url(r'^logout$', user_logout, name='user_logout'),
    url(r'^register$', user_register, name='user_register'),
    url(r"^comment/(?P<phone_id>\d+)$", user_comment, name="user_comment"),
    # url(r'^cart/$', cart),
    # url(r'^additem/(\d+)/(\d+)/$', add_to_cart, name='additem-url'),
    # url(r'^removeitem/(\d+)/$', remove_from_cart, name='removeitem-url'),

]
