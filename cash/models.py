from django.db import models

# Create your models here.



class ConnectionPackage(models.Model):
    package_name = models.CharField(max_length=100)
    package_amount = models.FloatField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.package_name



class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    box_number = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    connection_date = models.DateField()

    package = models.ForeignKey(
        ConnectionPackage,
        on_delete=models.PROTECT
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.customer_name

class Payment(models.Model):

    payment_choices = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Partial', 'Partial'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    amount_to_be_paid = models.FloatField()
    amount_paid = models.FloatField(default=0)
    remaining_amount = models.FloatField(default=0)

    payment_status = models.CharField(
        max_length=20,
        choices=payment_choices,
        default='Pending'
    )

    paid_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.customer.customer_name

class MonthlyBill(models.Model):

    customer = models.ForeignKey( Customer,  on_delete=models.CASCADE)

    bill_month = models.DateField()
    bill_amount = models.FloatField()
    due_date = models.DateField()

    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.customer_name



class Complaint(models.Model):

    complaint_status = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )


    complaint_title = models.CharField(max_length=200)

    complaint_description = models.TextField()

    complaint_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=complaint_status,
        default='Pending'
    )

    def __str__(self):
        return self.complaint_title








    