from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import CustomUser
from .forms import UserForm


def all_users(request):
    return render(request, 'user_templates/all_users.html', context={"users_list": CustomUser.get_all()})


def user_by_id(request, user_id):
    selected_user = get_object_or_404(CustomUser, pk=user_id)
    context = {"user_instance": selected_user}
    return render(request, 'user_templates/user_details.html', context=context)


def create_update_user(request, user_id=0):
    if request.method == "GET":
        if user_id == 0:
            form = UserForm()
        else:
            user = get_object_or_404(CustomUser, id=user_id)
            form = UserForm(instance=user)
        return render(request, "user_templates/user_form.html", {"form": form})
    else:
        if user_id == 0:
            form = UserForm(request.POST)
        else:
            user = get_object_or_404(CustomUser, id=user_id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            # CustomUser.create(email=form.cleaned_data['email'], password=form.cleaned_data['password'],
            #                   first_name=form.cleaned_data['first_name'], middle_name=form.cleaned_data['middle_name'],
            #                   last_name=form.cleaned_data['last_name'])
            new_user = form.save()
            new_user.save()

        return redirect('/users')


def delete_user_by_id(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    user.delete()
    return redirect('/users')


