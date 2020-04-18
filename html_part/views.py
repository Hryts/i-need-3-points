from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def poems_view(request, *args, **kwargs):
    return render(request, 'poems.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def html_view(request, *args, **kwargs):
    return render(request, 'html_basic.html', {})

def html_intro_view(request, *args, **kwargs):
   return render(request, 'html_intro.html', {})

def html_django_view(request, *args, **kwargs):
  return render(request, 'html_django.html', {})

def css_view(request, *args, **kwargs):
    return render(request, 'css_basic.html', {})

def css_intro_view(request, *args, **kwargs):
    return render(request, 'css_intro.html', {})

def css_history_view(request, *args, **kwargs):
    return render(request, 'css_history.html', {})
