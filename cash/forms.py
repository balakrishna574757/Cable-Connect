from django.forms import ModelForm
from .models import Customer,ConnectionPackage,Payment,MonthlyBill,Complaint




class packageForm(ModelForm):
    class Meta:
        model = ConnectionPackage
        fields = "__all__"




class customerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"




class paymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"        



from django import forms
from .models import MonthlyBill,Complaint


class MonthlyBillForm(forms.ModelForm):

    class Meta:
        model = MonthlyBill
        fields = '__all__'

        widgets = {
            'bill_month': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ComplaintForm(forms.ModelForm):


     class Meta:
       model=Complaint
       fields="__all__"





class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = '__all__'



