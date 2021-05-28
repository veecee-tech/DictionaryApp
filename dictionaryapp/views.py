from django.shortcuts import render
from PyDictionary import PyDictionary

def home(request):
    return render(request, 'index.html')

def word(request):
    word = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)
    context = {
        'meaning': meaning,
        'synonyms': synonyms,
        'antonyms': antonyms,
        'keyword': word
    }
    return render(request, 'word.html', context)