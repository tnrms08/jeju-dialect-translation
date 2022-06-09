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
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
