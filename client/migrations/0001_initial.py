"""Migrations for clients app."""

# Generated by Django 2.2.6 on 2019-11-21 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Migrations for product and images app."""

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(default=18)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Ot', 'Other')], default='M', max_length=2)),
                ('address', models.TextField(max_length=500)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaleMeasurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('cm', 'Centimetre'), ('inc', 'Inches')], default='inc', max_length=3)),
                ('shoulder', models.PositiveSmallIntegerField()),
                ('armscye', models.PositiveSmallIntegerField()),
                ('chest', models.PositiveSmallIntegerField()),
                ('bust', models.PositiveSmallIntegerField()),
                ('waist', models.PositiveSmallIntegerField()),
                ('arm_length', models.PositiveSmallIntegerField()),
                ('hips', models.PositiveSmallIntegerField()),
                ('ankle', models.PositiveSmallIntegerField()),
                ('neck', models.PositiveSmallIntegerField()),
                ('back_width', models.PositiveSmallIntegerField()),
                ('inseam', models.PositiveSmallIntegerField()),
                ('wrist', models.PositiveSmallIntegerField()),
                ('crutch_depth', models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_knee', models.PositiveSmallIntegerField(blank=True)),
                ('knee_line', models.PositiveSmallIntegerField(blank=True)),
                ('biceps', models.PositiveSmallIntegerField(blank=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
        migrations.CreateModel(
            name='FemaleMeasurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('cm', 'Centimetre'), ('inc', 'Inches')], default='inc', max_length=3)),
                ('shoulder', models.PositiveSmallIntegerField()),
                ('chest', models.PositiveSmallIntegerField()),
                ('waist', models.PositiveSmallIntegerField()),
                ('hips', models.PositiveSmallIntegerField()),
                ('armscye', models.PositiveSmallIntegerField()),
                ('bust', models.PositiveSmallIntegerField()),
                ('arm_length', models.PositiveSmallIntegerField()),
                ('ankle', models.PositiveSmallIntegerField()),
                ('neck', models.PositiveSmallIntegerField()),
                ('back_width', models.PositiveSmallIntegerField()),
                ('inseam', models.PositiveSmallIntegerField()),
                ('wrist', models.PositiveSmallIntegerField()),
                ('front_sh_to_waist', models.PositiveSmallIntegerField(blank=True)),
                ('crutch_depth', models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_knee', models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_hip', models.PositiveSmallIntegerField(blank=True)),
                ('knee_line', models.PositiveSmallIntegerField(blank=True)),
                ('top_arm', models.PositiveSmallIntegerField(blank=True)),
                ('body_rise', models.PositiveSmallIntegerField(blank=True)),
                ('waist_to_floor', models.PositiveSmallIntegerField(blank=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
        ),
    ]
