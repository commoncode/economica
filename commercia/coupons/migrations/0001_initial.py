# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('rea', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                (u'resource_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field=u'id', serialize=False, to='rea.Resource')),
                ('code', models.CharField(max_length=512)),
            ],
            options={
                u'abstract': False,
            },
            bases=('rea.resource',),
        ),
    ]
