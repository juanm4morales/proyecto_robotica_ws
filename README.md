# Proyecto Robótica Móvil - 2024

## Prerequisitos
- Ubuntu 22.04
- [ROS2 (Humble distro)](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
- [Colcon](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)

    ```
    sudo apt install python3-colcon-common-extensions
    ```
- Xacro Package

    ```
    sudo apt install ros-humble-xacro
    ```
- Packages for interfacing with Gazebo
    ```
    sudo apt install ros-humble-gazebo-ros-pkgs
    ```
- Control packages
    ```
    sudo apt-get install ros-humble-twist-mux ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gazebo-ros2-control  
    ```

## Estructura de paquetes

- Carpeta *description*
Archivos relacionados con la descripción del robot (modelos, materiales, texturas, etc.)


- Carpeta *launch*
Archivos de lanzamiento


## Instrucciones para construir paquetes del proyecto
Cada vez que se agregue un archivo nuevo es necesario.

```   
colcon build --symlink-install
```    

## Variables de entorno
Configuración del entorno para el shell actual.

```    
source install/setup.bash
```

## Instrucciones de lanzamiento

Launch simulación de robot con gazebo (mundo vacio)
```    
ros2 launch boxbots launch_sim.launch.py
```

Launch simulación de robot con gazebo y mundo personalizado

Race World:
```
ros2 launch boxbots launch_sim_race.launch.py 
```
Arena World:
```
ros2 launch boxbots launch_sim_arena.launch.py 
```

Launch teleoperation keyboard con namespace (cambiar namespaceBot por el namespace que se quiere controlar):
```    
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r __ns:=/namespaceBot
```    

Launch de control con joystick (joystick0.launch.py controla el robot donBarredora con el dispositivo que el sistema le asigno el id 0):
```  
ros2 launch boxbots joystick0.launch.py
```

Launch de control con joystick (joystick1.launch.py controla el robot axeBot con el dispositivo que el sistema le asigno el id 1):
```  
ros2 launch boxbots joystick1.launch.py
```  
