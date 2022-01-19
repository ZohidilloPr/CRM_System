# Generated by Django 4.0.1 on 2022-01-19 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50, verbose_name='ISM')),
                ('last_name', models.CharField(max_length=50, verbose_name='FAMILYA')),
                ('address', models.CharField(max_length=250, verbose_name='MANZIL')),
                ('img', models.ImageField(blank=True, null=True, upload_to='user_pic/', verbose_name='Profile uchun Rasm')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='EMAIL')),
                ('phone_number', models.CharField(max_length=9, verbose_name='TELEFON RAQAM')),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
