## Api para el manejo de todas las asentaderas en el territorio mexicano 


Si tienes un proyecto hecho con django en el cual necesites manejar todas las asentaderas existentes en México
tal vez esta aplicación de pueda ayudar.

La api maneja los puntos citados a continuación.

* Listado de todos los estados del territorio méxicano
* Busqueda de todos los municipios pertenecientes a un estado 
* Busqueda de todas las asentaderas existentes en un municipio
* Busqueda por codigo postal 

Para utilizar solo debes copiar la app que se encuentra en mexico_bd y agregarla en tu proyecto,
no olvides agregarla en *INSTALLED_APPS*, la api esta libre para cualquier usuario anonimo pero solo para obtener información,
solo los admnistradores del sistema *staf* pueden hacer modificaciones. 

```
INSTALLED_APPS = [
	...
    'rest_framework',
    *'app.mexico_bd',*
]

```

El paquete utils se utiliza para un permiso especifico, en el se especifica que los usuarios anonimos solo pueden consultar los datos y que 
los que son staf pueden hacer modificaciones. 



Se agrega la base de datos para que la puedan importar a su proyecto. La información se obtuvo el 10/01/2017 de las fuentes oficiales.
