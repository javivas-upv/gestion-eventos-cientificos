from datetime import datetime
from typing import List


class Conferencia:
    def __init__(self, titulo: str, ponente: str, duracion: int, sala: str = ""):
        self.titulo = titulo
        self.ponente = ponente
        self.duracion = duracion
        self.sala = sala
    
    def __str__(self):
        return f"{self.titulo} - {self.ponente} ({self.duracion} min)"


class Evento:
    def __init__(self, nombre: str, localizacion: str, fecha_inicio: datetime, fecha_fin: datetime):
        self.nombre = nombre
        self.localizacion = localizacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.conferencias: List[Conferencia] = []
    
    def agregar_conferencia(self, conferencia: Conferencia):
        self.conferencias.append(conferencia)
    
    def eliminar_conferencia(self, titulo: str):
        self.conferencias = [c for c in self.conferencias if c.titulo != titulo]
    
    def listar_conferencias(self):
        if not self.conferencias:
            return "No hay conferencias programadas"
        
        resultado = f"Conferencias de {self.nombre}:\n"
        for i, conf in enumerate(self.conferencias, 1):
            resultado += f"{i}. {conf}\n"
        return resultado
    
    def __str__(self):
        return f"{self.nombre} - {self.localizacion} ({self.fecha_inicio.strftime('%d/%m/%Y')} - {self.fecha_fin.strftime('%d/%m/%Y')})"
