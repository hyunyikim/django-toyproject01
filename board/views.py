import datetime

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.http import HttpResponse
from .models import Board
from .forms import BoardForm


def index(request):
    board_list = Board.objects.all()
    context = {'board_list': board_list}
    return render(request, 'board/index.html', context)

def detail(request, num):
    board = get_object_or_404(Board, pk=num)
    return render(request, 'board/detail.html', {'board':board})

def new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            obj = Board(num='5', id=form.data['id'], title=form.data['title'], content=form.data['content']
                        , dt=datetime.datetime.today(), hit=0)
            obj.save()
        return HttpResponse('save success')

    if request.method == 'GET':
        form = BoardForm()
        return render(request, 'board/write.html', {'form':form})


def update(request):
    return render()

def delete(request):
    return render()