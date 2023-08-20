# Tecnomania🛒

## Tabla de contenido

1. Introducción
2. Preview
3. Instalacion
4. Author

### **1. Introducción**

Tienda en línea utilizando Django de Python y PostgreSQL para la asignatura de "Desarrollo Sistemas de Información" en la Universidad Técnica de Manabí

### **2. Preview**

<img src="https://i.postimg.cc/65jqSyjH/Captura-de-pantalla-2023-08-19-234941.jpg" width="550" height="258"/>

### **3. Instalación**

1. Primero, necesitas instalar python 3.10 o superior desde el [repositorio oficial](https://www.python.org/downloads/)
2. Instalar las dependencias en la terminal de tu preferencia:

   `pip install Pillow==10.0.0`

   `pip install Django==4.2.4`

   `pip install psycopg2-binary==2.9.7`

3. Configurar la base de datos en "tecnomania/settings.py", databases
4. Crea la base de datos en tu gestor de base de datos de preferencia (PG Admin y otros) con el nombre "django"
5. Selecciona zona horaria de PostgreSQL, ingresa ala ruta:

   > C:\Program Files\PostgreSQL\14\data\postgresql.conf

   - Busca "timezone" y reemplázalo con la siguiente línea:

   `timezone = 'UTC'`

   - Realizado los cambios, guárdalo

6. Reinicia el servicio de PostgreSQL.
   - Windows + R
   - Escribe: services.msc
   - Busca el servicio: "postgresql-x64-14". La "x64" y reínicialo
7. Ejecuta los siguiente comandos para realizar la migración respectiva

   `python manage.py makemigrations `
   `python manage.py migrate`

8. Encender el servidor

   `python tecnomania/manage.py runserver`

9. Listo, ahora puedes acceder en http://localhost:8000

### **4. Autor**

- Merly Paola Zambrano Bravo
- Yanelly Doménica Arteaga Arteaga
  [Universidad Técnica de Manabí, Portoviejo](https://utm.edu.ec)
