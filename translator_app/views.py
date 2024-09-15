# pip install translate
from django.http import HttpResponse
from django.shortcuts import redirect, render
from translate import Translator


def translate(request):
    translation = ''
    if request.method == 'POST':
        text = request.POST['text']
        language = request.POST['language']

        translator = Translator(to_lang=language)
        translation = translator.translate(text)

        return render(request, 'home.html', {'translation': translation})


    return render(request, 'home.html')