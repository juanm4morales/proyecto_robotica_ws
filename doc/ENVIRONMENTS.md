# Implementacion de los entornos
    La herramienta utilizada para la construccion de los entornos fue el editor de modelos de gazbo.
    El proceso de construccion constó del uso de geometrias basicas propias del editor de gazebo, tanto para los obstaculos como para los objetos 
inamovibles. En el caso de los objetos obstaculo, gazebo provee la posibilidad para configurar la masa e inercia de los mismos, los cuales tuvieron que ser reescalados para que los robots interactuen correctamente con los mismos. Por otro lado, los objetos que detallan los limites de los entornos, como son los muross, tienen aplicada la configuracion de "kinematic" con el fin de evitar que estos objetos interactuen con el motor de fisicas y actuen como objetos estaticos y delimitantes.

# Formato SDF
    El formato que se utiliza para trabajar entornos y modelos 3d en gazebo es el estipulado en el formato .sdf, el cual es un estandar 
construido por encima de XML mediante el uso de etiquetas predefinidas para describir no solo la forma de la malla del modelo, sino todas las caracteristicas dirigidas al motor de fisicas de Gazebo. Algunas de estas etiquetas son:

## \<geometry\>: 
Define el inicio de una figura geometrica

## \<mesh\>: 
Define el modelo 3d utilizado mediante una uri apuntando a un archivo de la computadora o a un recurso alocado en internet

## \<friction\>,\<contact\>,\<collision\>: 
Definen variables de como debe afectar el motor de fisicas 

# Descripcion de entornos
    Habiendo explicado los cimientos, el proyecto cuenta con 2 entornos utilizables: Race.xml (/src/boxbots/worlds/Race_World) y Arena.xml (/src/
boxbots/worlds/Arena_World) los cuales estan compuestos por objetos moviles e inmoviles, en el caso de Race.xml, define un pequeño camino de obstaculos con muros paralelos y modelos abiertos provistos por gazebos. El otro entorno, denominado Arena.xml es un pequeño "ring" con juegos para multiples robots, nuevamente compuesto de muros, rampas y modelos abiertos de Gazebo.
