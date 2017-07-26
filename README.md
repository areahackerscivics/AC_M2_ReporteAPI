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

Dentro de la carpeta API se encuentra el archivo _inicio.py_ que permite arrancar el servicio REST. En este mismo fichero es donde se puede modificar el
puerto de acceso (línea 205), por defecto es el 8080.

Los servicios habilitados son:

**Distribución:** devuelve una lista de objetos JSON con el siguiente formato.
```json
[
  {
    "categoria" : "Turismo",
    "porTweets" : 1.3195098963242224,
    "numTweets" : 14
  },
...
]
```
Donde _categoria_ es el nombre de la categoría a la que pertenecen los tweets. El precálculo del porcentaje de tweets reside en el campo _porTweets_ y _numTweets_ representa el número de tweets.

**Evolución:** devuelve un diccionario, donde las claves son el nombre de la
categoría y el valor es una lista con el número de tweets para cada día del mes.
```json
{
  "Turismo" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 3, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  "Industria" : [0, 0, 0, 0, 0, 0, 0, 4, 5, 4, 3, 2, 9, 14, 10, 7, 9, 2, 8, 3, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  ...
}
```

**Catálogo:** devuelve una lista de objetos JSON con el siguiente formato.
```json
[
  {
    "categoria" : "Turismo",
    "numDatasets" : 14
  },
...
]
```
Donde _categoria_ es el nombre de la categoría a la que pertenecen los datasets
ofrecidos por el <a href="http://gobiernoabierto.valencia.es/es/" target="_blank">Ajuntament de València</a>.
Y _numDatasets_ es el número de datasets de ese tema que se ofrecen.

Los servicios **Top Palabras** y **Top Hashtags** están deshabilitados en esta versión. Estos servicios requieren de las librerías:

* [nltk 3.2.4](http://www.nltk.org/)
* [stop-words 2015.2.23.1](https://pypi.python.org/pypi/stop-words)

Todos los servicios se realizan mediante peticiones GET y requieren de dos parámetros, _anyo_ y _mes_. El año en formato de 4 dígitos (1995, 2016...) y el mes en formato de dos dígitos (02, 10...)

## Autores

**<a href="https://github.com/xikoto" target="_blank">José Miguel Benítez</a>**, estudiante de grado en ingeniería Informática.
**<a href="https://www.linkedin.com/in/marylin-mattos-a0a59b22/" target="_blank"> Marylin Mattos Barros</a>**, estudiante de Máster Oficial Universitario en Gestión de la Información
