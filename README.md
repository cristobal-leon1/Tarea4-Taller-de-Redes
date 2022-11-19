# Uso de Dockers y Postgres, modificación e inyección con Scapy
> En la presente actividad, se ha realizado la conexión del cliente postgres al servidor postgres montado en un contenedor de docker.


## Table of Contents
* [Información general](#Información-general)
* [Tecnologías utilizadas](#Tecnologías-utilizadas)
* [Configuración](#Configuración)
* [Uso](#Uso)
* [Estado del proyecto](#estado-del-proyecto)
* [Contacto](#contacto)



## Información general
- Este proyecto tiene como objetivo realizar la conexión del cliente postgres al servidor postgres montado en un contenedor de docker.
- Originalmente se debia conectar al contendedor del servidor un cliente pgcli montado en un contenedor.
- Esto no pudo ser logrador con exito, ya que al intentar conectarse a contenedor del servidor, devolvia un error el cual no esta en el alcance del curso resolver
- Por otro lado, la finalidad de esta actividad es comprender el us de docker y establecer conexión cliente-servidor utilizando esta tecnología.



## Tecnologías utilizadas
- Docker - version 19.03.8
- PostgreSQL - version 15.0
- Cliente Postgres - version 12.2
- Scapy - version 2.5.0




## Configuración
Como primera medida se debe tener instalado docker y postgres.
Luego, se debe descargar el Dockerfile del servidor de Postgres(https://github.com/mygeone2/softwares-dockerfiles-TDR-2022-2/blob/main/PSQL/posgresql.Dockerfile)
Finalmente, se debe utilizar la terminal en la carpeta en donde se tenga el Dockerfile, como tambien se debe tener abierto el cliente oficial de postgres para conectarnos al servidor montado en el contenedor.

## Uso
Para crear la imagen con Dockerfile:

```
    docker build .
```

Para crear el contenedor:

```
    docker run -it id_image
```

Para correr el servidor:

```
    docker start -i id_contenedor
```

Conocer la ip asociada al contenedor del servidor:
    
```
    docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' id_container
```
    


Conectar al servidor desde el cliente:

```
    psql -U postgres -h ip_server
```
    

## Estado del proyecto
El proyecto esta finalizado, por lo que no se seguira trabajando en el.


## Video de la modificación e inyección de trafico, mediante las herramientas Polymorph y Scapy
[![Watch the video](images/play2.png)](https://www.youtube.com/watch?v=p-FECoBrzTo)



## Contacto
cristobal.leon1@mail.udp.cl
jairo.morales@mail.udp.cl 

