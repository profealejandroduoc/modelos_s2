# Generated by Django 5.0.6 on 2024-06-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0011_persona_foto_alter_mascota_tipo_alter_persona_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='tipo',
            field=models.CharField(choices=[('Gato', 'Gato'), ('Anaconda', 'Anaconda'), ('Perro', 'Perro'), ('Manatí', 'Manatí')], max_length=30),
        ),
        migrations.AlterField(
            model_name='persona',
            name='f_nacto',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(null=True, upload_to='personas', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='pais',
            field=models.CharField(choices=[('AFGANISTAN', 'AF'), ('ALBANIA', 'AL'), ('ALEMANIA', 'DE'), ('ANGOLA', 'AO'), ('ANTILLAS HOLAND', 'AN'), ('ARABIA SAUDITA', 'SA'), ('ARGELIA', 'DZ'), ('ARGENTINA', 'AR'), ('ARMENIA', 'AM'), ('AUSTRALIA', 'AU'), ('AUSTRIA', 'AT'), ('BAHAMAS', 'BS'), ('BARBADOS', 'BB'), ('BELGICA', 'BE'), ('BELICE', 'BZ'), ('BENIN', 'BJ'), ('BERMUDAS', 'BM'), ('BOLIVIA', 'BO'), ('BOSNIA', 'BA'), ('BRASIL', 'BR'), ('BULGARIA', 'BG'), ('CABO VERDE', 'CV'), ('CAMERUN', 'CM'), ('CANADA', 'CA'), ('CHILE', 'CL'), ('CHINA', 'CN'), ('CHIPRE', 'CY'), ('COLOMBIA', 'CO'), ('CONGO', 'CG'), ('COSTA DE MARFIL', 'CI'), ('COSTA RICA', 'CR'), ('CROACIA', 'HR'), ('CUBA', 'CU'), ('CURAZAO', 'CX'), ('DINAMARCA', 'DK'), ('DOMINICA', 'DM'), ('ECUADOR', 'EC'), ('EGIPTO', 'EG'), ('EL SALVADOR', 'SV'), ('EMIRATOS ARABES', 'AE'), ('ESLOVAKIA', 'SK'), ('ESLOVENIA', 'SI'), ('ESPAÑA', 'ES'), ('ESTADOS UNIDOS', 'US'), ('ESTONIA', 'EE'), ('FILIPINAS', 'PH'), ('FINLANDIA', 'FI'), ('FRANCIA', 'FR'), ('GABON', 'GA'), ('GEORGEA', 'GE'), ('GHANA', 'GH'), ('GRAN BRETAÑA', 'GB'), ('GRANADA', 'GD'), ('GRECIA', 'GR'), ('GUATEMALA', 'GT'), ('GUERNSEY', 'GG'), ('GUYANA', 'GY'), ('HAITI', 'HT'), ('HOLANDA', 'NL'), ('HONDURAS', 'HN'), ('HONG KONG', 'HK'), ('HUNGRIA', 'HU'), ('INDIA', 'IN'), ('INDONESIA', 'ID'), ('INGLATERRA', 'IG'), ('IRAN', 'IR'), ('IRAQ', 'IQ'), ('IRLANDA', 'IE'), ('ISLA DE MAN', 'IM'), ('ISLANDIA', 'IS'), ('ISLAS CAIMAN', 'KY'), ('ISLAS MARSHALL', 'MH'), ('ISLAS VIRGENES (U.S)', 'VI'), ('ISLAS VIRGENES BRITANICAS', 'VG'), ('ISRAEL', 'IL'), ('ITALIA', 'IT'), ('JAMAICA', 'JM'), ('JAPON', 'JP'), ('JERSEY', 'JE'), ('JORDANIA', 'JO'), ('KAZAJISTAN', 'KZ'), ('KENYA', 'KE'), ('KUWAIT', 'KW'), ('LIBANO', 'LB'), ('LIBERIA', 'LR'), ('LUXEMBURGO', 'LU'), ('MALASIA', 'MY'), ('MALTA', 'MT'), ('MARRUECOS', 'MA'), ('MAURICIO', 'MU'), ('MAURITANIA', 'MR'), ('MEXICO', 'MX'), ('MONACO', 'MC'), ('MONGOLIA', 'MN'), ('MONTENEGRO', 'ME'), ('MOZAMBIQUE', 'MZ'), ('NAMIBIA', 'NA'), ('NEPAL', 'NP'), ('NICARAGUA', 'NI'), ('NIGERIA', 'NG'), ('NORUEGA', 'NO'), ('NUEVA ZELANDIA', 'NZ'), ('OMAN', 'OM'), ('PAKISTAN', 'PK'), ('PALESTINA', 'PS'), ('PANAMA', 'PA'), ('PARAGUAY', 'PY'), ('PERU', 'PE'), ('POLONIA', 'PL'), ('PORTUGAL', 'PT'), ('PUERTO RICO', 'PR'), ('QATAR', 'QA'), ('REINO DE BAHREIN', 'BH'), ('REP DOMINICANA', 'DO'), ('REP. COREA', 'KR'), ('REP. DEM. COREA', 'KP'), ('REP.ARABE SIRIA', 'SY'), ('REPUBLICA CHECA', 'CZ'), ('REPUBLICA DE AZERBAIYAN', 'AZ'), ('REPUBLICA DE BELARUS', 'BY'), ('REPUBLICA DE UZBEKISTAN', 'UZ'), ('RUMANIA', 'RO'), ('RUSIA', 'RU'), ('SAMOA AMERICANA', 'AS'), ('SAN MARINO', 'SM'), ('SENEGAL', 'SN'), ('SERBIA', 'RS'), ('SIERRA LEONE', 'SL'), ('SINGAPUR', 'SG'), ('SOMALIA', 'SO'), ('SRI LANKA', 'LK'), ('SUD AFRICA', 'ZA'), ('SUDAN', 'SD'), ('SUECIA', 'SE'), ('SUIZA', 'CH'), ('SURINAM', 'SR'), ('TAILANDIA', 'TH'), ('TAIWAN', 'TW'), ('TAYIKISTAN', 'TJ'), ('TRINIDAD TOBAGO', 'TT'), ('TURQUIA', 'TR'), ('UCRANIA', 'UA'), ('URUGUAY', 'UY'), ('VENEZUELA', 'VE'), ('VIETNAM', 'VN'), ('ZAIRE', 'ZR'), ('ZAMBIA', 'ZM')], default='CL', max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('Otro', 'O'), ('Masculino', 'M'), ('Femenino', 'F')], default='Otro', max_length=10),
        ),
    ]
