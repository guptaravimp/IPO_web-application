from django.contrib import admin
from home.models import IPOUpcoming
from home.models import FaqModel
from home.models import Broker
# Register your models here.
class upcommmingadmin(admin.ModelAdmin):
    list_display=('icons','company_name','company_link','price_band',
    'open_date','close_date','issue_size','issue_type','listing_date')

admin.site.register(IPOUpcoming,upcommmingadmin)

class faqAdmin(admin.ModelAdmin):
    list_display=('question','ans1','ans2','ans3','ans4','ans5')
admin.site.register(FaqModel,faqAdmin)

class brokerAdmin(admin.ModelAdmin):
    list_display=('icons','company_name','rating','Opening_charge','maintanance_charge',
    'percent_delivery_brokage','percent_interaday_brokage','created_at'
    ,'updated_at')
admin.site.register(Broker,brokerAdmin)





    