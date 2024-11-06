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


"""