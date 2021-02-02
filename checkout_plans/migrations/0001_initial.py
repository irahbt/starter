# Generated by Django 3.1.4 on 2021-02-02 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripeid', models.CharField(max_length=255)),
                ('stripe_subscription_id', models.CharField(max_length=255)),
                ('cancel_at_period_end', models.BooleanField(default=False)),
                ('membership', models.BooleanField(default=False)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plans', to='profiles.userprofile')),
            ],
        ),
    ]
