from django.shortcuts import render

from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    context = {'form': SubscriptionForm()} #quando é classe passo com parenteses para ser uma instancia
    return render(request, 'subscriptions/subscription_form.html', context)

