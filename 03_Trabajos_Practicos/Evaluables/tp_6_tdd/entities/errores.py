class ErrorValidacion(Exception):
    """Se lanza cuando un dato de la compra de entradas no es válido.
    campo: el dato que falló ("fecha", "cantidad", "edades", "tipo_pase", "forma_pago"), para mostrar el error debajo de él.
    indice: en las edades, la posición del visitante cuya edad es inválida."""

    def __init__(self, mensaje: str = "", campo: str | None = None, indice: int | None = None):
        super().__init__(mensaje)
        self.campo = campo
        self.indice = indice


class ErroresValidacion(ErrorValidacion):
    """Junta todos los errores de validación para informarlos a la vez y no de a uno."""

    def __init__(self, errores: list[ErrorValidacion]):
        super().__init__("\n".join(str(error) for error in errores))
        self.errores = errores


def validar_campo(campo: str, validacion, errores: list[ErrorValidacion]) -> bool:
    """Ejecuta la validación; si falla, agrega sus errores marcados con el campo y devuelve False."""
    try:
        validacion()
    except ErrorValidacion as error:
        encontrados = error.errores if isinstance(error, ErroresValidacion) else [error]
        for encontrado in encontrados:
            encontrado.campo = campo
        errores.extend(encontrados)
        return False
    return True


class ErrorPago(Exception):
    """Se lanza cuando Mercado Pago rechaza el pago."""


class ErrorMail(Exception):
    """Se lanza cuando no se pudo enviar el mail de confirmación."""
