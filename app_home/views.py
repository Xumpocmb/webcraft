import os
import requests
import logging
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Service, ContactRequest
from app_reviews.models import Review

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

from django.shortcuts import render, redirect


def about_page(request):
    return render(request, "app_home/about_page.html")


def services_page(request):
    services = Service.objects.all().order_by("id")
    return render(request, "app_home/services_page.html", {"services": services})


def why_us_page(request):
    return render(request, "app_home/why_us_page.html")


def contact_page(request):
    return render(request, "app_home/contact_page.html")


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        message_text = request.POST.get("message")

        if not all([name, phone_number, message_text]):
            messages.error(request, "Пожалуйста, заполните все поля формы.")
            return redirect(request.META.get("HTTP_REFERER", "index"))

        # Save to database
        contact_request = ContactRequest.objects.create(name=name, phone_number=phone_number, message=message_text)

        # Send to Telegram
        logger.info(f"Attempting to send Telegram message. Token: {TELEGRAM_BOT_TOKEN}, Chat ID: {TELEGRAM_CHAT_ID}")
        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            telegram_message = f"Новая заявка с сайта:\n" f"Имя: {name}\n" f"Телефон: {phone_number}\n" f"Сообщение: {message_text}"
            telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": telegram_message}
            try:
                response = requests.post(telegram_url, data=payload)
                response.raise_for_status()  # Raise an exception for HTTP errors
                logger.info("Telegram message sent successfully.")
                messages.success(request, "Ваша заявка успешно отправлена!")
            except requests.exceptions.RequestException as e:
                logger.error(f"Error sending to Telegram: {e}, response: {response.text}")
                messages.error(request, "Произошла ошибка при отправке заявки в Telegram. Пожалуйста, попробуйте еще раз.")
        else:
            logger.warning("Telegram configuration is incomplete. TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is missing.")
            messages.warning(request, "Конфигурация Telegram не завершена. Заявка сохранена, но не отправлена в Telegram.")

        return redirect(request.META.get("HTTP_REFERER", "index"))

    services = Service.objects.all().order_by("id")
    reviews = Review.objects.all()
    context = {
        "services": services,
        "reviews": reviews,
    }
    return render(request, "app_home/index.html", context)


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    context = {"service": service}
    return render(request, "app_home/service_detail.html", context)
