
<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center>¡Bienvenidos a la presentación de mi primer proyecto individual de la etapa de labs! en el rol de un ***Data Engineer***.</h1>

# <h1> **Labs PROYECTO INDIVIDUAL Nº1** </h1>
Este proyecto tiene como objeto, mostrar las diversas habilidades y destrezas adquiridas y desarrolladas a lo largo de los modulos I, II, III Y IV Concretamente.
# <h1> **Area de Proyecto Data Engineering** </h1>
Objetivo del Proyecto: Es simular el entorno de trabajo de un Data Engineer, debiendo realizar tareas inherentes al puesto. Aplicar criterio para realizar el EDA y la utilización de las herramientas. Desarrollar habilidades de aprendizaje en el uso python, fastAPI, render, gitHUB y git


<br/>

## **Descripción del problema (Contexto y rol a desarrollar)**

<br/>

## Contexto

Tienes tu modelo de recomendación entrenado dando unas buenas métricas :smirk:, y ahora, cómo lo llevas al mundo real? :eyes:

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

<br/>

## Rol a desarrollar

Empezaste a trabajar como **`Data Scientist`** en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha! 

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula :sob:): Datos sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas….  haciendo tu trabajo imposible :weary:. 


<br/>

## **Propuesta de trabajo (se usaran las siguientes transformaciones requeridas)**
<br/>

- dentro del archivo de "ETL.ipynb" se veran las tranformaciones aplicadas al proyecto 

- se entrega un CVS "DF_completo.csv" con todas  las tranformaciones aplicadas brindando un dataset limpio </h1> 

- se entrega un CSV "plataformas.csv" con las tranformaciones aplicadas en el EDA esta con el analisis de las variables

- modelo de recomendacion

<br/>

# <h1 > **I PARTE :** Transformaciones  </h1> 

 ### a) Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

 + cargamos los dataset de la carpeta csv: (Amazon, Disney, Hulo, Netflix)

 + Hacemos la asignacion de variable y las transformaciones para sustituir los valores, generar campo id con el formato requerido (Amazon = as123), utilizando y aplicando basicamente el metodo ".astype('str')" a las columnas que realmente precisamos


### b) Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”)

