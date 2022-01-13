# Generated by Django 3.2.3 on 2021-09-04 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('payment', models.IntegerField(default=150000)),
                ('added_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('expirence', models.CharField(max_length=100)),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='List.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('study_days', models.CharField(choices=[('choises...', 'Choises...'), ('du-ch-j', 'Du-Ch-J'), ('se-p-sh', 'Se-P-Sh'), ('du-se-ch-p-j', 'Du-Se-Ch-P-J'), ('every-day', 'Every-day')], default='choises...', max_length=100)),
                ('study_type', models.CharField(choices=[('choises...', 'Choises...'), ('individual', 'Individual'), ('team', 'Team')], default='choises...', max_length=100)),
                ('paied_payment', models.IntegerField(default=0)),
                ('phone_number', models.IntegerField()),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('study_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='List.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='List.teacher')),
            ],
        ),
    ]
