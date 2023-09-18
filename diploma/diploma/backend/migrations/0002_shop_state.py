from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='state',
            field=models.BooleanField(default=True, verbose_name='статус работы магазина'),
        ),
    ]