+ Los valores nulos del campo rating los reemplazare por el string “G” (corresponde al maturity rating: “general for all audiences con el siguiente metodo:  `df.fillna({"rating" : "G"})`

### c) De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Las fechas, existentes serán tratadas y transformadas y luego todas tener el formato AAAA-mm-dd en el cual aplique el metodo: pd.to_datetime de la siguiente manera expuesta en el ejemplo a continuación

+ peliculas_1["date_added"] = pd.to_datetime(peliculas_1["date_added"])

### d) Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ seleccionamos los campos a convertir de los dataset: (`type`, `title`, `director`, `cast`, `country`, `rating`, `duration`, `listed_in`, `description`)

+ la funcion aplicada es `.str.lower()`

### e) El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

+ Separamos el campo "duration" en 2 columnas con la funcion  `str.split(" ", n=1, expand=True)`

+ Insertamos una columna con la funcion `splitcolumnas[#]`

+ cambiamos el formato de la columna por un integer

+ eliminamos la columna duration

<br/>

## **generacion del score**

+ cargamos los dataset del la carpeta ratings: 

+ cambio el formato de la columna 'timestamp', aca lo paso de int a 'float'

+ Cambiamos el nombre del campo 'rating' por 'score'

<br/>

## **generacion de csv**

- `el primer csv que se crear es: MoviesScore.csv, (este no se puede cargar en el github ya que es muy pesado se recomienda ejecutar todo el  ETL.ipynb para poder generlo)`

- `el segundo  csv que se crear es: DF_completo.csv, (ejecutamos todo ETL.ipynb)` con este dataset trabajaremos nuestras funciones en la API

<br/>


# <h1 > **II PARTE :** Desarrollo API> 

Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***, generando diferentes endpoints que se consumiran en la API.

Creas 6 funciones (recuerda que deben tener un decorador por cada una (@app.get(‘/’)):

+ Película (sólo película, no serie, ni documentales, etc) con mayor duración según año, plataforma y tipo de duración. La función debe llamarse get_max_duration(year, platform, duration_type) y debe devolver sólo el string del nombre de la película.
+ Cantidad de películas (sólo películas, no series, ni documentales, etc) según plataforma, con un puntaje mayor a XX en determinado año. La función debe llamarse get_score_count(platform, scored, year) y debe devolver un int, con el total de películas que cumplen lo solicitado.

+ Cantidad de películas (sólo películas, no series, ni documentales, etc) según plataforma. La función debe llamarse get_count_platform(platform) y debe devolver un int, con el número total de películas de esa plataforma. Las plataformas deben llamarse amazon, netflix, hulu, disney.

+ Actor que más se repite según plataforma y año. La función debe llamarse get_actor(platform, year) y debe devolver sólo el string con el nombre del actor que más se repite según la plataforma y el año dado.

+ La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año. La función debe llamarse prod_per_county(tipo,pais,anio) deberia devolver el tipo de contenido (pelicula,serie,documental) por pais y año en un diccionario con las variables llamadas 'pais' (nombre del pais), 'anio' (año), 'pelicula' (tipo de contenido).

+ La cantidad total de contenidos/productos (todo lo disponible en streaming, series, documentales, peliculas, etc) según el rating de audiencia dado (para que publico fue clasificada la pelicula). La función debe llamarse get_contents(rating) y debe devolver el numero total de contenido con ese rating de audiencias.

<br/>

## Generacion de la API en fastAPI
<br/>

### a) creamos el ambiente virtual 

- la creacion del entorno virtual en python nos permite  aislar y controlar las dependencias y versiones de los paquetes de software utilizados en un proyecto.
- es muy útil en el desarrollo de una API en Python, ya que permite mantener un ambiente de trabajo limpio y organizado, evitando problemas de compatibilidad entre diferentes paquetes y versiones.
- en este se pueden instalar las dependencias necesarias sin afectar el resto del sistema. De esta manera, se evita la interferencia entre diferentes versiones de librerías, lo que puede resultar en errores y conflictos.
- Además, al utilizar un entorno virtual, se pueden replicar fácilmente los mismos paquetes y versiones de software en diferentes máquinas y sistemas operativos, lo que facilita la colaboración entre desarrolladores y el despliegue de la API en diferentes entornos.
- creacion del ambiente virtual desde la terminal 
<br/>

python -m venv venv -- crear el ambiente virtual desde la terminal

cd

.\venv\

Set-ExecutionPolicy -ExecutionPolicy Remotesigned -Scope process

.\Scripts\

.\activate

cd ..

cd ..

pip install (las librerias) ---> Carpeta raiz

<br/>  

###  b) creamos nuestra instancion en fastAPI

- Cargamos nuestras librerias 
- Declaración de la creación de la API  <br/> 
app = FastAPI()
<br/> 

###  c) Creamos las querys
Estas estan especificadas en el documento "main.py"

- Desarrollo de las consultas con formato:
   
```ruby
@app.get("/tipo_de_consulta/")
def tipo_de_consulta(variable1:tipo_de_dato, variable"n":...):
  desarrollo_de_la_funcion
```

###  d) Creamos Requierements.txt
Requierements.txt que contiene las dependencias necesarias para que funcione 

<br/> 

###  d) Creamos api en un puerto local 

- uvicorn main:app

- uvicorn main:app --reload #---> para que quede cocorriendo mientras dse programa

<br/> 


### para poder generar nuestras consultas es necesario ir a la siguientes rutas 

- http://localhost:8000

- http://localhost:8000/docs

<br/> 

###  e) cargamos el archivo a git hub

git init

git add .

git commit -m "first commit"

git branch -M main

git remote add origin ......

git push -u origin main

<br/> 

# <h1 > **III PARTE :** Deployment> 

este nos permite que la API se implemente en un ambiente de producción para que esté disponible para su uso por los usuarios finales, y proporciona una serie de beneficios, como la escalabilidad, el monitoreo y la capacidad de actualizar la API para mejorar su rendimiento.

- creamos un usuario

- nos conectamos con el github y el repo que vamos a trabajar y creamos el render

- ponemos el nombre y uvicorn main:app --host 0.0.0.0 --port 10000

- luego en environment ponemos PIP_VERSION y 23.0.1

- en logs seleccionamos manual deploy y elegimos la ultima opcion 

- esperamos que cargue(demora)

- obtenemos la direccion 

<br/> 

# <h1 > **IV PARTE :** Analisis Exploratorio de Datos

Una vez finalizado, procedi a realizar el EDA (archivo EDA.py) en donde realize varios pasos de Engeneering para acomodar el DF. Con los datos acomodados y sin nulos, utulize la libreria Pandas Profiling para generar un reporte y asi poder analizar posibles variables interesantes que sirvan para un modelo de prediccion

- analisamos cada columna eliminando las que no aperten informacion a un futuro modelo de recomendacion 

- obtenemos un csv limpio "plataformas.csv"

<br/> 


# <h1 > **IV PARTE :** Modelo de recomendacion 


Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas. Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse get_recommendation(titulo: str).

- creamos un nuevo dataframe 
- reinicia el índice del DataFrame user_item de modo que el índice numérico comience desde cero y descarta el índice anterior. 
- delimitamos el dataframe

- El código dado implementa un vectorizador TfidfVectorizer con parámetros de reducción de procesamiento, seguido de un cálculo de matriz de similitud de coseno utilizando la matriz ajustada del vectorizador. Luego, se utiliza la descomposición en valores singulares aleatoria (randomized SVD) para reducir la dimensionalidad de la matriz de similitud de coseno a un número deseado de componentes.

- Específicamente, el vectorizador TfidfVectorizer se ha configurado con tres parámetros:

- min_df: el número mínimo de documentos en los que una palabra debe aparecer para que se incluya en el vocabulario.
- max_df: el número máximo de documentos en los que una palabra puede aparecer para que se incluya en el vocabulario.
- ngram_range: el rango de longitud de n-gramas que se considerarán en la construcción del vocabulario.
- A continuación, se ajusta y transforma el texto de la columna "title" del DataFrame mediante el método fit_transform(), que devuelve una matriz dispersa de término-documento, donde cada fila representa un documento y cada columna representa un término en el vocabulario.

- Luego, se calcula la matriz de similitud de coseno utilizando la función cosine_similarity() de la biblioteca sklearn, que mide la similitud entre pares de documentos en términos de coseno del ángulo entre sus vectores de términos. Esta matriz de similitud tiene una forma cuadrada, donde el tamaño de la matriz es igual al número de documentos en la matriz de términos.

- Después de eso, se utiliza la descomposición en valores singulares aleatoria (randomized SVD) para reducir la dimensionalidad de la matriz de similitud de coseno a un número deseado de componentes. La descomposición en valores singulares aleatoria es un método rápido y eficiente para calcular una aproximación de baja dimensión de una matriz de similitud de coseno. El número deseado de componentes se ha establecido en 10 en este caso.

- La matriz de similitud de coseno reducida resultante se construye a partir de la matriz U, la matriz Sigma diagonal y la matriz transpuesta de V, que se obtienen como resultados de la descomposición en valores singulares aleatoria. El tamaño de la matriz reducida es de 500x500, que se especifica en el cálculo de la matriz reducida.


## Generacion de la funcion en la API

La función get_recommendation() toma un título como entrada y devuelve una lista de los 5 títulos más similares en base a la matriz de similitud de coseno reducida calculada previamente. A continuación, se explica la función paso a paso:

- Se busca el índice correspondiente al título pasado como parámetro en la columna 'title' del DataFrame user_item. Esto se realiza utilizando la función np.where(), que devuelve el índice de las filas donde se encuentra el valor del título en la columna 'title'. En este caso, se utiliza [0][0] para obtener el índice exacto y no una tupla con un único valor.

- Se encuentra las puntuaciones de similitud del título con todos los demás títulos en la matriz de similitud de coseno reducida. Esto se hace mediante la selección de la fila correspondiente al índice del título en la matriz reducida.

- Las puntuaciones de similitud se ordenan de menor a mayor utilizando la función argsort() de NumPy y se invierte el orden para obtener las puntuaciones de similitud de mayor a menor. Esto devuelve los índices ordenados de los títulos más similares en base a la matriz de similitud de coseno reducida.

- Se seleccionan los primeros 5 índices de los títulos más similares utilizando la sintaxis de segmentación de matrices. Esto se hace mediante la selección de los primeros 5 elementos de la lista de índices ordenados.

- Se devuelve una lista de los 5 títulos más similares en base a los índices seleccionados. Esto se realiza mediante la selección de los títulos correspondientes a los índices seleccionados en el DataFrame user_item y la conversión de los títulos en una lista utilizando el método tolist(). Si el título dado como parámetro no se encuentra en la base de datos, se imprime un mensaje de aviso.
 
 <br/> 

## Deploy

- se genera un cambio en los datos por lo tanto volvemos a aplicar el render  
- obtenemos las nuevas url para las consultas 
 
 
 https://proyecto-1-soy-henry.onrender.com

https://proyecto-1-soy-henry.onrender.com/docs
 
 
 # <h1 > **V PARTE :** Video 
 
 https://youtu.be/XaOKlqAgY98
 
