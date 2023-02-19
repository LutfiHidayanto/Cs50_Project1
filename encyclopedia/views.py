from django.shortcuts import render
from . import util
from markdown2 import Markdown
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    markdowner = Markdown()

    if content == None:
        return render(request, "encyclopedia\error.html", {"message": "The Page You Searched Doesn't Exist"})
    content = markdowner.convert(content)
    return render(request, "encyclopedia\entry.html", {
        "title": title,
        "content": content
    })   

def search(request):
    if request.method == "POST":
        query = request.POST['q']
        content = util.get_entry(query)
        markdowner = Markdown()

        if content:
            content = markdowner.convert(content)
            return render(request, "encyclopedia\entry.html", {
                "title": query,
                "content": content
            })
        else:
            entries = util.list_entries()
            suggestion = []
            for entry in entries:
                if query.lower() in entry.lower():
                    suggestion.append(entry)
            return render(request, "encyclopedia\suggestion.html", {
                "title": query,
                "content": suggestion
            })

def newPage(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/newPage.html", {
            "form": forms.newPageForm()
        })
    else:
        # saving user submitted form
        form = forms.newPageForm(request.POST)

        # checking if form is valid 
        if form.is_valid():
            # cleaning data
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            # if title already exist
            if (util.get_entry(title)):
                return render(request, "encyclopedia\entry.html", {
                    "message": "This Entry Already Exist!"
                })
                

        

