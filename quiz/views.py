# quiz/views.py
from django.shortcuts import render
from .models import Question

def index(request):
    questions = Question.objects.all()
    return render(request, 'quiz/index.html', {'questions': questions})

def submit_answer(request):
    # ユーザーの回答を受け取ってロジック処理
    # 結果を計算して result.html に表示
    return render(request, 'quiz/result.html')

