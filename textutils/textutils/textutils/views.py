from re import S
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     s='''<h1>hello<br></h1>
#     <a href="https://www.youtube.com/watch?v=AepgWsROO4k">django</a><br>
#     <a href="https://www.instagram.com/explore/">instagram</a><br>
#     <a href="https://drive.google.com/drive/u/0/my-drive">drive</a>'''
    
#     return HttpResponse(s)


# def about(request):
#     return HttpResponse('about jinay')

def index(request):
    return render(request,'index2.html')
    #return HttpResponse('hello')

def analyze(request):
    djtext=request.POST.get('text','default')
    #check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    charcount=request.POST.get('charcount','off')
    
    #check which checkbox is on
    if removepunc == "on":
        punctuations  = '''!()-[]{};:;' "\,<>./?@#$%^&*_~'''
        analyzed=""
        
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()

        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char != '\n' and char!="\r":
                analyzed=analyzed + char

        params={'purpose':'Removed newlines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(charcount=='on'):
        analyzed=0
        for char in djtext:
            analyzed=analyzed + 1

        params={'purpose':'count the character','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    else:
        return HttpResponse('error')

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remove")

# def charcount(request):
#     return HttpResponse("char count")