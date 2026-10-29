# Sistema de procesamiento de informes (Python)

Este proyecto contiene dos versiones de un ejemplo del patrón de creación
**Abstract Factory (Factoría Abstracta)**.

## Archivos

- `inicial.py`: versión inicial con las categorías `ENT` (ENTRADA) y
  `SAL` (SALIDA), y los tipos `FAC` (FACTURA) y `COM` (COMPRA).
- `evolucionado.py`: incorpora la categoría `MIX` (MIXTA) y el tipo
  `PED` (PEDIDO), permitido únicamente para la categoría `ENT`.

## Requisitos

- Python 3.8 o superior.
- No requiere instalar librerías externas.

## Cómo ejecutar

Abre una terminal en esta carpeta y ejecuta:

```bash
python3 inicial.py
```

Para ejecutar la versión ampliada:

```bash
python3 evolucionado.py
```

En Windows se puede usar `python` en lugar de `python3`, según la instalación.

## Formato de los nombres

Los archivos deben seguir el formato:

```text
CAT_TIPO_nombre.txt
```

Ejemplos:

- `ENT_FAC_001.txt`: factura de ENTRADA.
- `SAL_COM_001.txt`: compra de SALIDA.
- `MIX_FAC_001.txt`: factura MIXTA (solo versión evolucionada).
- `ENT_PED_001.txt`: pedido de ENTRADA (solo versión evolucionada).

El programa simula el procesamiento mostrando un mensaje por pantalla; no abre
ni modifica archivos reales.

## ¿Dónde se aplica Abstract Factory?

`ReportFactory` define el método común para crear procesadores. Las fábricas
`EntradaFactory`, `SalidaFactory` y `MixtaFactory` crean los procesadores
correspondientes a cada categoría. Todos los procesadores comparten la interfaz
`ReportProcessor`, pero cada uno implementa su propio mensaje de procesamiento.

La versión inicial permite observar la estructura básica. La versión
evolucionada muestra cómo se agregan una categoría y un tipo nuevo manteniendo
separadas las responsabilidades.
