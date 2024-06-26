# Generated by Django 5.0.6 on 2024-06-18 18:37

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('foto', models.ImageField(null=True, upload_to='personas', verbose_name='Imagen')),
                ('f_nacto', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('Otro', 'Otro')], default='Otro', max_length=10)),
                ('pais', models.CharField(choices=[('AFGANISTAN', 'AF'), ('ALBANIA', 'AL'), ('ALEMANIA', 'DE'), ('ANGOLA', 'AO'), ('ANTILLAS HOLAND', 'AN'), ('ARABIA SAUDITA', 'SA'), ('ARGELIA', 'DZ'), ('ARGENTINA', 'AR'), ('ARMENIA', 'AM'), ('AUSTRALIA', 'AU'), ('AUSTRIA', 'AT'), ('BAHAMAS', 'BS'), ('BARBADOS', 'BB'), ('BELGICA', 'BE'), ('BELICE', 'BZ'), ('BENIN', 'BJ'), ('BERMUDAS', 'BM'), ('BOLIVIA', 'BO'), ('BOSNIA', 'BA'), ('BRASIL', 'BR'), ('BULGARIA', 'BG'), ('CABO VERDE', 'CV'), ('CAMERUN', 'CM'), ('CANADA', 'CA'), ('CHILE', 'CL'), ('CHINA', 'CN'), ('CHIPRE', 'CY'), ('COLOMBIA', 'CO'), ('CONGO', 'CG'), ('COSTA DE MARFIL', 'CI'), ('COSTA RICA', 'CR'), ('CROACIA', 'HR'), ('CUBA', 'CU'), ('CURAZAO', 'CX'), ('DINAMARCA', 'DK'), ('DOMINICA', 'DM'), ('ECUADOR', 'EC'), ('EGIPTO', 'EG'), ('EL SALVADOR', 'SV'), ('EMIRATOS ARABES', 'AE'), ('ESLOVAKIA', 'SK'), ('ESLOVENIA', 'SI'), ('ESPAÑA', 'ES'), ('ESTADOS UNIDOS', 'US'), ('ESTONIA', 'EE'), ('FILIPINAS', 'PH'), ('FINLANDIA', 'FI'), ('FRANCIA', 'FR'), ('GABON', 'GA'), ('GEORGEA', 'GE'), ('GHANA', 'GH'), ('GRAN BRETAÑA', 'GB'), ('GRANADA', 'GD'), ('GRECIA', 'GR'), ('GUATEMALA', 'GT'), ('GUERNSEY', 'GG'), ('GUYANA', 'GY'), ('HAITI', 'HT'), ('HOLANDA', 'NL'), ('HONDURAS', 'HN'), ('HONG KONG', 'HK'), ('HUNGRIA', 'HU'), ('INDIA', 'IN'), ('INDONESIA', 'ID'), ('INGLATERRA', 'IG'), ('IRAN', 'IR'), ('IRAQ', 'IQ'), ('IRLANDA', 'IE'), ('ISLA DE MAN', 'IM'), ('ISLANDIA', 'IS'), ('ISLAS CAIMAN', 'KY'), ('ISLAS MARSHALL', 'MH'), ('ISLAS VIRGENES (U.S)', 'VI'), ('ISLAS VIRGENES BRITANICAS', 'VG'), ('ISRAEL', 'IL'), ('ITALIA', 'IT'), ('JAMAICA', 'JM'), ('JAPON', 'JP'), ('JERSEY', 'JE'), ('JORDANIA', 'JO'), ('KAZAJISTAN', 'KZ'), ('KENYA', 'KE'), ('KUWAIT', 'KW'), ('LIBANO', 'LB'), ('LIBERIA', 'LR'), ('LUXEMBURGO', 'LU'), ('MALASIA', 'MY'), ('MALTA', 'MT'), ('MARRUECOS', 'MA'), ('MAURICIO', 'MU'), ('MAURITANIA', 'MR'), ('MEXICO', 'MX'), ('MONACO', 'MC'), ('MONGOLIA', 'MN'), ('MONTENEGRO', 'ME'), ('MOZAMBIQUE', 'MZ'), ('NAMIBIA', 'NA'), ('NEPAL', 'NP'), ('NICARAGUA', 'NI'), ('NIGERIA', 'NG'), ('NORUEGA', 'NO'), ('NUEVA ZELANDIA', 'NZ'), ('OMAN', 'OM'), ('PAKISTAN', 'PK'), ('PALESTINA', 'PS'), ('PANAMA', 'PA'), ('PARAGUAY', 'PY'), ('PERU', 'PE'), ('POLONIA', 'PL'), ('PORTUGAL', 'PT'), ('PUERTO RICO', 'PR'), ('QATAR', 'QA'), ('REINO DE BAHREIN', 'BH'), ('REP DOMINICANA', 'DO'), ('REP. COREA', 'KR'), ('REP. DEM. COREA', 'KP'), ('REP.ARABE SIRIA', 'SY'), ('REPUBLICA CHECA', 'CZ'), ('REPUBLICA DE AZERBAIYAN', 'AZ'), ('REPUBLICA DE BELARUS', 'BY'), ('REPUBLICA DE UZBEKISTAN', 'UZ'), ('RUMANIA', 'RO'), ('RUSIA', 'RU'), ('SAMOA AMERICANA', 'AS'), ('SAN MARINO', 'SM'), ('SENEGAL', 'SN'), ('SERBIA', 'RS'), ('SIERRA LEONE', 'SL'), ('SINGAPUR', 'SG'), ('SOMALIA', 'SO'), ('SRI LANKA', 'LK'), ('SUD AFRICA', 'ZA'), ('SUDAN', 'SD'), ('SUECIA', 'SE'), ('SUIZA', 'CH'), ('SURINAM', 'SR'), ('TAILANDIA', 'TH'), ('TAIWAN', 'TW'), ('TAYIKISTAN', 'TJ'), ('TRINIDAD TOBAGO', 'TT'), ('TURQUIA', 'TR'), ('UCRANIA', 'UA'), ('URUGUAY', 'UY'), ('VENEZUELA', 'VE'), ('VIETNAM', 'VN'), ('ZAIRE', 'ZR'), ('ZAMBIA', 'ZM')], default='CL', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('direccion', models.CharField(max_length=500, null=True, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=9, null=True, verbose_name='Teléfono')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('tipo', models.CharField(choices=[('Anaconda', 'Anaconda'), ('Perro', 'Perro'), ('Manatí', 'Manatí'), ('Gato', 'Gato')], max_length=30)),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('subtipo', models.CharField(choices=[('Perro', [('Kiltro', 'Kiltro'), ('Verde', 'Verde')]), ('Gato', [('Angora', 'Angora'), ('Volador', 'Volador')]), ('Sin subtipo', 'Sin Subtipo')], default='Sin subtipo', max_length=20)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_orm.persona')),
            ],
        ),
    ]
