# API REST: REPORTES DEL CLASIFICADOR


Àrea Hackers Cívics 2017 [civichackers.cc](http://civichackers.cc)

## Información
El trabajo que contiene este repositorio se ha desarrollado en el contexto de colaboración entre el Ayuntamiento de València y la Universitat Politècnica de València, en la Càtedra GO. El Àrea Hackers Cívics es el espacio de trabajo colaborativo resultante 
de esta colaboración. 

## Términos de uso
El contenido de este repositorio está sujeto a la licencia Creative Commons de [Atribución 4.0](https://creativecommons.org/licenses/by/4.0/).

## Descripción
Este módulo está desarrollado en el márco del proyecto, "Sistema automático de clasificación de mensajes intercambiados entre la ciudadanía y el Ayuntamiento de València". Se ha desarrollado usando como objeto el Ayuntamiento de València, pero con la idea de que cualquier consistorio pueda adaptarlo a sus necesidades.

Básicamente la API está diseñada para operar solamente con el método GET para consultar y leer recursos.

## Guía de uso

##### Lenguaje de programación
Este módulo fue desearrollado usando **Python 2.7.11** 

##### Dependencias

* [Bottle 0.12.13](http://bottlepy.org/docs/0.12/ "Bottle: Python Web Framework")
* [Pymongo 3.4.0](https://api.mongodb.com/python/current/ "Pymongo 3.4.0")

**Nota**: El modulo fue desarrolloado usando las librerias que se mensionaron anteriormente, por lo que se recomienda para un adecuado funcionamiento se usen  las versiones establecidas.

##### Base de datos

Como sistema de almacenamiento se usa MongoDB que es una base de datos NoSQL que guarda los datos en documentos almacenados en BSON. Para este módulo se usa una colección que tiene la siguiente estructura:

```json
{
    "_id" : ObjectId("58de2570bc54f43b544428e0"),
    "categoria" : "Seguridad",
    "idt" : "844492061080535041",
    "texto" : "hola mundo",
    "puntaje" : 0.508395516543446,
    "fecha" : ISODate("2017-03-31T11:46:24.669Z"),
    "fechaTweet" : ISODate("2017-03-22T10:12:51.000Z")
}

```
Es importante que los nombres de las claves sean iguales como se muestra en el ejemplo anterior, debido a que  dentro del código se hace referencia a esos nombres.  

En el archivo **ConexionMongoPublico.py** del proyecto se indica el nombre de la colección y la base de datos con la que se trabajó, si desea poner otro nombre a la base de datos o a la colección es necesario que lo actualice también en ese archivo. Finalmente debe renombrar el archivo con el nombre  **ConexionMongo.py** .

El Àrea se abstiene de publicar los datos con los que se desarrolló el proyecto debido a la Ley Orgánica de  Protección de Datos.

##### Funcionamiento del proyecto

Dentro de la carpeta API se encuentra el archivo de inicio del programa que permite arrancar el servicio REST por el puerto 8080.
 
Los servicios habilitados son:

**Distribución:** http://localhost:8080/distribucion?anyo=2017&mes=07  

**Evolución:** http://localhost:8080/evolucion?anyo=2017&mes=03  

**Catálogo:** http://localhost:8080//catalogo?anyo=2017&mes=07  


## Autores

**José Miguel Benítez**, estudiante de grado en ingeniería Informática. 
**Marylin Mattos Barros**, estudiante de Máster Oficial Universitario en Gestión de la Información 

