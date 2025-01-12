# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice
from .forms import NoticeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

def user_is_authenticated(user):
    return user.is_authenticated

def login_required_403(function):
    """Custom decorator that returns 403 if user is not logged in."""
    return user_passes_test(user_is_authenticated, login_url=None)(function)

def notice_list(request):
    notices = Notice.objects.order_by('-is_pinned', '-pub_date')
    return render(request, 'notice_list.html', {'notices': notices})

def admin_login(request):
    return redirect(reverse('admin:login'))

@login_required_403
def notice_add(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice_list')
    else:
        form = NoticeForm()
    return render(request, 'notice_form.html', {'form': form, 'action': 'add'})

@login_required_403
def notice_edit(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice_list')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'notice_form.html', {'form': form, 'action': 'edit', 'notice': notice})

@login_required_403
def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    notice.delete()
    return redirect('notice_list')
    
@login_required_403
def notice_pin(request, notice_id):
      notice = get_object_or_404(Notice, id=notice_id)
      notice.is_pinned = not notice.is_pinned  # Toggle the pin status
      notice.save()
      return redirect('notice_list')

def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    return render(request, 'notice_detail.html', {'notice': notice})