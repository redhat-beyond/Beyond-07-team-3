from django.shortcuts import render, redirect
from events.forms import EventCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def create_event(request):

    if request.method == 'POST':
        form = EventCreationForm(request.POST, user_id=request.user)
        if form.is_valid():
            form.save()

            title = form.cleaned_data.get('title')
            messages.success(request, f'Event: {title} created!')
            return redirect('home')

    else:
        form = EventCreationForm(user_id=request.user)

    return render(request, 'events/create_event.html', {'form': form})
