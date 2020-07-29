from django.shortcuts import render
from .models import Page


def index(request, page_name):
    page_name += '/'
    pg = Page.objects.get(permalink=page_name)
    context = {
        'title': pg.title,
        'content': pg.body,
        'last_updated': pg.update_date
    }
    # assert False
    return render(request, 'pager/page.html', context)


