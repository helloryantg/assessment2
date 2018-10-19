from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'

def index(request):
    model = Widget
    widget_list = Widget.objects.all()
    form = WidgetForm()
    return render(request, 'index.html', { 'widget_list': widget_list, 'form': form })

def add_widget(request):
    form = WidgetForm(request.POST)
    form.save()
    return redirect('index')

def delete(request, id):
    widget = Widget.objects.get(id=id)
    widget.delete()
    return redirect('/')