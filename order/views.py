from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import CustomUser
from .forms import OrderForm
from order.models import Order
from book.models import Book


def all_orders(request):
    return render(request, 'order_templates/all_orders.html', context={"orders_list": Order.objects.all()})


def order_by_id(request, order_id):
    selected_order = get_object_or_404(Order, pk=order_id)
    context = {"order_instance": selected_order}
    return render(request, 'order_templates/order_details.html', context=context)


def create_update_order(request, order_id=-1):
    if request.method == 'POST':
        if order_id == -1:
            form = OrderForm(request.POST)
        else:
            order = get_object_or_404(Order, id=order_id)
            form = OrderForm(request.POST, order)
        if form.is_valid():
            if order_id == -1:
                new_order = Order.create(**form.cleaned_data)
                new_order.save()
            else:
                new_order = get_object_or_404(Order, id=order_id)
                print(form.cleaned_data)
                for va in form.cleaned_data:
                    setattr(new_order, va, form.cleaned_data[va])
                new_order.save()

        return redirect('/orders')
    else:
        if order_id == -1:
            form = OrderForm()
        else:
            order = get_object_or_404(Order, id=order_id)
            print("here")
            form = OrderForm(initial=order.to_dict())
            print("here111")
        return render(request, "order_templates/order_form.html", {"form": form})


def delete_order_by_id(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('/orders')
