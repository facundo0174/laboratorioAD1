#**Laboratorio 1 de Analisis de Datos**#

##**Adquisicion de datos sobre distintos formatos de archivos**##

Las pruebas de codigo se realizaron mediante el uso de **MySQL Workbench 8.0 CE** y **XAMPP Control Panel** para el deploit local
**Algunas concideraciones**
- las apis suelen tener distintos formatos anidados, por lo que se implemento funciones de inspeccion para determinar bajo cuales campos se aplanara en el dataset, determinado  
por el archivo Dataset_api.py
- actualmente no se eliminan los campos nulos, solo avisa que se han encontrado a la hora de ejecutar la carga, aunque el inspector tambien da un resumen completo de estas situaciones
- existen algunos errores persistentes con archivos csv complejos que poseen varios tipos de codificaciones en un solo archivo, actualmente le es posible determinar el tipo de codificacion  
parcial leyendo 50kBytes primarios para no relentizar el proceso, asi como el tipo de elemento separador, ya que este puede variar
- la carga en la base de datos no especifica tipos de datos en las columnas, realiza una carga parcial o plana del dataframe hecho por pandas
- los archivos de pruebas fueron sacados de **[https://apis.datos.gob.ar/]**
- el valor del **.env** utilizado en **/data** durante sus pruebas es el siguiente:
  - DB_NAME=laboratorioad1
  - DB_USER=root
  - DB_PASSWORD=
  - DB_HOST=localhost
  - DB_PORT=3306 

