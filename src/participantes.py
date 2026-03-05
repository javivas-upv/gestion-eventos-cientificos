from datetime import datetime
from typing import Optional


class Participante:
    def __init__(self, nombre: str, email: str, institucion: str, tipo: str = "asistente"):
        self.id: Optional[int] = None
        self.nombre = nombre
        self.email = email
        self.institucion = institucion
        self.tipo = tipo
        self.fecha_registro = datetime.now()
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.institucion}"


class Inscripcion:
    def __init__(self, participante: Participante, evento_id: int):
        self.id: Optional[int] = None
        self.participante = participante
        self.evento_id = evento_id
        self.fecha_inscripcion = datetime.now()
        self.estado = "pendiente"
    
    def confirmar(self):
        self.estado = "confirmada"
    
    def cancelar(self):
        self.estado = "cancelada"
    
    def __str__(self):
        return f"Inscripción de {self.participante.nombre} - Estado: {self.estado}"


class GestorParticipantes:
    def __init__(self):
        self.participantes = []
        self.inscripciones = []
    
    def registrar_participante(self, participante: Participante):
        participante.id = len(self.participantes) + 1
        self.participantes.append(participante)
        return participante.id
    
    def inscribir_participante(self, participante: Participante, evento_id: int):
        inscripcion = Inscripcion(participante, evento_id)
        inscripcion.id = len(self.inscripciones) + 1
        self.inscripciones.append(inscripcion)
        return inscripcion
    
    def listar_participantes(self, tipo: Optional[str] = None):
        participantes = self.participantes
        if tipo:
            participantes = [p for p in participantes if p.tipo == tipo]
        return participantes
    
    def obtener_inscripciones_evento(self, evento_id: int):
        return [i for i in self.inscripciones if i.evento_id == evento_id]
    
    def buscar_por_email(self, email: str):
        for p in self.participantes:
            if p.email == email:
                return p
        return None
