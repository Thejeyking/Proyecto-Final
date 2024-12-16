Bienvenido a mi aplicación de Python

INSTALACION:

				LIBRERIAS

El código requiere de una sola librería externa llamada "colorama"

Instalación de Colorama:
La forma más sencilla de instalar Colorama es utilizando el gestor de paquetes pip. Abre tu terminal o línea de comandos y ejecuta el siguiente comando:


		pip install colorama


la versión actual y utilizada es "colorama 0.4.6"


				BASE DE DATOS

El programa genera automáticamente 3 bases de datos para su funcionamiento los cuales son:

-Producto: almacena la información de los productos y el inventario

-usuario: almacena la información de los usuarios registrados y sus contraseñas

-información: almacena la información del negocio/comercio/empresa



INFORMACION:

				
				INFORMACION DEL PROGRAMA
Contiene un menú sencillo dinámico que dependiendo el stock del negocio puede ser de dos maneras:

- Mayor a 10 unidades en los productos:
	El menú contiene un marco verde
- Menor a 10 unidades en los productos:
	El menú contiene un marco Rojo con una notificación avisado el bajo stock del producto


El programa tiene un CRUD sencillo y además tiene opciones como:

- Info Empresa: muestra la información de la empresa

- Bajo Stock: Muestra una tabla con los productos que contenga menos de 20 unidades en el inventario

- Editar Datos: Se puede modificar datos como información del negocio o usuarios y contraseñas

- REINICIAR APP: Esta opción es para borrar las bases de datos y volver a empezar de 0

- Salir: Opción que finaliza el bucle y finaliza el programa con un mensaje de saludo