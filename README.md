Python 3.8.16

# README #

This README would normally document whatever steps are necessary to get your application up and running.


### Cómo me configuro? ###

* Resumen de la configuración
* Configuración
Contenedores
- *db* - Base de datos
- *app* - Aplicación en Django (no NGINX)
- docker version: 20.10.18
- docker comnpose version: v2.10.2

Construir imagenes: `docker compose build`


La primera vez que se ejecuta el comando se construyen las imagenes de los contenedores a partir del template, posterior a esto solo se refresca la información. Adicionalmente, aplica las migraciones y carga los fixtures. El proceso completo tarda alrededor de 10 minutos.

luego de crear los contenedores para la aplicaion y la base de datos(Postgres) 

Aplica migraciones: `docker compose run web python manage.py migrate`

Cargue los fixtures: `docker compose run web python manage.py loaddata fixtures/model_name.json --app app.model_name`


* Dependencias
Para configuración local Docker
* Configuración de la base de datos
### Cómo ejecutar Tests Unitarios ###
  Para ejecutar los test unitrarios se usa el siguiente comando:
  `docker compose run web python manage.py test`
* Instrucciones de implementación (Deployment)

### Pautas de contribución ###

* Lanzar servidor
`docker compose up`


* Pruebas de escritura
* Revisión de código
* Otras pautas

### Con quien hablo? ###

* Propietario o administrador del repositorio
* Otro contacto de la comunidad o del equipo
