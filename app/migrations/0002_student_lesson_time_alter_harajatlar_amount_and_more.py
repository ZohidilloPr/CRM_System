# Generated by Django 4.0.1 on 2022-01-19 12:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lesson_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Dars boshlanish vaqti'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='harajatlar',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Qancha miqdorda'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment',
            field=models.IntegerField(default=0, verbose_name='Tolov summasi'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.teacher', verbose_name="O'qituvchisi"),
        ),
    ]
