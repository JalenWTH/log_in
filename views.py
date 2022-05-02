from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from log_in.models import sign_up_model
from log_in.forms import sign_up_form, log_in_form

def home(request):
    try:
        if request.session['signed_in'] == True:
            return render(request, 'log_in/home.html', {})
            
    except KeyError:
        return redirect('log_in')
        
        
    return redirect('log_in')
        
def sign_up(request):
    if request.method == 'POST':
        form=sign_up_form(request.POST)
        if form.is_valid():
            fname=form.cleaned_data['fname']
            lname=form.cleaned_data['lname']
            phone=form.cleaned_data['phone']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            for queryset in sign_up_model.objects.values():
                #if the user enters an email that is already registered, they will not be allowed to register again with the same email
                if queryset['email'] == email:
                    signed_up=True
                    form=sign_up_form(request.POST)
                    return render(request, 'sign_up.html', {'form':form,'signed_up':signed_up})
                    
            instance=sign_up_model(fname=fname,lname=lname,phone=phone,password=password,email=email)
            instance.save()
            return redirect('log_in')
    
    form=sign_up_form()           
    return render(request, 'log_in/sign_up.html', {'form':form})
    
def log_in(request):
    if request.method == 'POST':
        form=log_in_form(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            x=sign_up_model.objects.filter(email__iexact=email).values()
            
            if len(x) == 0:
                #if an empty queryset is returned because the email is not registered in the db
                 signed_up=False
                 form=log_in_form(request.POST)
                 return render(request, 'log_in/log_in.html', {'form':form, 'signed_up':signed_up})
            
            elif x[0]['password'] != password:
                #if the entered password does not match the password associated with the email
                signed_up=False
                form=log_in_form(request.POST)
                return render(request, 'log_in/log_in.html', {'form':form, 'signed_up':signed_up})
                
            request.session['signed_in'] = True
            request.session.set_expiry(600)
            return redirect('home')
            
    form=log_in_form()
    return render(request, 'log_in/log_in.html', {'form':form})