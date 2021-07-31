# EXAMEN-1B-ADD

# Jorge Alba


# Ejercicio 1
Se debe importar las herramientas necesarias y posteriormente se colocan las credenciales de Twitter, dentro de la funcion se obtienen los datos provenientes de Twitter y se los procede a guradar. Posteriormente se hace la conexion con couchdb y colocando las credenciales y los nombres de la BD que sera creada. Por ultimo se envian las locaciones y se guardaran en la base de datos llamada ciudades.

![image](https://user-images.githubusercontent.com/66254573/127722836-fbdc2501-2765-460a-a183-2011c98d6601.png)

# Ejercicio 2
Se debe importar las herramientas necesarias y posteriormente se colocan las credenciales de Twitter, dentro de la funcion se obtienen los datos provenientes de Twitter y se los procede a guradar. Posteriormente se hace la conexion con couchdb y colocando las credenciales y los nombres de la BD que sera creada. Por ultimo se envia los datos que genere Twitter por medio del track Juegos Olimpicos y se guardaran en la base de datos llamada ciudades2.

![image](https://user-images.githubusercontent.com/66254573/127722865-c07c9012-11b5-446a-9339-6e0cf2584966.png)

# Ejercicio 3
Se empieza realizando la conexion con mongodb por medio de pymongo, se muestra el mensaje de si se realizo correctamente la conexion o no. Se importan las herramientas necesarias y se generan las funciones que permitiran limpiar las etiquetas. Usamos el request para obtener los datos html y posteriormente se los limpia con un for el cual guardara los datos limpiados en Titles, una vez realizado esto se lo guarada como json y se lo manda a la BD y coleccion previamente creadas. 

![image](https://user-images.githubusercontent.com/66254573/127722972-c4e85602-db41-4eea-a99c-bf88927270df.png)

# Ejercicio 4
Se realzia la importacion de las herramientas necesarias y se realiza la conexion con mongodb en donde previamente se debem crear tanto la BD como coleccion. Posteriormente se genera el codigo para que se vaya producien un documento el cual ira iterando entre los datos de Facebook y los ira guardando y ambien mostrará si se guardo o no con exito.

![image](https://user-images.githubusercontent.com/66254573/127725263-eb787702-5c1b-462f-ad07-5c45c9e1fd4e.png)


# Ejercicio 5
Se comienza exportando las herramientas necesarias, se realiza la conexion con sqlite por medio del nombre de la base de datos previamente creada. Se realzia la lectura de los arhivos para comprobar que se esten leyendo correctamente y posterior a ello se guardan en la BD creada denominada BD1.

![image](https://user-images.githubusercontent.com/66254573/127724457-a00e06fe-a5cf-4af6-98ad-270d7373efb1.png)

# Ejercicio 6
El proceso se lo realiza por medio de la exportacion de sqlite en archivos json. Posteriormente se importa los json generados por sqlite en mongo y los json se pueden obserbar ahora en mongodb.

![image](https://user-images.githubusercontent.com/66254573/127724692-29426270-97c9-4bb3-956d-d48d6bd4fbdd.png)


# Ejercicio 7 
Para realizar el traspaso de datos de couchdb a mongodb se debe importar las herramientas necesarias, posteriormente se realiza la conexion con couch debe por medio de la url con las correspondientes credenciales. Se continua con la conexion a mongodb. En ambos casos es necesario manejar la presentacion en apnatlla si la conexion se realizo o se tuvo algun problema. El traspaso de datos se lo realiza con una funcion for que iterara en la BD original e ira guradando los datos en relacion al id en mongodb en el caso de que ya exista ese id se mostrata un mensaje de que ya existe ese id de lo contrario con la funcion insert ira insertando en mongodb. 

![image](https://user-images.githubusercontent.com/66254573/127723785-c988d8e5-3466-491e-b298-ea015563fa86.png)

# Ejercicio 8
El proceso es realizar las importaciones correspondientes, posteriormente se realiza las conexiones tanto en mongodb como en mongodb atlas. Sin embargo mi cluster se encontraba pausado y no pude realizar la coexion por a misma razon no pude continuar con los siguientes ejercicios.

![image](https://user-images.githubusercontent.com/66254573/127725235-1a03dc31-470d-44bd-89e2-bfa69779ac1b.png)

