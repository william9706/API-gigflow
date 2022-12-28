from rest_framework import serializers
from servicios import models




class EntregableSerializer(serializers.ModelSerializer):
    """ serializador para tipos de servicio """
    
    class Meta:
        model= models.Entregables
        fields = (
            'id',
            'nombre'
        )


class PaquetesSerializer(serializers.ModelSerializer):
    """ serializador para paquetes. """

    entregables = EntregableSerializer(many=True)

    class Meta:
        model= models.Paquetes
        fields = (
            'id',
            'descripcion',
            'precio',
            'entregables',
        )
    
    
    def create(self, validated_data):
        """ metodo para crear paquetes. """
        entregables = validated_data.pop('entregables', [])      
        paquete = models.Paquetes.objects.create(**validated_data)
        paquete.save()

        for entregable in entregables:
            entregable_obj = models.Entregables.objects.get(
                nombre=entregable['nombre']
            )
            paquete.entregables.add(entregable_obj)
        return paquete

    def update(self, instance, validated_data):
        """ metodo para actualizar un paquete. """
        instance.entregables.clear()
        entregables_data = validated_data.pop('entregables')
        instance = super(PaquetesSerializer, self).update(instance, validated_data)

        for entregable_data in entregables_data:
            entregable_qs = models.Entregables.objects.filter(
                nombre__iexact=entregable_data['nombre']
            )

            if entregable_qs.exists():
                entregable = entregable_qs.first()
            else:
                entregable = models.Entregables.objects.create(**entregable_data)

            instance.entregables.add(entregable)

        return instance
    
    def validate(self, data):
        if data['descripcion'] == '':
            raise serializers.ValidationError(
                "El campo descripcion no puede estar vacio."
            )
        elif data['precio'] == '' or data['precio'] is None:
            raise serializers.ValidationError(
                "El campo precio no puede estar vacio."
            )
        return data


class ServicioSerializer(serializers.ModelSerializer):
    """ serializador para tipos de servicio """

    paquetes = PaquetesSerializer(many=True)


    class Meta:
        model= models.Servicios
        fields = (
            'id',
            'nombre',
            'paquetes'
        )
        read_only_fields = ('id',)
    
    def create(self, validated_data):
        """ metodo para crear servicio. """
        paquetes = validated_data.pop('paquetes', [])
        servicios = models.Servicios.objects.create(**validated_data)
        servicios.save()

        for paquete in paquetes:
            paquete_obj = models.Paquetes.objects.get(
                descripcion=paquete['descripcion']
            )
            servicios.paquetes.add(paquete_obj)
            for entregable in paquete['entregables']:
                entregable_obj = models.Entregables.objects.get(
                    nombre=entregable['nombre']
                )
                paquete_obj.entregables.add(entregable_obj)
        return servicios


    def update(self, instance, validated_data):
        """ metodo para actualizar un servicio. """
        instance.paquetes.clear()
        paquetes_data = validated_data.pop('paquetes')
        instance = super(ServicioSerializer, self).update(instance, validated_data)

        for paquete_data in paquetes_data:
            paquete_qs = models.Paquetes.objects.filter(
                descripcion__iexact=paquete_data['descripcion']
            )

            if paquete_qs.exists():
                paquete = paquete_qs.first()
            else:
                paquete = models.Paquetes.objects.create(**paquete_data)

            instance.paquetes.add(paquete)

        return instance
    
    def validate(self, data):
        if data['nombre'] == '':
            raise serializers.ValidationError(
                "El campo nombre no puede estar vacio."
            )
        return data
