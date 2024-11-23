# Gymboard - Análisis de Rendimiento y Hábitos de Entrenamiento en Miembros de un Gimnasio

## Objetivo general
El objetivo de este proyecto es analizar los datos de los miembros de un gimnasio para identificar patrones y relaciones entre diferentes variables que afectan el rendimiento y los hábitos de entrenamiento.

## Requisitos del proyecto:

- Python 3.9 ~
- Node 14.0 ~ 

## Configuración del proyecto

Para poder ejecutar el proyecto exitosamente, debemos ubicarnos en el proyecto en una terminal

### Backend

Nos ubicamos a la carpeta backend:

``cd backend``

Seguidamente, debemos crear un entorno virtual, en este caso se muestra como crearlo con virtualenv:

``py -m virtualenv venv``

Una vez creado accedemos al entorno virtual:

#### Linux & Mac
``source venv/bin/activate``

#### Windows
``.\venv\Scripts\activate``

Una vez ahi, instalamos las librerias necesarias:

``pip install -r requirements.txt``

Al instalarlos, podemos ejecutar exitosamente el servidor:

``uvicorn main:app --reload``

### Frontend

Nos ubicamos a la carpeta frontend:

``cd frontend``

Seguidamente, instalamos las librerias necesarias:

``npm install``

Al instalar las librerias, tenemos que crear un archivo `.env` con el mismo contenido del archivo `.env.example`, cambiando el valor de la variable **VITE_API_URL** con la direccion del backend.

Una vez instaladas las librerias y creado el archivo de variables de entorno virtual, podemos ejecutar el frontend:

``npm run dev``

Con esto podemos ver el dashboard de manera local