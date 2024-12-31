from django.shortcuts import render, redirect

from django.contrib import messages

from .models import Contact
from ..common.models import Sub_Email


def contactView(request):
    url = request.build_absolute_uri()

    if request.method == "POST":
        sub_email = request.POST.get("sub_email")
        email = request.POST.get("email")
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if sub_email:
            sub_email = Sub_Email.objects.create(sub_email=sub_email)
            return redirect(url)
        
        if email and name and subject and message:
            contact = Contact()
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()
            messages.success(request, "Message sent successfully!")
            return redirect(url) # messages.success redirectdan oldin yozilishi kerak
        else:
            messages.error(request, "Please fill all fields!")
            return redirect(url)
        
    return render(request=request, template_name="contact.html")
