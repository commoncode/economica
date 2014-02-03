# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('promotions', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CampaignPromotion',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('promotion', models.ForeignKey(to='promotions.Promotion', to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
