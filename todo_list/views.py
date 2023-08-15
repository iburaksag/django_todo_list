from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo, Category, Tag


@login_required(login_url = '/admin/login/')
def home_view(request):

    todos = Todo.objects.filter(
        is_active = True,
        user = request.user,
    )

    context  = dict(
        todos=todos,
    )

    return render(request,"todo_list/todo_list.html", context)


@login_required(login_url = '/admin/login/')
def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    todos = Todo.objects.filter(is_active = True, category=category,)
    context  = dict(
        category=category,
        todos=todos,
    )
    return render(request,"todo_list/todo_list.html", context)


@login_required(login_url = '/admin/login/')
def todo_detail_view(request, category_slug, id):
    todo = get_object_or_404(Todo, category__slug=category_slug, pk=id, user=request.user)
    context  = dict(
        todo=todo,
    )
    return render(request,"todo_list/todo_detail.html", context)


@login_required(login_url = '/admin/login/')
def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    context  = dict(
        todos=tag.todo_set.filter(user=request.user),
        tag=tag,
    )
    return render(request,"todo_list/todo_list.html", context)






# def todo_detail_view(request, id):
#     try:
#         todo = Todo.objects.get(pk = id)
#         context  = dict(
#             todo=todo,
#         )
#         return render(request,"todo_list/todo_detail.html", context)
#     except Todo.DoesNotExist:
#         return Http404    
