# Django REST Framework API

Este proyecto es un ejemplo de cómo usar APIView y ViewSet en Django REST Framework para proporcionar acceso y autenticación a los usuarios.

## Estructura del Proyecto
## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd tu_repositorio
    ```
3. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```
4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```
5. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```
6. Crea un superusuario para acceder al panel de administración:
    ```sh
    python manage.py createsuperuser
    ```
7. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Endpoints

### HelloWorldAPIView

- **GET** `/api/hello-view/`: Retorna un mensaje de saludo.
- **POST** `/api/hello-view/`: Crea un mensaje con el nombre proporcionado.

### HelloWorldViewSet

- **GET** `/api/hello-viewset/`: Lista los mensajes de saludo.
- **POST** `/api/hello-viewset/`: Crea un nuevo mensaje de saludo.
- **GET** `/api/hello-viewset/{id}/`: Obtiene un mensaje por su ID.
- **PUT** `/api/hello-viewset/{id}/`: Actualiza un mensaje por su ID.
- **PATCH** `/api/hello-viewset/{id}/`: Actualiza parcialmente un mensaje por su ID.
- **DELETE** `/api/hello-viewset/{id}/`: Elimina un mensaje por su ID.

### UserProfileViewSet

- **GET** `/api/profile/`: Lista todos los perfiles de usuario.
- **POST** `/api/profile/`: Crea un nuevo perfil de usuario.
- **GET** `/api/profile/{id}/`: Obtiene un perfil de usuario por su ID.
- **PUT** `/api/profile/{id}/`: Actualiza un perfil de usuario por su ID.
- **PATCH** `/api/profile/{id}/`: Actualiza parcialmente un perfil de usuario por su ID.
- **DELETE** `/api/profile/{id}/`: Elimina un perfil de usuario por su ID.

### UserLoginApiView

- **POST** `/api/login/`: Autentica un usuario y retorna un token de autenticación.

### UserProfileFeedViewSet

- **GET** `/api/feed/`: Lista todos los elementos del feed de usuario.
- **POST** `/api/feed/`: Crea un nuevo elemento en el feed de usuario.
- **GET** `/api/feed/{id}/`: Obtiene un elemento del feed de usuario por su ID.
- **PUT** `/api/feed/{id}/`: Actualiza un elemento del feed de usuario por su ID.
- **PATCH** `/api/feed/{id}/`: Actualiza parcialmente un elemento del feed de usuario por su ID.
- **DELETE** `/api/feed/{id}/`: Elimina un elemento del feed de usuario por su ID.

## Autenticación

Este proyecto utiliza autenticación basada en tokens. Para obtener un token, envía una solicitud POST a `/api/login/` con las credenciales del usuario. Incluye el token en el encabezado de autorización para acceder a los endpoints protegidos.

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:
```sh
python manage.py test

# Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.
