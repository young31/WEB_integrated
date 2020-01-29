from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm#, UserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login as signin, logout as signout# as auth_login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from .forms import CunstomUserChangeForm
from IPython import embed
# Create your views here.

#################  template 반복으로 통합시켜놨음 주의해서 사용할 것!!!!   #########################
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            signin(request, user)
            # 로그인한채로 넘겨주기
            return redirect('articles:index')
            # redirect('accounts:login')
    else:
        form=CustomUserCreationForm()
    context = {'form':CustomUserCreationForm()}
    return render(request, 'accounts/form.html', context)


# @login_required
def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            signin(request, form.get_user())
            next_page = request.GET.get('next') # next가 있으면 !!
            return redirect(next_page or 'articles:index')
    next_page = request.META['HTTP_REFERER']    
    context = {
        'form': AuthenticationForm(),
        'next': next_page
    }
    #embed()
    return render(request, 'accounts/form.html', context)


def logout(request):
    signout(request)
    next_page = request.GET.get('next')
    return redirect(next_page or 'articles:index')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        return redirect('articles:index')


@login_required
# update바로 넘기면 못볼정보까지 다 넘겨버리게 됨
def update(request): # userchangeform import!!
    if request.method=='POST':
        form = CunstomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
        # else:
        #     form = CunstomUserChangeForm(instance=request.user)
    form = CunstomUserChangeForm(instance=request.user) # update바로 넘기면 못볼정보까지 다 넘겨버리게 됨
    context = {'form': form}
    return render(request, 'accounts/form.html', context)


@login_required
def password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:update')
            # return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/form.html', context)