from django.shortcuts import render, redirect
from .forms import ModifiedUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = ModifiedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        username = form.cleaned_data.get('username')
        print('***********', username,'*********')
        return render(request, 'signup_confirmation.html',
                      {'username': username})
    else:
        form = ModifiedUserCreationForm
        return render(request, 'signup.html', {'form' : form})
