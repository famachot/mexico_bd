## Api para el manejo de todas las asentaderas en el territorio mexicano 


Si tienes un proyecto hecho con django en el cual necesites manejar todas las asentaderas existentes en México
tal vez esta aplicación de pueda ayudar.

La api maneja los puntos citados a continuación.

* Listado de todos los estados del territorio mexicano
* Búsqueda de todos los municipios pertenecientes a un estado 
* Búsqueda de todas las asentaderas existentes en un municipio
* Búsqueda por código postal 

Para utilizar solo debes copiar la app que se encuentra en mexico_bd y agregarla en tu proyecto,
no olvides agregarla en *INSTALLED_APPS*, la api está libre para cualquier usuario anónimo pero solo para obtener información,
solo los administradores del sistema *staf* pueden hacer modificaciones. 

```
INSTALLED_APPS = [
	...
    'rest_framework',
    'app.mexico_bd',
]

```

El paquete utils se utiliza para un permiso especifico, en él se especifica que los usuarios anónimos solo pueden consultar los datos y que 
los que son staf pueden hacer modificaciones. 



Se agrega la base de datos para que la puedan importar a su proyecto. La información se obtuvo el 10/01/2017 de las fuentes oficiales.

Para instalar solo ejecuta 
pip install -r requeriments.txt

Para probar la api en el servidor proporcionado por django

**localhost:8000/ubicacion/estado/**

Retorna el listado de todos los estados de la república mexicana 


**localhost:8000/ubicacion/estado/21/municipio/tepe/**

Retorna el listado de todos los municipios pertenecientes a un estado, tomando en cuenta que e ultimo segmento de url
*tepe* es un parámetro que se utiliza para realizar la búsqueda del municipio y que solo se regresen los municipios en el que 
su nombre cumpla con ese filtro. 


**localhost:8000/ubicacion/estado/21/municipio/21164/ce/**

Retorna todas las asentaderas (colonias) de un municipio es especifico "21" es la clave del estado y "21164" es la clave del municipio
"ce" de igual forma es un criterio de búsqueda para que solo se retornen las asentaderas (colonias) que cumplan con ese criterio en 
su nombre


**localhost:8000/ubicacion/cp/75200/**

Retorna todas las asentaderas (colonias) que tienen ese código postal *75200*, además de que se retorna a que municipio pertenecen y el estado.
