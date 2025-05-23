# Generated by Django 3.2.16 on 2023-01-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('서비스안내', '서비스안내'), ('점검안내', '점검안내'), ('약관안내', '약관안내')], max_length=10, verbose_name='공지종류')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='등록시간')),
                ('title', models.TextField(max_length=128, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='공지내용')),
                ('hits', models.PositiveBigIntegerField(default=0, verbose_name='조회수')),
                ('top_fixed', models.BooleanField(default=False, verbose_name='상단고정')),
                ('notice_image', models.ImageField(blank=True, upload_to='nImg', verbose_name='공지이미지')),
            ],
        ),
    ]
