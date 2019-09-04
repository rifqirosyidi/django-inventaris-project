# Generated by Django 2.2.4 on 2019-09-04 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=4)),
                ('nama', models.CharField(max_length=100)),
                ('jenis', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nomor_handphone', models.CharField(max_length=20)),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Inventaris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarisir.Barang')),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarisir.Karyawan')),
            ],
        ),
    ]
