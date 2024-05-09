from django.db import models
from django.forms import ModelForm
from dashboard.models import show
from django.contrib.auth.models import User



TICKET_STATUS_CHOICES=(
    (1,'AVAILABLE'),
    (2,'BLOCKED'),
    (3,'BOOKED')
)

class booking1(models.Model):

    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(null=False)
    phonenumber=models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    row_num = models.PositiveSmallIntegerField(null=False, blank=False)
    col_num = models.PositiveSmallIntegerField(null=False, blank=False)
    show = models.ForeignKey(show, related_name="booking1_movie", null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="booking1_show", null=False, default=None, on_delete=models.CASCADE)
    status = models.IntegerField(choices=TICKET_STATUS_CHOICES, default=1)
    session = models.CharField(blank=False, null=False, max_length=200)

    def __str__(self):
        return str(self.phonenumber)
    class Meta:
        unique_together=('show','row_num','col_num')



class TicketsForm(ModelForm):
    class Meta:
        model = booking1
        fields = ['name','age','phonenumber','col_num','row_num',]


