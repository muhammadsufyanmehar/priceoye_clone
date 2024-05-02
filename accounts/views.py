from django.http import  HttpResponse
from django.core.mail import send_mail

def simple_mail(request):

    send_mail(subject='Mail from Abdul Rehman',
               message='AOA',
                 from_email='django@mailtrap.club', 
                    recipient_list=['test.mailtrap1234@gmail.com'])
    
    return HttpResponse('Message sent!')