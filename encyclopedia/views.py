from django.shortcuts import render
from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    markdowner = Markdown()

    if content == None:
        return render(request, "encyclopedia\error.html", {"title": title})
    content = markdowner.convert(content)
    return render(request, "encyclopedia\entry.html", {
        "title": title,
        "content": content
    })   
