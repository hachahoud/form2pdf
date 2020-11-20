from django.shortcuts import render
from .forms import InfoForm

import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from xhtml2pdf import pisa

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def index(request):
    print("index called!!")
    """Manage the form"""
    if request.method != "POST":
        # no date submitted; render a blank form
        info_form = InfoForm(auto_id="id-%s")
        print("index passed!!")

    # xhtml2pdf
    else:
        # data is submitted
        info_form = InfoForm(data=request.POST)
        if info_form.is_valid():
            print("OK2")
            template_path = 'form/pdf.html'
            # retrieve submitted data
            f_name = request.POST.get("first_name")
            l_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            selection = request.POST.get("selection")
            type0 = request.POST.get("type0")
            type1 = request.POST.get("type1")
            type2 = request.POST.get("type2")
            context = {'f_name': f_name, 'l_name':l_name, 'email':email,
                'phone':phone, 'selection':selection, "type0":type0, "type1":type1, "type2":type2}
            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # find the template and render it.
            template = get_template(template_path)
            html = template.render(context)

            # create a pdf
            pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback, encoding="UTF-8")
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response

    context = {'f':info_form}
    return render(request, 'form/index.html', context)