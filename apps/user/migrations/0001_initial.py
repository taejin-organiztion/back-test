# Generated by Django 5.1.7 on 2025-04-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=15, unique=True, verbose_name='닉네임')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='전화번호')),
                ('last_login', models.DateTimeField(null=True, verbose_name='마지막 로그인')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저 목록',
                'db_table': 'users',
            },
        ),
    ]
