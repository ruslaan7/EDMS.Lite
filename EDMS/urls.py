"""EDMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from project import views

from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('sign_in/', LoginView.as_view(template_name='sign_in.html'), name='sign_in'),
    path('sing_out/', LogoutView.as_view(next_page='/'), name='sign_out'),

    path('account/', views.account, name='account'),
    path('docs/', views.docs, name='docs'),
    path('docs/add', views.docsadd, name='docsadd'),
    path('docs/edit/<int:doc_id>/', views.docsedit, name='docsedit'),
    path('docs/delete', views.docsdelete, name='docsdelete'),
    path('docs/send', views.docssend, name='docssend'),
    path('docs/send/<int:doc_id>/', views.docssenduser, name='docssenduser'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
