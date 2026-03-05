CREATE TABLE IF NOT EXISTS participantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    institucion VARCHAR(150),
    tipo VARCHAR(20) DEFAULT 'asistente',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(200) NOT NULL,
    localizacion VARCHAR(150),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS inscripciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    participante_id INTEGER NOT NULL,
    evento_id INTEGER NOT NULL,
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) DEFAULT 'pendiente',
    FOREIGN KEY (participante_id) REFERENCES participantes(id) ON DELETE CASCADE,
    FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE,
    UNIQUE(participante_id, evento_id)
);

CREATE TABLE IF NOT EXISTS conferencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evento_id INTEGER NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    ponente VARCHAR(100),
    duracion INTEGER,
    sala VARCHAR(50),
    FOREIGN KEY (evento_id) REFERENCES eventos(id) ON DELETE CASCADE
);

CREATE INDEX idx_participantes_email ON participantes(email);
CREATE INDEX idx_inscripciones_evento ON inscripciones(evento_id);
CREATE INDEX idx_inscripciones_participante ON inscripciones(participante_id);
CREATE INDEX idx_conferencias_evento ON conferencias(evento_id);
