from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    #Send Email

    _send_mail('subscriptions/subscription_email.txt',
               form.cleaned_data,
               'Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               form.cleaned_data['email']
               )

    Subscription.objects.create(**form.cleaned_data)
    #Success Fedback
    messages.success(request, 'Inscrição realizada com sucesso!')

    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()}) #quando é classe, passo com parenteses  SubscriptionForm para ser uma instancia


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])