from django.shortcuts import render
# from django.http import HttpResponse

from django.views import View


class Postview(View):

    def get(self, request):
        massage = "hello"
        return render(request, 'dialect/main_page.html',
                      {'msg': massage}
                      )
