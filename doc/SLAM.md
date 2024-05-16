## SLAM (Simultaneous Localization and Mapping)
Utilizamos SLAM (Simultaneous Localization and Mapping) para mapear el entorno y localizar el robot en tiempo real. Para ello, utilizamos el paquete slam_toolbox de ROS2.

Para instalar el paquete slam_toolbox, se debe ejecutar el siguiente comando en la terminal:

```bash
sudo apt install ros-humble-slam-toolbox
```

Para correr el nodo slam_toolbox, se debe ejecutar el siguiente comando en la terminal:

```bash
ros2 launch slam_toolbox online_sync_launch.py slam_params_file:=./src/boxbots/config/mapper_params_online_sync.yaml use_sim_time:=true
```

- Aqui hay dos partes importantes a tener en cuenta:
  - Si queremos mappear el entorno en tiempo real, debemos modificar en el archivo mapper_params_online_sync.yaml el valor de mode en los ROS params de la siguiente manera:
      ```yaml
      mode: "mapping"
      ```
    y comentar el map_file_name y map_start_at_dock
  - Luego si queremos utilizar ese mapa debemos cambiar la linea por
      ```yaml
      mode: "localization"
      ```
    y descomentar el map_file_name y map_start_at_dock

Para visualizar el mapa generado por el nodo slam_toolbox, se debe ejecutar el siguiente comando en la terminal:

```bash
ros2 run nav2_map_server map_saver_cli -f map
```
## AMCL (Adaptive Monte Carlo Localization)
En caso de que no este instalado, para utilizar el paquete amcl de ROS2, se debe ejecutar el siguiente comando en la terminal:

```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
```

Para utilizar el metodo de montecarlo para la localizacion del robot, se debe ejecutar el siguiente comando en la terminal:

```bash
ros2 run nav2_map_server map_server --ros-args -p yaml_file_name:=./my_map_save.yaml -p use_sim_time:=true
```
Luego en otra terminal

```bash
ros2 run nav2_util lifecycle_bringup map_server
```
Esto activa el nodo map_server que se encarga de publicar el mapa en el topico /map y de suscribirse a los comandos de localizacion del robot.

Para correr el nodo amcl, se debe ejecutar el siguiente comando en la terminal:

```bash
ros2 run nav2_amcl amcl --ros-args -p use_sim_time:=true
```
Esto activa el nodo amcl que se encarga de localizar el robot en el mapa.

Y en otra terminal

```bash
ros2 run nav2_util lifecycle_bringup amcl
```
Luego se debe señalar el punto de inicio del robot en el mapa en Rviz, para ello se debe hacer click en el boton 2D Pose Estimate y seleccionar el punto de inicio del robot en el mapa.

