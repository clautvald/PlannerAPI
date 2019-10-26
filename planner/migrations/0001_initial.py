# Generated by Django 2.2.6 on 2019-10-26 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=150)),
                ('apellidos_cliente', models.CharField(max_length=150)),
                ('celular_cliente', models.CharField(max_length=150)),
                ('correo_cliente', models.CharField(max_length=150)),
                ('genero', models.CharField(max_length=150)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventos_nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=150)),
                ('caracteristicas', models.CharField(max_length=150)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicios_nombre', models.CharField(max_length=150)),
                ('eventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedores_nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('contacto_nombre', models.CharField(max_length=150)),
                ('celular', models.IntegerField(default=0)),
                ('correo', models.CharField(max_length=150)),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Producto')),
                ('servicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Servicio')),
            ],
        ),
        migrations.CreateModel(
            name='MiEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evento', models.DateTimeField(verbose_name='fecha de evento')),
                ('eventos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Evento')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Producto')),
                ('proveedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Proveedore')),
                ('servicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.Servicio')),
            ],
        ),
    ]
