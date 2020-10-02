from django.shortcuts import render
from WebApp.forms import MailAttachForm
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
from django.core.mail import EmailMessage


def MailView(request):
    if request.method=='POST':
        form=MailAttachForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['Name']
            email=form.cleaned_data['Email']
            subject=form.cleaned_data['Subject']
            message=form.cleaned_data['Message']
            imgattach=request.FILES['Imgatta']

            try:
                mail=EmailMessage('got a mail from'+str(email),
                "Name: "+str(name)+"\n"
                "Email: "+str(email)+"\n"
                "Subject: "+str(subject)+"\n"
                "Message: "+str(message),
                settings.EMAIL_HOST_USER,
                ['kovurucharan@gmail.com'])
                mail.attach(imgattach.name,imgattach.read(),imgattach.content_type)
                mail.send()
                return HttpResponseRedirect('/bye')
            except:
                return HttpResponse("Sorry Mail Attachment Error....!!")
    else:
      form=MailAttachForm()
    return render(request,'Myapp/mail.html',{'form':form})

def ThankView(request):
    return render(request,'Myapp/thanks.html')








