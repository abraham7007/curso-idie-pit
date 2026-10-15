#!/usr/bin/env python3
"""Sesión 4 · Formulación de proyectos — formato ponencia (11.ª edición).

Temas: «Diagnóstico del problema, objetivos y estado del arte» (tema 01:
documentos y cartilla del concurso, árbol de problemas y de objetivos,
magnitud y enunciado del problema, objetivos, búsqueda declarada y
diferenciación técnica) y «Marco lógico, plan de trabajo y equipo del
proyecto» (tema 02: matriz e indicadores, supuestos, cadena de resultados y
teoría del cambio, metodología, cronograma con hitos, equipo y acuerdos).

Secuencia (scratchpad/s4-auditoria-secuencia.md, §4): U1 la propuesta y su
evaluación → U2 diagnóstico del problema → U3 objetivos y estado del arte →
receso → U4 matriz e indicadores → U5 cadena de resultados y teoría del cambio
→ U6 plan de trabajo, equipo y acuerdos.

Concurso de referencia: Proyectos de Desarrollo Tecnológico E041-2027-02 de
PROCIENCIA (bases integradas y modificadas al 3 de septiembre de 2026,
anexos, cartilla de evaluación firmada el 3 de septiembre de 2026; cierre el 7
de diciembre de 2026), más la guía de soporte, seguimiento y evaluación de los
concursos 2027 y el manual de Ortegón, Pacheco y Prieto (ILPES-CEPAL, 2005).

Ejemplos (scratchpad/asignacion-ejemplos.md, banco-ejemplos.md y
ejemplos-s4.md): cada herramienta se ilustra con un proyecto distinto de la
UNI seleccionado por PROCIENCIA. Caso del concurso, objetivos y estado del
arte: monitoreo acústico de la tala ilegal (Desarrollo Tecnológico 2026-03).
Árbol de problemas y de objetivos, magnitud y enunciado: recuperación de oro
sin mercurio en la minería artesanal (Desarrollo Tecnológico 2025-03). Matriz,
meta, indicador y supuestos: potabilización solar de pozos con arsénico
(Desarrollo Tecnológico 2024-02). Cadena de resultados: inventarios urbanos
para la gestión del riesgo (Investigación Aplicada 2025-02). Metodología y
cronograma: agricultura digital del palto Hass (Desafíos de Innovación 2024,
INICTEL-UNI). Las metas, los montos y los meses de los ejemplos son
ilustrativos y se declaran así. Datos nuevos verificados: DS 034-2016-PCM,
Ashe (2012), DS 031-2010-SA, OMS (2022), reporte de alerta temprana del
PNCBMCC-MINAM y consulta a OpenAlex del 14 de octubre de 2026 (cotejo en
scratchpad/s4-cotejo-v2.md). Recursos: scratchpad/recursos-s4.md (4 por
unidad). Ningún recurso se cita en clase.

Formato expositivo: la sesión no incluye actividades en el aula. Las notas
reúnen contenido de respaldo con dato y fuente, errores frecuentes de los
formuladores y puntos por verificar.

Antes de dictar, verificar: nueva integración de bases de E041-2027-02 después
del 3 de septiembre de 2026; mediciones de mercurio en Madre de Dios
posteriores a 2016; la cita de Doran (1981), confirmada en fuentes
secundarias; el reglamento de convenios de la UNI.

Uso:  python3 tools/ponencia/clase-04.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from graficos import (  # noqa: E402
    arbol, arbol_portada, barras_valor, criterios_svg, gantt, icono_nodo_acustico, matriz_ml,
    matriz_riesgo,
)
from plantillas import (  # noqa: E402
    agenda, caso, cierre, cifra, construir, duo, pasos, portada, recursos, referencias,
    seccion, tarjetas, visual,
)

FUENTE_REC = "Enlaces verificados en octubre de 2026"
BASES = "PROCIENCIA, bases integradas E041-2027-02, 3 de septiembre de 2026"
CARTILLA = "PROCIENCIA, cartilla de evaluación de Desarrollo Tecnológico, E041-2027-02"
ILPES = "Ortegón, Pacheco y Prieto, ILPES-CEPAL, 2005"

L = []

# ================================================================ APERTURA (5 min)

L.append(portada(
    "portada",
    "Sesión 4 · Diseño y Gestión de Proyectos {I+D+i+e}",
    "Formulación de proyectos",
    "Redacción de una propuesta de I+D+i según las bases y la cartilla de evaluación de un "
    "concurso",
    ["Diagnóstico del problema, objetivos y estado del arte",
     "Marco lógico, plan de trabajo y equipo del proyecto"],
    "Abraham Caso-Torres · OTI-UNI · CC BY-SA 4.0",
    visual=arbol_portada(),
    notas=[
        "Dar la bienvenida y presentar los dos temas de la sesión: el diagnóstico que "
        "justifica el proyecto y el plan que permite comprobar su avance.",
        "La sesión redacta la propuesta con los documentos de un concurso abierto el día de la "
        "clase, Proyectos de Desarrollo Tecnológico 2027-02 de PROCIENCIA, que cierra el 7 de "
        "diciembre de 2026. Cada herramienta se ilustra con un proyecto distinto de la UNI "
        "seleccionado por PROCIENCIA; los objetivos, las metas, los montos y los meses de esos "
        "ejemplos son ilustrativos.",
    ],
))

L.append(agenda(
    "agenda",
    "Agenda",
    "Temas y contenidos de la sesión 4",
    [
        ("Diagnóstico del problema, objetivos y estado del arte",
         ["Documentos y cartilla de evaluación",
          "Diagnóstico del problema",
          "Objetivos y estado del arte"]),
        ("Marco lógico, plan de trabajo y equipo del proyecto",
         ["Matriz de marco lógico e indicadores",
          "Cadena de resultados y teoría del cambio",
          "Plan de trabajo, equipo y acuerdos"]),
    ],
    notas=[
        "Presentar los dos temas y las tres unidades de cada uno.",
        "Tiempo: apertura, 5 min; tema 01, 77 min; receso, 10 min; tema 02, 77 min; cierre, "
        "5 min; holgura para preguntas, 6 min.",
        "El presupuesto por partidas, el contrato de subvención, la rendición de cuentas y la "
        "protección de los resultados corresponden a la sesión 5.",
    ],
))

# ============== TEMA 01 · DIAGNÓSTICO DEL PROBLEMA, OBJETIVOS Y ESTADO DEL ARTE

L.append(seccion(
    "tema-01", "01", "Diagnóstico del problema, objetivos y estado del arte",
    "Documentos que rigen la postulación, problema que atiende el proyecto, objetivos "
    "verificables y antecedentes del tema",
    notas=[
        "Presentar el tema 01, que produce la parte de la propuesta que describe qué problema "
        "se atiende, con qué objetivos y qué se sabe ya del tema.",
        "Tiempo: 77 minutos; presentación del tema, 1; la propuesta y su evaluación, 22; "
        "diagnóstico del problema, 25; objetivos y estado del arte, 26; síntesis, 3.",
    ],
))

# ---------- U1 · La propuesta y su evaluación

L.append(tarjetas(
    "documentos-convocatoria",
    "01 · Documentos del concurso",
    "Documentos de un concurso de *PROCIENCIA* que rigen la postulación",
    [
        ("Bases", "Condiciones, montos, plazos, equipo y resultados exigidos"),
        ("Anexos", "Cartas de compromiso, declaraciones juradas y rubros financiables"),
        ("Cartilla de elegibilidad", "Requisitos que se verifican antes de la evaluación"),
        ("Cartilla de evaluación", "Criterios, preguntas al evaluador y peso de cada criterio"),
        ("Guía de seguimiento y modelo de contrato", "Reglas de la ejecución del proyecto seleccionado"),
    ],
    clave=3,
    iconos=["file", "agreement", "check", "rubric", "calendar"],
    fuente=BASES + ", num. 1.5 y 3.2",
    notas=[
        "Las bases del concurso E041-2027-02 establecen que la postulación «implica la lectura "
        "y entendimiento» de las bases, los anexos, las cartillas de elegibilidad y de "
        "evaluación, la guía de soporte, seguimiento y evaluación y el modelo de contrato "
        "(num. 1.5).",
        "La propuesta se registra en la plataforma de postulación de PROCIENCIA con el usuario "
        "del CTI Vitae del responsable técnico. Cada integrante del equipo necesita su registro "
        "actualizado en CTI Vitae, el directorio de hojas de vida de investigadores del "
        "CONCYTEC (num. 2.3 y 3).",
        "Dato: los documentos de postulación incluyen las cartas de presentación y compromiso "
        "de las entidades (Anexos 4A, 4B y 4C), la declaración jurada del responsable técnico "
        "(Anexo 5), la declaración de ética e integridad científica (Anexo 10), el compromiso "
        "de finalización de la tesis cuando el equipo tiene tesista (Anexo 6) y el plan de "
        "gestión de datos (Anexo 14), que se desarrolla en la sesión 5 (num. 1.5 y 3.2).",
        "Dato: en Desarrollo Tecnológico, la propuesta adjunta además un video de cinco minutos "
        "como máximo y la evidencia del TRL de entrada, con el resultado de la calculadora TRL "
        "de la plataforma Vincúlate (num. 1.5).",
        "Error frecuente: firmar los anexos con una imagen de la firma pegada en el documento. "
        "Las bases admiten la firma electrónica o la manuscrita y no aceptan documentos con "
        "firma digitalizada (num. 3.2).",
    ],
))

L.append(caso(
    "caso-tala-ilegal",
    "01 · Caso de estudio · concurso",
    "Alerta acústica de tala ilegal",
    "UNI (FIEE) con OSINFOR y la UNTRM · Desarrollo Tecnológico 2026-03 de PROCIENCIA",
    [
        ("S/ 350 000", "Subvención de PROCIENCIA, tope del concurso"),
        ("14 de 64", "Propuestas seleccionadas en el concurso"),
        ("TRL 6", "Salida mínima de las bases 2026, con entrada en TRL 4 o 5"),
    ],
    icono_nodo_acustico(),
    fuente="PROCIENCIA, RDE 044-2026-PROCIENCIA-DE, 6 de mayo de 2026 · bases E041-2026-03, "
           "num. 1.5 · Andina, 14 de mayo de 2026",
    notas=[
        "El proyecto «Validación y optimización de un sistema de monitoreo acústico basado en "
        "Edge AI para la detección de tala ilegal en ecosistemas amazónicos», de la UNI, con "
        "responsable técnico Luis Miguel Romero Goytendia (FIEE), fue uno de los 14 "
        "seleccionados del concurso de Desarrollo Tecnológico 2026-03 (Resolución de Dirección "
        "Ejecutiva, RDE, 044-2026-PROCIENCIA-DE). La sesión 3 lo citó como ejemplo de "
        "subvención y de contrapartida no monetaria.",
        "La IA en el borde (_edge AI_) procesa la señal en el propio nodo de campo. Según la "
        "prensa, el sistema identifica sonidos de motosierras y maquinaria para generar "
        "alertas tempranas de vigilancia ambiental, y se desarrolla con el Organismo de "
        "Supervisión de los Recursos Forestales y de Fauna Silvestre (OSINFOR) y la Universidad "
        "Nacional Toribio Rodríguez de Mendoza (UNTRM). La resolución no lista entidades "
        "asociadas; ese dato consta en prensa (Andina, 2026).",
        "Dato: se registraron 64 postulaciones; 36 aprobaron la evaluación por pares en simple "
        "ciego, 31 resultaron aptas y tres paneles seleccionaron 14, sin accesitarias (RDE "
        "044-2026).",
        "Dato: las bases 2026 exigían entrada en TRL 4 o 5 y salida en TRL 6 o superior. Las "
        "bases 2027-02 piden entrada en TRL 3 o 4 y salida en TRL 5 o superior, con hasta "
        "S/ 350 000, hasta 36 meses y al menos 20 subvenciones (num. 1.2 y 1.5, tabla 5). Los "
        "TRL declarados por el propio proyecto no son públicos.",
        "Dato: con una universidad pública como solicitante, PROCIENCIA financia hasta el 75 % "
        "del costo total y la contrapartida no monetaria es de al menos 25 %. Con el monto "
        "máximo, el ejemplo de las bases da S/ 116 667 de contrapartida y S/ 466 667 de costo "
        "total (tablas 7 y 8). El presupuesto real del proyecto no es público.",
        "Verificar antes de la clase: si PROCIENCIA publicó otra integración de las bases "
        "E041-2027-02 después del 3 de septiembre de 2026.",
    ],
))

L.append(visual(
    "ponderacion-criterios",
    "01 · Cartilla de evaluación",
    "Peso de los criterios de evaluación en *Desarrollo Tecnológico* 2027 de PROCIENCIA",
    barras_valor([
        ("Propuesta científico-tecnológica", 20, ""),
        ("Resultados, sostenibilidad e impacto", 20, ""),
        ("Relevancia, pertinencia y coherencia", 15, ""),
        ("Potencialidad de mercado", 15, "clave"),
        ("Experiencia y funciones del equipo", 10, ""),
        ("Viabilidad de la propuesta", 10, ""),
        ("Presupuesto", 10, ""),
    ], maximo=25, paso=5, menor=1, decimales=0, sufijo=" %", xb=650,
        unidad="PORCENTAJE DEL PUNTAJE TOTAL"),
    fuente=CARTILLA + ", firmada el 3 de septiembre de 2026",
    notas=[
        "Dato: cada criterio se califica de 0 (no cumple) a 5 (sobresaliente) y la propuesta "
        "se aprueba con un promedio igual o mayor a 3,5. La propuesta científico-tecnológica "
        "se evalúa en cuatro subcriterios: antecedentes y justificación, objetivo, metodología "
        "y coherencia.",
        "El criterio marcado, potencialidad de mercado (15 %), es propio de la cartilla de "
        "Desarrollo Tecnológico: pregunta por el público objetivo, el potencial de adopción, "
        "transferencia, escalamiento y mercado, y el riesgo tecnológico. En Investigación "
        "Aplicada 2027-03, Avanzados I, la cartilla tiene seis criterios y la propuesta "
        "científico-tecnológica pesa 25 %.",
        "Evaluadores externos califican en modalidad simple ciego (el evaluador conoce al "
        "postulante y el postulante no conoce al evaluador). Un panel de selección de 4 a 6 "
        "investigadores elige después entre las propuestas aprobadas; entre sus criterios "
        "está la coherencia entre el TRL de entrada, las actividades, las evidencias y el TRL "
        "de salida (Anexo 9).",
        "Las propuestas aprobadas reciben un puntaje adicional no acumulable de 10 % en casos "
        "como una responsable técnica mujer o un responsable técnico menor de 35 años (Anexo 9).",
        "Dato: en una réplica experimental con 43 evaluadores y 25 propuestas presentadas a "
        "los Institutos Nacionales de Salud de los Estados Unidos (NIH), no hubo acuerdo entre "
        "evaluadores en las calificaciones ni en los comentarios (Pier et al., 2018).",
    ],
))

L.append(pasos(
    "orden-redaccion",
    "01 · Orden de redacción",
    "Orden de redacción de la propuesta y *criterio* de la cartilla que califica cada sección",
    [
        ("Problema", "Desafío que atiende, magnitud y justificación"),
        ("Objetivos", "General y específicos, con el TRL de salida"),
        ("Estado del arte", "Novedad frente a patentes y estudios"),
        ("Metodología", "Desarrollo y validación por objetivo"),
        ("Plan de trabajo", "Infraestructura, cronograma y riesgos"),
    ],
    clave=1,
    marcas=["III.a", "III.b", "II.a", "III.c", "IV"],
    fuente=CARTILLA + " · secuencia del docente",
    notas=[
        "El orden de redacción no sigue el orden del formulario. El problema y los "
        "objetivos van primero porque la cartilla califica la coherencia entre el problema, "
        "los objetivos, la justificación, la metodología y las actividades (subcriterio III.d).",
        "La marca de cada paso es el criterio o subcriterio de la cartilla de Desarrollo "
        "Tecnológico 2027 que califica esa sección. Los resultados (criterio V, 20 %) y la "
        "potencialidad de mercado (criterio VI, 15 %) se redactan al final, con el plan de "
        "trabajo cerrado. La coherencia entre problema, tipo de I+D, TRL y entidad postulante "
        "se presentó en la sesión 1.",
        "Las bases piden además analizar la relación entre los resultados esperados y los "
        "desafíos locales, regionales, sectoriales o nacionales que atiende el proyecto "
        "(num. 1.5).",
        "Las bases no publican el formulario completo. La cartilla remite a campos de "
        "postulación como «Proyecto», «Funciones del Equipo», «Entidades», «Cronograma de "
        "actividades» y «Niveles de Madurez Tecnológica y adjuntos».",
        "Error frecuente: redactar primero el resumen y el título. Ambos se ajustan cuando los "
        "objetivos y los resultados están cerrados.",
    ],
))

L.append(recursos(
    "recursos-propuesta",
    "01 · Recursos recomendados",
    "Recursos sobre la estructura y la evaluación de una propuesta de I+D",
    [
        {"tipo": "Guía", "titulo": "Guía práctica para la formulación y ejecución de proyectos de investigación y desarrollo (I+D)",
         "autor": "CONCYTEC, 2020",
         "detalle": "Estructura de un proyecto de I+D y aspectos que se evalúan",
         "url": "gob.pe · CONCYTEC, guía práctica I+D (2020)",
         "enlace": "https://www.gob.pe/institucion/concytec/informes-publicaciones/1323538-guia-practica-para-la-formulacion-y-ejecucion-de-proyecto-de-investigacion-y-desarrollo"},
        {"tipo": "Guía", "titulo": "EU Grants: Application form (HE RIA and IA), versión 5.1",
         "autor": "Comisión Europea, 2026",
         "detalle": "Formulario de Horizonte Europa con una sección por criterio de evaluación",
         "url": "ec.europa.eu · HE application form RIA/IA",
         "enlace": "https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/temp-form/af/af_he-ria-ia_en.pdf"},
        {"tipo": "Sitio web", "titulo": "How We Make Funding Decisions",
         "autor": "National Science Foundation, vigente en 2026",
         "detalle": "Revisión por mérito de la NSF y sus dos criterios",
         "url": "nsf.gov/funding/merit-review",
         "enlace": "https://www.nsf.gov/funding/merit-review"},
        {"tipo": "Artículo", "titulo": "Ten Simple Rules for Getting Grants",
         "autor": "Bourne y Chalupa, PLoS Computational Biology, 2006",
         "detalle": "Pautas para redactar una solicitud de financiamiento competitiva",
         "url": "doi.org/10.1371/journal.pcbi.0020012",
         "enlace": "https://doi.org/10.1371/journal.pcbi.0020012"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía del CONCYTEC (2020) describe la estructura de un proyecto de I+D y una tabla de aspectos que se evalúan; sirve para contrastar con la cartilla de Desarrollo Tecnológico. Es de 2020 y no reemplaza las bases 2027.",
        "El formulario de Horizonte Europa organiza la parte técnica en excelencia, impacto y calidad de la ejecución, con tablas de paquetes de trabajo, hitos y riesgos críticos.",
        "La página de la National Science Foundation (NSF) resume sus criterios de mérito intelectual e impactos amplios. Bourne y Chalupa (2006) es un editorial breve con pautas de redacción.",
    ],
))

# ---------- U2 · Diagnóstico del problema

L.append(pasos(
    "etapas-marco-logico",
    "01 · Metodología del marco lógico",
    "Etapas de diseño de un proyecto con la *metodología del marco lógico*",
    [
        ("Involucrados", "Intereses y posición de cada actor"),
        ("Árbol de problemas", "Problema central, causas y efectos"),
        ("Árbol de objetivos", "Medios y fines en estado positivo"),
        ("Alternativa", "Objetivos dentro y fuera del proyecto"),
        ("Estructura y matriz", "Fin, propósito, componentes y actividades"),
    ],
    clave=1,
    fuente="Ortegón, Pacheco y Prieto, Instituto Latinoamericano y del Caribe de Planificación "
           "Económica y Social (ILPES-CEPAL), 2005, pp. 15-22",
    notas=[
        "El manual del Instituto Latinoamericano y del Caribe de Planificación Económica y "
        "Social (ILPES), de la Comisión Económica para América Latina y el Caribe (CEPAL), "
        "distingue dos etapas. La identificación del problema y de las alternativas reúne "
        "cuatro análisis (involucrados, problemas, objetivos y estrategias); la planificación "
        "produce la estructura analítica del proyecto y la matriz (Ortegón, Pacheco y Prieto, 2005, pp. 15 y 19-21). El manual se presentó como "
        "recurso en la sesión 1.",
        "El mapa de involucrados reúne a todos los que participan o tienen que ver con el "
        "proyecto, con sus intereses y expectativas: personas, instituciones, empresas u "
        "organizaciones públicas y privadas (ILPES, 2005, p. 10).",
        "Las bases y cartillas 2027 de PROCIENCIA no mencionan el marco lógico ni el árbol de "
        "problemas; puntúan la coherencia entre problema, hipótesis, objetivos, metodología y "
        "actividades. La metodología del marco lógico se usa como herramienta de diseño que "
        "produce esas secciones.",
    ],
))

L.append(visual(
    "arbol-problemas",
    "01 · Árbol de problemas",
    "Árbol de problemas del uso de *mercurio* en la minería aurífera artesanal, ejemplo",
    arbol(
        "Recuperación de oro con mercurio en la minería artesanal amazónica",
        ["Amalgamación barata y fácil de operar",
         "Proceso sin mercurio no validado con mineral local",
         "Asistencia técnica y fiscalización limitadas"],
        ["Mercurio liberado al aire, el suelo y los ríos",
         "Mercurio en peces de consumo local",
         "Exposición de mineros y población ribereña"],
    ),
    fuente="Esquema según " + ILPES + ", p. 16 · DS 034-2016-PCM · ejemplo ilustrativo",
    notas=[
        "Se identifica el problema central, luego sus efectos y sus causas, y el árbol se "
        "revisa hasta que cada causa sea una causa, cada efecto un efecto y las relaciones "
        "causales estén bien expresadas (ILPES, 2005, p. 16).",
        "El ejemplo parte del proyecto de la UNI «Reactivando la Amazonía Peruana: "
        "recuperación eficiente y sostenible de oro mediante el proceso COA en la minería "
        "artesanal» (responsable técnica: Jessica Ivana Nieto Juárez), seleccionado en "
        "Desarrollo Tecnológico 2025-03 con S/ 350 000. El árbol es del docente y no "
        "reproduce la propuesta.",
        "Dato: el sustento del Ministerio de Salud para la declaratoria de emergencia de 2016 "
        "en Madre de Dios describe mercurio en el aire, el agua, los sedimentos y los peces, en "
        "especial en la mota punteada (_Calophysus macropterus_), parte de la dieta habitual de "
        "la población (DS 034-2016-PCM, considerandos).",
        "En el ejemplo, los involucrados son los mineros artesanales, la población ribereña "
        "que consume pescado, la autoridad regional de minería y los comercializadores de oro. "
        "Solo las causas que el proyecto puede atender pasan a componentes.",
        "Error frecuente: escribir como causa la ausencia de la solución («falta del proceso "
        "COA»). Esa redacción da por elegida la alternativa antes de analizarla.",
    ],
))

L.append(visual(
    "arbol-objetivos",
    "01 · Árbol de objetivos",
    "Árbol de objetivos de la recuperación de oro sin *mercurio*, ejemplo",
    arbol(
        "Recuperación de oro sin mercurio en la minería artesanal amazónica",
        ["Proceso sin mercurio de costo y operación competitivos",
         "Proceso sin mercurio validado con mineral local",
         "Asistencia técnica y fiscalización ampliadas"],
        ["Menos mercurio liberado al aire, el suelo y los ríos",
         "Menos mercurio en peces de consumo local",
         "Menor exposición de mineros y población ribereña"],
        modo="objetivos", supuestos=(2,),
    ),
    fuente="Esquema según " + ILPES + ", pp. 17-21 · ejemplo ilustrativo",
    notas=[
        "El árbol de objetivos convierte los estados negativos del árbol de problemas en "
        "estados positivos; las causas pasan a medios y los efectos, a fines (ILPES, 2005, "
        "p. 17). La lámina retoma el árbol de problemas anterior.",
        "El medio marcado como supuesto queda fuera del control del proyecto, porque la "
        "asistencia técnica y la fiscalización corresponden al Estado. El manual indica tratar "
        "esos elementos como supuestos de la matriz (p. 21, nota 7).",
        "La alternativa del proyecto es validar el proceso que su título denomina COA. Otras "
        "alternativas, como recuperar el mercurio con retortas, se comparan por costo, plazo y "
        "capacidad del equipo (p. 19).",
        "Verificar antes de la clase: el significado de la sigla COA, que no se confirmó en "
        "una fuente pública.",
    ],
))

L.append(cifra(
    "magnitud-problema",
    "01 · Magnitud del problema",
    "11", "distritos",
    "de Madre de Dios declarados en estado de emergencia por contaminación por mercurio, "
    "mayo de 2016",
    "Sustento del Ministerio de Salud: mercurio en ríos, peces y población por encima de los "
    "límites",
    fuente="DS 034-2016-PCM, _El Peruano_, 23 de mayo de 2016 · Ashe, _PLoS ONE_, 2012",
    notas=[
        "Dato: el decreto declaró la emergencia por 60 días en Tambopata, Inambari, Las Piedras "
        "y Laberinto (provincia de Tambopata); Fitzcarrald, Manu, Madre de Dios y Huepetuhe "
        "(Manu); e Iñapari, Iberia y Tahuamanu (Tahuamanu), por la contaminación asociada a la "
        "minería artesanal en Madre de Dios.",
        "Dato: en una muestra de 100 residentes de zonas mineras de Madre de Dios y 104 de "
        "Puerto Maldonado, el 11 % y el 5 %, respectivamente, tenían más de 6 µg de mercurio "
        "por gramo de cabello, umbral de niveles no saludables que el estudio toma de la OMS; "
        "entre quienes comían pescado más de 12 veces al mes, la proporción fue 18 % (Ashe, "
        "2012).",
        "La magnitud responde a lo que la cartilla busca en «antecedentes y justificación» "
        "(subcriterio III.a) y en la atención de desafíos locales, regionales o nacionales "
        "(subcriterio II.c).",
        "Implicación para el formulador: la cifra de magnitud lleva año, lugar, universo y "
        "fuente; un dato de 2012 o de 2016 se cita con su fecha y se actualiza antes de "
        "postular.",
        "Verificar antes de la clase: si la Dirección General de Salud Ambiental (DIGESA) o el "
        "Ministerio del Ambiente publicaron mediciones de mercurio en Madre de Dios posteriores "
        "a 2016.",
    ],
))

L.append(duo(
    "enunciado-problema",
    "01 · Enunciado del problema",
    "Enunciado difuso y acotado del *problema* del mercurio",
    {"cab": "Difuso", "t": "Contaminación por la minería en la Amazonía",
     "items": ["Sin población afectada ni lugar",
               "Sin magnitud ni periodo de referencia"]},
    {"cab": "Acotado", "t": "Exposición al mercurio en 11 distritos mineros de Madre de Dios",
     "items": ["Mercurio en ríos, peces y población (DS 034-2016-PCM)",
               "11 % en zonas mineras sobre 6 µg/g en cabello (Ashe, 2012)"]},
    fuente="DS 034-2016-PCM · Ashe, _PLoS ONE_, 7(3), e33305, 2012",
    notas=[
        "Un enunciado evaluable indica a quién afecta el problema, dónde, en qué magnitud y "
        "desde cuándo. El enunciado difuso no nombra población ni contaminante y no permite "
        "comprobar al cierre si el problema disminuyó.",
        "El problema se formula como exposición al mercurio usado para recuperar oro y no como "
        "minería ilegal en general, porque un proyecto de desarrollo tecnológico de "
        "S/ 350 000 actúa sobre el proceso de recuperación y no sobre la fiscalización.",
        "Error frecuente: un problema sin magnitud. Sin cifra ni fuente, el evaluador no puede "
        "calificar la relevancia (criterio II, 15 %) ni la justificación.",
    ],
))

L.append(recursos(
    "recursos-problema",
    "01 · Recursos recomendados",
    "Recursos sobre el diagnóstico del problema y el árbol de problemas",
    [
        {"tipo": "Guía", "titulo": "Formulación de programas con la metodología de marco lógico",
         "autor": "Aldunate y Córdoba, CEPAL-ILPES, 2011",
         "detalle": "Problema, árbol de causas y efectos y matriz aplicados a programas",
         "url": "hdl.handle.net/11362/5507",
         "enlace": "https://repositorio.cepal.org/handle/11362/5507"},
        {"tipo": "Guía", "titulo": "Guía general para la identificación, formulación y evaluación de proyectos de inversión",
         "autor": "MEF, 2024",
         "detalle": "Diagnóstico, problema central, causas y efectos en la inversión pública",
         "url": "mef.gob.pe · Guía general Invierte.pe 2024",
         "enlace": "https://www.mef.gob.pe/contenidos/inv_publica/docs/Metodologias_Generales_PI/GUIA_EX_ANTE_InviertePe.pdf"},
        {"tipo": "Guía", "titulo": "Aid Delivery Methods. Volume 1: Project Cycle Management Guidelines",
         "autor": "Comisión Europea, 2004",
         "detalle": "Análisis de involucrados, problemas y objetivos con el marco lógico",
         "url": "europa.eu · PCM Guidelines 2004",
         "enlace": "https://international-partnerships.ec.europa.eu/document/download/f7ed20c4-5fc2-4ed7-b54c-0805e4ed952d_en?filename=methodology-aid-delivery-methods-project-cycle-management-200403_en.pdf"},
        {"tipo": "Sitio web", "titulo": "draw.io (diagrams.net)",
         "autor": "JGraph, versión 32.4.1, 2026",
         "detalle": "Editor de diagramas en línea y de escritorio, sin registro",
         "url": "drawio.com",
         "enlace": "https://www.drawio.com/"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "Aldunate y Córdoba (2011) dedican el capítulo 4 a acotar el problema y construir el árbol; es distinto del manual de 2005, recurso de la sesión 1.",
        "La guía del Ministerio de Economía y Finanzas (MEF) aplica el diagnóstico, el árbol de causas y efectos y la matriz de marco lógico a la inversión pública peruana (cap. 1 y § 3.6).",
        "La guía de la Comisión Europea incluye una matriz de involucrados (§ 5.2). draw.io es un editor de diagramas gratuito para dibujar y versionar los árboles.",
    ],
))

# ---------- U3 · Objetivos y estado del arte

L.append(visual(
    "objetivo-smart",
    "01 · Objetivos verificables",
    "Criterios de un objetivo verificable: sigla *SMART* de Doran, 1981",
    criterios_svg([
        ("Específico", "Área o resultado concreto que se busca mejorar"),
        ("Medible", "Indicador o cantidad que muestra el avance"),
        ("Asignable", "Responsable identificado en el equipo"),
        ("Realista", "Alcanzable con los recursos y el plazo disponibles"),
        ("Temporal", "Fecha o plazo en que se espera el resultado"),
    ]).replace("Actividad de I+D", "Objetivo verificable"),
    fuente="Doran, _Management Review_, 70(11), 1981",
    notas=[
        "La sigla SMART procede de un artículo de George T. Doran (1981) y reúne las iniciales "
        "en inglés de los cinco criterios (_specific, measurable, assignable, realistic, "
        "time-related_). Versiones posteriores sustituyen «asignable» por «alcanzable» y "
        "«realista» por «pertinente».",
        "En el marco lógico los objetivos se redactan como logros y no como tareas: "
        "«aeropuerto construido» y no «construir un aeropuerto» (ILPES, 2005, p. 28). En la "
        "propuesta de PROCIENCIA se escriben en infinitivo, y cada verbo nombra un resultado "
        "comprobable.",
        "El objetivo general describe el cambio que busca el proyecto; cada objetivo "
        "específico, un resultado parcial que contribuye a él.",
        "Error frecuente: objetivos con «mejorar» o «fortalecer» sin condición de logro. Al "
        "cierre no hay forma de verificar si se cumplieron.",
        "Verificar antes de la clase: la cita de Doran (1981) se confirmó en fuentes "
        "secundarias; el artículo original no se consultó.",
    ],
))

L.append(tarjetas(
    "objetivos-caso",
    "01 · Objetivos del caso",
    "Objetivo general y objetivos específicos del caso de *tala ilegal*, ejemplo",
    [
        ("Objetivo general", "Validar en un bosque amazónico un sistema acústico con IA en el "
                             "borde que alerta la tala (TRL 6)"),
        ("Específico 1 · OE1", "Obtener un clasificador de sonidos de motosierra y maquinaria "
                               "que opere en el nodo"),
        ("Específico 2 · OE2", "Integrar nodos de campo que envíen alertas con la hora y la "
                               "ubicación del evento"),
        ("Específico 3 · OE3", "Validar el sistema con OSINFOR en parcelas forestales "
                               "supervisadas"),
    ],
    clave=0,
    iconos=["target", "search", "robot", "check"],
    fuente="Objetivos ilustrativos redactados a partir del título del proyecto · " + CARTILLA +
           ", subcriterio III.b",
    notas=[
        "La cartilla pregunta si los objetivos están claramente definidos y son posibles de "
        "lograr con las actividades y la metodología, y si las actividades se relacionan con "
        "los objetivos (subcriterio III.b). La cartilla de Desarrollo Tecnológico no pide "
        "hipótesis; la de Investigación Aplicada sí.",
        "Los objetivos de la lámina son del docente; los de la propuesta real no son públicos. "
        "El TRL 6 corresponde a la salida que exigían las bases 2026 del concurso que ganó el "
        "proyecto.",
        "OE1 a OE3 son los objetivos específicos; cada uno produce un componente y un "
        "entregable con su informe de pruebas.",
        "Error frecuente: un objetivo específico con un verbo de proceso, como «realizar» o "
        "«aplicar», sin el producto que lo comprueba. Como componente de una matriz, OE1 se "
        "reescribe como «clasificador de sonidos validado en el nodo».",
    ],
))

L.append(pasos(
    "busqueda-declarada",
    "01 · Estado del arte",
    "Etapas de una búsqueda declarada de antecedentes según *PRISMA 2020*",
    [
        ("Identificación", "57 artículos en OpenAlex con la cadena del caso, 14-10-2026"),
        ("Cribado de registros", "Título y resumen frente a criterios de inclusión"),
        ("Cribado de informes", "Texto completo y motivo de cada exclusión"),
        ("Incluidos", "Estudios que sostienen los antecedentes"),
    ],
    clave=0,
    fuente="Page et al., _BMJ_, 2021, PRISMA 2020 (_Preferred Reporting Items for Systematic "
           "reviews and Meta-Analyses_) · OpenAlex, consulta del 14 de octubre de 2026",
    notas=[
        "PRISMA 2020 (_Preferred Reporting Items for Systematic reviews and Meta-Analyses_) es "
        "una guía para informar revisiones sistemáticas, con una lista de 27 ítems y "
        "diagramas de flujo (Page et al., 2021). Una propuesta no exige una revisión "
        "sistemática; toma de PRISMA la práctica de declarar dónde, cuándo y con qué cadena se "
        "buscó.",
        "El diagrama de PRISMA 2020 tiene tres fases: identificación, cribado e incluidos. El "
        "cribado comprende la revisión de registros por título y resumen y la evaluación de "
        "los informes completos; la elegibilidad como fase aparte corresponde a la versión de "
        "2009.",
        "Dato: la cadena («illegal logging» OR chainsaw) AND (acoustic OR sound OR audio) AND "
        "(detection OR classification), en título o resumen y limitada a artículos, devolvió "
        "57 registros en OpenAlex; al añadir edge, embedded o microcontroller, 20; al añadir "
        "Amazon o Peru, 3 (consulta del 14 de octubre de 2026). OpenAlex es un índice abierto "
        "de publicaciones científicas.",
        "Entre los 57 registros hay trabajos ajenos al tema, como la reseña de un libro de "
        "poemas de 1995 y un artículo sobre igualdad de género en la India. El cribado por "
        "título y resumen los excluye, y el diagrama declara cuántos registros salen en cada "
        "fase.",
        "La cartilla pide antecedentes «respaldados con estudios revisados por pares, estudios "
        "reconocidos, recientes, resultados preliminares» (subcriterio III.a). Las bases "
        "exigen además el análisis de la novedad frente a patentes, modelos de utilidad, "
        "registros de software y publicaciones (num. 1.5), tema de la sesión 1.",
        "Error frecuente: afirmar que «no existen antecedentes» sin declarar la búsqueda. El "
        "evaluador no puede comprobarlo.",
    ],
))

L.append(visual(
    "literatura-del-campo",
    "01 · Literatura del campo",
    "Artículos sobre detección acústica de la *tala ilegal* por bienio de publicación, "
    "2014-2025",
    barras_valor([
        ("2014-2015", 2, ""),
        ("2016-2017", 3, ""),
        ("2018-2019", 4, ""),
        ("2020-2021", 6, ""),
        ("2022-2023", 7, ""),
        ("2024-2025", 17, "clave"),
    ], maximo=20, paso=5, menor=1, decimales=0, xb=360,
        unidad="ARTÍCULOS · CADENA DECLARADA, EN TÍTULO O RESUMEN"),
    fuente="OpenAlex, consulta del 14 de octubre de 2026, cálculo propio",
    notas=[
        "Dato: la consulta devolvió 57 artículos: 39 de 2014 a 2025, 7 anteriores y 11 de "
        "2026, contados al 14 de octubre. El bienio 2024-2025 reúne 17 de los 39 artículos de "
        "2014-2025.",
        "Con un campo de este tamaño, la propuesta puede leer los textos completos y declarar "
        "cuáles descarta y por qué. En un campo con cientos de artículos al año, la cadena se "
        "acota con términos del problema.",
        "Los conteos cambian con la cadena, los campos consultados y la fecha. Scopus y Web of "
        "Science, bases de suscripción, darán cifras distintas.",
        "VOSviewer, en los recursos de esta unidad, construye mapas de coocurrencia de "
        "términos a partir de OpenAlex.",
    ],
))

L.append(tarjetas(
    "diferenciacion-tecnica",
    "01 · Diferenciación técnica",
    "Atributos de la alerta satelital, de los nodos acústicos publicados y del *sistema* del "
    "caso",
    [
        ("Alerta satelital GLAD", "Imágenes ópticas Landsat; registra el dosel ya removido; "
                                  "sin datos bajo nubes"),
        ("Nodos acústicos publicados", "20 de 57 artículos citan edge, embedded o "
                                       "microcontroller; 3, Amazon o Peru"),
        ("Sistema del caso", "Alerta durante el corte; validación en la Amazonía con el "
                             "usuario, OSINFOR"),
    ],
    clave=2,
    iconos=["chart", "book", "target"],
    fuente="PNCBMCC-MINAM y GRAM Loreto, reporte de alerta temprana, febrero de 2023 · "
           "OpenAlex, 14 de octubre de 2026 · Andina, 2026",
    notas=[
        "Dato: las alertas tempranas de pérdida de bosque que difunde Geobosques provienen del "
        "laboratorio GLAD de la Universidad de Maryland y usan imágenes ópticas Landsat 7 y 8. "
        "Tienen áreas sin información por nubes y una cobertura potencial de 8 días; con "
        "nubosidad, una alerta puede corresponder a una pérdida de semanas antes. Una alerta "
        "indica que un píxel registró una remoción del dosel mayor al 50 %, sin distinguir "
        "causas naturales de humanas (reporte del Programa Nacional de Conservación de Bosques, "
        "PNCBMCC, y la Gerencia Regional del Ambiente de Loreto, febrero de 2023).",
        "La cartilla de Desarrollo Tecnológico pregunta si el proyecto aporta novedad frente a "
        "patentes, modelos de utilidad, registros de software y publicaciones, y si describe "
        "los atributos que justifican su novedad o valor diferencial (subcriterio II.a). En el "
        "caso, el nodo acústico ya aparece en la literatura; el atributo diferencial es la "
        "alerta durante el corte, validada en un bosque amazónico con el usuario.",
        "Implicación para el formulador: la diferenciación se escribe con atributos medibles "
        "(tiempo hasta la alerta, cobertura por nodo, costo, falsas alarmas) y con la fuente "
        "de cada uno.",
        "Verificar antes de la clase: el contenido de los 20 artículos, que no se leyeron "
        "completos; la tarjeta solo informa qué términos contienen.",
    ],
))

L.append(recursos(
    "recursos-objetivos",
    "01 · Recursos recomendados",
    "Recursos sobre búsqueda de antecedentes y estado del arte",
    [
        {"tipo": "Artículo", "titulo": "PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews",
         "autor": "Rethlefsen et al., Systematic Reviews, 2021",
         "detalle": "Lista de 16 ítems para informar una búsqueda bibliográfica reproducible",
         "url": "doi.org/10.1186/s13643-020-01542-z",
         "enlace": "https://doi.org/10.1186/s13643-020-01542-z"},
        {"tipo": "Base de datos", "titulo": "The Lens",
         "autor": "The Lens, actualización continua",
         "detalle": "Literatura científica y patentes enlazadas en una misma búsqueda",
         "url": "lens.org",
         "enlace": "https://www.lens.org/"},
        {"tipo": "Sitio web", "titulo": "VOSviewer 1.6.21 y manual",
         "autor": "Van Eck y Waltman, CWTS, Universidad de Leiden, 2026",
         "detalle": "Mapas de coocurrencia de términos y de coautoría",
         "url": "vosviewer.com",
         "enlace": "https://www.vosviewer.com/"},
        {"tipo": "Base de datos", "titulo": "LA Referencia: Red Latinoamericana y Española de Ciencia Abierta",
         "autor": "LA Referencia, actualización continua",
         "detalle": "Tesis y artículos de repositorios latinoamericanos en acceso abierto",
         "url": "buscador.lareferencia.info",
         "enlace": "https://buscador.lareferencia.info/"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "PRISMA-S es la extensión de PRISMA 2020 dedicada a la búsqueda: bases, cadenas completas, filtros y fechas.",
        "The Lens enlaza artículos y patentes y permite ver qué patentes citan un artículo; complementa la diferenciación técnica. VOSviewer consulta OpenAlex directamente; el sitio informó de un ejecutable alterado el 31 de agosto de 2026, por lo que conviene descargarlo solo del sitio oficial.",
        "LA Referencia agrega los repositorios nacionales de la región, entre ellos los del Perú; sirve para hallar tesis y artículos de la región, como estudios sobre la tala o la minería en la Amazonía.",
    ],
))

L.append(cierre(
    "sintesis-01",
    "01 · Síntesis",
    "Problema y *objetivos* de la propuesta",
    [
        "Cartilla: siete criterios, con 15 % para el potencial de mercado",
        "Problema: afectados, magnitud con fuente y causas",
        "Objetivo: logro verificable con TRL de salida",
        "Antecedentes: búsqueda declarada",
    ],
    ("Receso", "10 minutos · Tema 02: marco lógico, plan de trabajo y equipo del proyecto"),
    notas=[
        "Recapitular el criterio de cada término del tema 01 antes del receso de 10 minutos.",
        "Dato: 11 distritos de Madre de Dios fueron declarados en emergencia por contaminación "
        "por mercurio en mayo de 2016 (DS 034-2016-PCM).",
    ],
))

# ============== TEMA 02 · MARCO LÓGICO, PLAN DE TRABAJO Y EQUIPO DEL PROYECTO

L.append(seccion(
    "tema-02", "02", "Marco lógico, plan de trabajo y equipo del proyecto",
    "Matriz e indicadores de cada objetivo, cadena de resultados, cronograma con hitos y "
    "entidades que se comprometen",
    notas=[
        "Mantener esta lámina en pantalla durante el receso.",
        "Presentar el tema 02, que trata cómo se comprobará el logro de los objetivos, en qué "
        "plazo y con qué equipo y entidades.",
        "Tiempo: 77 minutos; presentación del tema, 1; matriz e indicadores, 29; cadena de "
        "resultados y teoría del cambio, 19; plan de trabajo, equipo y acuerdos, 25; síntesis, 3.",
    ],
))

# ---------- U4 · Matriz de marco lógico e indicadores

L.append(visual(
    "matriz-marco-logico",
    "02 · Matriz de marco lógico",
    "Matriz de marco lógico de un proyecto de potabilización de agua con *arsénico*, ejemplo",
    matriz_ml([
        ("Fin", "Menor exposición al arsénico en familias con agua de pozo",
         "Familias que beben agua dentro de los límites",
         "Vigilancia sanitaria de la autoridad de salud",
         "Mantenimiento de la planta tras el proyecto"),
        ("Propósito", "Agua potable de pozo en uso por una comunidad de la selva",
         "Agua tratada dentro del DS 031-2010-SA al mes 24",
         "Informes de ensayo de un laboratorio acreditado",
         "Familias que dejan el agua sin tratar"),
        ("Componentes", "Planta solar con operación remota",
         "Planta piloto en operación en un pozo al mes 20",
         "Informe de pruebas y acta de entrega",
         "Operación y cuidado de la planta por la comunidad"),
        ("Actividades", "Diagnóstico del agua, diseño, instalación y capacitación",
         "Presupuesto por componente", "Registros contables e informes de hito",
         "Acceso al pozo y llegada de equipos en el plazo"),
    ], resaltar=2),
    fuente="Esquema según ILPES-CEPAL, 2005, pp. 21-27 · DS 031-2010-SA · ejemplo ilustrativo",
    notas=[
        "El ejemplo parte del proyecto de la UNI «Sistema automatizado remoto alimentado por "
        "energía solar para potabilizar aguas subterráneas con arsénico, manganeso, aluminio y "
        "bacterias en comunidades de la selva» (responsable técnico: Edward Arsenio Carpio "
        "Deza), seleccionado en Desarrollo Tecnológico 2024-02 con S/ 350 000. La matriz es "
        "del docente y no reproduce la propuesta.",
        "La matriz resume qué hará el proyecto, cómo se medirá cada nivel y de qué factores "
        "externos depende. El fin es el objetivo superior al que el proyecto contribuye sin "
        "bastar por sí solo; el propósito, el efecto directo al final de la ejecución; los "
        "componentes, los resultados que entrega el equipo; y las actividades, las acciones "
        "que los producen (ILPES, 2005, pp. 23-24). El propósito depende también de que las "
        "familias usen el agua tratada.",
        "Cada supuesto va en la fila desde la que se pasa al nivel siguiente: el acceso al "
        "pozo y la llegada de los equipos condicionan que las actividades produzcan los "
        "componentes (p. 27). La fila resaltada, los componentes, es el nivel del que responde "
        "el equipo (p. 24).",
        "En el manual del ILPES, el indicador de las actividades es el presupuesto de las "
        "actividades de cada componente (p. 26); el presupuesto por partidas se calcula en la "
        "sesión 5.",
        "Las bases 2027 de PROCIENCIA no piden la matriz en la postulación. El plan operativo "
        "del proyecto (POP), que se aprueba al iniciar la ejecución, registra indicadores de "
        "propósito, de gestión y de hito con sus medios de verificación (guía de soporte, "
        "seguimiento y evaluación 2027). La matriz anticipa esos indicadores.",
        "Los límites del indicador de propósito vienen del reglamento de calidad del agua "
        "(lámina «Meta del indicador»); los meses son ilustrativos.",
    ],
))

L.append(duo(
    "logica-vertical-horizontal",
    "02 · Lógica de la matriz",
    "Lógica vertical y lógica horizontal de la *matriz* de marco lógico",
    {"cab": "Vertical", "t": "Relación causal de abajo arriba",
     "items": ["Actividades y supuestos producen los componentes",
               "Componentes y supuestos logran el propósito, que contribuye al fin"]},
    {"cab": "Horizontal", "t": "Objetivo, indicador y medio de verificación",
     "items": ["Medios necesarios y suficientes para calcular cada indicador",
               "Indicadores que permiten evaluar el logro de cada objetivo"]},
    fuente=ILPES + ", pp. 24 y 26-27",
    notas=[
        "La lógica vertical se lee como una cadena de condiciones. Si se ejecutan las "
        "actividades y se cumplen ciertos supuestos, se producen los componentes; si se "
        "producen los componentes y se cumplen otros supuestos, se logra el propósito (ILPES, "
        "2005, p. 27).",
        "El medio de verificación indica dónde el ejecutor o el evaluador obtienen el dato del "
        "indicador. Si la fuente no existe, recogerla pasa a ser una actividad del proyecto "
        "(p. 26); su costo se calcula en la sesión 5.",
        "Aplicado a la matriz de la lámina anterior, el medio de verificación del indicador "
        "de propósito es el informe de ensayo de un laboratorio acreditado con las "
        "concentraciones del agua tratada.",
        "Error frecuente: un indicador cuyo medio de verificación no existe o no tiene "
        "responsable.",
    ],
))

L.append(cifra(
    "meta-desempeno",
    "02 · Meta del indicador",
    "0,010", "mg/L",
    "límite máximo permisible de arsénico en el agua para consumo humano en el Perú",
    "Mismo valor que la guía de la OMS (10 µg/L) · meta del propósito en la matriz de "
    "potabilización",
    fuente="DS 031-2010-SA, Reglamento de la calidad del agua para consumo humano, anexo III "
           "· OMS, nota descriptiva sobre el arsénico, 2022",
    notas=[
        "El límite máximo permisible es la concentración que el agua para consumo humano no "
        "debe superar. El mismo reglamento fija 0,4 mg/L para el manganeso y 0,2 mg/L para el "
        "aluminio (anexo II) y 0 UFC/100 mL para las bacterias coliformes totales y "
        "termotolerantes (anexo I): son las metas de los otros contaminantes que nombra el "
        "título del proyecto.",
        "Dato: la disposición octava del reglamento permite a la autoridad de salud admitir "
        "hasta 0,05 mg/L de arsénico en el agua tratada de fuentes con características "
        "hidrogeológicas naturales, siempre que no afecte la salud. La OMS califica su valor de "
        "10 µg/L como provisional.",
        "Implicación para el formulador: la meta del indicador toma su valor de una norma "
        "externa y no de una cifra fijada por el equipo, y el evaluador puede comprobarla.",
        "La línea de base es la concentración del agua cruda del pozo, medida antes de "
        "instalar la planta; el indicador mide el cambio entre esa línea y el agua tratada.",
    ],
))

L.append(tarjetas(
    "indicador-caso",
    "02 · Indicador del caso",
    "Partes del indicador de *calidad del agua tratada* en el proyecto de potabilización",
    [
        ("Cantidad", "Litros diarios de agua tratada para las familias de la comunidad"),
        ("Calidad", "Arsénico de 0,010 mg/L o menos; manganeso, aluminio y coliformes en sus "
                    "límites"),
        ("Tiempo", "Al mes 24, con muestreo mensual desde el mes 20"),
        ("Lugar", "Pozo de una comunidad de la selva"),
        ("Línea de base", "Concentraciones del agua cruda del pozo, medidas antes de la "
                          "instalación"),
    ],
    clave=1,
    iconos=["users", "target", "calendar", "building", "chart"],
    fuente=ILPES + ", pp. 25, 30 y 35 · DS 031-2010-SA · metas ilustrativas",
    notas=[
        "El manual del ILPES pide especificar cada indicador en cantidad, calidad y tiempo "
        "(p. 25), identificar el grupo meta y el lugar (p. 30) y establecer la línea de base "
        "contra la que se medirán las metas (p. 35). La lámina retoma la matriz de "
        "potabilización.",
        "El medio de verificación de este indicador es el informe de ensayo de un laboratorio "
        "acreditado, con muestras del agua cruda y de la tratada.",
        "Error frecuente: un indicador sin línea de base, que mide un estado y no un cambio "
        "atribuible al proyecto.",
        "Los meses y la comunidad son ilustrativos.",
    ],
))

L.append(visual(
    "supuestos-riesgos",
    "02 · Supuestos y riesgos",
    "*Supuestos* de la planta potabilizadora según importancia y probabilidad",
    matriz_riesgo(
        ["Alta, más de 90 %", "Media, 10 a 90 %", "Baja, menos de 10 %"],
        ["Alta", "Baja"],
        [
            (0, 0, 0, "Hecho previsto, no es supuesto", "hecho"),
            (0, 1, 1, "Supuesto en la matriz", "clave"),
            (0, 2, 2, "Rediseño; si no es posible, supuesto fatal", "fatal"),
            (1, 0, 2, "No se incluye en la matriz", "tenue"),
        ],
        [
            (1, "Acceso al pozo concedido por la comunidad durante la instalación", 0, 1),
            (2, "Llegada de los equipos importados en el plazo", 0, 1),
            (3, "Arsénico del pozo dentro del rango medido en el diagnóstico", 0, 0),
            (4, "Continuidad de las autoridades comunales", 1, 1),
        ],
        "Probabilidad de que se cumpla la condición",
        "Importancia",
    ),
    fuente=ILPES + ", pp. 27 y 42-44 · ejemplo ilustrativo",
    notas=[
        "Un supuesto es un factor externo, fuera del control de la gerencia del proyecto, que "
        "debe cumplirse para pasar al nivel siguiente de la matriz (ILPES, 2005, p. 27). El "
        "manual lo verifica con cuatro preguntas: si es externo, si es importante, cuál es su "
        "probabilidad de ocurrencia y si el proyecto puede rediseñarse (pp. 43-44).",
        "Un factor con probabilidad muy alta es un hecho y no un supuesto; uno con "
        "probabilidad media (10 % a 90 %) se escribe en la matriz; uno importante con "
        "probabilidad muy baja obliga a rediseñar el proyecto, y si el rediseño no es "
        "posible es un supuesto fatal y el proyecto se detiene (p. 44).",
        "Los riesgos que el equipo controla, como el retraso de un tesista o un error en el "
        "diseño de un ensayo, no son supuestos y se gestionan con una estrategia propia. La "
        "cartilla los califica en «limitaciones y riesgos» (subcriterio IV.c) y pregunta si "
        "se describe la estrategia frente a cada uno.",
        "Para el factor 1, una estrategia es acordar por escrito el acceso con la comunidad y "
        "prever un segundo pozo con agua de composición similar.",
        "Error frecuente: escribir como supuesto un factor bajo control del equipo, como la "
        "buena coordinación entre los ejecutores (ILPES, 2005, p. 43).",
    ],
))

L.append(recursos(
    "recursos-matriz",
    "02 · Recursos recomendados",
    "Recursos sobre matriz de marco lógico, indicadores y metas",
    [
        {"tipo": "Libro", "titulo": "Diez pasos hacia un sistema de seguimiento y evaluación basado en resultados",
         "autor": "Kusek y Rist, Banco Mundial, 2005",
         "detalle": "Selección de indicadores, línea de base y metas de desempeño",
         "url": "hdl.handle.net/10986/14926",
         "enlace": "https://openknowledge.worldbank.org/server/api/core/bitstreams/daa5137c-ebfe-5c9c-a547-ee1d53f9cac8/content"},
        {"tipo": "Guía", "titulo": "Indicadores de desempeño en el sector público",
         "autor": "Bonnefoy y Armijo, CEPAL-ILPES, 2005",
         "detalle": "Tipos de indicadores, requisitos de las metas y pasos para construirlos",
         "url": "hdl.handle.net/11362/5611",
         "enlace": "https://repositorio.cepal.org/handle/11362/5611"},
        {"tipo": "Guía", "titulo": "Manual de planificación, seguimiento y evaluación de los resultados de desarrollo",
         "autor": "PNUD, 2009",
         "detalle": "Indicadores, líneas de base, metas y medios de verificación",
         "url": "undp.org · Manual PSE de resultados (2009)",
         "enlace": "http://web.undp.org/evaluation/handbook/spanish/documents/manual_completo.pdf"},
        {"tipo": "Guía", "titulo": "Planificación estratégica e indicadores de desempeño en el sector público",
         "autor": "Armijo, CEPAL-ILPES, 2011",
         "detalle": "Tipos de indicadores de desempeño y su construcción",
         "url": "hdl.handle.net/11362/5509",
         "enlace": "https://repositorio.cepal.org/handle/11362/5509"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "Kusek y Rist (2005) desarrollan en los pasos 3 a 5 la elección de indicadores, la línea de base y las metas. Bonnefoy y Armijo (2005) comparan metas ambiguas y metas adecuadas (recuadro 14).",
        "El manual del Programa de las Naciones Unidas para el Desarrollo (PNUD) ordena indicadores de impacto, efecto y producto con su línea de base y medio de verificación; el servidor responde solo por http.",
        "Armijo (2011), Serie Manuales 69 de la CEPAL, dedica el capítulo VII a los indicadores de desempeño: tipos según la etapa del proceso (insumos, procesos, productos y resultados) y según el desempeño (eficacia, eficiencia, economía y calidad).",
    ],
))

# ---------- U5 · Cadena de resultados y teoría del cambio

L.append(pasos(
    "cadena-resultados",
    "02 · Cadena de resultados",
    "Cadena de resultados de un inventario urbano para la *gestión del riesgo*",
    [
        ("Insumos", "Equipo, imágenes y S/ 500 000"),
        ("Actividades", "Etiquetado de imágenes y entrenamiento del modelo"),
        ("Productos", "Modelo de visión e inventario piloto"),
        ("Efectos", "Uso del inventario por una municipalidad"),
        ("Impacto", "Menores pérdidas por sismo en el distrito"),
    ],
    clave=3,
    fuente="OCDE-CAD, _Glosario de los principales términos sobre evaluación_, 2002 · "
           "PROCIENCIA, Investigación Aplicada 2025-02 · ejemplo ilustrativo",
    notas=[
        "El glosario del Comité de Ayuda al Desarrollo (CAD) de la Organización para la "
        "Cooperación y el Desarrollo Económicos (OCDE) define los productos "
        "como «los productos, los bienes de capital y los servicios que resultan de una "
        "intervención»; los efectos, como «el conjunto de resultados a corto y mediano plazo "
        "probables o logrados por los productos»; y el impacto, como los efectos de largo "
        "plazo, positivos y negativos, producidos directa o indirectamente por la "
        "intervención. Las definiciones se citan según el anexo de marco lógico de la "
        "Comisión Europea (2021).",
        "El ejemplo parte del proyecto de la UNI «Inventarios urbanos multifinalitarios para "
        "la gestión del riesgo de desastres con IA y visión por computadora» (responsable "
        "técnico: Miguel Luis Estrada Mendoza), seleccionado en Investigación Aplicada 2025-02 "
        "con S/ 500 000. Los eslabones son del docente.",
        "En inglés los tres niveles se nombran _output_, _outcome_ e _impact_. El proyecto "
        "responde por los productos y busca los efectos; el impacto depende también de otros "
        "actores.",
        "Dato: en Desarrollo Tecnológico 2027-02, los resultados exigidos incluyen un "
        "resultado tecnológico validado en TRL 5 o más con su informe de pruebas y "
        "validación, una actividad de validación con usuarios o adoptantes, un paquete "
        "tecnológico, un reporte de viabilidad de patente, un plan de uso, transferencia o "
        "adopción, una ficha tecnológica y un plan de escalamiento; la tesis de posgrado es "
        "opcional (bases, tabla 2).",
        "La cartilla pregunta además cómo la participación de los adoptantes o usuarios "
        "finales fortalecerá el impacto de la tecnología (subcriterio V.b) y si la "
        "colaboración entre entidades llevará a acciones conjuntas para su uso (V.c). En el "
        "ejemplo, el adoptante es una municipalidad y la estrategia, un inventario piloto de "
        "un distrito.",
        "Error frecuente: prometer impacto con el presupuesto y el plazo de un proyecto que "
        "entrega productos.",
    ],
))

L.append(duo(
    "marco-logico-y-teoria-del-cambio",
    "02 · Teoría del cambio",
    "Marco lógico y *teoría del cambio* en el diseño de un proyecto",
    {"cab": "Marco lógico", "t": "Jerarquía de objetivos con indicadores",
     "items": ["Cadena lineal de insumos, productos y efectos",
               "Supone un avance previsible del proyecto"]},
    {"cab": "Teoría del cambio", "t": "Secuencia de eventos hacia los efectos de largo plazo",
     "items": ["Condiciones y supuestos explícitos de cada paso",
               "Revisión periódica durante la ejecución"]},
    fuente="Maini, Mounier-Jack y Borghi, _BMJ Global Health_, 2018 · Maru et al., "
           "_Agricultural Systems_, 2018",
    notas=[
        "Maini, Mounier-Jack y Borghi (2018) describen la teoría del cambio como la "
        "articulación del proceso de cambio de una intervención y de la secuencia de eventos "
        "que vincula sus actividades con los efectos de largo plazo, con las condiciones y los "
        "supuestos explícitos. Los marcos lógicos y los modelos lógicos tienden a ser más "
        "rígidos y lineales, y la teoría del cambio se modifica durante la evaluación.",
        "Maru et al. (2018, p. 349) recogen de otros autores que el marco lógico puede "
        "inculcar una creencia equivocada en la previsibilidad y el control de un proyecto, y "
        "que maneja mal el avance lento o negativo de las etapas tempranas.",
        "La teoría del cambio explica por qué un "
        "eslabón debería llevar al siguiente y la matriz fija qué se medirá. La cartilla de "
        "PROCIENCIA pregunta cómo y dónde se aplicarán los resultados y qué actores los "
        "adoptarán (criterio V, 20 %).",
        "Error frecuente: redactar la teoría del cambio una vez y no revisarla. Maru et al. "
        "citan a Cracknell (1989), quien advirtió que el marco lógico podía convertirse en "
        "«otra pieza de burocracia» si no se aplicaba con criterio.",
    ],
))

L.append(duo(
    "okr-moscow",
    "02 · Gestión interna del equipo",
    "Objetivos y resultados clave (*OKR*) y priorización MoSCoW de requisitos",
    {"cab": "OKR", "t": "Objetivo del equipo y resultados medibles",
     "items": ["Objetivo del trimestre: prototipo integrado y probado en laboratorio",
               "Resultados clave: 30 ensayos completos, informe de pruebas y manual de "
               "operación"]},
    {"cab": "MoSCoW", "t": "Prioridad de los requisitos del prototipo",
     "items": ["Debe tener operación autónoma; debería tener registro local de datos",
               "Podría tener pantalla; no tendrá aplicación móvil en este proyecto"]},
    fuente="Doerr, _Measure What Matters_, 2018 · Agile Business Consortium, DSDM, "
           "_MoSCoW Prioritisation_ · ejemplo ilustrativo",
    notas=[
        "Doerr (2018) define el objetivo como lo que se quiere lograr y los resultados clave "
        "como la forma de comprobar el avance hacia él; los resultados clave son específicos, "
        "tienen plazo y son medibles y verificables.",
        "MoSCoW reúne las iniciales en inglés de cuatro categorías: _must have_ (debe tener), "
        "_should have_ (debería tener), _could have_ (podría tener) y _won't have this time_ "
        "(no tendrá en este plazo). El método de desarrollo de sistemas dinámicos (DSDM, "
        "_Dynamic Systems Development Method_) recomienda que los requisitos «debe tener» no "
        "superen el 60 % del esfuerzo.",
        "Las dos herramientas organizan el trabajo interno del equipo; no reemplazan los "
        "indicadores de la matriz ni los del plan operativo de PROCIENCIA.",
        "Los ejemplos son ilustrativos y no corresponden a un proyecto real.",
    ],
))

L.append(recursos(
    "recursos-resultados",
    "02 · Recursos recomendados",
    "Recursos sobre cadena de resultados y teoría del cambio",
    [
        {"tipo": "Libro", "titulo": "La evaluación de impacto en la práctica, segunda edición",
         "autor": "Gertler et al., BID y Banco Mundial, 2017",
         "detalle": "Teoría del cambio, cadena de resultados y evaluación de impacto",
         "url": "doi.org/10.1596/978-1-4648-0888-3",
         "enlace": "https://openknowledge.worldbank.org/server/api/core/bitstreams/6f2eebf7-1a3c-5f67-a9c3-c39f68299ed9/content"},
        {"tipo": "Guía", "titulo": "Logic Model Development Guide",
         "autor": "W. K. Kellogg Foundation, 2004",
         "detalle": "Construcción de modelos lógicos con ejercicios y plantillas",
         "url": "wkkf.issuelab.org · Logic Model Guide",
         "enlace": "https://wkkf.issuelab.org/resource/logic-model-development-guide.html"},
        {"tipo": "Guía", "titulo": "Theory of Change. UNDAF Companion Guidance",
         "autor": "UNSDG, 2017",
         "detalle": "Pasos para formular una teoría del cambio con supuestos y riesgos",
         "url": "unsdg.un.org · Theory of Change guidance",
         "enlace": "https://unsdg.un.org/resources/theory-change-undaf-companion-guidance"},
        {"tipo": "Guía", "titulo": "Teoría de cambio. Un enfoque de pensamiento-acción para navegar en la complejidad de los procesos de cambio social",
         "autor": "Retolaza, PNUD e Hivos, 2010",
         "detalle": "Cambio deseado, actores, supuestos y ruta de cambio",
         "url": "hegoa.ehu.eus · Retolaza, Teoría de cambio",
         "enlace": "https://biblioteca.hegoa.ehu.eus/downloads/19844/%2Fsystem%2Fpdf%2F3487%2FTeoria_del_cambio.pdf"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "Gertler et al. (2017) explican en el capítulo 2 cómo construir una teoría del cambio y una cadena de resultados antes de evaluar el impacto.",
        "La guía de la Fundación Kellogg (2004) incluye ejercicios para un modelo lógico; no tiene edición oficial en español. La guía del Grupo de las Naciones Unidas para el Desarrollo Sostenible (UNSDG) es breve y trata los supuestos y riesgos.",
        "Retolaza (2010) es una guía escrita en la región, orientada al cambio social; sirve para el eslabón entre los efectos y el impacto.",
    ],
))

# ---------- U6 · Plan de trabajo, equipo y acuerdos

L.append(tarjetas(
    "metodologia-por-objetivo",
    "02 · Metodología por objetivo",
    "Método, entregable y *TRL* por objetivo de un proyecto de agricultura digital, ejemplo",
    [
        ("OE1 · TRL 6", "Estaciones de monitoreo y vuelos de dron en huertos de palto; base de "
                        "imágenes etiquetada"),
        ("OE2", "Entrenamiento y prueba de modelos multimodales con datos nuevos; informe de "
                "desempeño"),
        ("OE3 · TRL 7", "Validación del sistema con productores durante una campaña; informe "
                        "de validación"),
    ],
    clave=2,
    iconos=["search", "chart", "robot"],
    fuente="PROCIENCIA, RDE 084-2024-PROCIENCIA-DE · " + CARTILLA + ", subcriterio III.c · "
           "metodología ilustrativa",
    notas=[
        "El ejemplo parte del proyecto «Agricultura digital: validación de un sistema con "
        "monitoreo, imágenes, drones y modelos multimodales y generativos para la salud del "
        "palto Hass» (responsable técnico: Ricardo Yauri Rodríguez, INICTEL-UNI), "
        "seleccionado en Desafíos de Innovación para el Desarrollo Regional 2024, modalidad "
        "de validación, con S/ 367 300. Las bases de esa modalidad exigían entrada mínima en "
        "TRL 6; el TRL 7 de salida es una estimación del docente.",
        "La cartilla de Desarrollo Tecnológico pregunta si los métodos para desarrollar y "
        "validar la tecnología, con la estrategia de transferencia, están bien sustentados "
        "para llegar a TRL 5 o más, si la estrategia de análisis de la información está "
        "descrita y si se citan referencias de la metodología (subcriterio III.c).",
        "La prueba con datos que no se usaron en el entrenamiento estima el error que tendrá "
        "el modelo en campo.",
        "Dato: en 123 707 solicitudes R01 a los NIH entre 2010 y 2013, cada punto de la "
        "calificación del enfoque metodológico multiplicó por 6,2 la razón de probabilidades "
        "de recibir financiamiento, frente a 2,1 de la significancia y 1,5 de la innovación "
        "(Eblen et al., 2016).",
        "Error frecuente: una sola metodología para todos los objetivos. Indica que los "
        "objetivos son etapas de un mismo procedimiento y no resultados distintos.",
    ],
))

L.append(visual(
    "cronograma-gantt",
    "02 · Cronograma",
    "Diagrama de *Gantt* de un proyecto de agricultura digital, 24 meses",
    gantt(
        [
            ("OE1", "Antecedentes y patentes", 1, 3, False),
            ("OE1", "Instalación en los huertos", 1, 4, True),
            ("OE1", "Vuelos de dron y etiquetado", 4, 11, True),
            ("OE2", "Entrenamiento de modelos", 9, 14, True),
            ("OE2", "Prueba con datos nuevos", 13, 16, False),
            ("OE3", "Integración de la plataforma", 11, 17, False),
            ("OE3", "Validación con productores", 16, 21, True),
            ("OE3", "Informes y transferencia", 20, 24, True),
        ],
        [(1, 8, "Hito 1 · meses 1–8"), (9, 16, "Hito 2 · meses 9–16"),
         (17, 24, "Hito 3 · meses 17–24")],
    ),
    fuente="PROCIENCIA, guía de soporte, seguimiento y evaluación, concursos 2027 · "
           "cronograma ilustrativo",
    notas=[
        "La lámina retoma la metodología del proyecto de agricultura digital; los meses son "
        "del docente.",
        "La guía de PROCIENCIA define el hito como un periodo de seis a doce meses en el que se "
        "evalúa el avance con indicadores técnicos clave vinculados a los objetivos "
        "específicos; los hitos se registran en el plan operativo del proyecto (POP).",
        "Al vencer cada hito, los monitores de PROCIENCIA levantan el acta de acompañamiento y "
        "revisión de avances del proyecto (ARAP). El hito se aprueba con 70 % o más de sus "
        "indicadores cumplidos, se aprueba con reserva entre 50 % y 70 % y se desaprueba por "
        "debajo de 50 %.",
        "El entregable de un hito, como el informe de validación con productores, es el medio "
        "de verificación de su indicador. Las bases de Desarrollo Tecnológico 2027-02 prevén "
        "desembolsar, de manera referencial, el 100 % del monto aprobado en una sola armada "
        "(num. 2.4.1); el flujo de caja se trata en la sesión 5.",
        "La ruta crítica es la secuencia de actividades sin holgura, en la que un retraso "
        "atrasa el fin del proyecto. En el ejemplo, los vuelos de dron condicionan el "
        "entrenamiento de los modelos, y una campaña de cultivo perdida retrasa la "
        "validación. El manual del ILPES incluye el diagrama de Gantt y el método del camino "
        "crítico entre las técnicas de programación (2005, p. 11).",
        "La cartilla pregunta si las actividades del cronograma están detalladas y son "
        "factibles en el periodo de ejecución (subcriterio IV.b).",
    ],
))

L.append(tarjetas(
    "equipo-del-proyecto",
    "02 · Equipo del proyecto",
    "Roles mínimos del *equipo* en Desarrollo Tecnológico 2027 de PROCIENCIA",
    [
        ("Responsable técnico", "Maestría o doctorado; 3 proyectos o 3 artículos en el área, "
                                "o una combinación"),
        ("Coinvestigador", "Entre 2 y 6, al menos uno de otra disciplina"),
        ("Usuario final", "Responsable técnico o coinvestigador de la entidad usuaria de la "
                          "tecnología"),
        ("Gestor tecnológico", "Paquete tecnológico, viabilidad de patente y propiedad "
                               "intelectual"),
        ("Gestor de proyectos", "Gestión administrativa y financiera hasta el cierre"),
    ],
    clave=1,
    iconos=["users", "network", "building", "patent", "gantt"],
    fuente=BASES + ", num. 2.2.2 y 2.3, tabla 4",
    notas=[
        "Dato: el responsable técnico tiene vínculo con la entidad solicitante, reside en el "
        "Perú, tiene grado de maestro o doctor y ha participado en al menos tres proyectos de "
        "investigación, desarrollo tecnológico o innovación, o publicado al menos tres "
        "artículos originales en Scopus o Web of Science del área, o una combinación de ambos "
        "(num. 2.3). El tesista de posgrado es opcional.",
        "Cada integrante cumple un único rol y necesita registro en CTI Vitae. Al menos uno de "
        "los coinvestigadores o el responsable técnico pertenece a una entidad del sector "
        "productivo, de servicios, público o social interesada en ser usuaria final de la "
        "tecnología (num. 2.2.2).",
        "Dato: el equipo pesa 10 % en la cartilla de Desarrollo Tecnológico, en tres "
        "subcriterios: experiencia del responsable técnico, experiencia complementaria del "
        "equipo y funciones del equipo. La cartilla pregunta si el equipo integra todas las "
        "disciplinas del proyecto.",
        "Dato: Xu, Wu y Evans (2022) estimaron los roles de los autores de más de 16 millones "
        "de artículos a partir de 89 575 declaraciones de contribución y hallaron que los "
        "equipos más jerárquicos producen menos novedad.",
        "Error frecuente: un integrante con una restricción o un impedimento para su rol. Las "
        "bases consideran no apta la propuesta aunque cumpla la conformación mínima "
        "(nota 19).",
    ],
))

L.append(tarjetas(
    "acuerdos-entre-entidades",
    "02 · Acuerdos entre entidades",
    "Documentos que formalizan la participación de las *entidades* y del equipo",
    [
        ("Anexo 4A", "Carta de presentación y compromiso de la entidad solicitante"),
        ("Anexo 4B", "Carta de la entidad asociada peruana, con sus aportes valorizados"),
        ("Anexo 6", "Compromiso de finalización de la tesis, si el equipo tiene tesista"),
        ("Convenio de colaboración", "Acuerdo entre entidades públicas según el art. 88 del "
                                     "Texto Único Ordenado de la Ley 27444"),
        ("Acuerdo de confidencialidad", "Reserva de la información técnica que se comparte"),
    ],
    clave=1,
    iconos=["building", "agreement", "book", "file", "patent"],
    fuente="PROCIENCIA, anexos de las bases E041-2027-02, 2026 · DS 004-2019-JUS, art. 88",
    notas=[
        "La carta del Anexo 4B la firma el representante legal de la entidad asociada; "
        "detalla el personal que aporta y el total valorizado de sus aportes, y se mantiene "
        "vigente durante toda la ejecución. Las cartas de los Anexos 4A y 4B tienen carácter "
        "de declaración jurada (bases, num. 3.2).",
        "El Texto Único Ordenado (TUO) de la Ley 27444, aprobado por el DS 004-2019-JUS, "
        "permite a las entidades públicas celebrar convenios de colaboración, obligatorios "
        "para las partes y con cláusula expresa de libre adhesión y separación (art. 88). En "
        "las universidades, un convenio marco fija la cooperación general y un convenio "
        "específico, las actividades, aportes y plazos de un proyecto.",
        "El acuerdo de confidencialidad (_non-disclosure agreement_) se firma antes de "
        "compartir información técnica no publicada, como el diseño del prototipo. La carta "
        "de intención (_letter of intent_) expresa interés sin obligar a las partes y no "
        "reemplaza los anexos de PROCIENCIA.",
        "La titularidad de los resultados entre socios se trató en la sesión 2; el contrato de "
        "subvención con PROCIENCIA se trata en la sesión 5.",
        "Verificar antes de la clase: el reglamento vigente de convenios de la UNI y si existe "
        "un convenio marco con la entidad asociada.",
    ],
))

L.append(recursos(
    "recursos-plan",
    "02 · Recursos recomendados",
    "Recursos sobre plan de trabajo, equipo y acuerdos de colaboración",
    [
        {"tipo": "Guía", "titulo": "Metodología de gestión de proyectos PM². Guía 3.1",
         "autor": "Comisión Europea, 2024",
         "detalle": "Plan de trabajo, hitos, registro de riesgos y diagrama de Gantt",
         "url": "doi.org/10.2799/2009747",
         "enlace": "https://op.europa.eu/es/publication-detail/-/publication/97cc2f12-c648-11ee-95d9-01aa75ed71a1"},
        {"tipo": "Sitio web", "titulo": "GanttProject",
         "autor": "BarD Software, versión 3.3",
         "detalle": "Programa libre para diagramas de Gantt, dependencias y recursos",
         "url": "ganttproject.biz",
         "enlace": "https://www.ganttproject.biz/"},
        {"tipo": "Guía", "titulo": "Collaboration and Team Science Field Guide, 2.ª edición",
         "autor": "Bennett, Gadlin y Marchand, National Cancer Institute, 2018",
         "detalle": "Roles, confianza y acuerdos de colaboración en equipos de investigación",
         "url": "cancer.gov · Team Science Field Guide",
         "enlace": "https://www.cancer.gov/about-nci/organization/crs/research-initiatives/team-science-field-guide/collaboration-team-science-guide.pdf"},
        {"tipo": "Guía", "titulo": "DESCA Horizon Europe Model Consortium Agreement, versión 2.1",
         "autor": "DESCA Core Group, 2026",
         "detalle": "Modelo de acuerdo de consorcio para proyectos de Horizonte Europa",
         "url": "desca-agreement.eu",
         "enlace": "https://www.desca-agreement.eu/desca-model-consortium-agreement/"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía PM² de la Comisión Europea incluye plantillas abiertas de plan de trabajo, registro de riesgos y diagrama de Gantt (anexo C.12). GanttProject es gratuito y lee archivos de Microsoft Project.",
        "La guía del National Cancer Institute incluye un apéndice con preguntas para un acuerdo de colaboración: autoría, datos y roles.",
        "El modelo DESCA reúne cláusulas de gobernanza, aportes, confidencialidad y propiedad de resultados entre socios; es pertinente si la UNI participa en un consorcio europeo.",
    ],
))

L.append(cierre(
    "sintesis-02",
    "02 · Síntesis",
    "Matriz, plan de trabajo y *equipo*",
    [
        "Matriz: lógica vertical y lógica horizontal",
        "Indicador: cantidad, calidad, tiempo, lugar y línea de base",
        "Hito: periodo de 6 a 12 meses con indicadores",
        "Equipo: roles de las bases y anexos firmados",
    ],
    notas=[
        "Recapitular el criterio de cada término del tema 02.",
        "Dato: el límite máximo permisible de arsénico en el agua para consumo humano es "
        "0,010 mg/L (DS 031-2010-SA, anexo III).",
    ],
))

# ================================================================ CIERRE (5 min)

L.append(cierre(
    "sintesis-sesion",
    "Cierre",
    "Propuesta de I+D+i redactada según la *cartilla* de evaluación",
    [
        "Diagnóstico: problema con magnitud, objetivos verificables y antecedentes declarados",
        "Plan: matriz con indicadores, cronograma con hitos y equipo con anexos firmados",
    ],
    ("Sesión 5", "Ejecución del proyecto y transferencia de resultados"),
    notas=[
        "Recapitular la sesión: los documentos y la cartilla del concurso, el diagnóstico del "
        "problema, los objetivos y antecedentes, la matriz con sus indicadores, el cronograma "
        "con hitos y el equipo con sus compromisos.",
        "La sesión 5 parte de la matriz con sus medios de verificación y del cronograma con "
        "hitos. Calcula el presupuesto por partidas, que el manual del ILPES usa como "
        "indicador de las actividades, y trata el contrato, la rendición de cuentas y la "
        "protección de los resultados.",
    ],
))

L.append(referencias(
    "fuentes",
    "Referencias de la sesión",
    [
        ("documentos-convocatoria", "PROCIENCIA (2026). _Bases, anexos y cartillas_, E041-2027-02."),
        ("caso-tala-ilegal", "PROCIENCIA (2026). RDE 044-2026-PROCIENCIA-DE."),
        ("ponderacion-criterios", "Pier, E. L. et al. (2018). _PNAS_, 115(12), 2952-2957. https://doi.org/10.1073/pnas.1714379115"),
        ("etapas-marco-logico", "Ortegón, E., Pacheco, J. F. y Prieto, A. (2005). _Metodología del marco lógico_. CEPAL-ILPES, Serie Manuales 42."),
        ("arbol-problemas", "DS 034-2016-PCM. _El Peruano_, 23-05-2016."),
        ("magnitud-problema", "Ashe, K. (2012). _PLoS ONE_, 7(3), e33305. https://doi.org/10.1371/journal.pone.0033305"),
        ("objetivo-smart", "Doran, G. T. (1981). _Management Review_, 70(11), 35-36."),
        ("busqueda-declarada", "Page, M. J. et al. (2021). _BMJ_, 372, n71. https://doi.org/10.1136/bmj.n71"),
        ("literatura-del-campo", "OpenAlex (2026). Consulta del 14 de octubre de 2026."),
        ("diferenciacion-tecnica", "MINAM y GRAM Loreto (2023). Alerta temprana, febrero."),
        ("matriz-marco-logico", "DS 031-2010-SA. Reglamento de calidad del agua."),
        ("meta-desempeno", "OMS (2022). Arsénico. Nota descriptiva."),
        ("cadena-resultados", "OCDE-CAD (2002). _Glosario de los principales términos sobre evaluación_. Comisión Europea (2021)."),
        ("marco-logico-y-teoria-del-cambio", "Maini, R. et al. (2018). https://doi.org/10.1136/bmjgh-2017-000617. Maru, Y. T. et al. (2018). https://doi.org/10.1016/j.agsy.2018.04.010"),
        ("okr-moscow", "Doerr, J. (2018). _Measure What Matters_. Agile Business Consortium, DSDM."),
        ("metodologia-por-objetivo", "Eblen, M. K. et al. (2016). _PLoS ONE_, 11(6), e0155060. https://doi.org/10.1371/journal.pone.0155060"),
        ("cronograma-gantt", "PROCIENCIA (2026). _Guía de soporte, seguimiento y evaluación_, concursos 2027."),
        ("equipo-del-proyecto", "Xu, F., Wu, L. y Evans, J. (2022). _PNAS_, 119(23), e2200927119. https://doi.org/10.1073/pnas.2200927119"),
        ("acuerdos-entre-entidades", "DS 004-2019-JUS. Texto Único Ordenado de la Ley 27444, art. 88."),
    ],
))


def _sin_corte(lam):
    """Espacio de no separación en montos y cifras de los nodos de texto
    («S/ 300 000», «7 µg/m³»), para que el salto de línea no parta la cifra."""
    import re

    def fijo(txt):
        txt = re.sub(r"(S/|US\$|€) (?=\d)", "\\1\u00a0", txt)
        txt = re.sub(r"(?<=\d) (?=µg)", "\u00a0", txt)
        return re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", txt)

    lam.cuerpo = re.sub(r">([^<]+)<", lambda m: ">" + fijo(m.group(1)) + "<", lam.cuerpo)
    return lam


L = [_sin_corte(lam) for lam in L]

construir("clase-04", "Sesión 4 · Formulación de proyectos", L)
