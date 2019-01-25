# Generated by Django 2.1.2 on 2018-10-06 23:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('housing', '0006_hostteammatch'), ('housing', '0007_auto_20181006_2346')]

    dependencies = [
        ('housing', '0005_tournament_date_lockout'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostTeamMatch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time the match was created.', verbose_name='time created')),
                ('team', models.OneToOneField(help_text='The team that is matched with the hosts.', on_delete=django.db.models.deletion.CASCADE, to='housing.Team')),
            ],
            options={
                'verbose_name': 'host team match',
                'verbose_name_plural': 'host team matches',
                'ordering': ('time_created',),
            },
        ),
        migrations.AddField(
            model_name='host',
            name='match',
            field=models.ForeignKey(blank=True, help_text='The match object that the host is associated with.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hosts', related_query_name='host', to='housing.HostTeamMatch', verbose_name='match'),
        ),
    ]