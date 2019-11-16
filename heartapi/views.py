from django.shortcuts import render,redirect
from .forms import TestForm
from django.core import serializers
from . models import Test
from sklearn.externals import joblib
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.contrib import messages
import razorpay
import json
# Create your views here.

"""class TestView(viewsets.ModelViewSet):
	queryset = Test.objects.all()
	serializer_class = TestSerializers"""

def acceptpayments(request):
	razorpay_client = razorpay.Client(auth=("rzp_test_HNcMCOUHPcHzn3", "kTIqOIRrWsa989G9LRpprMyA"))
	template_name='payment_form.html'

	if request.method=='POST':
		#chargeapp()
		return redirect('heartapi:test')
	else:
		return render(request,template_name,{})

def chargeapp():
    amount = 5100
    payment_id = request.form['razorpay_payment_id']
    razorpay_client.payment.capture(payment_id, amount)
    return json.dumps(razorpay_client.payment.fetch(payment_id))


def form_view(request):
	template_name='form.html'
	answer=0
	if request.method=='POST':
		test_form=TestForm(request.POST)
		if test_form.is_valid():
			name=test_form.cleaned_data['name']
			age=test_form.cleaned_data['age']
			sex=test_form.cleaned_data['sex']
			sex=int(sex)
			chestpain=test_form.cleaned_data['chestpain']
			chestpain=int(chestpain)
			blood_pressure=test_form.cleaned_data['blood_pressure']
			cholestrol=test_form.cleaned_data['cholestrol']
			sugar=test_form.cleaned_data['sugar']
			sugar=int(sugar)
			restecg=test_form.cleaned_data['restecg']
			restecg=int(restecg)
			max_heart_rate=test_form.cleaned_data['max_heart_rate']
			exang=test_form.cleaned_data['angina']
			oldpeak=test_form.cleaned_data['oldpeak']
			MyDict= (request.POST).dict()
			data=pd.DataFrame(MyDict,index=[0])

			answer=get_answer(data)[0]
			answer=int(answer*100)
			print(answer)
	else:
		test_form=TestForm(request.POST)
		answer=0
	context={
				'test_form':test_form,
				'answer':answer,
	}
	return render(request,template_name,context)



def get_answer(data):
	print(type(data),'1')
	X=data.drop(['name','csrfmiddlewaretoken'],axis=1)
	print(type(X),'2')
	min_max_scaler = joblib.load('heartapi/transformer.save')
	X_scaled = min_max_scaler.transform(X)
	print(X_scaled)
	mdl=joblib.load('heartapi/Heart_Attack_prediction.pkl')
	y_pred=mdl.predict(X_scaled)
	print(y_pred)
	return y_pred
