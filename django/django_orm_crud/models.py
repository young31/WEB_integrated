from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20) 
    email = models.CharField() 
	birthday = models.DateField()
	age = models.IntergerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.age} ,{self.birthday}, {self.email}'