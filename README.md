# Repositorio de Actividades: Refactorización y Sistemas Avanzados

Este repositorio contiene un conjunto de prácticas avanzadas de programación en Python, divididas en tres grandes bloques de aprendizaje: Refactorización de Código, Algoritmos y Estructuras de Datos y un Sistema de Gestión de Tareas con persistencia.

# 📁 Estructura del Proyecto 

## 1. Refactorización (ACTIVIDAD_INTERMEDIO_REFACTORIZACION)

Enfocado en la mejora de la calidad del código, legibilidad y patrones de diseño.

Bloque 1: Análisis, corrección de nomenclatura y simplificación de lógica.

Bloque 2: Modularización y aplicación del patrón Strategy.

Bloque 3 & 5: Transición de sistemas legacy a sistemas modernos de gestión de usuarios e inventarios.

## 2. Algoritmos y Optimización (Bloques 1 al 4) 

Implementaciones de lógica compleja y optimización de recursos.

Bloque 1: Sistemas de caché LRU (Least Recently Used) para optimización de memoria.

Bloque 2: Teoría de grafos, comparando implementaciones manuales vs. asistidas por IA.

Bloque 3: Algoritmos de Rate Limiting para control de tráfico.

Bloque 4: Ejercicios de Ingeniería Inversa y reconstrucción de código.

## 3. Sistema de Gestión de Tareas (Bloque 5) 

Un sistema completo con arquitectura profesional.

auth/ & handlers/: Manejo de autenticación JWT y lógica de negocio.

middleware/: Capas de auditoría (logs) y limitadores de velocidad.

models/ & Base de Datos: Definición de objetos task y persistencia en SQLite (task_manager.db).

# 🚀 Guía de Ejecución

Para asegurar que las importaciones internas funcionen correctamente, ejecuta los módulos desde la raíz del repositorio usando el comando python -m.

Ejecución de Refactorización
Bash

## Ejemplo: Ejecutar patrón Strategy

python -m "Bloque 2.2.2. patrón Strategy.Strategy_código"
Ejecución de Algoritmos
Bash

## Ejemplo: Ejecutar Sistema de Caché LRU

python -m "Bloque 1.1.2. Implantación Correcto.Sistema caché LRU(2)"
Ejecución del Sistema de Tareas
Para iniciar la aplicación principal del sistema de gestión:

Bash
python -m "Bloque 5 - Sistema de gestión de tareas.main"

# 🛠️ Requisitos

Python 3.12+ (detectado por la configuración de archivos .pyc).

SQLite (incluido nativamente en Python para la base de datos de tareas).

