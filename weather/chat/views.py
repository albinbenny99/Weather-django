from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib.auth.decorators import login_required

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone


openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.
@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})


