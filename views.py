from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


# Create your views here.

reminders=[]
class NewReminderForm(forms.Form):
    reminder=forms.CharField(label='New Reminder')
    #forms=forms.IntegerField(label='Importance',min_value=1,max_value=10)


def index(request):
    
    return render(request,"reminders/index.html" , {"reminders":reminders})

def add(request):
    
    if request.method=="POST":
        form=NewReminderForm(request.POST)
        if form.is_valid():
            reminder=form.cleaned_data["reminder"]
            reminders.append(reminder)
            HttpResponse("h1111")
            
            return HttpResponseRedirect(reverse("reminders:index"))
        else:
            HttpResponse("h112222")
            return render(request,"reminders/add.html", {"form":form})
    else:        
        HttpResponse("h1113333")
        return render(request,"reminders/add.html" ,{"form":NewReminderForm()})        


     