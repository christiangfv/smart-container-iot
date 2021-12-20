# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import urllib, json
import ssl; ssl._create_default_https_context = ssl._create_stdlib_context
@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        if load_template in ['charts-morris.html', 'maps-google.html']:
            data = getData(request)
            return HttpResponse(html_template.render(data, request))

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def getData(request):
    url = "https://smartcontainerstorage.blob.core.windows.net/container-001/0_1303a71c9f6a489889e63924ded8d299_1.json"
    response = urllib.request.urlopen(url)
    stringdata = response.read()
    data = json.loads("["+str(stringdata).replace("\\r\\n","").replace("\'","").replace("}{","},{").replace("b","")+"]")
    final = {'device_id': data[0]["deviceId"]}
    graph = [{"y":i["EventEnqueuedUtcTime"], 
                        "a":i["temperature"], 
                        "b":i["humidity"],
                        "c":i["luminosity"]} for i in data]
    alerts = [i for i in data if i["temperature"] > 30]
    final["graph"] = graph
    final["data"] = data[-9:]
    final["alerts"] = alerts
    return final
    #return HttpResponse(json.dumps(final))