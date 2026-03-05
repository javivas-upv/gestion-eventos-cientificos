import sqlite3
from datetime import datetime
from eventos import Evento, Conferencia
from participantes import Participante, GestorParticipantes


def crear_base_datos():
    conn = sqlite3.connect('eventos.db')
    cursor = conn.cursor()
    
    with open('schema.sql', 'r') as f:
        cursor.executescript(f.read())
    
    conn.commit()
    conn.close()
    print("Base de datos creada correctamente")


def ejemplo_participantes():
    gestor = GestorParticipantes()
    
    p1 = Participante("Dr. Carlos Martínez", "carlos@unizar.es", "Universidad de Zaragoza", "ponente")
    p2 = Participante("Ana López", "ana@upv.es", "Universidad Politécnica de Valencia", "asistente")
    p3 = Participante("Dra. Laura Sánchez", "laura@csic.es", "CSIC", "ponente")
    
    gestor.registrar_participante(p1)
    gestor.registrar_participante(p2)
    gestor.registrar_participante(p3)
    
    inscripcion1 = gestor.inscribir_participante(p1, 1)
    inscripcion2 = gestor.inscribir_participante(p2, 1)
    
    inscripcion1.confirmar()
    
    print("=== Participantes registrados ===")
    for p in gestor.listar_participantes():
        print(f"  {p}")
    
    print("\n=== Ponentes ===")
    for p in gestor.listar_participantes(tipo="ponente"):
        print(f"  {p}")
    
    print("\n=== Inscripciones al evento 1 ===")
    for i in gestor.obtener_inscripciones_evento(1):
        print(f"  {i}")


def main():
    print("=== Sistema de Gestión de Eventos Científicos ===\n")
    
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
    
    evento.agregar_conferencia(conf1)
    
    print(evento)
    print()
    
    ejemplo_participantes()


if __name__ == "__main__":
    main()
