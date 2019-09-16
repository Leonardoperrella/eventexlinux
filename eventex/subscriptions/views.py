import re

from django.conf import settings
from django.core import mail
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()}) #quando é classe, passo com parenteses  SubscriptionForm para ser uma instancia


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    subscription = Subscription.objects.create(**form.cleaned_data)

    #Send Email
    _send_mail('subscriptions/subscription_email.txt',
               {'subscription': subscription}, #substitui form.cleane_data por dicionario de contexto {'subscription': subscription}
               'Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email
               )
    return HttpResponseRedirect(r('subscriptions:detail', subscription.hashid))
    #return HttpResponseRedirect('/inscricao/{}/'.format(subscription.hashid))


def detail(request, hashid):
    try:
        subscription = Subscription.objects.get(hashid=hashid)
    except (Subscription.DoesNotExist, ValidationError):
        raise Http404("Página não encontrada")

    return render(request, 'subscriptions/subscription_detail.html', {'subscription': subscription})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])