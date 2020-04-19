from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    #return HttpResponse('Hello')
    return render(request, 'home.html', {'greeting': 'Hi there! This is Javi'})

def countPage(request):
    fulltext = request.GET['fulltext']
    print('Full Text: ' + fulltext)

    wordlist = fulltext.split()
    fulltextLength = str(len(wordlist))
    print('Number of words: ' + fulltextLength)

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase the number
            worddictionary[word] += 1
        else:
            # Add to the dictionary
            worddictionary[word] = 1

    print(worddictionary)

    return render(request, 'count.html', {'fulltext': fulltext, 'length': fulltextLength, 'worddictionary': worddictionary.items()})

def aboutPage(request):    
    return render(request, "about.html", {"companyName": "Cognizant Technology Solutions", "companyAddress": "Maria de Molina st, 54, 1st & 8th floor", "companyCityAndPostalCode": "Madrid, 28006", "companyCountry": "Spain", "companyContactEmail": "contact@cognizant.com"})