# API REST: REPORTES DEL CLASIFICADOR


## Descripción

Este repositorio contiene  la Api Rest que alimenta los reportes  del  proyecto "Sistema automático de clasificación de mensajes intercambiados entre la ciudadanía y el Ayuntamiento de València". A partir de los canales de comunicación del Ayuntamiento de València se ha generado un formato que cualquier consistorio puede adaptar a sus necesidades.

El trabajo realizado se concreta en forma de código fuente  que  está diseñada para operar solamente con el método GET para consultar y leer recursos.


## Guía de uso

##### Lenguaje de programación
<<<<<<< HEAD
Este módulo fue desarrollado usando **Python 2.7.11**
=======
Este módulo fue desearrollado con **Python 2.7.11**
>>>>>>> c896c5d79e75252a805495181fb3834fe57ec9ad

##### Dependencias

* [Bottle V 0.12.13](http://bottlepy.org/docs/0.12/ "Bottle: Python Web Framework")
* [Pymongo V 3.4.0](https://api.mongodb.com/python/current/ "Pymongo 3.4.0")

**Nota**: El modulo fue desarrollado usando las librerías que se mencionaron anteriormente, por lo que se recomienda para un adecuado funcionamiento se usen  las versiones establecidas.

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



## Equipo
- Autores principales:  
  - **<a href="https://github.com/xikoto" target="_blank">José Miguel Benítez</a>**, estudiante de grado en ingeniería Informática.
  - **<a href="https://www.linkedin.com/in/marylin-mattos-a0a59b22/" target="_blank"> Marylin Mattos Barros</a>**, estudiante de Máster Oficial Universitario en Gestión de la Información


- Director del proyecto:
  - [Diego Álvarez](https://about.me/diegoalsan) | @diegoalsan


## Contexto del proyecto

El trabajo que contiene este repositorio se ha desarrollado en el [**Àrea Hackers cívics**](http://civichackers.cc). Un espacio de trabajo colaborativo formado por [hackers cívics](http://civichackers.webs.upv.es/conocenos/que-es-una-hacker-civicoa/) que buscamos y creamos soluciones a problemas que impiden que los ciudadanos y ciudadanas podamos influir en los asuntos que nos afectan y, así, construir una sociedad más justa. En definitiva, abordamos aquellos retos que limitan, dificultan o impiden nuestro [**empoderamiento**](http://civichackers.webs.upv.es/conocenos/una-aproximacion-al-concepto-de-empoderamiento/).

El [**Àrea Hackers cívics**](http://civichackers.cc) ha sido impulsada por la [**Cátedra Govern Obert**](http://www.upv.es/contenidos/CATGO/info/). Una iniciativa surgida de la colaboración entre la Concejalía de Transparencia, Gobierno Abierto y Cooperación del Ayuntamiento de València y la [Universitat Politècnica de València](http://www.upv.es).

![ÀHC](http://civichackers.webs.upv.es/wp-content/uploads/2017/02/Logo_CGO_web.png) ![ÀHC](http://civichackers.webs.upv.es/wp-content/uploads/2017/02/logo_AHC_web.png)



## Términos de uso

![](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)El contenido de este repositorio está sujeto a la licencia [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
