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


    #return render(request, "encyclopedia/search.html", {
    #       "queryon": search_string,
    #       "entries": entries
    #})
     

    #if search_string:
    #    return render(request, "encyclopedia/search.html", {
    #        "queryon": search_string
    #    })


def search2(request, search_string):

    
    # Ask the user to enter string to search
    search_path = "encyclopedia/entries"
    file_type = ".md"
    search_str = search_string

    # Append a directory separator if not already present
    if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
    # If path does not exist, set search path to current directory
    if not os.path.exists(search_path):
        search_path ="."

    titles =[]
    # Repeat for each file in the directory  
    for fname in os.listdir(path=search_path):

        # Apply file type filter   
        if fname.endswith(file_type):
            # 
            if search_string == fname:
                #return (request, "wiki/<str:title>")
                # TODO redirect to the relevant page
            #elif search_string in fname:
                # add it to a list
                titles.append(fname)  
                # TODO redirect to the search results page
            #else:
                # TODO redirect toa results not found page
        