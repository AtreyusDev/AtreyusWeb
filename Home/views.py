from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Project
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def projects(request):
    project_counter = 1
    projects = Project.objects.all()
    projects_quanty = Project.objects.count()
    context = {'projects':projects, 'projects_quanty':projects_quanty}
    
    return render(request, 'projects.html', context)

def contact(request):

    if request.method == "POST":

        message_data = ContactForm(request.POST)

        if message_data.is_valid():

            name = request.POST.get("name")

            infForm = message_data.cleaned_data

            send_mail('Correo originado de AtreyusWeb', f'''Usuario: {infForm['name']}.
Correo: {infForm['email']}.
Mensaje: {infForm['message']}.''', 'Solicitud de Contacto con AtreyusDev', ['jizdsing@gmail.com'], fail_silently= False,)
            
            send_mail('From AtreyusWeb', f'''Hi {infForm['name']}. Your message has been sent successfully! Please be patience waiting the answer. 

Adittional, I want to invite you to check my GitHub and my projects.

My GitHub: https://github.com/AtreyusRey''', f'Request of contact to AtreyusDev', [f'{infForm["email"]}'], fail_silently=False,)
            
            return redirect("/contact/?message_sent")
        
        else:
            
            return redirect("/contact/?sent_error")
    
    else:

        message_data = ContactForm()

    return render(request, 'contact.html', {'form':message_data})
