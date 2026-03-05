from datetime import datetime
from eventos import Evento, Conferencia


def main():
    evento = Evento(
        nombre="Congreso Internacional de Astrofísica 2026",
        localizacion="Teruel, España",
        fecha_inicio=datetime(2026, 6, 15),
        fecha_fin=datetime(2026, 6, 17)
    )
    
    conf1 = Conferencia(
        titulo="Detección de exoplanetas mediante tránsitos",
        ponente="Dra. María García",
        duracion=45,
        sala="Auditorio Principal"
    )
    
    conf2 = Conferencia(
        titulo="Materia oscura en galaxias enanas",
        ponente="Dr. Juan Pérez",
        duracion=30,
        sala="Sala A"
    )
    
    evento.agregar_conferencia(conf1)
    evento.agregar_conferencia(conf2)
    
    print(evento)
    print("\n" + evento.listar_conferencias())


if __name__ == "__main__":
    main()
