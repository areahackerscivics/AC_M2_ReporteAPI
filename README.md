# API REST: REPORTES DEL CLASIFICADOR


## Descripción

Este repositorio contiene  la Api Rest que alimenta los reportes  del  proyecto "Sistema automático de clasificación de mensajes intercambiados entre la ciudadanía y el Ayuntamiento de València". A partir de los canales de comunicación del Ayuntamiento de València se ha generado un formato que cualquier consistorio puede adaptar a sus necesidades.

El trabajo realizado se concreta en forma de código fuente  que  está diseñada para operar solamente con el método GET para consultar y leer recursos.


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
    "idt" : "123456789",
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

## Equipo
- Autores principales:
**José Miguel Benítez**, estudiante de grado en ingeniería Informática. 
**Marylin Mattos Barros**, estudiante de Máster Oficial Universitario en Gestión de la Información

- Director del proyecto:

  [Diego Álvarez](https://about.me/diegoalsan) | @diegoalsan

- Codirector del proyecto:

  [David Pardo](https://about.me/david_pardo) | @davidpardo

## Contexto del proyecto

El trabajo que contiene este repositorio se ha desarrollado en el [**Àrea Hackers cívics**](http://civichackers.cc). Un espacio de trabajo colaborativo formado por [hackers cívics](http://civichackers.webs.upv.es/conocenos/que-es-una-hacker-civicoa/) que buscamos y creamos soluciones a problemas que impiden que los ciudadanos y ciudadanas podamos influir en los asuntos que nos afectan y, así, construir una sociedad más justa. En definitiva, abordamos aquellos retos que limitan, dificultan o impiden nuestro [**empoderamiento**](http://civichackers.webs.upv.es/conocenos/una-aproximacion-al-concepto-de-empoderamiento/).

El [**Àrea Hackers cívics**](http://civichackers.cc) ha sido impulsada por la [**Cátedra Govern Obert**](http://www.upv.es/contenidos/CATGO/info/). Una iniciativa surgida de la colaboración entre la Concejalía de Transparencia, Gobierno Abierto y Cooperación del Ayuntamiento de València y la [Universitat Politècnica de València](http://www.upv.es).

![ÀHC](http://civichackers.webs.upv.es/wp-content/uploads/2017/02/Logo_CGO_web.png) ![ÀHC](http://civichackers.webs.upv.es/wp-content/uploads/2017/02/logo_AHC_web.png)



## Términos de uso

![](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)El contenido de este repositorio está sujeto a la licencia [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
