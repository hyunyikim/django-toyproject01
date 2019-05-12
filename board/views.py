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


class UpdateView(generic.View):
    form_class = BoardForm
    template_name = 'board/write.html'

    def get(self, request, *args, **kwrags):
        try:
            num = self.kwargs.get("pk")
            board = Board.objects.get(num=num)
            form = self.form_class(
                initial={
                    'num': board.num,
                    'title': board.title,
                    'content': board.title,
                    'id': board.id
                }
            )
            return render(request, self.template_name, {'form':form})
        except(KeyError, Board.DoesNotExist):
            return render(request, 'board/detail.html', {
                'board':board,
                'error_message':'update failed'
            })

    def post(self, request, *args, **kwrags):
        form_class = BoardForm
        try:
            form = form_class(request.POST)
            if form.is_valid():
                board = get_object_or_404(Board, pk=request.POST['num'])
                board.title = form.cleaned_data['title']
                board.content = form.cleaned_data['content']
                board.save()
                return render(request, 'board/detail.html', {'board':board})
        except(KeyError, Board.DoesNotExist):
            return render(request, 'board/detail.html', {
                'board': board,
                'error_message': 'delete failed'
            })



class DeleteView(generic.View):
    def get(self, request, *args, **kwargs):
        num = self.kwargs.get("pk")
        try:
            board = Board.objects.get(num=num)
            board.delete()
            return HttpResponseRedirect(reverse('board:index'))
        except(KeyError, Board.DoesNotExist):
            return render(request, 'board/detail.html', {
                'board':board,
                'error_message':'delete failed'
            })
