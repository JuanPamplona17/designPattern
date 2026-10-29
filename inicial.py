"""
Sistema de procesamiento de informes - versión inicial.
Patrón de diseño: Abstract Factory.
Categorías: ENTRADA (ENT) y SALIDA (SAL).
Tipos: FACTURA (FAC) y COMPRA (COM).
"""


class ReportProcessor:
    """Interfaz común de los procesadores."""

    def process(self):
        raise NotImplementedError


class EntradaFacturaProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de ENTRADA de tipo FACTURA")


class EntradaCompraProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de ENTRADA de tipo COMPRA")


class SalidaFacturaProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de SALIDA de tipo FACTURA")


class SalidaCompraProcessor(ReportProcessor):
    def process(self):
        print("Procesando informe de SALIDA de tipo COMPRA")


class ReportFactory:
    """Interfaz común para las fábricas."""

    def create_processor(self, report_type):
        raise NotImplementedError


class EntradaFactory(ReportFactory):
    def create_processor(self, report_type):
        processors = {
            "FAC": EntradaFacturaProcessor,
            "COM": EntradaCompraProcessor,
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


def get_factory(category):
    factories = {
        "ENT": EntradaFactory,
        "SAL": SalidaFactory,
    }
    if category not in factories:
        raise ValueError(f"Categoría no válida: {category}")
    return factories[category]()


def procesar_informes(reports):
    for report in reports:
        try:
            parts = report.split("_")
            if len(parts) != 3 or not parts[2].endswith(".txt") or len(parts[2]) <= 4:
                raise ValueError("Formato de archivo no válido")

            category, report_type, _filename = parts
            factory = get_factory(category)
            processor = factory.create_processor(report_type)
            processor.process()

        except (AttributeError, ValueError) as error:
            print(f"No se pudo procesar {report}: {error}")


if __name__ == "__main__":
    reports = [
        "ENT_FAC_001.txt",
        "ENT_COM_001.txt",
        "SAL_FAC_001.txt",
        "SAL_COM_001.txt",
        "ARCHIVO_INVALIDO.txt",
    ]
    procesar_informes(reports)
