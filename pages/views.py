from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    my_text = {"location_context": ""}
    return render(request, "pages/index.html", context=my_text)


# def indexfa(request):

#     my_text = {"location_context": ""}
#     return render(request, "pages/indexfa.html", context=my_text)



from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import JsonResponse


def indexfa(request):
    contact_form = ContactForm()
    success_message = None

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # دریافت داده‌های فرم
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            phone_number = contact_form.cleaned_data['phone_number']
            message = contact_form.cleaned_data['message']


            # ارسال ایمیل
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Message: {message}\n\nFrom: {name}, phone number : {phone_number}, email : <{email}>",
                from_email='sepid.tejaraat.web@gmail.com',
                recipient_list=['sabvard@gmail.com'],  # ایمیل گیرنده
            )

            # نمایش پیام موفقیت
            success_message = "Your message has been sent successfully!"
            contact_form = ContactForm()  # ریست فرم

    return render(request, 'pages/indexfa.html', {'form': contact_form, 'success_message': success_message})



def send_email(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        message = request.POST.get('message')
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")
        # متن ایمیل
        subject = f"پیام جدید از {name}"
        full_message = f"پیام:\n{message}\n\nنام: {name}\nایمیل: {email}\nتلفن: {phone}"


        try:
            send_mail(
                subject,
                full_message,
                'sepid.web.555@gmail.com',  # ایمیل ارسال‌کننده
                ['sabvard@gmail.com'],  # ایمیل گیرنده
                fail_silently=False,
            )
            context = {'success': 'پیام با موفقیت ارسال شد!'}
            return render(request, 'pages/contact.html', context)
        except Exception as e:
            # در صورت خطا
            context = {'error': f'خطا در ارسال پیام: {str(e)}'}
            return render(request, 'pages/contact.html', context)
    else:
        return render(request, 'pages/contact.html')




