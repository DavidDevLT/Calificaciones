class Calificaciones():
    def __init__(self, nota):
        self.nota = nota

    def rangoCalificaciones(self):
        if self.nota > 9.0:
            rango = 'A - Excelente'
        elif self.nota > 8.0:
            rango = 'B - Muy bien'
        elif self.nota >= 7.5:
            rango = 'C - Bien'
        else:
            rango = 'R - Reprobado'

        return rango

    def imprimirReporte(self):
        print(f'El rango de su nota es: {Calificaciones.rangoCalificaciones(self)}.')
