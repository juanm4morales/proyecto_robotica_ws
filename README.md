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

Launch simulación de robot con gazebo
```    
ros2 launch boxbots launch_sim launch.py
```

Launch teleoperation keyboard
```    
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```    

Launch teleoperation joystick 
``` 
ros2 run teleop_twist_joy teleop_node
```