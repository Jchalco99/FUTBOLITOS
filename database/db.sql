DROP DATABASE futbolitos;

CREATE DATABASE futbolitos;

USE futbolitos;

CREATE TABLE IF NOT EXISTS `clasificacion` (
  `posicion` int(11) NOT NULL,
  `idEquipo` varchar(3) DEFAULT NULL,
  `pjugados` int(11) NOT NULL,
  `pganados` int(11) NOT NULL,
  `pempatados` int(11) NOT NULL,
  `pperdidos` int(11) NOT NULL,
  `gfavor` int(11) NOT NULL,
  `gcontra` int(11) NOT NULL,
  `diferencia` varchar(11) NOT NULL,
  `puntos` int(11) NOT NULL,
  PRIMARY KEY (`posicion`),
  KEY `fk_idEquipo_clasificacion` (`idEquipo`),
  CONSTRAINT `fk_idEquipo_clasificacion` FOREIGN KEY (`idEquipo`) REFERENCES `equipo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;