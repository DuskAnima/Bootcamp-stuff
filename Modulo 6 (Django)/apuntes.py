"""
Django trabaja con una arquitectura de 3 capas: MODELO - VISTA - TEMPLATE

Capa = grupo de funcionalidades.

MODELO:

* Es un conjunto de funcionalidades que van a permitir que Python se conecte con la base de datos.
* Es en esta capa en la que se aplica la programación orientada a objetos conectada a la base de datos.
    * Porque cada registro de la base de datos es un objeto. 
        * Estos poseerán la capacidad de Crearse, Editarse, Elminarse y Listarse.


        
VISTA:

* Es la capa intermedia entre lo que ve el usuario y lo que el usuario guarda u obtiene como información.
    * Permite la interación entre la PLANTILLA y el MODELO.
* También considerada controlador. 
    * Puede Filtrar, Validar Operaciones, Cálculos, etc.

TEMPLATE:

* Es lo que el usuario visualiza.
    * En esta capa se establece el Front-End

    
Comandos para trabajar con django:
    
django-admin startproject (nombre de projecto)
manage.py startapp (nombre de la app) 
python manage.py runserver <- ejecuta servidor de desarrollo
pip freeze > requirements.txt <- Archivo de texto para crear requerimientos establecidos en un venv
pip install -r requirements.txt <- invoca el archivo requirements para que instale las dependencias




makemigrations: Crea archivos de migración para los cambios en los modelos.
migrate: Aplica las migraciones a la base de datos.
shell: Abre una consola interactiva de Python en el entorno Django.
dbshell: Abre la consola de la base de datos para interactuar directamente con la base de datos.
showmigrations: Muestra el estado de las migraciones.
dumpdata: Exporta los datos de la base de datos a un archivo.
test: Ejecuta las pruebas automatizadas del proyecto.
testserver: Ejecuta el servidor con la base de datos de pruebas.
diffsettings: Muestra las diferencias entre la configuración actual y la predeterminada.


"""