from django.urls import path
from .views import  package_view, customer_view,payment_view,customer_display,payments_display
from .views import dashboard_view, monthlybill_view, logout_view, customer_details, loginView, package_edit, package_delete,customer_edit,customer_delete,payment_edit,monthlybill_edit,complaint_view,complaint_edit
urlpatterns = [
    
    path('package/', package_view, name='package'),
    path('package/edit/<int:id>/', package_edit, name='package-edit'),
    path('package/delete/<int:id>/', package_delete, name='package-delete'),
    path('customer/', customer_view, name='customer'),
    path('customerlist/',customer_display, name='customer_display'),
    path('customeredit/<int:customer_id>/', customer_edit, name='customer-edit'),
    path('customerdelete/<int:customer_id>/', customer_delete, name='customer-delete'),
    path('payment/',payment_view,name="payment"),
    path('payment_list/', payments_display, name='payments_display'),
    path('paymentedit/<int:payment_id>/', payment_edit, name='payment-edit'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('monthlybill/', monthlybill_view, name='monthlybill'),
    path('monthlybilledit/<int:monthlybill_id>/', monthlybill_edit, name='monthlybill-edit'),
    path("",loginView,name="login"),
    path('complaint/', complaint_view, name='complaint'),
    path('customerdetails/<int:customer_id>/', customer_details, name='customer_details'),
    path('complaintedit/<int:complaint_id>/', complaint_edit, name='complaint_edit'),
    path('logout/', logout_view, name='logout'),
   
]