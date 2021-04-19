from django.shortcuts import render, redirect, get_object_or_404
from shortner.models import UrlModels
from shortner.forms import UrlForms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404    
import random, string
from django.views import View


class BaseView(View):
    def get(self, request, *args, **kwargs):
        form = UrlForms()
        context = {
            "form": form,
        }
        return render(request, 'shortner/base.html', context) 

    def post(self, request, *args, **kwargs):
        form = UrlForms(request.POST)
        context = {
            "form": form
        }
        template = "shortner/base.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = UrlModels.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            template = "shortner/success.html"
            if created:
                context['title'] = 'CREATED SHORT URL'
            else:
                context['title'] = 'SHORT URL EXISTS'
        return render(request, template ,context)

        
class URLRedirectView(View):
    def get(self, request, short_url=None, *args, **kwargs):
        qs = UrlModels.objects.filter(short_url__iexact=short_url)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)
        
