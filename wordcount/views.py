from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            #Increase
            wordDictionary[word] += 1
        else:
            #add to the dictionary
            wordDictionary[word] = 1
    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordList), 'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')