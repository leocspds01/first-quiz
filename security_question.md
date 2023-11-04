## Sistema de seguridad

En esta sección, queremos que demuestre su conocimiento de las mejores prácticas de seguridad. Escribe tu respuesta a esto.
pregunta en `security_question.md` ya sea en inglés o español.

Suponga que es el jefe de ingeniería de una nueva y emocionante startup tecnológica que instala paneles solares a través de una aplicación.
¡Es Uber para paneles solares! Estás realizando una auditoría de seguridad de la infraestructura de tu aplicación. Estás utilizando el Top 10 de OWASP
para 2021 como guía sobre qué problemas de seguridad podrían ser un problema para usted.

Su infraestructura se implementa en contenedores de Kubernetes en Amazon Web Services. Tiene estos componentes:
- Una aplicación móvil para Android e iOS.
- Una interfaz web que el cliente puede utilizar en lugar de la aplicación móvil. Esto está escrito en Javascript con Next.js.
- Una base de datos MySQL que almacena información del cliente, incluidas contraseñas, direcciones particulares, números de teléfono, etc.
   También contiene información del pedido del cliente.
- Un backend de Python implementado en FastAPI. Esto se comunica con la base de datos y proporciona datos tanto a la interfaz web como al \
   aplicaciones móviles.

Tiene 12 empleados de ingeniería de software que tienen acceso completo al sistema, 3 empleados de atención al cliente que pueden ver
información del cliente y realizar cambios en pedidos y cuentas, y un empleado de ventas.

Utilizando OWASP Top 10, ¿qué buscaría para que su sistema sea seguro?

Respuesta:

Yo buscaria que no haya posibilidades de que ingresaran codigo malisioso en mi sistema, como SQL, NoSQL y OS. Les recordaria la importancia de tener buenas practicas de autenticacion como lo son las contraseñas robustas, los multi factores de autenticacion para evitar el robo de identidad. Me aseguraria de que los usuarios solo puedan acceder a los recuersos y funciones para los cuales estan autorizados, implementaria una estrategia de registro y monitoreo solida para detectar y responder rapidamente a posibles ataques.   
