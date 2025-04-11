# Sistema de Gestión de Productos (3 Capas)

Este proyecto demuestra una arquitectura en tres capas para un sistema simple de gestión de productos.

## Estructura de Capas

1. **Capa de Presentación (capa_presentacion.py)**:
   - Maneja la interacción con el usuario
   - Recibe inputs y muestra outputs
   - No contiene lógica de negocio, solo la presenta

2. **Capa de Negocio (capa_negocio.py)**:
   - Contiene las reglas de negocio (validaciones, cálculos)
   - Coordina el flujo de datos
   - No sabe nada sobre cómo se almacenan los datos o cómo se presentan

3. **Capa de Datos (data_layer.py)**:
   - Maneja el almacenamiento y recuperación de datos
   - No contiene lógica, solo operaciones CRUD básicas
   - Podría cambiarse por una base de datos real sin afectar otras capas

## Ventajas sobre la versión monolítica

1. **Separación de preocupaciones**: Cada capa tiene una responsabilidad clara
2. **Mayor mantenibilidad**: Los cambios en una capa no suelen afectar a las otras
3. **Mejor testabilidad**: Cada capa puede probarse independientemente
4. **Escalabilidad**: Es más fácil añadir nuevas características
5. **Reusabilidad**: La lógica de negocio podría usarse con diferentes interfaces (CLI, web, API)
6. **Flexibilidad**: Se puede cambiar la capa de datos sin modificar el negocio o presentación

## Cómo ejecutar
```bash
python presentation_layer.py