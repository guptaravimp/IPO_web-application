from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('broker/', views.broker, name='broker'),
    path('ipoupcomming/', views.ipoupcomming, name='ipoupcomming'),
    path('tradingview/', views.tradingview, name='tradingview'),
    path('community/', views.community, name='community'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
