<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
=======
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
>>>>>>> b1abfc4bea14afd7c1e982562f2192b2c099a91a
from .models import Page
from .forms import ContactForm


def index(request, page_name):
    page_name = '/' + page_name
    pg = get_object_or_404(Page, permalink=page_name)
    context = {
        'title': pg.title,
        'content': pg.body,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False
    return render(request, 'pager/page.html', context)


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
<<<<<<< HEAD
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'nonreply@anonymous.com'),
                ['nonreply.strict@pager.com'],
                connection=con
            )
=======
>>>>>>> b1abfc4bea14afd7c1e982562f2192b2c099a91a
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True
    context = {'form': form, 'page_list': Page.objects.all(),
               'submitted': submitted}
    return render(request, 'pager/contact.html', context)
