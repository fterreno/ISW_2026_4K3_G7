class ErrorValidacion(Exception):
    """Se lanza cuando un dato de la compra de entradas no es válido."""


class ErrorPago(Exception):
    """Se lanza cuando Mercado Pago rechaza el pago."""


class ErrorMail(Exception):
    """Se lanza cuando no se pudo enviar el mail de confirmación."""
