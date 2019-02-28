from django.shortcuts import render, redirect
from django.core.mail import send_mail



def index(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        final_message = name + "'s query in the contact form of QuintTech -> " + message
        # print(email)
        # print(subject)

        send_mail(
            subject,
            final_message,
            email,
            ['info@quinttech.io', 'aditalha@gmail.com', 'nawabhaider19@gmail.com', 'sazzadhossain1206@gmail.com', 'alvee9@gmail.com'],
            fail_silently=True,
        )
        return redirect('home:index')



    return render(request, 'home/index.html')


    # form = ContactForm(request.POST or None)
    # if form.is_valid():
    #
    #     form_name = form.cleaned_data.get('name')
    #     form_email = form.cleaned_data.get('email')
    #     form_subject = form.cleaned_data.get('subject')
    #     form_message = form.cleaned_data.get('message')

