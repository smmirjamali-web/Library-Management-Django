from django.db import models

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    USER_TYPE_CHOICES = [
        ('member', 'عضو عادی'),
        ('librarian', 'کتابدار'),
        ('admin', 'مدیر'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='member')
    national_id = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=11)
    joined_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {(self.national_id)}"
    
    class Meta:
        ordering = ['-joined_at']
