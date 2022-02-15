
Lista de ajustes y/o mejoras pendientes por implementar
===

Descripción - Desarrollador - Fecha
--

- En `update_stock.py` de Amazon Lambda, línea 28, se está comparando ID de `ProductCompany` con `company_id` de mensaje de log, arreglar la condición para que se compare con `company_id` de `ProductCompany` - Gerardo - 13/06/2020
- En funciones de Amazon Lambda implementar Flake8 y PyLint para una mejor calidad de código fuente - Gerardo - 13/06/2020
- Validar existencia de stock de productos al crear y actualizar requisición y al actualizar estado de requisición - Gerardo - 13/06/2020
- Cargar sólo los países en los que tiene relación el producto (En Precios Producto) - Gerardo - 13/06/2020
- Implementar escritura automática de pruebas - Team - 13/06/2020
- Implementar uso de debug con Sentry - Gerardo - 13/06/2020
  - Víctor lo implementó en una tarea y está a la espera de revisión
- Mejorar ramificación de código fuente en `/dao` con validadores - Team - 13/06/2020
  - Giordano lo desarrolló en una tarea con CRUD de permisos y está a la espera de revisión
- Mejorar estructura de código fuente de modelos de datos - Gerardo - 13/06/2020
  - Herbert presentó propuestas en una tarea y está a la espera de revisión
- Optimizar las condiciones de variables sin valor en toda la lógica - Gerardo - 23/06/2020
- Remover el tipo de dato de respuestas en los métodos de módulos, proveedores, interfaces y dao - Gerardo - 24/06/2020
- Desactivar JWT en ambiente `develop` - Gerardo - 18/06/2020
- Mejorar la captura de error de ocurriencia en QA con una guía para obtener la entrada y respuesta de API en el caso - Gerardo - 18/06/2020
- Incluir eventos en segundo plano para actualización de registros de índice en ES, ejemplo una actualización de producto conlleva a actualizar los índices de `ProviderQuotationProduct` y `PurchaseProduct` - Gerardo - 20/06/2020