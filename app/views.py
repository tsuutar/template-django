from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request, "app/index.html", {})


# 定義
index = IndexView.as_view()
