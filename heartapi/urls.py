from django.urls import path
from . import views
"""from rest_framework import routers

router = routers.DefaultRouter()
router.register('Form', views.form_view)
"""
app_name='heartapi'
urlpatterns=[
			path('predict/', views.form_view, name='test'),
			path('payment/', views.acceptpayments, name='payment'),
			#path('api/', include(router.urls)),

]