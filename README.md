# CoderPythonProjectFinal
Proyecto Final CoderHouse

# Autor:
Desarrollado 100% por Alejandro Isnardi

# Requerimientos
pip install Pillow

# Proyecto:
Web App estilo blog con Python en DJango.
Front-End basado en Bootstrap, implementa herencia
Contempla DOS CRUDs Usuarios y Paginas.
La Home dede la NavBar tiene los accesos a:
~ Home
~ About
~ Admin (DJango)
~ Publicar (Requiere Autenticación)
~ Login/Logout
~ Registro Usuario
~ Editar Perfil (Requiere Autenticación)
~ Editar imágen Avatar (Requiere Autenticación)

# Video demostración
https://drive.google.com/file/d/1VL9w89hBcE2vjhwPMaI3_AaAet-f-h2Z/view

# Pagina principal
Contiene el NavBar con todos los accesos
Se listan las paginas con el botón "Continuar leyendo"
Link: http://127.0.0.1:8000/blogapp/



Todas las URL que se detallan, están disponibles desde el FRONT-END no es necesario recordarlas

# Pagina Login
Se validan los datos, ante usuario o contraseña incorrecto se muestra en pantalla el error. Caso correcto redirije a index
Link: http://127.0.0.1:8000/blogapp/login/

# Página registro de usuario
Se validan los datos mostrando una alerta ante faltante o datos incorrectos
Link: http://127.0.0.1:8000/blogapp/registrar/

# Pagina para publicar o cambiar AVATAR del usuario
Se puede setear o cambiar la imágen del AVATAR del usuario.
Link: http://127.0.0.1:8000/blogapp/perfil/

# Metodo de cierre de sessión
http://127.0.0.1:8000/blogapp/logout

# Pagina para editar datos de usuario (Requiere Login)
Se pueden cambiar el mail, password, nombre y apellido
Link: http://127.0.0.1:8000/blogapp/perfil/

# Acerca de mí
Se cuenta una breve descripción de blog y de mi.
Link: http://127.0.0.1:8000/blogapp/about/

# Lista de páginas o posts
En el mismo index se listan todos las paginas, igualmente esta imlpementado en pages/
Link: http://127.0.0.1:8000/blogapp/
Link: http://127.0.0.1:8000/blogapp/pages/

# Pagina para publicar páginas o posts
Desde la misma el usuario puede publicar por cada pagina un título, subtítulo, cuerpo y una imagen, automáticamente el usuario se asigna como Autor y la fecha de publicación se registran automáticamente tomando la fecha/hora de publicación.
Link: http://127.0.0.1:8000/blogapp/pages/new/

# Pagina por ID
Permite acceder por ID a cada post ampliar
Link: http://127.0.0.1:8000/blogapp/pages/1/

# Si no existe ninguna página mostrar un "No hay páginas aún". 
Tanto en el Index como en Pages se mostrará la leyenda "No hay páginas publicadas." cuando no exita una publicada.
Link: http://127.0.0.1:8000/blogapp/

# Para crear, editar o borrar las fotos debes estar registrado como Administrador.
Todas las funcionalidades del sitio para editar, borrar o publicar validan que el usuario haya iniciado sesion y además el usuario Owner solo puede borrar o editar una Pages o publigación.

# Formulario para publicar una Nota
http://127.0.0.1:8000/blogapp/pages/new/

# Página para editar una nota
Requiere autenticación!
Solo el usuario Owner podrá editar la Page
http://127.0.0.1:8000/blogapp/pages/1/edit/

# Página para borrar una nota
Requiere autenticación!
Antes de eliminar la Pages pregunta al usuario, solo el usario Owner podrá eliminar la Page
http://127.0.0.1:8000/blogapp/pages/3/delete/

Usuarios prueba:
    palonso | 1234567-


