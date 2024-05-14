## NAVIGATION
Utilizamos navigation para definir la ruta que deben seguir los robots dentro del mapa.

### DEPENDENCIAS
Package: twist-mux

```bash
sudo apt install ros-humble-twist-mux
```

### SCRIPT AUTOMATIZADO 
Para saltearse los pasos a seguir, podemos ejecutar el script start_navigation.sh de la siguiente manera

```bash
./start_navigation.sh
```

### PASO A PASO
Para realizar el paso a paso debemos ejecutar el comando que permite la detección del joystick aún cuando se ha definido la ruta:
```bash
ros2 run twist_mux twist_mux --ros-args --params-file boxbots/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped

!!!! NO SÉ SI FUNCIONA ASÍ, HAY QUE PROBARLO CON EL JOYSTICK
```

Luego, podemos ejecutar el navigation launch con el siguiente comando:
```bash
ros2 launch boxbots launch_sim_navigation.launch.py
```

Una vez se abra la simulación de gazebo, podemos abrir rviz para visualizar el resultado, esto se realiza con el comando:
```bash
ros2 run rviz2 rviz2 -d boxbots/config/rviz_slam_with_navigation.rviz 
```

Esta configuración de rviz muestra el mapa resultante de slam + el mapa resultante del navigation.