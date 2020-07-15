# Angulo Sales 
Proyecto para estudiar django, inventario, ventas y tiempos de mtto y entrega

# DevRecs
Para poder desarrollar sobre este proyecto se requiere

* Python 3.8 
  * Django
* Node  
  * Gentelella
* Docker

# DevIns
> Para generar el ambiente utilizo docker ya que es mas facil jalar dependicias sin "instalar" mas nada sin mas empesamos

Para generar el proyecto es requerido descargar [Gentelella](https://github.com/ColorlibHQ/gentelella) por lo cual es requerido generar un contenedor con node para descargar el proyecto,
abrimos una terminal y nos pocicionamos en el proyecto y despues generamos un contenedor con un blind mount a el codigo
```
cd <ruta_a_el_protecto>
docker run -itd --rm --mount type=bind,source="$(pwd)",target=/home node
docker exec -it <hash_de_contenedor>  /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"
cd /home
npm update
exit
docker stop <hash_de_contenedor>
```
cerramos conexion con el contenedor y detenemos contenedor para que se elimine 
una ves descargado gentelella se requiere generar una imagen con el proyecto
```
docker build . -t angulo
```
a continuacion generamos el contenedor 
```
docker run -itd -p 8000:8000  --name angulo --mount type=bind,source="$(pwd)",target=/src angulo
```
para iniciar django entramos en el contenedor y ejecutamos el servidor dev
```
docker exec -it angulo  /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"
pipenv run python manage.py runserver 0.0.0.0:8000
```