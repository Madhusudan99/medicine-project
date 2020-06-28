# Generated by Django 3.0.7 on 2020-06-25 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('license_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('patient_visiting_date', models.DateField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription_direction_day_week_month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_week_month', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription_direction_frequency_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency_count', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_id', models.IntegerField()),
                ('prescription_date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
                ('drug_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Drug')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Patient')),
                ('prescription_direction_day_week_month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Prescription_direction_day_week_month')),
                ('prescription_direction_frequency_count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Prescription_direction_frequency_count')),
            ],
        ),
    ]
