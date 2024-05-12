# Control 

Para el control del robot simulado se utilizara ros2_control,el cuál es un framework para el control (en tiempo real) de robots utilizando (ROS 2). Sus paquetes son una reescritura de los paquetes ros_control utilizados en ROS (Robot Operating System). El objetivo de ros2_control es simplificar la integración de nuevo hardware y superar algunos inconvenientes.

## ros2_control

En esta sección se presenta cómo funciona ros2_control y cómo se utilizará en la simulación. 

### Controller Manager
Como principal componente se encuentra Controller Manager. El cuál encontrará todos los bits de código para nuestros drivers de hardware y controladores y los vinculará. Es una biblioteca que se carga en tiempo de ejecución y tiene un conjunto de funciones que se vincularán al sistema.

<p style="text-align:center;"><img src="./documentation_data/images/controller_manager.png" alt="" height="150" width="250"></p>

Hardware diferente se debe controlar diferente. Cualquiera que sea el aspecto del hardware, para usar ros2_control con él, necesitamos algo llamado hardware interface  (a veces llamado hardware component). Este es un fragmento de código que se comunica con el hardware y lo expone de la forma estándar ros2_control. 

<p style="text-align:center;"><img src="./documentation_data/images/hardware_interface.png" alt="" height="150" width="250"></p>

*Hardware interface* actúa como una abstracción, de modo que, como usuarios, todo lo que necesitamos entender es la forma en que representa nuestro hardware, que es a través de interfaces de comando e interfaces de estado. Las interfaces de comando son cosas que podemos controlar y las interfaces de estado son cosas que solo podemos monitorear.

El trabajo del *controller manager* es tomar los controladores que se le solicita cargar y relacionarlos con las interfaces de comando y estado correctas que el administrador de recursos está exponiendo. Para configurar los controladores, escribimos un archivo YAML con los diversos parámetros que necesitamos y lo pasamos al controller manager. 

El proyecto en el que estamos trabajando es un robot de accionamiento diferencial (differential drive), por lo que, naturalmente, usaremos diff_drive_controller. 

<p style="text-align:center;"><img src="./documentation_data/images/diff_drive.png" alt="" height="150" width="250"></p>


La tracción diferencial (differential drive) es un sistema de tracción de dos ruedas con actuadores independientes para cada rueda. El nombre se refiere al hecho de que el vector de movimiento del robot es la suma de los movimientos independientes de las ruedas. Las ruedas motrices generalmente se colocan a cada lado del robot. 

#### Ejecución de controller manager

Para ejecutar el controller manager se utilizará `ros2_control_node` provided by the `controller_manager` package. Al cual se le debe proporcionar los detalles de las interfaces de hardware (generalmente a través de URDF) y los controladores (generalmente a través de parámetros YAML).
