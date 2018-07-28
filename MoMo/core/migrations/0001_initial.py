# Generated by Django 2.0.7 on 2018-07-26 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('date_received', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaasInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.GenericIPAddressField()),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.SaasInstance'),
        ),
        migrations.AddField(
            model_name='payment',
            name='psp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.PaymentServiceProvider'),
        ),
    ]