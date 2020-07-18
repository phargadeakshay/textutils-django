#i have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   # params = {'name':'THOR','place' : 'aasgaurd'}
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get("text",'default')
    removepunc = request.GET.get("removepunc",'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    print(removepunc)
    print(djtext)
    analyzed =""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punctuations','analyzed_text':analyzed}
        djtext = analyzed
       # return render(request,'analyze.html',params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on"and fullcaps != "on"and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Please Enter At Least One Key")
    return render(request, 'analyze.html', params)
#