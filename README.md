# Taller-Final-Ruta-optima
Ruta Óptima 
Descripción del proyecto
Ruta Óptima es un sistema logístico desarrollado para una empresa de envíos que necesita clasificar paquetes antes de cargarlos a los camiones.
El sistema permite:
- Registrar envíos
- Clasificar paquetes según peso
- Calcular costos automáticamente
- Almacenar información en SQLite
- Gestionar registros mediante una interfaz gráfica
- Analizar información mediante Power BI
- Tecnologías utilizadas
- Python
- SQLite
- Tkinter
- Power BI
- Programación Orientada a Objetos (POO)
- Arquitectura utilizada
El proyecto se desarrolló utilizando una arquitectura modular dividida en:
- Backend
- Contiene:
- Lógica de negocio
- Clases POO
- CRUD
- Base de datos SQLite
- Modelo relacional tipo Esquema Estrella
- Frontend
Contiene:
- Interfaz gráfica Tkinter
- Manejo de errores con messagebox
- Conexión con la base de datos
- Apertura automática del dashboard Power BI
- Inteligencia de Negocios
Contiene:
- Dashboard en Power BI
- Modelo estrella
- Medidas DAX
- Columna calculada DAX
- Indicadores y gráficos interactivos
- Estructura del proyecto
- ruta-optima-logistica/
- Backend/
- Frontend/
- main.py
- ruta_optima_final.pbix
- README.md
- Instrucciones para ejecutar el proyecto
Descargar o clonar el repositorio:
- git clone URL_DEL_REPOSITORIO
- Instalar dependencias:
- pip install -r pillow
Ejecutar Backend:
- python Backend/main.py
- Ejecutar la aplicación:
- python main.py
- Abrir Power BI desde el botón "Abrir Dashboard"
- Funcionalidades principales
- Registrar envíos
- Ver registros
- Actualizar información
- Eliminar registros
- Clasificar paquetes automáticamente
- Calcular costos
- Dashboard analítico conectado a SQLite

Grupo 11
-Paula Andrea Arciniegas Cárdenas
-Isabella Carranza Tapiero
-Valeria Morales
 
Universidad de La Sabana
Programación y Decisiones — 2026-1
