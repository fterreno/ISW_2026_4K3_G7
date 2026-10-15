from dataclasses import dataclass, field
import calendar
from datetime import date, datetime, time

from entities.errores import ErrorValidacion


@dataclass
class Parque:
    # el parque abre todos los días de 8:30 a 19:00, menos los lunes y los días festivos
    nombre: str = 'EcoHarmony Park'
    dias_abiertos: set[int] = field(default_factory=lambda: {1, 2, 3, 4, 5, 6})  # 0 es lunes ... 6 es domingo
    dias_festivos: set[tuple[int, int]] = field(default_factory=lambda: {(12, 25), (1, 1)})  # (mes, día): 25/12 y 1/1
    hora_apertura: time = time(8, 30)
    hora_cierre: time = time(19, 0)
    hora_limite_compra: time = time(17, 30)  # para la fecha actual solo se puede comprar hasta las 17:30

    def validar_disponibilidad(self, fecha: date, ahora: datetime | None = None) -> None:
        """Confirma que el parque está disponible en la fecha pedida; si no, lanza ErrorValidacion con el motivo."""
        if ahora is None:  # si viene cargada es porque viene por el test
            ahora = datetime.now()

        if fecha < ahora.date():
            raise ErrorValidacion("La fecha de visita no puede ser anterior a la fecha actual.")
        if fecha.weekday() not in self.dias_abiertos:
            raise ErrorValidacion("El parque está cerrado ese día.")
        if (fecha.month, fecha.day) in self.dias_festivos:
            raise ErrorValidacion("El parque está cerrado ese día por ser feriado.")
        if fecha > self.sumar_un_mes(ahora.date()):
            raise ErrorValidacion("La fecha de visita no puede ser posterior a un mes desde la fecha actual.")
        # La compra para hoy tiene un horario límite, pero no exige que el parque ya haya abierto (FAQ, punto 26).
        if fecha == ahora.date() and ahora.time() > self.hora_limite_compra:
            raise ErrorValidacion(f"Para la fecha actual solo se puede comprar hasta las {self.hora_limite_compra:%H:%M}.")

    @staticmethod
    def sumar_un_mes(fecha: date) -> date:
        """Devuelve el mismo día del mes siguiente; si ese mes no tiene ese día, el último día del mes."""
        anio, mes = (fecha.year + 1, 1) if fecha.month == 12 else (fecha.year, fecha.month + 1)
        dia = min(fecha.day, calendar.monthrange(anio, mes)[1])
        return date(anio, mes, dia)
