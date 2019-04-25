from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board


def index(request):
    board_list = Board.objects.all()
    context = {'board_list': board_list}
    return render(request, 'board/index.html', context)

def detail(request, num):
    board = get_object_or_404(Board, pk=num)
    return render(request, 'board/detail.html', {'board':board})

