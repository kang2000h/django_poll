from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
# Create your views here.
"""
def index(request):
    candidates = Candidate.objects.all()
    str=''
    for candidate in candidates:
        str += "<p>{} 기호{}({})<br>".format(candidate.name,
                            candidate.party_number,
                            candidate.area)
        str += candidate.introduction+"</p>"
    return HttpResponse(str)
"""

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates':candidates}
    return render(request, 'elections/index.html', context)
