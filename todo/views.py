from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/index.html', {
        "todo_items": todo_items
    })

def todo(request):
    current_date = timezone.now()
    content = request.POST.get('content', False)
    Todo.objects.create(added_date=current_date, text=content)
    Todo.objects.all().count()
    return HttpResponseRedirect("/")

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")