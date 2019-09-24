from django.shortcuts import render
from .models import Content,Section
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import strip_tags
import re, pyperclip

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        type = request.POST.get("list")
        type = int(type)
        return HttpResponseRedirect(reverse('list', kwargs={'type': type}))
    return render(request, 'balaghahPWA/Home.html')

def list(request,type):
    context = {}

    titleList = Content.objects.all().values('title_En','id').filter(type=type)
    context['titles'] = titleList

    if request.method == 'POST':
        contentID = request.POST.get("goToContent")
        contentID = int(contentID)
        return HttpResponseRedirect(reverse('content', kwargs={'contentID': contentID}))

    if type == "1":
        context['listTitle'] = "Preface"
        print("s")
    elif type == "2":
        context['listTitle'] = "Sermons"
        print("ss")
    elif type == "3":
        context['listTitle'] = "Letters"
    elif type == "4":
        context['listTitle'] = "Aphorisms"
    else:
        context['listTitle'] = "Rare Words"

    return render(request, 'balaghahPWA/List.html',context)

def contentView(request,contentID):
    context = {}

    # bodyEnglishArray = []
    # bodyArabicArray = []
    # mainBody = []
    body = Section.objects.all().filter(content=contentID)

    # for body in body:
    #     arabicBody = body.body_fa
    #     # arabicBody = strip_tags(arabicBody)
    #     # arabicBody = re.sub('[>}&#zwnj'']', '', arabicBody)
    #     # bodyArabicArray.append(arabicBody)
    #     mainBody.append(arabicBody)
    #
    #     # englishBody = body.body_ar
    #     # englishBody = strip_tags(englishBody)
    #     # englishBody = re.sub('[>}&#]', '', englishBody)
    #     # bodyEnglishArray.append(englishBody)
    #     mainBody.append(englishBody)


    # for copy and past an string to clipboard we use below command and 'pyperclip'
    # # pip install pyperclip
    # if request.method == "POST":
    #     str = ""
    #     for string in mainBody:
    #         str = str + string
    #     pyperclip.copy(str)
    #     pyperclip.paste()

    # context['bodyAr'] = bodyArabicArray
    # context['bodyEn'] = bodyEnglishArray
    # context['mainBody'] = mainBody
    context['body']=body




    return render(request,'balaghahPWA/Content.html',context)