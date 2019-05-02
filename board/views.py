import datetime
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse, get_object_or_404
from .models import Board
from .forms import BoardForm


class IndexView(generic.ListView):
    template_name = 'board/index.html'
    model = Board


class DetailView(generic.View):
    template_name = 'board/detail.html'

    def get(self, request, *args, **kwargs):
        board = get_object_or_404(Board, pk=self.kwargs.get("pk"))
        board.hit += 1
        board.save()
        print('board :', board.num)
        return render(request, self.template_name, {'board':board})


class WriteView(generic.View):
    form_class = BoardForm
    template_name = 'board/write.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            num_sequence = Board.objects.order_by('num').last().num + 1
            obj = Board(num=num_sequence, id=form.data['id'], dt=datetime.datetime.now(),
                        title=form.data['title'], content=form.data['content'], hit=0)
            obj.save()
            return HttpResponseRedirect(reverse('board:detail', args=(obj.num,)))
