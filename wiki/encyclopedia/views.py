from django.http import HttpResponse
from django.shortcuts import render
import markdown2
from markdown2 import Markdown
#Import os module
import os
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):

    markdown_text = util.get_entry(title)
    html = markdown2.markdown(markdown_text)
    return render(request, "encyclopedia/wiki.html", {
        "text":html
    })

def search(request):
    search_string = request.GET.get('q', '')
    titles = util.list_entries()
    if search_string:
        searchResult = []
        for title in titles:
            if search_string == title:
                markdown_text = util.get_entry(title)
                html = markdown2.markdown(markdown_text)
                return render(request, "encyclopedia/wiki.html", {
                "text":html
                })
            elif search_string in title:
                searchResult.append(title)
        return render(request, "encyclopedia/search.html", {
               "queryon": search_string,
               "titles": searchResult
                })