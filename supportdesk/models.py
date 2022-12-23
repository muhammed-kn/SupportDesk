from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SupportTicket(models.Model):
    summary=models.CharField(max_length=20)
    description=models.TextField()
    assigned_to=models.ForeignKey(User,on_delete=models .CASCADE,related_name="assigned")
    is_completed=models.BooleanField(default=False) 
    is_priority=models.BooleanField() 
    created_date=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="created")
    updated_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="updated",null=True,blank=True)

    def __str__(self) -> str:
        return self.summary

