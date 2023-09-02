# Generated by Django 4.1.6 on 2023-07-03 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college_app', '0002_initial'),
        ('faculty_app', '0001_initial'),
        ('course_app', '0001_initial'),
        ('person_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person_app.person')),
                ('level', models.IntegerField()),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='major_students', to='college_app.department')),
                ('minor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='minor_students', to='college_app.department')),
            ],
            bases=('person_app.person',),
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_app.section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_sections', to='student_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_app.section')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transcript', to='student_app.student')),
            ],
            options={
                'unique_together': {('section', 'student')},
            },
        ),
        migrations.CreateModel(
            name='Grad_Student',
            fields=[
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='grade_student', serialize=False, to='student_app.student', unique=True)),
                ('collage', models.CharField(max_length=50)),
                ('degree', models.FloatField()),
                ('year', models.IntegerField()),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advisor_of', to='faculty_app.faculty')),
                ('committee', models.ManyToManyField(related_name='committee', to='faculty_app.faculty')),
            ],
        ),
    ]