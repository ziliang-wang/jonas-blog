from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='用戶')
    fullname = models.CharField('全名', max_length=20, blank=True)
    aliasname = models.CharField('別名', max_length=20, blank=True)
    title = models.CharField('職稱', max_length=120, blank=True)
    avatar = models.ImageField('頭像', default='avatars/avatar.png', upload_to='avatars')
    line = models.CharField('Line', max_length=50, blank=True)
    weixin = models.CharField('微信', max_length=50, blank=True)
    facebook = models.CharField('Facebook', max_length=50, blank=True)
    email = models.CharField('email', max_length=120, blank=True)
    url = models.URLField('個人網站', max_length=250, blank=True)
    github = models.URLField('GitHub主頁', max_length=250, blank=True)
    bio = models.TextField('個人簡介', blank=True)
    hits = models.IntegerField('點擊量', default=0)
    created = models.DateTimeField('創建時間', auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username}的個人資料'

    class Meta:
        verbose_name = '個人資料'
        verbose_name_plural = '個人資料'