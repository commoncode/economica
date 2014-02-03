# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    
    dependencies = [
        ('offers', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rea', '__first__'),
        ('platforms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteItem',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('offer', models.ForeignKey(to='offers.Offer', to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(to_field=u'id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(to_field=u'id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('platform', models.ForeignKey(to='platforms.Platform', to_field=u'id')),
                ('recieving_agent', models.ForeignKey(to='rea.Agent', to_field=u'id')),
                ('providing_agent', models.ForeignKey(to='rea.Agent', to_field=u'id')),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
