# Minicore
Arquitectura General:
Tenemos el MiniCore se cuenta con patrón Modelo-Vista-Controlador dentro del cual tengo lo siguiente

Base de Datos (minicore): Contiene dos tablas, una para usuarios y otra para ventas.

app.py: Es la aplicación principal de Flask que actúa como un controlador en el patrón Modelo-Vista-Controlador (MVC). Se encarga de manejar las solicitudes HTTP y las vistas. Ademas se definen las siguientes Tareas para app.py:

- Define rutas y funciones para las vistas.
- Conecta con la base de datos minicore para recuperar datos de ventas y usuarios.
- Renderiza plantillas HTML para la interfaz de usuario.
- Proporciona endpoints para acceder a la funcionalidad.

models.py: Define los modelos de datos en el patrón Modelo-Vista-Controlador (MVC). Utilizando Flask-SQLAlchemy para representar las tablas en la base de datos. Ademas se definen las siguientes Tareas para models.py:

- Define modelos User y Venta para mapear las tablas de usuarios y ventas, respectivamente.
- Configura la conexión a la base de datos (minicore) para SQLAlchemy.
- Carpeta templates: Contiene las vistas HTML que se renderizan en el navegador.


Finalmente tenemos las vistas de este modelo vista controlador
index.html: Página de inicio.
comision.html: Página para mostrar comisiones de ventas.
formulario_busqueda.html: Formulario de búsqueda de comisiones.


Flujo de la Aplicación:

- Un usuario accede a la página de inicio (/) en su navegador.

- Flask maneja la solicitud HTTP y muestra la página de inicio (index.html) al usuario.

- El usuario decide buscar comisiones y hace clic en el enlace o botón correspondiente.

- La solicitud se envía a la ruta /buscar_comisiones.

- Flask renderiza el formulario de búsqueda (formulario_busqueda.html).

- El usuario completa el formulario y lo envía. Los datos ingresados se envían a través del método POST a la ruta /comisiones.

- Flask recopila los datos del formulario, se conecta a la base de datos minicore y ejecuta una consulta SQL para obtener las comisiones.

- Los resultados se devuelven a través de la plantilla comision.html y se muestran al usuario.
