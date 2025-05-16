from django.shortcuts import render, redirect
from. form import MessageForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        print('post method')
        form = MessageForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('success')
        else:
            message.error(request, 'Please correct the below error ')
    else:
        form = MessageForm()
        return render(request,'base/index.html', {'form':form})

def success_page(request):
    return render(request, 'base/success.html')

def about(request):
    return render(request,'base/about.html')

def services(request):
    return render(request,'base/services.html')

def portfolio(request):
    return render(request,'base/portfolio.html')

def skill(request):
    return render(request,'base/skill.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('success')
        else:
            message.error(request, 'Please correct the below error ')
    else:
        form = MessageForm()
        return render(request,'base/contact.html', {'form':form})

def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            form.save()
            message.success(request, 'Your message has been sent successfully!')
            return redirect('base/msg_success.html')
        
        else:
            message.error(request, 'Please correct the below error ')
    else:
        form = MessageForm()
    return render(request, "base/success.html")