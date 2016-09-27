from django.shortcuts import render


import json,urllib

# Create your views here.

def post_list(request):
    data = urllib.urlopen('http://jobs.fortinet.com/test.json').read()
    return render(request, 'app_list/app_list.html', {'lists': list(json.loads(data))})