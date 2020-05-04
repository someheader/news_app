from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404 ,render
from django.urls import reverse

from .models import Contact, ContactType
#Get Contacts and disply them
def index(request):
    contacts_list = Contact.objects.order_by('contact_name')[:10]
    context = {'contacts_list': contacts_list}
    return render(request, 'notebook/index.html', context)

#
def detail(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        raise Http404('Contact does not exists')
    return render(request, 'notebook/detail.html', { 'contact' : contact})
