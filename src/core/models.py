from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
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


class Category(models.Model):
    """ 博文分類 """
    slug = models.SlugField('地址縮寫', max_length=120)
    name = models.CharField('名稱', max_length=50)
    description = models.CharField('描述', max_length=250, blank=True)
    order = models.IntegerField('排序', default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-order', 'id')
        verbose_name = '博文分類'
        verbose_name_plural = '博文分類'


class PublishedManager(models.Manager):
    """ 自定義模型管理器(查詢邏輯) """    
    def get_queryset(self) -> models.QuerySet:
        return super(PublishedManager, self).get_queryset().filter(status='published')
    

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'),
        ('published', '發佈')
    )
    title = models.CharField('標題', max_length=250)
    slug = models.SlugField('地址縮寫', max_length=120, unique_for_date='created')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name='分類')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='作者')
    img = models.ImageField('圖片', upload_to='uploads', blank=True, null=True)
    summary = models.CharField('摘要', max_length=250, blank=True)
    body = models.TextField('正文')

    # tags = models.CharField('標簽', max_length=200)
    tags = TaggableManager('標籤')

    views = models.IntegerField('瀏覽數', default=0)
    flag = models.BooleanField('標記', default=False)
    status = models.CharField('狀態', max_length=120, choices=STATUS_CHOICES, default='draft')

    updated = models.DateTimeField('更新時間', auto_now=True)
    created = models.DateTimeField('創建時間', auto_now_add=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        """ 獲取當前博文的絕對地址 """
        # return reverse('details', args=[self.id,])
        return reverse('details', args=[self.slug,])
    
    # default 模型管理器
    objects = models.Manager()
    
    # 自定義模型管理器(獲取所有已發佈博文)
    published = PublishedManager()
    
    class Meta:
        verbose_name = '博文管理'
        verbose_name_plural = '博文管理'
        ordering = ('-created',)


class Comment(models.Model):
    """ 評論表 """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='博文')
    name = models.CharField('暱稱', max_length=120)
    ip = models.CharField('留言者的ip', max_length=50, blank=True)
    body = models.TextField('評論內容')

    active = models.BooleanField('有效', default=True)
    created = models.DateTimeField('評論時間', auto_now_add=True)

    def __str__(self):
        return f'<{self.name}> commented <{self.post}>'
    

    class Meta:
        ordering = ('-created',)
        verbose_name = '博文評論'
        verbose_name_plural = '博文評論'

