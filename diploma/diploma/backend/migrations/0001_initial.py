from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('type', models.CharField(choices=[('distributor', 'Магазин'), ('client', 'Покупатель')], default='client', max_length=15, verbose_name='Тип пользователя')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Ник пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Список пользователей',
                'ordering': ('email',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Список категорий',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('confirmed', 'подтвержден'), ('canceled', 'отменен'), ('in_process', 'в процессе выбора клиентом'), ('paid', 'оплачен'), ('assembly', 'в процессе сборки'), ('in delivery', 'передан в службу доставки'), ('in client', 'доставлен')], max_length=35, verbose_name='Статус заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Список заказов',
                'ordering': ('-dt',),
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Список параметров',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='backend.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Список продуктов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('bp_number', models.PositiveIntegerField(verbose_name='Внутренний артикул')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('price_rrc', models.PositiveIntegerField(verbose_name='Стоимость без скидки')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_info', to='backend.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Информация о продукте',
                'verbose_name_plural': 'Список продуктов',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.URLField(blank=True, null=True)),
                ('filename', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь в базе')),
            ],
            options={
                'verbose_name_plural': 'Список магазинов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Значение')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='backend.parameter', verbose_name='Параметр продукта')),
                ('product_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='backend.productinfo', verbose_name='Информация по продукту')),
            ],
            options={
                'verbose_name_plural': 'Список параметров',
            },
        ),
        migrations.AddField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_info', to='backend.shop', verbose_name='Магазин'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='backend.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='backend.productinfo', verbose_name='Инфо о продукте')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='backend.shop', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Список заказанных позиций',
            },
        ),
        migrations.CreateModel(
            name='ClientCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apt', models.CharField(blank=True, max_length=70, verbose_name='апартаменты')),
                ('buildings', models.CharField(blank=True, max_length=70, verbose_name='номер дома')),
                ('street', models.CharField(blank=True, max_length=150, verbose_name='улица')),
                ('city', models.CharField(max_length=70, verbose_name='город')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('postcode', models.PositiveIntegerField(verbose_name='почтовый индекс')),
                ('mobile', models.CharField(max_length=20, verbose_name='Контактный номер телефона')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Карточка  контактов клиента',
                'verbose_name_plural': 'Карточки клиентов',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='shops',
            field=models.ManyToManyField(to='backend.shop'),
        ),
        migrations.AddConstraint(
            model_name='productparameter',
            constraint=models.UniqueConstraint(fields=('product_info', 'parameter'), name='unique_product_parameters'),
        ),
        migrations.AddConstraint(
            model_name='productinfo',
            constraint=models.UniqueConstraint(fields=('product', 'shop', 'bp_number'), name='unique_product_info'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order_id', 'product'), name='unique_order_item'),
        ),
    ]
