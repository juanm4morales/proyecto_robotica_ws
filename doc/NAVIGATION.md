# NAVIGATION
Para la navegación autónoma de los robots, utilizamos el paquete `nav2_bringup`. Este paquete proporciona las funcionalidades básicas para definir las rutas por las cuales los robots se desplazarán durante la prueba.

## CÓMO FUNCIONA
Al analizar el código fuente, observamos que se generan diversos nodos que nos ayudarán a configurar un grupo de nodos para la navegación de los robots los cuales se detallan a continuación.


- `nav2_controller`: Ejecuta el servidor del controlador de navegación. Es responsable de generar comandos de velocidad para que el robot siga una trayectoria específica. Utiliza los parámetros configurados y remapea las conexiones de los tópicos, como el tópico de velocidad de comandos (cmd_vel).

- `nav2_smoother`: Suaviza la trayectoria generada por el planificador de navegación. Ayuda a evitar movimientos bruscos y mejora la estabilidad del robot.

- `nav2_planner`: Es responsable de generar una trayectoria global para el robot. Utiliza información del mapa y otros datos para planificar la ruta.

- `nav2_behaviors`: Maneja los comportamientos de alto nivel del robot, como detenerse, evitar obstáculos o seguir una referencia de posición.

- `nav2_bt_navigator`: Implementa un árbol de comportamiento (Behavior Tree) para coordinar las acciones de navegación del robot.

- `nav2_waypoint_follower`: Sigue una serie de puntos de referencia (waypoints) en la trayectoria global. Es útil para seguir rutas predefinidas.

- `nav2_velocity_smoother`: Suaviza aún más las velocidades de comandos antes de enviarlas al controlador. Esto ayuda a evitar cambios bruscos en la aceleración.

- `nav2_lifecycle_manager`: Gestiona el ciclo de vida de los nodos de navegación. Puede iniciar, detener o reiniciar los nodos según sea necesario.


## EJECUCIÓN

Para poder ejecutar el script correspondiente a la navegación de nodos, primero debemos asegurarnos de instalar las dependencias correspondientes. Si se ha ejecutado el comando [dependencies.sh](./../scripts/dependencies.sh) no hay de que preocuparse, caso contrario se debe hacer o instalar el paquete `twist-mux` con el siguiente comando:

```bash
sudo apt install ros-humble-twist-mux
```
### EJECUCIÓN AUTOMÁTICA
Una vez tengamos las dependencias instaladas podemos ejecutar el siguiente [script](./../scripts/start_navigation.sh) el cual abrirá una ventana con la simulación en gazebo y otra en rviz en el mapa que se haya definido dentro del archivo de lanzamiento `launch_sim_slam`. Esto se puede realizar con el siguiente comando:
```bash
./start_navigation.sh
```
><small>*Cabe destacar que debemos estar posicionados en la carpeta `scripts` del proyecto dentro de la terminal.*</small>

### EJECUCIÓN MANUAL
Si no queremos que se ejecute lo antes mencionado, podemos seguir los siguientes pasos para realizarlo manualmente o solo por partes.

1) Ejecución de simulación en Gazebo.

    ```bash
    ros2 launch boxbots navigation_launch.launch.py
    ```
2) Ejecución de simulación en RVIZ. *(Verifique el path hacia la configuración)*
    ```bash
    ros2 run rviz2 rviz2 -d boxbots/config/rviz_slam_with_navigation.rviz 
    ```

    >*Esta configuración muestra el mapa resultante de slam + el mapa resultante del navigation.*

## Joystick

```bash
ros2 run twist_mux twist_mux --ros-args --params-file boxbots/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped
```
!!!! NO SÉ SI FUNCIONA ASÍ, HAY QUE PROBARLO CON EL JOYSTICK