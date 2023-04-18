#Importo librerias 
from fastapi import FastAPI, HTTPException
import pandas as pd
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional
import uvicorn
import numpy as np 

# creo una instancia de FastAPI
app = FastAPI(tittle= "Proyecto 1 - Soy Henry")


# introduccion
@app.get("/")
def presentacion():
    return {"PI 01 - Javier Alezander Rios Sanmartin"}

@app.get("/contacto")
def contacto():
    return "Email: alekzander_bk@hotmail.com / Github: Alekzander10"

@app.get("/menu")
def menu():
    return "Las funciones utilizadas: get_max_duration, get_score_count, get_count_platform, get_actor, prod_per_county, get_contents "



#---------- Queries-----

#Primer consigna: Película (sólo película, no serie, ni documentales, etc) con mayor duración según año, 
# plataforma y tipo de duración. La función debe llamarse get_max_duration(year, platform, duration_type)
# y debe devolver sólo el string del nombre de la película..


@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
def get_max_duration(year: Optional[int] = None, platform: Optional[str] = None, duration_type: Optional[str] = 'min'):
    #Lectura de la base de datos:
    
    df = pd.read_csv('Df_completo.csv')

    # Verificar que la plataforma sea una de las opciones válidas
    if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("opciones válidas: Disney, Amazon, Hulu o Netflix.")
    if duration_type is not None and duration_type not in ['min', 'season']:
        return('Los valores validos son: min, season')

   
    canalplataforma= df[df['Id'].str.contains(platform[0], case= False)]

    #Aplico filtro para el año y e tipo de duracion
    año_duracion= canalplataforma[(canalplataforma.release_year == year) & (canalplataforma.duration_type == duration_type)]
    #Accedo a las columnas y tomo el indice mayor de cada columna
    idmax= año_duracion[['title']].loc[año_duracion.duration_int.idxmax()] 
    #El resultado lo paso a un formato de diccionario
    pelicula_max= idmax.T.to_dict() 

    return pelicula_max

# Segunda consigna: Cantidad de películas (sólo películas, no series, ni documentales, etc) 
# según plataforma, con un puntaje mayor a XX en determinado año. La función debe llamarse 
# get_score_count(platform, scored, year) y debe devolver un int, con el total de películas que cumplen lo solicitado

#Segunda consigna: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/{platform}/{scored}/{release_year}")
def get_score_count(platform : str, scored : float, release_year: int):
        # Lectura de la base de datos:
    df = pd.read_csv('Df_completo.csv')

    # Verificar que la plataforma sea una de las opciones válidas
    if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("La plataforma debe ser una de las opciones válidas: Disney, Amazon, Hulu o Netflix.")

    # Filtrar las películas para la plataforma, año y puntaje especificados
    filtro = df[(df.platform == platform) & (df.score > scored) & (df.release_year == release_year) & (df.type == 'movie')]

    # Agrupar por plataforma y contar el número de filas resultantes
    respuesta = filtro.groupby('platform').size().to_dict()

    return {
        'plataforma y cantidad': respuesta,
        'anio': release_year,
        'score': scored
    }

#Tercer consigna: Cantidad de películas (sólo películas, no series, ni documentales, etc) según plataforma.
# La función debe llamarse get_count_platform(platform) y debe devolver un int, 
# con el número total de películas de esa plataforma. Las plataformas deben llamarse amazon, netflix, hulu, disney.


@app.get("/get_count_platform/{platform}")
def get_count_platform(platform: str):
    #Lectura de la base de datos:
    df = pd.read_csv('Df_completo.csv')

    # Verificar que la plataforma sea una de las opciones válidas
    if platform is not None and platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("La plataforma debe ser una de las opciones válidas: Disney, Amazon, Hulu o Netflix.")
    
    # Check if input value is valid and exists in DataFrame
    assert platform.lower() in df['platform'].unique(), f"Invalid platform: {platform}"
    
    #Filtrar las películas para la plataforma y duración mínima especificada
    filtro = df[(df.platform == platform)  & (df.type == 'movie')]

    #luego hago un conteo del tamaño del filtro que hice
    conteo = len(filtro)

    respuesta = {'plataforma': platform, 'peliculas': conteo}

    return respuesta

#Cuarta consigna: Actor que más se repite según plataforma y año.
#  La función debe llamarse get_actor(platform, year) y debe devolver sólo el string con el nombre del actor
#  que más se repite según la plataforma y el año dado.

