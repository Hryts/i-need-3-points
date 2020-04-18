"""web_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


# from pages.views import home_view
from html_part.views import home_view, html_view,  css_view, poems_view, about_view, html_intro_view, html_django_view, css_intro_view, css_history_view

urlpatterns = [
    path('', home_view, name='home'),
    path('poems', poems_view, name='poems_view'),
    path('about', about_view, name='about_view'),
    path('html', html_view, name='html_view'),
    path('html_intro', html_intro_view, name='html_intro_view'),
    path('html_django', html_django_view, name='html_django_view'),
    path('css', css_view, name='css_view'),
    path('css_intro', css_intro_view, name='css_intro_view'),
    path('css_history', css_history_view, name='css_history_view'),

#     path('contact/', contact_view),
#     path('product/', product_detail_view),
#     path('create/', product_create_view),
#     path('about/', about_view),
#     path('admin/', admin.site.urls),
]
