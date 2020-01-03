from django.conf.urls import url
from . import views

urlpatterns = [
    # 判断用户名是否重复
    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # 注册
    url(r'^register/$', views.RegisterView.as_view()),
    # 用户名登录的子路由:
    url(r'^login/$', views.LoginView.as_view()),
    # 用户中心的子路由
    url(r'^info/$', views.UserInfoView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    # 用户中心的子路由
    url(r'^info/$', views.UserInfoView.as_view()),
    # 添加邮箱
    url(r'^emails/$', views.EmailView.as_view()),
    # 验证邮箱
    url(r'^emails/verification/$', views.VerifyEmailView.as_view()),
    # 新增收货地址
    url(r'^addresses/create/$', views.CreateAddressView.as_view()),
    url(r'^addresses/$', views.AddressView.as_view()),
    # 修改和删除收货地址
    url(r'^addresses/(?P<address_id>\d+)/$', views.UpdateDestroyAddressView.as_view()),
    # 设置默认地址
    url(r'^addresses/(?P<address_id>\d+)/default/$', views.DefaultAddressView.as_view()),
    # 更新地址标题
    url(r'^addresses/(?P<address_id>\d+)/title/$', views.UpdateTitleAddressView.as_view()),
    # 修改密码
    url(r'^password/$', views.ChangePasswordView.as_view()),
]
