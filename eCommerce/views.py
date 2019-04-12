from django.shortcuts import render
from forms.contact_forms import ContactForm


def home_page(request):
    pass


def about_page(request):
    pass


def contact_page(request):
    contact_form = ContactForm()
    context = {
        'title': 'Contact',
        'content': 'Welcome to Contact Page',
        'form': contact_form
    }
    if request.method == 'POST':
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)
