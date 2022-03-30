from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    contacts = Contact.objects.order_by('name')
    paginator = Paginator(contacts, 10)
    
    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts\index.html', 
    {
        'contacts' : contacts
    })


def page_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)     # if the id doesn't exist, it will raise "ERRor 404"

    if not contact.show:     # if it is not checked to show, it will raise "ERROR 404"
        raise Http404()

    return render(request, 'contacts\page_contact.html', {
        'contact' : contact
    })


def search(request):
    term = request.GET.get('term')

    if term is None or not term:    # Alert if nothing is written in the search bar.
        messages.add_message(request, messages.ERROR, 'Search bar cannot be empty.')
        return redirect('index')

    search_field = Concat('name', Value(' '), 'last_name')

    contacts = Contact.objects.annotate(
        full_name=search_field).filter(
            Q(full_name__icontains=term)|Q(phone_number__icontains=term))   # search field for full name or number
    
    if term is not None and len(contacts) >= 1:     # Alert when search finds results.
        messages.add_message(request, messages.SUCCESS, 'Search completed.')

    if term is not None and len(contacts) < 1:      # Alert when search does not find results.
        messages.add_message(request, messages.WARNING, 'Nothing found.')

    paginator = Paginator(contacts, 10)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts\search.html', 
    {
        'contacts' : contacts
    })