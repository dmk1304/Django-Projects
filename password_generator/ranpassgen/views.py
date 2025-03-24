from django.shortcuts import render
from django.views import View
from .forms import PassGenForm
import string
import re
import random

# Create your views here.
class Index(View):

    def get(self, request):
        form = PassGenForm()

        context = {'form': form}
        return render(request,'ranpassgen/index.html', context)
    
    def post(self, request):
        form = PassGenForm(request.POST)

        if form.is_valid():
            available_characters = string.ascii_letters + string.digits
            print(form.cleaned_data)
            
            if form.cleaned_data['include_symbols']:
                available_characters += string.punctuation

            if form.cleaned_data['include_similar_characters']:
                ambigous_characters = ['Z', 'z', 'O', 'o', 'I', 'l', '1', '0', '2']
                available_characters += re.sub('|'.join(ambigous_characters),'', available_characters)
            
            password = ''.join(random.choice(available_characters) for i in range(form.cleaned_data['length']))
            print(password)

        return render(request, 'ranpassgen/password.html', {'password': password})
