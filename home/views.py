from django.shortcuts import render, render_to_response

# Create your views here.

def home_page(request, template='home.html'):

    context = {
        
    }
    return render_to_response(template, context)