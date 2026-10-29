"""
Sistema de procesamiento de informes - versión evolucionada.
Patrón de diseño: Abstract Factory.
Categorías: ENTRADA (ENT), SALIDA (SAL) y MIXTA (MIX).
Tipos: FACTURA (FAC), COMPRA (COM) y PEDIDO (PED).
PEDIDO solamente está permitido para ENTRADA.
"""


class ReportProcessor:
    """Interfaz común de los procesadores."""

    def process(self):
        raise NotImplementedError


# Procesadores de ENTRADA
class EntradaFacturaProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de ENTRADA de tipo FACTURA")


class EntradaCompraProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de ENTRADA de tipo COMPRA")


class EntradaPedidoProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de ENTRADA de tipo PEDIDO")


# Procesadores de SALIDA
class SalidaFacturaProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de SALIDA de tipo FACTURA")


class SalidaCompraProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de SALIDA de tipo COMPRA")


# Procesadores de MIXTA
class MixtaFacturaProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de MIXTA de tipo FACTURA")


class MixtaCompraProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de MIXTA de tipo COMPRA")


class ReportFactory:
    """Interfaz común para las fábricas."""

    def create_processor(self, report_type):
        raise NotImplementedError


class EntradaFactory(ReportFactory):
    def create_processor(self, report_type):
        processors = {
            "FAC": EntradaFacturaProcessor,
            "COM": EntradaCompraProcessor,
            "PED": EntradaPedidoProcessor,
        }
        if report_type not in processors:
            raise ValueError(f"Tipo no compatible con ENTRADA: {report_type}")
        return processors[report_type]()


class SalidaFactory(ReportFactory):
    def create_processor(self, report_type):
        processors = {
            "FAC": SalidaFacturaProcessor,
            "COM": SalidaCompraProcessor,
        }
        if report_type not in processors:
            raise ValueError(f"Tipo no compatible con SALIDA: {report_type}")
        return processors[report_type]()


class MixtaFactory(ReportFactory):
    def create_processor(self, report_type):
        processors = {
            "FAC": MixtaFacturaProcessor,
            "COM": MixtaCompraProcessor,
        }
        if report_type not in processors:
            raise ValueError(f"Tipo no compatible con MIXTA: {report_type}")
        return processors[report_type]()


def get_factory(category):
    factories = {
        "ENT": EntradaFactory,
        "SAL": SalidaFactory,
        "MIX": MixtaFactory,
    }
    if category not in factories:
        raise ValueError(f"Categoría no válida: {category}")
    return factories[category]()


def procesar_informes(reports):
    for report in reports:
        try:
            if not isinstance(report, str):
                raise ValueError("El nombre del archivo debe ser texto")

            parts = report.split("_")
            if len(parts) != 3 or not parts[2].endswith(".txt") or len(parts[2]) <= 4:
                raise ValueError("Formato de archivo no válido")

            category, report_type, _filename = parts

            # PEDIDO está permitido únicamente para la categoría ENTRADA.
            if report_type == "PED" and category != "ENT":
                raise ValueError("PEDIDO solo está permitido para ENTRADA")

            factory = get_factory(category)
            processor = factory.create_processor(report_type)
            processor.process()

        except ValueError as error:
            print(f"No se pudo procesar {report}: {error}")


if __name__ == "__main__":
    reports = [
        "ENT_FAC_001.txt",
        "ENT_COM_001.txt",
        "SAL_FAC_001.txt",
        "SAL_COM_001.txt",
        "MIX_FAC_001.txt",
        "MIX_COM_001.txt",
        "ENT_PED_001.txt",
        "SAL_PED_001.txt",       # Debe rechazarse: PEDIDO no aplica a SALIDA.
        "ARCHIVO_INVALIDO.txt",
    ]
    procesar_informes(reports)
