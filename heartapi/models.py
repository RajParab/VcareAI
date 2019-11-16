from django.db import models

# Create your models here.

class Test(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField(default=0)
	sex=models.CharField(max_length=5,choices=(('1', 'Male'),('0', 'Female')))
	chestpain=models.CharField(max_length=30,choices=(('1','Typical Angina'),('2','Atypical Angina'),
													  ('3','Non-anginal Pain'),('4','Asymptomatic')))
	blood_pressure=models.IntegerField(default=0)
	cholestrol=models.IntegerField(default=0)
	sugar=models.CharField(max_length=30,choices=(('0','Less than 120mg/dl'),('1','More than 120mg/dl')))
	restecg=models.CharField(max_length=30,choices=(('0','Normal'),('1','ST-T wave abnormality'),('2', 'Estes criteria')))
	max_heart_rate=models.IntegerField(default=0)
	angina=models.CharField(max_length=30,choices=(('0','No'),('1','Yes')),default=0)
	oldpeak=models.IntegerField(default=0)

	def __str__(self):
		return self.name
