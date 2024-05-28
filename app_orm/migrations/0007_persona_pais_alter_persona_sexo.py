# Generated by Django 5.0.6 on 2024-05-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0006_persona_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='pais',
            field=models.CharField(choices=[('AF', 'AFGANISTAN'), ('AL', 'ALBANIA'), ('DE', 'ALEMANIA'), ('AO', 'ANGOLA'), ('AN', 'ANTILLAS HOLAND'), ('SA', 'ARABIA SAUDITA'), ('DZ', 'ARGELIA'), ('AR', 'ARGENTINA'), ('AM', 'ARMENIA'), ('AU', 'AUSTRALIA'), ('AT', 'AUSTRIA'), ('BS', 'BAHAMAS'), ('BB', 'BARBADOS'), ('BE', 'BELGICA'), ('BZ', 'BELICE'), ('BJ', 'BENIN'), ('BM', 'BERMUDAS'), ('BO', 'BOLIVIA'), ('BA', 'BOSNIA'), ('BR', 'BRASIL'), ('BG', 'BULGARIA'), ('CV', 'CABO VERDE'), ('CM', 'CAMERUN'), ('CA', 'CANADA'), ('CL', 'CHILE'), ('CN', 'CHINA'), ('CY', 'CHIPRE'), ('CO', 'COLOMBIA'), ('CG', 'CONGO'), ('CI', 'COSTA DE MARFIL'), ('CR', 'COSTA RICA'), ('HR', 'CROACIA'), ('CU', 'CUBA'), ('CX', 'CURAZAO'), ('DK', 'DINAMARCA'), ('DM', 'DOMINICA'), ('EC', 'ECUADOR'), ('EG', 'EGIPTO'), ('SV', 'EL SALVADOR'), ('AE', 'EMIRATOS ARABES'), ('SK', 'ESLOVAKIA'), ('SI', 'ESLOVENIA'), ('ES', 'ESPAÑA'), ('US', 'ESTADOS UNIDOS'), ('EE', 'ESTONIA'), ('PH', 'FILIPINAS'), ('FI', 'FINLANDIA'), ('FR', 'FRANCIA'), ('GA', 'GABON'), ('GE', 'GEORGEA'), ('GH', 'GHANA'), ('GB', 'GRAN BRETAÑA'), ('GD', 'GRANADA'), ('GR', 'GRECIA'), ('GT', 'GUATEMALA'), ('GG', 'GUERNSEY'), ('GY', 'GUYANA'), ('HT', 'HAITI'), ('NL', 'HOLANDA'), ('HN', 'HONDURAS'), ('HK', 'HONG KONG'), ('HU', 'HUNGRIA'), ('IN', 'INDIA'), ('ID', 'INDONESIA'), ('IG', 'INGLATERRA'), ('IR', 'IRAN'), ('IQ', 'IRAQ'), ('IE', 'IRLANDA'), ('IM', 'ISLA DE MAN'), ('IS', 'ISLANDIA'), ('KY', 'ISLAS CAIMAN'), ('MH', 'ISLAS MARSHALL'), ('VI', 'ISLAS VIRGENES (U.S)'), ('VG', 'ISLAS VIRGENES BRITANICAS'), ('IL', 'ISRAEL'), ('IT', 'ITALIA'), ('JM', 'JAMAICA'), ('JP', 'JAPON'), ('JE', 'JERSEY'), ('JO', 'JORDANIA'), ('KZ', 'KAZAJISTAN'), ('KE', 'KENYA'), ('KW', 'KUWAIT'), ('LB', 'LIBANO'), ('LR', 'LIBERIA'), ('LU', 'LUXEMBURGO'), ('MY', 'MALASIA'), ('MT', 'MALTA'), ('MA', 'MARRUECOS'), ('MU', 'MAURICIO'), ('MR', 'MAURITANIA'), ('MX', 'MEXICO'), ('MC', 'MONACO'), ('MN', 'MONGOLIA'), ('ME', 'MONTENEGRO'), ('MZ', 'MOZAMBIQUE'), ('NA', 'NAMIBIA'), ('NP', 'NEPAL'), ('NI', 'NICARAGUA'), ('NG', 'NIGERIA'), ('NO', 'NORUEGA'), ('NZ', 'NUEVA ZELANDIA'), ('OM', 'OMAN'), ('PK', 'PAKISTAN'), ('PS', 'PALESTINA'), ('PA', 'PANAMA'), ('PY', 'PARAGUAY'), ('PE', 'PERU'), ('PL', 'POLONIA'), ('PT', 'PORTUGAL'), ('PR', 'PUERTO RICO'), ('QA', 'QATAR'), ('BH', 'REINO DE BAHREIN'), ('DO', 'REP DOMINICANA'), ('KR', 'REP. COREA'), ('KP', 'REP. DEM. COREA'), ('SY', 'REP.ARABE SIRIA'), ('CZ', 'REPUBLICA CHECA'), ('AZ', 'REPUBLICA DE AZERBAIYAN'), ('BY', 'REPUBLICA DE BELARUS'), ('UZ', 'REPUBLICA DE UZBEKISTAN'), ('RO', 'RUMANIA'), ('RU', 'RUSIA'), ('AS', 'SAMOA AMERICANA'), ('SM', 'SAN MARINO'), ('SN', 'SENEGAL'), ('RS', 'SERBIA'), ('SL', 'SIERRA LEONE'), ('SG', 'SINGAPUR'), ('SO', 'SOMALIA'), ('LK', 'SRI LANKA'), ('ZA', 'SUD AFRICA'), ('SD', 'SUDAN'), ('SE', 'SUECIA'), ('CH', 'SUIZA'), ('SR', 'SURINAM'), ('TH', 'TAILANDIA'), ('TW', 'TAIWAN'), ('TJ', 'TAYIKISTAN'), ('TT', 'TRINIDAD TOBAGO'), ('TR', 'TURQUIA'), ('UA', 'UCRANIA'), ('UY', 'URUGUAY'), ('VE', 'VENEZUELA'), ('VN', 'VIETNAM'), ('ZR', 'ZAIRE'), ('ZM', 'ZAMBIA')], default='CL', max_length=20),
        ),
        migrations.AlterField(
            model_name='persona',
            name='sexo',
            field=models.CharField(choices=[('O', 'Otro'), ('M', 'Masculino'), ('F', 'Femenino')], default='O', max_length=1),
        ),
    ]
