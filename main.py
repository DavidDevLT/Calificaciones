from logica.calificaciones import Calificaciones

if __name__ == '__main__':
    nota = float(input("Ingrese su nota: "))
    calificacion = Calificaciones(nota)
    calificacion.rangoCalificaciones()
    calificacion.imprimirReporte()