
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import customerForm,packageForm,paymentForm,MonthlyBillForm,ComplaintForm
from .models import ConnectionPackage,Customer,Payment,MonthlyBill





from django.shortcuts import render, redirect, get_object_or_404
from .models import ConnectionPackage
from .forms import packageForm


# CREATE AND DISPLAY

def package_view(request):

    form = packageForm()

    if request.method == "POST":
        form = packageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('package')

    packages = ConnectionPackage.objects.all()

    return render(request, 'package.html', {
        'form': form,
        'packages': packages
    })


# UPDATE

def package_edit(request, id):

    package = get_object_or_404(ConnectionPackage, id=id)

    if request.method == "POST":
        form = packageForm(request.POST, instance=package)

        if form.is_valid():
            form.save()
            return redirect('package')

    else:
        form = packageForm(instance=package)

    return render(request, 'package_edit.html', {
        'form': form
    })


# DELETE

def package_delete(request, id):

    package = get_object_or_404(ConnectionPackage, id=id)

    if request.method == "POST":
        package.delete()
        return redirect('package')

    return render(request, 'package_delete.html', {
        'package': package
    })





def customer_view(request):
    form = customerForm()

    if request.method == "POST":
        form = customerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('customer_display')

    return render(request, 'customer.html', {'form': form})

def customer_display(request):
    customers = Customer.objects.all().order_by('-id')

    return render(
        request,
        'customer_list.html',
        {'customers': customers}
    )

def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    form = customerForm(instance=customer)

    if request.method == "POST":
        form = customerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            return redirect('customer_display')

    return render(request, 'customer_edit.html', {
        'form': form,
        'customer': customer
    })



def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == "POST":
        customer.delete()
        return redirect('customer_display')

    return render(request, 'customer_delete.html', {
        'customer': customer
    })






def payment_view(request):

    form = paymentForm()

    if request.method == "POST":
        form = paymentForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('payments_display')

    return render(request, "payment.html", {"form": form})


def payments_display(request):
    payments = Payment.objects.all().order_by('-id')

    return render(request, "payment_list.html", {
        "payments": payments
    })


def payment_edit(request, payment_id):

    payment = get_object_or_404(Payment, id=payment_id)

    form = paymentForm(instance=payment)

    if request.method == "POST":
        form = paymentForm(request.POST, instance=payment)

        if form.is_valid():
            form.save()
            return redirect('payments_display')

    return render(request, "payment_edit.html", {
        "form": form,
        "payment": payment
    })





def monthlybill_view(request):

    form = MonthlyBillForm()

    if request.method == "POST":
        form = MonthlyBillForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('monthlybill')

    bills = MonthlyBill.objects.all().order_by('-id')

    return render(request, 'monthlybill.html', {
        'form': form,
        'bills': bills
    })


def monthlybill_edit(request, monthlybill_id):

    monthlybill = get_object_or_404(
        MonthlyBill,
        id=monthlybill_id
    )

    form = MonthlyBillForm(instance=monthlybill)

    if request.method == "POST":
        form = MonthlyBillForm(
            request.POST,
            instance=monthlybill
        )

        if form.is_valid():
            form.save()
            return redirect('monthlybill')

    return render(request, 'monthlybill_edit.html', {
        'form': form,
        'monthlybill': monthlybill
    })



from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Customer, ConnectionPackage, Payment, MonthlyBill,Complaint
from .forms import ComplaintForm

def dashboard_view(request):

    total_customers = Customer.objects.count()

    active_customers = Customer.objects.filter(
        is_active=True
    ).count()

    total_packages = ConnectionPackage.objects.count()

    total_collection = Payment.objects.aggregate(
        total=Sum('amount_paid')
    )['total'] or 0

    pending_bills = MonthlyBill.objects.filter(
        is_paid=False
    ).count()

    paid_bills = MonthlyBill.objects.filter(
        is_paid=True
    ).count()

    pending_amount = Payment.objects.aggregate(
        total=Sum('remaining_amount')
    )['total'] or 0

    recent_payments = Payment.objects.order_by(
        '-paid_date'
    )[:5]

    context = {
        'total_customers': total_customers,
        'active_customers': active_customers,
        'total_packages': total_packages,
        'total_collection': total_collection,
        'pending_bills': pending_bills,
        'paid_bills': paid_bills,
        'pending_amount': pending_amount,
        'recent_payments': recent_payments,
    }

    return render(request, 'dashboard.html', context)


from django.contrib.auth import authenticate
def loginView(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        if user is not None:
            return redirect("dashboard")
        else:
            return redirect("login")

    return render(request,"login.html")




def complaint_view(request):
    complaints = Complaint.objects.all().order_by('-id')
    print(complaints)
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
      

        if form.is_valid():
            form.save()
            return redirect('complaint')

    else:
        form = ComplaintForm()

    return render(request, 'complaint.html', {'form': form,"complaints":complaints})



def customer_details(request, customer_id):

    customer = get_object_or_404(Customer, id=customer_id)

    complaints = Complaint.objects.filter(
        customer=customer
    ).order_by('-complaint_date')

    return render(request, 'customer_details.html', {
        'customer': customer,
        'complaints': complaints
    })


def complaint_edit(request, complaint_id):

    complaint = get_object_or_404(Complaint, id=complaint_id)

    if request.method == 'POST':

        form = ComplaintForm(request.POST, instance=complaint)

        if form.is_valid():
            form.save()
            return redirect('customer_details', customer_id=complaint.customer.id)

    else:
        form = ComplaintForm(instance=complaint)

    return render(request, 'complaint_edit.html', {
        'form': form,
        'complaint': complaint
    })

    


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

