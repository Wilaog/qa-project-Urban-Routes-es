# Proyecto de Pruebas de Automatización de UrbanRoutes
# Autor: Wilmer Andres Otalvaro Gutierrez
## Descripción

Este proyecto contiene un conjunto de pruebas automatizadas para la aplicación UrbanRoutes. Utiliza Selenium WebDriver para interactuar con la aplicación y verificar diversas funcionalidades, como establecer rutas, seleccionar tarifas, ingresar números de teléfono, agregar tarjetas de pago y más.

## Tecnologías y Técnicas Utilizadas

- **Python 3.12**: Lenguaje de programación utilizado para escribir los scripts de prueba.
- **Selenium WebDriver**: Herramienta utilizada para la automatización de pruebas de aplicaciones web.
- **Pytest**: Framework de pruebas utilizado para ejecutar y organizar las pruebas.
- **Google Chrome**: Navegador utilizado para ejecutar las pruebas.
- **ChromeDriver**: Driver necesario para que Selenium pueda controlar Google Chrome.

## Estructura del Proyecto

- **main.py**: Define la clase `UrbanRoutesPage` que contiene métodos para interactuar con diferentes elementos de la interfaz de usuario de la aplicación UrbanRoutes.
- **tests.py**: Contiene la clase `TestUrbanRoutes` con métodos de prueba que verifican las funcionalidades de la aplicación UrbanRoutes.
- **methods.py**: Proporciona métodos de utilidad, incluyendo `retrieve_phone_code`, que recupera un código de confirmación de teléfono de los registros de rendimiento del navegador.
- **data.py**: Contiene datos de prueba como URL, direcciones, números de teléfono, detalles de tarjeta y mensajes (no incluido en este repositorio por razones de seguridad).

## Instrucciones para Ejecutar las Pruebas

### Prerrequisitos

- Python 3.12
- Selenium
- Google Chrome
- ChromeDriver

### Instalación

1. Clona este repositorio.
   ```bash
   git clone https://github.com/tu-usuario/urbanroutes-automation.git
   cd urbanroutes-automation


### Ejecucion de pruebas
    Para ejecutar todas las pruebas, utiliza el siguiente comando:
    pytest

### Notas
    Asegúrate de que el archivo data.py contenga los datos de prueba necesarios, tales  como URL, direcciones, números de teléfono, detalles de tarjeta y mensajes.
No modifiques el archivo methods.py ya que contiene métodos de utilidad críticos para la recuperación de datos.
