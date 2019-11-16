from django.urls import path
from . import views

app_name='home'
urlpatterns=[
			path('', views.homepage, name='homepage'),
			#path('payment/', views.acceptpayments, name='payment'),
			#path('api/', include(router.urls)),

]