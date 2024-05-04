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


En la raíz del proyecto:

```   
colcon build --symlink-install
```    

Configuración del entorno para el shell actual.

```    
source install/setup.bash
```

 