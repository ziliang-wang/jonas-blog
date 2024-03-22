# Generated by Django 5.0.3 on 2024-03-22 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_remove_post_tags_post_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=120, verbose_name="暱稱")),
                (
                    "ip",
                    models.CharField(blank=True, max_length=50, verbose_name="留言者的ip"),
                ),
                ("body", models.TextField(verbose_name="評論內容")),
                ("active", models.BooleanField(default=True, verbose_name="有效")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="評論時間"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="core.post",
                        verbose_name="博文",
                    ),
                ),
            ],
            options={
                "verbose_name": "博文評論",
                "verbose_name_plural": "博文評論",
                "ordering": ("-created",),
            },
        ),
    ]
