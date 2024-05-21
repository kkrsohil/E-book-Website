from django.shortcuts import render,redirect
from .models import contact_details,blog_details
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

def home_page(request):
    return render(request,'includes/index.html')

def service_page(request):
    return render(request,'includes/service.html')

def blog_page(request):
    data=blog_details.objects.all()
    context={'blog_data':data}
    return render(request,'includes/blog.html',context)

def add_blog(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        blog_content = request.POST['message']
        blog_link = request.POST['link']
        data_collect=blog_details(
            user_name = user_name,
            blog_msg = blog_content,
            blog_link = blog_link,
        )
        data_collect.save()
        if data_collect:
            # redirect('blog')
            pass
    return render(request , 'includes/add_blog.html')

def price_page(request):
    return render(request,'includes/pricing.html')

def contact_page(request):
    if request.method == 'POST':
        u_name = request.POST['name']
        u_email = request.POST['email']
        u_msg = request.POST['message']
        data_collect=contact_details(
            user_name = u_name,
            user_email = u_email,
            message = u_msg,
        )
        data_collect.save()                
        if data_collect:
            mydict={'username': u_name}
            html_template= 'includes/email.html'
            html_message=render_to_string(html_template,context=mydict)
            subject='Yuo have created your account successfully! '
            email_from=settings.EMAIL_HOST_USER
            message=EmailMessage(subject,html_message,email_from,[u_email])
            message.content_subtype = 'html'
            message.send()
    return render(request,'includes/contact.html')
