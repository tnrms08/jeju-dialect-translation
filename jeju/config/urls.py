"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dialect import views
from django.conf.urls.static import static
from django.conf import settings

"""dialect url 설정"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dialect/', views.Postview.as_view(), name='main_page'),
    path('trans/', views.Postview.success, name='trans_suc'),
    path('dictionary/', views.Postview.dic, name='dictionary'),
    path('dictionary/dictionary.html', views.dict_list0, name='dictionary'),
    path('dictionary/dict_list1.html', views.dict_list1, name='dict_list1'),
    path('dictionary/dict_list2.html', views.dict_list2, name='dict_list2'),
    path('dictionary/dict_list3.html', views.dict_list3, name='dict_list3'),
    path('dictionary/dict_list4.html', views.dict_list4, name='dict_list4'),
    path('dictionary/dict_list5.html', views.dict_list5, name='dict_list5'),
    path('dictionary/dict_list6.html', views.dict_list6, name='dict_list6'),
    path('dictionary/dict_list7.html', views.dict_list7, name='dict_list7'),
    path('dictionary/dict_list8.html', views.dict_list8, name='dict_list8'),
    path('dictionary/dict_list9.html', views.dict_list9, name='dict_list9'),
    path('dictionary/dict_list10.html', views.dict_list10, name='dict_list10'),
    path('dictionary/dict_list11.html', views.dict_list11, name='dict_list11'),
    path('dictionary/dict_list12.html', views.dict_list12, name='dict_list12'),
    path('dictionary/dict_list13.html', views.dict_list13, name='dict_list13'),
    path('dictionary/dict_list14.html', views.dict_list14, name='dict_list14'),
    path('dictionary/dict_list15.html', views.dict_list15, name='dict_list15'),
    path('dictionary/dict_list16.html', views.dict_list16, name='dict_list16'),
    path('dictionary/dict_list17.html', views.dict_list17, name='dict_list17'),
    path('dictionary/dict_list18.html', views.dict_list18, name='dict_list18'),
    path('dictionary/dict_list19.html', views.dict_list19, name='dict_list19'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
