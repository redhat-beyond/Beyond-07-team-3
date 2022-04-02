# Generated by Django 4.0.3 on 2022-04-01 12:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import reminders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0004_add_event_participant_test_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now,
                                                   validators=[reminders.models.validate_date])),
                ('messages', models.TextField(blank=True, null=True)),
                ('method', models.CharField(choices=[('web', 'Website'), ('ema', 'Email'),
                                                     ('wae', 'Website and Email')], default='web', max_length=3)),
                ('participant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                     to='events.eventparticipant')),
            ],
        ),
    ]
