Para correr el entorno dockerizado se puede utilizar el archivo run_docker_gpu.bash. Para correr el entorno dockerizado se debe ejecutar el siguiente comando en la terminal:

```bash
./run_docker_gpu.bash
```
Es necesario tener instalado Docker y xhost para poder correr la visualización de Gazebo. 

Una vezz ejecutado el comando anterior, para entrar en el container creado se debe ejecutar el siguiente comando en la terminal:

```bash
docker exec -it r2_container bash
```

Entendiendo la logica del primer comando vemos:

```bash
docker run -it \ # Ejecuta el contenedor en modo interactivo
  --name=r2_test_container \ # nombre del contenedor
  --env="DISPLAY=$DISPLAY" \ # le indica que el display de salida es el display de la maquina host
  --env="QT_X11_NO_MITSHM=1" \ # le indica que no se use el MIT-SHM extension
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \ # monta el directorio de salida de la maquina host en el contenedor (para grafica)
  --volume="${PWD}:/root/project" \ # monta el directorio actual en el contenedor
  --env="XAUTHORITY=$XAUTH" \ # le indica que el archivo de autorización es el de la maquina host
  --volume="$XAUTH:$XAUTH" \ # monta el archivo de autorización en el contenedor
  --net=host \ # le indica que use la red de la maquina host
  --privileged \ # le da privilegios al contenedor
  project_test \ # nombre de la imagen
  bash # comando a ejecutar
```

