from django.shortcuts import render
# from django.http import HttpResponse

from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import TransForm

# 다양한 방법이 있지만 CLASS 관리 진행
class Postview(View):
    def get(self, request):
        massage = "hello"
        return render(request, 'dialect/main_page.html',
                      {'msg': massage}
                      )

    @csrf_exempt
    def success(request):
        content = request.POST.get('content')
        context = {
            'content': content
        }
        return render(request, 'dialect/trans_suc.html',
                      context
                      )
    def dic(request):
        word = request.POST.get('dictionary')
        Word = {
            'word': word
        }
        return render(request, 'dialect/dictionary.html',
                      Word
                      )
