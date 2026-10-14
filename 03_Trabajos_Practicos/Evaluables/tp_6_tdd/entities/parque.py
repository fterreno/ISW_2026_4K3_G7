from dataclasses import dataclass, field
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
        if fecha == ahora.date() and not (self.hora_apertura <= ahora.time() <= self.hora_cierre):
            raise ErrorValidacion("La hora actual está fuera del horario de apertura.")
