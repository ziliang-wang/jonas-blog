# Generated by Django 5.0.3 on 2024-03-20 12:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fullname",
                    models.CharField(blank=True, max_length=20, verbose_name="全名"),
                ),
                (
                    "title",
                    models.CharField(blank=True, max_length=120, verbose_name="職稱"),
                ),
                (
                    "avatar",
                    models.ImageField(
                        default="avatars/avatar.png",
                        upload_to="avatars",
                        verbose_name="頭像",
                    ),
                ),
                (
                    "line",
                    models.CharField(blank=True, max_length=50, verbose_name="Line"),
                ),
                (
                    "weixin",
                    models.CharField(blank=True, max_length=50, verbose_name="微信"),
                ),
                (
                    "facebook",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Facebook"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=120, verbose_name="Facebook"
                    ),
                ),
                (
                    "url",
                    models.URLField(blank=True, max_length=250, verbose_name="個人網站"),
                ),
                (
                    "github",
                    models.URLField(
                        blank=True, max_length=250, verbose_name="GitHub主頁"
                    ),
                ),
                ("bio", models.TextField(blank=True, verbose_name="個人簡介")),
                ("hits", models.IntegerField(default=0, verbose_name="點擊量")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="創建時間"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用戶",
                    ),
                ),
            ],
            options={
                "verbose_name": "個人資料",
                "verbose_name_plural": "個人資料",
            },
        ),
    ]
