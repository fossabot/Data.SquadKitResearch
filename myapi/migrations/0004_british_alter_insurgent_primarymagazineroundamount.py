# Generated by Django 4.0.4 on 2022-05-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_insurgent'),
    ]

    operations = [
        migrations.CreateModel(
            name='British',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleName', models.CharField(default='N/A', max_length=60, verbose_name='Role Name')),
                ('faction', models.CharField(default='N/A', max_length=20, verbose_name='Role Faction')),
                ('PrimaryWeapon', models.CharField(default='N/A', max_length=30, verbose_name='Role Primary Weapon')),
                ('PrimaryWeaponSights', models.CharField(default='N/A', max_length=30, verbose_name='Role Primary Weapon Sight')),
                ('PrimaryFiringModes', models.CharField(default='N/A', max_length=30, verbose_name='Role Primary Weapon Firing Modes')),
                ('PrimaryMagazineAmount', models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Amount')),
                ('PrimaryMagazineRoundAmount', models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount')),
                ('SecondaryWeapon', models.CharField(default='N/A', max_length=60, verbose_name='Role Secondary')),
                ('SecondaryWeaponSights', models.CharField(default='N/A', max_length=60, verbose_name='Role Secondary Weapon Sights')),
                ('SecondaryWeaponFiringModes', models.CharField(default='N/A', max_length=60, verbose_name='Role Secondary Weapon Firing Modes')),
                ('SecondaryWeaponMagAmount', models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Amount')),
                ('SecondaryWeaponMagRoundAmount', models.IntegerField(default=0, verbose_name='Role Secondary Weapon Magazine Round Amount')),
                ('Knife', models.CharField(default='N/A', max_length=30, verbose_name='Role Knife')),
            ],
        ),
        migrations.AlterField(
            model_name='insurgent',
            name='PrimaryMagazineRoundAmount',
            field=models.IntegerField(default=0, verbose_name='Role Primary Weapon Mag Round Amount'),
        ),
    ]