@app.get("/get_actor/{platform}/{year}")
def get_actor(platform: str, year: int):
    # Lectura de la base de datos:
    df = pd.read_csv('Df_completo.csv')

    df = pd.read_csv('Df_completo.csv')

    # Verificar que la plataforma sea una de las opciones válidas
    if platform.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("La plataforma debe ser una de las opciones válidas: Disney, Amazon, Hulu o Netflix.")

    filtro = df[(df.release_year == year) & (df.platform == platform)]

    if filtro.empty:
        return {"plataforma": platform, "anio": year, "actor": None, "apariciones": None}

    cast = filtro.assign(actor=df.cast.str.split(',')).explode('actor')
    actor_counts = cast['actor'].value_counts()

    if not actor_counts.empty:
        max_actor = actor_counts.index[0]
        max_count = int(actor_counts.iloc[0])

        actor_repetido = {'actor': max_actor, 'count': max_count}

        return {"plataforma": platform, "anio": year, "actor": actor_repetido['actor'], "apariciones": actor_repetido['count']}
    else:
        return {"plataforma": platform, "anio": year, "actor": None, "apariciones": None}
    
#Quinta consigna:La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año.
# La función debe llamarse prod_per_county(tipo,pais,anio) deberia devolver el tipo de contenido 
# (pelicula,serie,documental) por pais y año en un diccionario con las variables 
# llamadas 'pais' (nombre del pais), 'anio' (año), 'pelicula' (tipo de contenido).

@app.get('/prod_per_county/{tipo}/{pais}/{anio}')
def prod_per_county(tipo: str, pais: str, anio: int):

    # Lectura de la base de datos:
    df = pd.read_csv('Df_completo.csv')

    # Comprueba si los valores de entrada son válidos y existen en DataFrame
    assert tipo.lower()  in df['type'].unique(), f"Invalid type of content: {tipo}"
    assert pais.lower()  in df['country'].unique(), f"Invalidntr couy: {pais}"
    assert anio in df['release_year'].unique(), f"Invalid year: {anio}"
       
    # Filtra los datos por el tipo de contenido solicitado, año y país
    filter_5 = df.loc[(df['type'] == tipo.lower() ) & 
                            (df['country'] == pais.lower() ) & 
                            (df['release_year'] == anio)]       
        
    # Comprueba si los datos filtrados están vacíos. Si no, devuelve la información deseada.
    if filter_5.empty:
        return {"pais": pais, "anio": anio, "peliculas": None}
    else:
        return {"pais": pais, "anio": anio, "peliculas": filter_5.shape[0]}

#Sexta consigna: La cantidad total de contenidos/productos 
# (todo lo disponible en streaming, series, documentales, peliculas, etc) 
# según el rating de audiencia dado (para que publico fue clasificada la pelicula).
#  La función debe llamarse get_contents(rating) y debe devolver el numero total de
#  contenido con ese rating de audiencias.

     
@app.get('/get_contents/{rating}')
def get_contents(rating: str):
    
    # Lectura de la base de datos:
    df = pd.read_csv('Df_completo.csv') 
    
    # Checks if the input value is valid and exists in DataFrame
    assert rating.lower() in df['rating'].unique(), f"Invalid rating: {rating}"
    
    # Filters the data for the requested audience
    filter_6 = df.loc[df['rating'] == rating.lower()]       
        
    # Checks if filtered data is empty. If not, it returns the desired information.
    if filter_6.empty:
        return {"error": "No result was found with the specified criteria."}
    else:
        return {'rating': rating, 'contenido': filter_6.shape[0]}
    

    #Septima consigna: modelo de recomendacion 
    # Éste consiste en recomendar películas a los usuarios basándose en películas similares, 
    # por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, 
    # se ordenarán según el score y devolverá una lista de Python con 5 valores,
    # cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. 
    # Debe ser deployado como una función adicional de la API anterior y debe llamarse get_recommendation(titulo: str).


@app.get('/get_recommendation/{title}')
def get_recommendation(title: str):

        # Lectura de la base de datos:

    df2 = pd.read_csv('reduced_similarity_matrix.csv') 
    df3 = pd.read_csv("user_item.csv")

    array = df2.to_numpy()

    try:
        #Ubicamos el indice del titulo pasado como parametro en la columna 'title' del dts user_item
        indice = np.where(df3['title'] == title)[0][0]
        #Encontramos los indices de las puntuaciones y caracteristicas similares del titulo 
        puntuaciones_similitud = array[indice,:]
        #Ordenamos los indices de menor a mayor
        puntuacion_ordenada = np.argsort(puntuaciones_similitud)[::-1]
        #seleccionamos solo 5 
        top_indices = puntuacion_ordenada[:5]
        #retornamos los 5 items con sus titulos como una lista
        return df3.loc[top_indices, 'title'].tolist()
        #Si el titulo dado no se encuentra damos un aviso
    except IndexError:
        print(f"El título '{title}' no se encuentra en la base de datos. Intente con otro título.")

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)