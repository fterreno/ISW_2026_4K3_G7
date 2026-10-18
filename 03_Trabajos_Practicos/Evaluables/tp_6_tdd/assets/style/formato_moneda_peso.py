def formatear_monto(monto: float) -> str:
    """Formato de moneda argentino: $ 20.000,00"""
    return "$ " + f"{monto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
