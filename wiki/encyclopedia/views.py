from django.http import HttpResponse
from django.shortcuts import render
import markdown2
from markdown2 import Markdown
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):

    markdown_text = util.get_entry(title)
    html = markdown2.markdown(markdown_text)
    #markdowner = Markdown()
    #html = HttpResponse(markdowner.convert(markdown_text))
    return render(request, "encyclopedia/wiki.html", {
        "text":html
    })