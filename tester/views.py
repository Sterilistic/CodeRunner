from django.shortcuts import render
from django.http import HttpResponse
import runcode

# Create your views here.

default_py_code = """import sys
import os

if __name__ == "__main__":
    print "Hello Python World!!"
"""

default_rows = "15"
default_cols = "60"

def runpy(request):
    if request.method == 'POST':
        code = request.POST['code']
        print code
        run = runcode.RunPyCode(code)
        rescompil, resrun = run.run_py_code()
        if not resrun:
            resrun = 'No result!'
    else:
        code = default_py_code
        resrun = 'No result!'
        rescompil = "No compilation for Python"
        
    return render(request,'main.html',
                           {'code':code,
                           #'target':"runpy",
                           'resrun':resrun,
                           'rescomp':rescompil,#"No compilation for Python",
                           'rows':default_rows, 'cols':default_cols})
