#!/usr/bin/env python3
"""Sesión 1 · Fundamentos y ecosistema I+D+i+e — formato ponencia (11.ª edición).

Temas: «Definiciones y madurez tecnológica» (tema 01: clasificación de la idea
y nivel de madurez) e «Institucionalidad del sistema peruano» (tema 02:
entidades a las que se presenta la propuesta). La apertura es mínima (portada
y agenda); la serie de la Ley 30309 (11 % en 2016, 54 % en 2019) va en la
unidad de indicadores del país, después de presentar a CONCYTEC como
calificador de proyectos.

Secuencia (scratchpad/secuencia.md): U1 I+D → U2 innovación y sigla → U3 TRL
→ receso → U4 actores y programas → U5 indicadores del país → U6 aplicación a
la propuesta. Ninguna sigla se usa antes de la lámina que la presenta.

Formato expositivo: la sesión no incluye actividades en el aula. Las notas
reúnen contenido de respaldo con dato y fuente, errores frecuentes de los
formuladores y puntos por verificar. Un comentario de marcador por unidad
señala, al cierre de cada una, el lugar de las láminas de recursos recomendados.
Ejemplos (scratchpad/asignacion-ejemplos.md y banco-ejemplos.md): cada concepto
se ilustra con un proyecto distinto de la UNI; los titulares y las
explicaciones conceptuales no nombran proyectos.

Versión 6 (14 oct 2026): ejemplos de proyectos de la UNI en lugar de un ejemplo
único. Versión 5 (13 oct 2026): sesión expositiva y revisión del vocabulario. Versión 4: correcciones de los verificadores de
contenido y de estilo (scratchpad/verif-contenido.md y verif-estilo.md) y slugs
descriptivos. Versión 3: redacción impersonal según scratchpad/guia-redaccion.md
y orden de scratchpad/secuencia.md. Versión 2: panel de expertos
(scratchpad/experto-*.md).

Antes de dictar, verificar: estado actual de qAIRa; resultado de UNI-SAT en
CubeDesign 2025; RR del VRI-UNI; meta OP.06.01 (0,25 %) en el PDF del
DS 093-2025-PCM; fecha de la Directiva 001-2019-CONCYTEC-DPP; si los S/ 52,3 M
de PROCIENCIA 2027 incluyen préstamo; referencia del término «valle de la
muerte» (Ehlers, 1998; Auerswald y Branscomb, 2003); reparto del
cofinanciamiento de EMBRAPII (Portal da Indústria).

Uso:  python3 tools/ponencia/clase-01.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from graficos import (  # noqa: E402
    cuadruple_helice, escalera_trl, icono, peldanos, pendiente, rangos_trl, valle,
)
from plantillas import (  # noqa: E402
    agenda, barras, caso, circuito, cierre, cifra, construir, duo, frase, pasos, portada,
    recursos, referencias, seccion, tarjetas, visual,
)

FUENTE_REC = "Enlaces verificados en octubre de 2026"

L = []

# ================================================================ APERTURA (5 min)

L.append(portada(
    "portada",
    "Sesión 1 · Diseño y Gestión de Proyectos {I+D+i+e}",
    "Fundamentos y ecosistema I+D+i+e",
    "Definiciones de I+D e innovación, madurez tecnológica (TRL) y financiamiento de la "
    "ciencia, tecnología e innovación (CTI) en el Perú",
    ["Definiciones y madurez tecnológica", "Institucionalidad del sistema peruano"],
    "Abraham Caso-Torres · OTI-UNI · CC BY-SA 4.0",
    visual=peldanos(),
    notas=[
        "Dar la bienvenida y presentar los dos temas de la sesión: las definiciones de I+D e "
        "innovación con la escala de madurez tecnológica, y la institucionalidad del sistema "
        "peruano de ciencia, tecnología e innovación.",
    ],
))

L.append(agenda(
    "agenda",
    "Agenda",
    "Temas y contenidos de la sesión 1",
    [
        ("Definiciones y madurez tecnológica",
         ["Definición y tipos de I+D", "Innovación y sigla I+D+i+e", "Madurez tecnológica (TRL)"]),
        ("Institucionalidad del sistema peruano",
         ["Actores y programas de apoyo", "Indicadores de CTI del Perú", "Elegibilidad y entidad de destino"]),
    ],
    franja=("Receso", "10 minutos, entre el tema 01 y el tema 02"),
    notas=[
        "Presentar los dos temas y las tres unidades de cada uno.",
        "Tiempo: apertura, 5 min; tema 01, 75 min; receso, 10 min; tema 02, 80 min; cierre, "
        "5 min; holgura para preguntas, 5 min.",
    ],
))

# ===================================== TEMA 01 · DEFINICIONES Y MADUREZ TECNOLÓGICA

L.append(seccion(
    "tema-01", "01", "Definiciones y madurez tecnológica",
    "Clasificación de la actividad como I+D o innovación y nivel de madurez tecnológica",
    notas=[
        "Presentar el tema 01, que reúne las definiciones de I+D e innovación de los manuales "
        "internacionales y la escala de madurez tecnológica. Los programas de financiamiento "
        "peruanos se presentan en el tema 02.",
        "Tiempo: 75 minutos; presentación del tema, 1; definición y tipos de I+D, 22; innovación "
        "y sigla I+D+i+e, 17; madurez tecnológica, 30; síntesis, 5.",
    ],
))

# ---------- U1 · I+D

L.append(frase(
    "definicion-id",
    "01 · Definición de I+D",
    "I+D es el *trabajo creativo y sistemático* realizado para aumentar el conocimiento e idear "
    "nuevas aplicaciones del conocimiento disponible.",
    "Síntesis del Manual de Frascati (OCDE, 2015)",
    notas=[
        "El Manual de Frascati reúne las directrices de la Organización para la Cooperación "
        "y el Desarrollo Económicos (OCDE) para medir la I+D. Su definición incluye el "
        "conocimiento sobre la humanidad, la cultura y la sociedad, y es la que usan los fondos "
        "públicos peruanos.",
        "La condición de I+D no garantiza la elegibilidad; las bases de cada concurso fijan las "
        "áreas que admiten.",
        "Una tesis de pregrado cuenta como I+D cuando genera conocimiento nuevo; la que aplica un "
        "método conocido a un caso de rutina no cumple los criterios de Frascati.",
    ],
))

L.append(circuito(
    "cinco-criterios",
    "01 · Criterios de Frascati",
    "Requisitos de una actividad de *I+D*",
    [
        ("Novedosa", "Orientada a hallazgos nuevos"),
        ("Creativa", "Con conceptos e hipótesis originales"),
        ("Incierta", "Resultado final desconocido al inicio"),
        ("Sistemática", "Planificada y presupuestada"),
        ("Transferible", "Resultados que otros pueden reproducir o usar"),
    ],
    fuente="OCDE, _Manual de Frascati_ 2015 · PROCIENCIA, bases 2026",
    notas=[
        "Las bases del concurso de investigación aplicada de 2026 citadas al pie exigen los "
        "cinco criterios en simultáneo.",
        "Error frecuente: afirmar que «no existe nada similar». En la evaluación, esa afirmación "
        "suele indicar que no se hizo la búsqueda de antecedentes; las bases piden un análisis "
        "de la novedad frente a patentes, software y otras investigaciones.",
        "Una actividad que incumple alguno de los criterios no es I+D; suele tratarse de "
        "ingeniería de rutina, servicio técnico o consultoría.",
    ],
))

L.append(duo(
    "rutina-o-id",
    "01 · Criterio de incertidumbre",
    "*Incertidumbre* del resultado en un ensayo normado y en un método nuevo",
    {"cab": "Rutina", "t": "Análisis de residuos de pesticidas en arándanos con un método normado",
     "items": ["Procedimiento de laboratorio establecido", "Exactitud conocida del método"]},
    {"cab": "I+D", "t": "Sensor químico selectivo para cuantificar esos residuos",
     "items": ["Polímeros molecularmente impresos con marcadores fluorescentes",
               "Selectividad y exactitud desconocidas al inicio"]},
    fuente="PROCIENCIA, seleccionados de Investigación Aplicada 2025-02",
    notas=[
        "En el Manual de Frascati, la incertidumbre se refiere al resultado, que no se conoce de "
        "antemano. El análisis de residuos con un método normado, por ejemplo la norma europea "
        "EN 15662, sigue un procedimiento con exactitud establecida; el desarrollo "
        "de un sensor químico nuevo comienza sin saber qué selectividad ni qué exactitud "
        "alcanzará frente a ese método.",
        "El contenido de pesticida de una muestra tampoco se conoce antes del análisis, pero esa "
        "incertidumbre la resuelve el propio método normado y no corresponde a la del Manual de "
        "Frascati.",
        "Dato: el proyecto de la derecha es «Materiales fluorescentes como marcadores ópticos en "
        "polímeros molecularmente impresos (MIP) para cuantificar pesticidas en arándanos de "
        "exportación», de Gino Picasso Escobar (UNI), seleccionado en el concurso de "
        "Investigación Aplicada 2025-02 de PROCIENCIA, multidisciplinario, con S/ 500 000. El "
        "problema lo plantea el mercado de exportación.",
        "Error frecuente: confundir la dificultad técnica con la incertidumbre del resultado.",
        "Implicación para el formulador: la propuesta indica qué podría no funcionar y con qué "
        "prueba se comprobará.",
    ],
))

L.append(tarjetas(
    "tres-tipos",
    "01 · Tipos de I+D",
    "Tipos de I+D según Frascati en tres proyectos de la *UNI*, 2025-2026",
    [
        ("Investigación básica", "Nueva física en colisiones relativistas ultraperiféricas de iones pesados"),
        ("Investigación aplicada", "Sistemas agrivoltaicos con módulos de distinta transmitancia en Tumbes, Lima y Tacna"),
        ("Desarrollo experimental", "Prototipo de aislador sísmico de bajo costo con caucho reciclado"),
    ],
    iconos=["search", "target", "building"],
    fuente="OCDE, _Manual de Frascati_ 2015 · PROCIENCIA, RDE 052-2026, 087-2026 y 068-2025",
    notas=[
        "Según el Manual de Frascati (OCDE, 2015), la investigación básica produce conocimiento "
        "sobre los fundamentos de un fenómeno sin una aplicación prevista, y la aplicada lo "
        "produce con un objetivo práctico determinado. El desarrollo experimental parte del "
        "conocimiento existente y genera conocimiento adicional para crear productos o procesos "
        "nuevos o mejorar los existentes.",
        "Dato: el proyecto de investigación básica, de Orlando Pereyra Ravinez, ganó el concurso "
        "de Investigación Básica 2026-01 de PROCIENCIA, modalidad semilla, con S/ 100 000 "
        "(RDE 052-2026); estudia física de altas energías sin aplicación prevista.",
        "Dato: el de investigación aplicada, de Mónica Gómez León, ganó el concurso de "
        "Investigación Aplicada 2026-02, multidisciplinario, con S/ 500 000 (RDE 087-2026). "
        "Instala paneles solares sobre cultivos para evaluar a la vez la energía, el agua y la "
        "producción agrícola.",
        "Dato: el de desarrollo experimental, de Roy Reyna Salazar, ganó el concurso de "
        "Desarrollo Tecnológico 2025-03 con S/ 350 000. Desarrolla un aislador elastomérico "
        "con láminas de llanta reciclada para vivienda de bajo costo; parte de ensayos "
        "publicados en 2019 y 2024.",
        "La clasificación de cada proyecto sigue el concurso que lo financió. Implicación para el "
        "formulador: el tipo de I+D lo define el resultado esperado al cierre del proyecto, no "
        "el tema.",
    ],
))

# ---------- U2 · Innovación

L.append(recursos(
    "recursos-id",
    "01 · Recursos recomendados",
    "Recursos sobre la definición y los tipos de I+D",
    [
        {"tipo": "Guía", "titulo": "Meaning of research and development for tax purposes",
         "autor": "Gobierno del Reino Unido (DSIT), 2023",
         "detalle": "Criterios y ejemplos para distinguir la I+D del trabajo rutinario",
         "url": "gov.uk · Meaning of R&D for tax purposes",
         "enlace": "https://www.gov.uk/government/publications/guidelines-on-the-meaning-of-research-and-development-for-tax-purposes/meaning-of-research-and-development-for-tax-purposes-guidelines"},
        {"tipo": "Libro", "titulo": "Pasteur's Quadrant: Basic Science and Technological Innovation",
         "autor": "Donald E. Stokes, Brookings Institution Press, 1997",
         "detalle": "Concepto de investigación básica orientada por el uso (cuadrante de Pasteur)",
         "url": "brookings.edu/books/pasteurs-quadrant",
         "enlace": "https://www.brookings.edu/books/pasteurs-quadrant/"},
        {"tipo": "Base de datos", "titulo": "Espacenet",
         "autor": "Oficina Europea de Patentes",
         "detalle": "Más de 170 millones de documentos de patente; interfaz LatiPat en español",
         "url": "worldwide.espacenet.com",
         "enlace": "https://worldwide.espacenet.com/"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía británica define la incertidumbre como aquello que un profesional competente no puede resolver sin investigar (párrafos 13 y 14) y excluye el análisis rutinario, la copia y la adaptación (párrafo 12). Complementa la lámina sobre el ensayo normado y el desarrollo de un método nuevo.",
        "Stokes (1997) muestra que la investigación básica y la aplicada no son extremos de una sola línea: hay investigación que busca entender un fenómeno y tiene a la vez un uso previsto. Es de pago; verificar disponibilidad en la biblioteca de la UNI.",
        "Espacenet sirve para el criterio de novedad: la búsqueda de patentes por palabras clave o clasificación precede a cualquier afirmación de que no existen soluciones similares.",
    ],
))

L.append(frase(
    "definicion-innovacion",
    "01 · Definición de innovación",
    "Innovación es un *producto o proceso* nuevo o mejorado, al menos para la unidad que lo "
    "introduce, que está a disposición de los usuarios o en uso.",
    "Síntesis del Manual de Oslo (OCDE y Eurostat, 2018)",
    notas=[
        "El Manual de Oslo define la innovación como un producto o proceso nuevo o "
        "mejorado que difiere significativamente de los productos o procesos que la unidad "
        "tenía antes y que se puso a disposición de los usuarios (producto) o en uso (proceso). "
        "Basta con que sea nuevo para la empresa que lo introduce.",
        "Un prototipo validado en el laboratorio pasa a ser innovación cuando se pone "
        "a disposición de los usuarios, por ejemplo, cuando una empresa lo vende o una entidad "
        "pública lo incorpora a su servicio. El caso qAIRa, en el tema 02, sigue ese recorrido.",
        "Implicación para el formulador: un fondo de innovación pide identificar el riesgo "
        "tecnológico del proyecto, que no existe cuando se compra una solución disponible en el "
        "mercado.",
    ],
))

L.append(duo(
    "id-frente-a-innovacion",
    "01 · I+D frente a innovación",
    "Rasgos distintivos de la *I+D* y de la innovación según Frascati y Oslo",
    {"cab": "I+D", "t": "Genera conocimiento nuevo, llegue o no al mercado",
     "items": ["Se mide por el gasto y el personal de I+D (Frascati)"]},
    {"cab": "Innovación", "t": "Introduce un producto o proceso, propio o adquirido",
     "items": ["Se mide por la proporción de empresas que innovan (Oslo)"]},
    notas=[
        "Dato: un grupo de la UNI estudió en 2022 electrolitos eutécticos en un proyecto de "
        "investigación básica; ese trabajo es I+D con independencia de que llegue a un producto. En 2026 "
        "el grupo de Lyda La Torre Riveros ganó el concurso de Investigación Aplicada 2026-02 "
        "de PROCIENCIA (S/ 500 000) para un sistema portátil de baterías de ion litio con geles "
        "poliméricos biodegradables y esos electrolitos (Vicerrectorado de Investigación de la "
        "UNI, 2025; RDE 087-2026).",
        "En el otro sentido, la empresa que compra e instala una máquina nueva innova sin "
        "realizar I+D.",
        "Un proyecto es I+D e innovación a la vez cuando el conocimiento nuevo termina en un "
        "producto o proceso a disposición de los usuarios o en uso.",
    ],
))

L.append(pasos(
    "componentes-sigla",
    "01 · Sigla {I+D+i+e}",
    "Componentes de la sigla *I+D+i+e* y resultado de cada uno",
    [
        ("Investigación", "Conocimiento nuevo"),
        ("Desarrollo", "Prototipo o proceso piloto"),
        ("Innovación", "Producto o proceso en uso"),
        ("Emprendimiento", "Empresa nueva que comercializa el resultado"),
    ],
    clave=3,
    marcas=["I", "D", "i", "e"],
    notas=[
        "La «e» es un uso local y no figura en los manuales internacionales; corresponde a la "
        "creación de una empresa nueva (_spin-off_ o _startup_). La licencia a una empresa "
        "existente es otra vía de transferencia al mercado, y la sesión 2 compara ambas.",
        "La sigla se lee de izquierda a derecha, pero el proceso real tiene retroalimentación "
        "entre etapas; el tema 02 comienza con un modelo que describe esa retroalimentación.",
        "La distancia entre un prototipo y un producto en uso se mide con la escala de madurez "
        "tecnológica, que abre la unidad siguiente.",
    ],
))

# ---------- U3 · Madurez tecnológica

L.append(recursos(
    "recursos-innovacion",
    "01 · Recursos recomendados",
    "Recursos sobre innovación y emprendimiento",
    [
        {"tipo": "Guía", "titulo": "Manual de Bogotá: normalización de indicadores de innovación tecnológica en América Latina y el Caribe",
         "autor": "RICYT, OEA y CYTED, 2001",
         "detalle": "Adaptación latinoamericana del Manual de Oslo",
         "url": "ricyt.org · Manual de Bogotá",
         "enlace": "https://www.ricyt.org/wp-content/uploads/2019/09/bogota-1.pdf"},
        {"tipo": "Libro", "titulo": "Managing Innovation, 8.ª edición",
         "autor": "Joe Tidd y John Bessant, Wiley, 2024",
         "detalle": "Gestión de la innovación como proceso organizacional",
         "url": "wiley.com · Managing Innovation, 8th Edition",
         "enlace": "https://www.wiley.com/en-us/Managing+Innovation%3A+Integrating+Technological%2C+Market+and+Organizational+Change%2C+8th+Edition-p-9781394252060"},
        {"tipo": "Informe", "titulo": "Global Entrepreneurship Monitor: Reporte Nacional del Perú 2025-2026",
         "autor": "GEM Perú, 2026",
         "detalle": "Indicadores de actividad emprendedora en el Perú",
         "url": "gemconsortium.org · GEM Perú 2025/2026",
         "enlace": "https://gemconsortium.org/report/global-entrepreneurship-monitor-reporte-nacional-del-peru-20252026"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "El Manual de Bogotá adapta las definiciones de Oslo a países donde buena parte de la innovación consiste en adquirir y adaptar tecnología; anticipa el dato del gasto en maquinaria de la unidad 5.",
        "Tidd y Bessant tratan los tipos de innovación, la innovación como proceso y los modelos de innovación abierta, de usuario y social. Es de pago; verificar disponibilidad en la biblioteca de la UNI.",
        "El informe GEM Perú aporta cifras sobre la «e» de la sigla: actividad emprendedora temprana, consolidación de negocios y entorno para emprender. Enlaza con la sesión 2.",
    ],
))

L.append(visual(
    "escala-trl",
    "01 · _Technology Readiness Level_ (TRL)",
    "Escala de madurez tecnológica (*TRL*) por entorno de validación",
    escalera_trl(),
    fuente="Comisión Europea, _Horizonte 2020_, Anexo G · ISO 16290",
    notas=[
        "El nivel depende del entorno en que se validó la tecnología y de la evidencia "
        "documentada de esa validación. Laboratorio hasta TRL 4; entorno relevante en TRL 5 y 6; "
        "entorno operacional de TRL 7 a 9.",
        "La escala proviene de la NASA y la Comisión Europea la adoptó en Horizonte 2020. Los "
        "criterios para asignar cada nivel están en la norma ISO 16290.",
        "La correspondencia con los tipos de Frascati es aproximada: investigación básica u "
        "orientada en TRL 1 y 2, aplicada en TRL 3 y 4, y desarrollo experimental de TRL 5 a 7.",
        "El entorno relevante reproduce las condiciones principales de uso; el entorno "
        "operacional es el lugar real de uso.",
    ],
))

L.append(frase(
    "nivel-probado",
    "01 · Regla de asignación del TRL",
    "El *TRL de partida* es el nivel acreditado con evidencia a la fecha de cierre del concurso.",
    fuente="PROCIENCIA, bases 2026 · CONCYTEC, Directiva 001-2022-CONCYTEC-P",
    notas=[
        "Las bases de los concursos exigen que la evidencia exista a la fecha de cierre. El "
        "evaluador contrasta el nivel declarado con el anexo de evidencias; si el anexo no lo "
        "respalda, asigna el nivel inferior y la propuesta puede quedar fuera del rango del "
        "concurso.",
        "Error frecuente: declarar el TRL que el proyecto espera alcanzar al cierre en lugar del "
        "nivel acreditado al inicio.",
        "Dato: en el concurso Desarrollo de Tecnologías desde Consorcios para Cadenas de Valor "
        "2024, la tabla oficial de seleccionados de PROCIENCIA consigna el TRL de entrada y el de "
        "salida de cada proyecto. El de la UNI sobre detección de deforestación en cultivos de "
        "exportación con análisis satelital, inteligencia artificial y _blockchain_ (S/ 285 000) "
        "declara entrada en TRL 2 y salida en TRL 4 (PROCIENCIA, página del concurso, 2024).",
    ],
))

L.append(caso(
    "caso-satelites",
    "01 · Caso de estudio · satélites de estudiantes",
    "Chasqui I y UNI-SAT",
    "Universidad Nacional de Ingeniería · Lima",
    [
        ("2014", "Chasqui I en órbita, sin señal confirmada"),
        ("2025", "UNI-SAT: ensayos de vibración y de ciclos térmicos en Brasil"),
        ("TRL 9", "No acreditado para Chasqui I por falta de registro de señal"),
    ],
    icono("satelite"),
    fuente="nanosats.eu · Andina, 2014 · Infobae, 2025",
    notas=[
        "Dato: Chasqui I, CubeSat de 1 kg desarrollado por estudiantes de la UNI, se liberó desde "
        "la Estación Espacial Internacional el 18 de agosto de 2014; no hay registro de que "
        "enviara señal. Estuvo en el entorno operacional, pero sin telemetría no hay evidencia "
        "que acredite TRL 9.",
        "Dato: UNI-SAT (2U, detección de derrames de petróleo) se presentó en 2025 a ensayos de "
        "vibración y de ciclos térmicos en CubeDesign, Brasil; si los superó, son evidencia de "
        "entorno relevante. El documento que permitiría declarar TRL 6 es el informe de esos "
        "ensayos con los resultados medidos.",
        "Verificar antes de la clase: resultado de UNI-SAT en CubeDesign 2025.",
    ],
))

L.append(duo(
    "sin-trl",
    "01 · Límites de la escala TRL",
    "Medición de la *madurez* en proyectos sociales, educativos y de política pública",
    {"cab": "Tecnología", "t": "TRL del 1 al 9",
     "items": ["Evidencia: ensayo, prototipo o piloto"]},
    {"cab": "Intervención social o educativa", "t": "Madurez medida por evidencia de adopción",
     "items": ["Puede ser I+D según el Manual de Frascati",
               "Escala de preparación social (SRL)"]},
    fuente="OCDE, _Manual de Frascati_ 2015 · Innovation Fund Denmark, SRL",
    notas=[
        "Un proyecto educativo o de política pública puede ser I+D según el Manual de Frascati, "
        "que incluye las ciencias sociales y las humanidades. Su madurez se documenta con datos de "
        "adopción, como el número de instituciones o personas que aplican el resultado, o con la "
        "escala SRL (_Societal Readiness Levels_) de Innovation Fund Denmark.",
    ],
))

L.append(visual(
    "valle-de-la-muerte",
    "01 · Valle de la muerte (_valley of death_)",
    "Fondos de investigación e inversión privada según el nivel de *TRL*",
    valle(),
    notas=[
        "En política de innovación, el valle de la muerte es el tramo, aproximadamente entre los "
        "niveles 4 y 7, en que los fondos de investigación disminuyen antes de que comience la "
        "inversión privada, de modo que el financiamiento disponible es escaso.",
        "Dato: el concurso de Escalamiento de Tecnologías de PROCIENCIA (Proyectos Especiales, "
        "2022) financió con S/ 500 000 a un equipo de la UNI, de las facultades de Ciencias y de "
        "Ingeniería Química y Textil, para escalar telas de algodón o poliéster con "
        "nanopartículas de óxido de zinc (ZnO), antimicrobianas y con protección ultravioleta, en "
        "la planta de Tejidos San Jacinto (El Peruano, 2026). Las bases fijaban la salida en TRL 7 u 8: es un "
        "instrumento para el tramo final del valle (PROCIENCIA, página del concurso, 2022).",
        "Los instrumentos peruanos creados para este tramo se presentan en el tema 02.",
        "Verificar antes de la clase: la referencia del término (Ehlers, 1998, _Unlocking Our "
        "Future_; Auerswald y Branscomb, 2003), para añadirla al pie.",
    ],
))

L.append(recursos(
    "recursos-trl",
    "01 · Recursos recomendados",
    "Recursos sobre madurez tecnológica y valle de la muerte",
    [
        {"tipo": "Guía", "titulo": "Technology Readiness Assessment Guide (GAO-20-48G)",
         "autor": "U.S. Government Accountability Office, 2020",
         "detalle": "Procedimiento en cinco pasos para evaluar la madurez tecnológica",
         "url": "gao.gov/products/gao-20-48g",
         "enlace": "https://www.gao.gov/products/gao-20-48g"},
        {"tipo": "Artículo", "titulo": "From NASA to EU: the evolution of the TRL scale in Public Sector Innovation",
         "autor": "Mihály Héder, The Innovation Journal, 2017",
         "detalle": "Evolución de la escala TRL desde la NASA hasta la Unión Europea",
         "url": "eprints.sztaki.hu/9204",
         "enlace": "https://eprints.sztaki.hu/9204/1/Heder_1_3269345_ny.pdf"},
        {"tipo": "Informe", "titulo": "The TRL Scale as a Research & Innovation Policy Tool",
         "autor": "EARTO, 2014",
         "detalle": "Usos y límites del TRL en el financiamiento público de la investigación",
         "url": "earto.eu · The TRL Scale as a R&I Policy Tool",
         "enlace": "https://www.earto.eu/wp-content/uploads/The_TRL_Scale_as_a_R_I_Policy_Tool_-_EARTO_Recommendations_-_Final.pdf"},
        {"tipo": "Artículo", "titulo": "Crossing the valley of death: Five underlying innovation processes",
         "autor": "Ellwood, Williams y Egan, Technovation, 2022",
         "detalle": "Seis proyectos tecnológicos y cinco procesos para cruzar el valle de la muerte",
         "url": "livrepository.liverpool.ac.uk/3096441",
         "enlace": "https://livrepository.liverpool.ac.uk/3096441/"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía de la GAO explica cómo se identifican las tecnologías críticas, qué evidencia se exige en cada nivel y cómo se redacta el informe de evaluación; responde a la cuestión del documento que debe salir de los ensayos de UNI-SAT.",
        "Héder (2017) sostiene que la escala pierde precisión fuera de su disciplina de origen y que cada campo necesita su propia guía, lo que respalda la lámina sobre proyectos sociales, educativos y de política pública.",
        "EARTO analiza el TRL como criterio de selección en concursos y el papel de los centros tecnológicos en el valle de la muerte (secciones 1.3 y 2.1). Ellwood, Williams y Egan (2022) plantean cinco procesos de innovación necesarios para cruzar ese tramo; el repositorio de la Universidad de Liverpool ofrece la versión aceptada por los autores.",
    ],
))

L.append(cierre(
    "sintesis-01",
    "01 · Síntesis",
    "Clasificación de una propuesta y asignación del *TRL*",
    [
        "I+D: cinco criterios de Frascati en simultáneo",
        "Innovación: producto o proceso nuevo en uso",
        "TRL: nivel acreditado con evidencia",
    ],
    ("Receso", "10 minutos · Tema 02: institucionalidad del sistema peruano"),
    notas=[
        "Recapitular el criterio de cada término del tema 01 antes del receso de 10 minutos.",
    ],
))

# ========================================= TEMA 02 · INSTITUCIONALIDAD DEL SISTEMA PERUANO

L.append(seccion(
    "tema-02", "02", "Institucionalidad del sistema peruano",
    "Entidades y programas del sistema peruano, indicadores del país y entidad de destino",
    notas=[
        "Mantener esta lámina en pantalla durante el receso.",
        "Presentar el tema 02, que trata el modelo de innovación, los actores del sistema "
        "peruano de ciencia, tecnología e innovación, los indicadores del país y las entidades "
        "de destino para un equipo de la UNI.",
        "Tiempo: 80 minutos; presentación del tema, 1; actores y programas, 30; indicadores del "
        "país, 25; elegibilidad y entidad de destino, 19; síntesis, 5.",
    ],
))

# ---------- U4 · Actores y programas

L.append(duo(
    "modelos-innovacion",
    "02 · Modelos del proceso de innovación",
    "Modelo lineal y modelo de *eslabón en cadena* (Kline y Rosenberg, 1986)",
    {"cab": "Modelo lineal", "t": "Secuencia fija de la ciencia a la tecnología y al mercado"},
    {"cab": "Eslabón en cadena", "t": "El proceso empieza en un mercado potencial",
     "items": ["Retroalimentación entre etapas",
               "Investigación cuando el conocimiento existente no resuelve el problema"]},
    fuente="Kline y Rosenberg, 1986",
    notas=[
        "La sigla I+D+i+e se presentó como una secuencia. En el modelo de eslabón en cadena "
        "(_chain-linked model_), ante un problema se recurre primero al conocimiento existente y "
        "se investiga cuando ese conocimiento es insuficiente.",
        "El modelo supone la interacción de varios actores, que la lámina siguiente presenta con "
        "el modelo de cuádruple hélice.",
    ],
))

L.append(visual(
    "cuadruple-helice",
    "02 · Sistema Nacional de CTI (SINACTI)",
    "Estado, academia, empresa y sociedad en el modelo de *cuádruple hélice*",
    cuadruple_helice([
        ("Estado", ["Regula y financia", "Gobierno central y regional"]),
        ("Academia", ["Genera conocimiento", "Universidades e institutos"]),
        ("Empresa", ["Produce y comercializa", "Empresas de todo tamaño"]),
        ("Sociedad", ["Uso y validación del resultado", "Usuarios y comunidades"]),
    ]),
    fuente="Carayannis y Campbell, 2009 · Ley 31250",
    notas=[
        "La triple hélice (universidad, empresa y Estado) no incluye a quien usa el resultado. "
        "La cuádruple hélice añade a la sociedad civil (Carayannis y Campbell, 2009); para el "
        "formulador, incluye a los usuarios de la definición de Oslo. La quíntuple hélice añade "
        "el medio ambiente.",
        "Un sistema nacional de innovación es la red de instituciones cuyas interacciones crean "
        "y difunden tecnología (Freeman, 1987). En el Perú es el Sistema Nacional de Ciencia, "
        "Tecnología e Innovación (SINACTI), regulado por la Ley 31250.",
    ],
))

L.append(tarjetas(
    "entidades-sinacti",
    "02 · Institucionalidad peruana de CTI",
    "Funciones de las entidades del *SINACTI* en la formulación de proyectos",
    [
        ("CONCYTEC", "Ente rector; califica investigadores y proyectos"),
        ("PROCIENCIA", "Financia investigación por concurso"),
        ("PROINNÓVATE", "Cofinancia innovación de empresas"),
        ("Red CITE", "Ofrece ensayos y validación"),
        ("INDECOPI", "Otorga patentes y modelos de utilidad"),
    ],
    numerar=False,
    iconos=["scale", "fund", "rocket", "sliders", "patent"],
    fuente="Ley 31250 · DS 002-2026-PRODUCE",
    notas=[
        "CONCYTEC (Consejo Nacional de Ciencia, Tecnología e Innovación Tecnológica) es el ente "
        "rector. Fija la política nacional, actualmente la Política Nacional de CTI al 2030 "
        "(POLCTI), que incluye la innovación en servicios sociales y públicos; califica "
        "investigadores en el Registro Nacional Científico, Tecnológico y de Innovación "
        "Tecnológica (RENACYT) y califica proyectos de empresas para el beneficio tributario de "
        "la Ley 30309. Las tres siglas se enuncian completas al presentarlas.",
        "PROCIENCIA es el antiguo FONDECYT (desde 2021); PROINNÓVATE se relanzó en 2026 "
        "con un préstamo del Banco Interamericano de Desarrollo (BID). Los documentos anteriores "
        "al cambio de nombre usan FONDECYT, y las bases anteriores a 2024 pueden no reflejar las "
        "normas vigentes; se consultan las del año en curso.",
        "Las principales normas desde 2021 son la Ley 31250, el reglamento de 2024, la POLCTI "
        "de 2025 y el DL 1727 (2026), que reforzó la potestad de CONCYTEC para sancionar el "
        "fraude científico.",
        "Chile (ANID y CORFO) y Colombia (Minciencias e iNNpulsa) tienen agencias distintas para "
        "ciencia e innovación, como el Perú con PROCIENCIA y PROINNÓVATE. A diferencia de "
        "Minciencias, que es un ministerio, CONCYTEC no tiene ese rango.",
    ],
))

L.append(frase(
    "entidad-postulante",
    "02 · Entidad postulante por programa",
    "En PROCIENCIA el proyecto lo lidera *un investigador*; en PROINNÓVATE el solicitante es una "
    "empresa.",
    fuente="PROCIENCIA, bases 2026 · PROINNÓVATE",
    notas=[
        "Las bases de cada programa fijan qué tipo de entidad puede postular; por eso el programa "
        "depende sobre todo de la entidad postulante, cualquiera que sea el tema del proyecto.",
        "PROCIENCIA también financia prototipos con el concurso de Desarrollo Tecnológico, y en "
        "ambos programas participan entidades asociadas del otro sector.",
    ],
))

L.append(visual(
    "trl-en-fondos",
    "02 · Rangos de TRL por concurso",
    "TRL de entrada y de salida en los concursos de *PROCIENCIA*, 2026",
    rangos_trl([
        ("Proyectos avanzados", "Investigación aplicada · de 2–3 a 3–4", 2.5, 3.5, False),
        ("Multidisciplinarios", "Investigación aplicada · salida en 4 o más", 2, 4, False),
        ("Desarrollo Tecnológico", "De 4–5 a 6 o más", 4.5, 6, True),
    ]),
    fuente="PROCIENCIA, bases E041-2026-02 y E041-2026-03",
    notas=[
        "El concurso de investigación aplicada (PIA) exige empezar como mínimo en TRL 2; la "
        "modalidad Semilla no exige subir de nivel. El PIA y Desarrollo Tecnológico 2026 excluyen "
        "las ciencias sociales y las humanidades, aunque el Manual de Frascati las incluye en la "
        "I+D.",
        "Cada concurso fija entregables distintos. El PIA pide artículos, una tesis y un "
        "informe de validación del TRL; Desarrollo Tecnológico pide un prototipo en TRL 6, una "
        "tesis de posgrado y un reporte de viabilidad de patente.",
        "La evidencia del TRL debe existir a la fecha de cierre del concurso (PIA 2026). "
        "PROCIENCIA aplica la Directiva 001-2022-CONCYTEC-P y recomienda la Calculadora TRL de la "
        "plataforma Vincúlate.",
        "Desarrollo Tecnológico es el instrumento de PROCIENCIA para el tramo del valle de la "
        "muerte y corresponde a lo que el Manual de Frascati llama desarrollo experimental. "
        "PROINNÓVATE cubre el mismo tramo con su concurso de Validación; no usa un TRL numérico y "
        "pide un prototipo o piloto con el riesgo tecnológico superado.",
        "Dato: el concurso Desafíos de Innovación para el Desarrollo Regional 2024 de "
        "PROCIENCIA, modalidad Validación, exigía TRL 6 como mínimo de entrada. Entre los "
        "seleccionados está una estación de monitoreo de calidad de agua y dosificación de "
        "floc bacteriano para piscigranjas, con aprendizaje automático e internet de las cosas, "
        "del Instituto Nacional de Investigación y Capacitación de Telecomunicaciones "
        "(INICTEL-UNI), unidad ejecutora de la UNI (S/ 367 600, RDE 084-2024).",
        "Dato: Brasil creó la Empresa Brasileira de Pesquisa e Inovação Industrial (EMBRAPII), "
        "que aporta hasta un tercio del costo de proyectos en TRL 3 a 6 entre una empresa y un "
        "centro acreditado; desde 2014 suma más de 3 500 proyectos.",
        "PROCIENCIA no financia la compra ni la validación de tecnología «llave en mano», "
        "término de las bases para la tecnología adquirida lista para operar.",
        "Verificar antes de la clase: el reparto del cofinanciamiento de EMBRAPII (Portal da "
        "Indústria, «Saiba o que é a Embrapii»).",
    ],
))

L.append(recursos(
    "recursos-sistema",
    "02 · Recursos recomendados",
    "Recursos sobre modelos de innovación y política de CTI",
    [
        {"tipo": "Artículo", "titulo": "The Linear Model of Innovation: The Historical Construction of an Analytical Framework",
         "autor": "Benoît Godin, Science, Technology, & Human Values, 2006",
         "detalle": "Origen histórico del modelo lineal de innovación y su persistencia",
         "url": "doi.org/10.1177/0162243906291865",
         "enlace": "https://doi.org/10.1177/0162243906291865"},
        {"tipo": "Artículo", "titulo": "La ciencia y la tecnología en el desarrollo futuro de América Latina",
         "autor": "Jorge Sábato y Natalio Botana, 1968",
         "detalle": "Relación entre gobierno, infraestructura científica y estructura productiva",
         "url": "proglocode.unam.mx · Sábato y Botana (1968)",
         "enlace": "https://proglocode.unam.mx/files/S%C3%A1bato%20y%20Botana%201968_La%20ciencia%20y%20la%20tecnolog%C3%ADa%20en%20el%20desarrollo%20futuro%20de%20AL%20%5BDoc5%5D.pdf"},
        {"tipo": "Libro", "titulo": "La política de innovación en América Latina y el Caribe: nuevos caminos",
         "autor": "Olivari y Navarro (eds.), BID, 2016",
         "detalle": "Instrumentos públicos de apoyo a la innovación en América Latina",
         "url": "doi.org/10.18235/0000338",
         "enlace": "https://doi.org/10.18235/0000338"},
        {"tipo": "Libro", "titulo": "El Estado emprendedor",
         "autor": "Mariana Mazzucato, Taurus, 2022",
         "detalle": "Papel del Estado como inversor en etapas de alto riesgo tecnológico",
         "url": "marianamazzucato.com/books/the-entrepreneurial-state",
         "enlace": "https://marianamazzucato.com/books/the-entrepreneurial-state"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "Godin (2006) reconstruye en tres etapas la formación del modelo lineal y sostiene que las estadísticas de I+D explican en parte su vigencia. Complementa la lámina sobre los modelos de Kline y Rosenberg. Acceso por suscripción.",
        "Sábato y Botana (1968) formularon el «triángulo de Sábato» (gobierno, infraestructura científico-tecnológica y estructura productiva), antecedente latinoamericano de la triple y la cuádruple hélice. La copia disponible es un escaneo de la reimpresión de 1975.",
        "El libro del BID trata instrumentos de apoyo a la innovación empresarial, innovación en recursos naturales y servicios, inclusión social y propiedad intelectual; descarga gratuita. Mazzucato desarrolla el papel del Estado en las inversiones de mayor riesgo; edición en español de pago.",
    ],
))

# ---------- U5 · Indicadores del país

L.append(visual(
    "gasto-comparado",
    "02 · Intensidad de I+D",
    "Gasto en I+D como porcentaje del PBI: *Perú* y países seleccionados, 2022-2023",
    barras([
        ("Corea del Sur", 4.96, ""),
        ("OCDE", 2.70, "ref"),
        ("Brasil", 1.19, ""),
        ("América Latina", 0.60, "ref"),
        ("Chile", 0.39, ""),
        ("México", 0.27, ""),
        ("Perú", 0.18, "clave"),
    ], ancho=1376, etq_w=300, fila=58, guia=(0.25, "Meta oficial 2030 · 0,25 %")),
    fuente="RICYT 2025 · OCDE MSTI · OMPI · último dato disponible, 2022–2023 · POLCTI, OP.06.01",
    notas=[
        "Dato: el indicador mide la I+D definida en el Manual de Frascati como porcentaje del "
        "producto bruto interno (PBI). El Perú (0,18 %) gasta la mitad que Chile (0,39 %) y un "
        "tercio del agregado de América Latina y el Caribe (0,60 %). Brasil concentra el 62,5 % "
        "del gasto en I+D de la región, lo que eleva el indicador regional.",
        "Dato: la meta oficial de gasto en I+D para 2030 es 0,25 % del PBI (indicador "
        "OP.06.01); el 1 % que se cita con frecuencia es la aspiración de inversión en I+D+i de "
        "la POLCTI, distinta de esa meta.",
        "Verificar antes de la clase: la meta OP.06.01 (0,25 %) en el PDF del DS 093-2025-PCM.",
    ],
))

L.append(cifra(
    "ciencia-e-innovacion",
    "02 · Producción científica e innovación",
    "×3", "",
    "documentos peruanos en Scopus: 3 657 en 2018 y 11 220 en 2024",
    "Puesto 80 de 139 en el Índice Mundial de Innovación 2026",
    fuente="El Peruano (2026), con datos de CONCYTEC · OMPI, _Global Innovation Index_ 2026",
    oscuro=True,
    notas=[
        "Dato: en Scopus, la producción peruana pasó de 3 657 documentos en 2018 a 11 220 en "
        "2024. En el Índice Mundial de Innovación 2026 de la Organización Mundial de la Propiedad "
        "Intelectual (OMPI), el Perú ocupa el puesto 80 de 139, igual que en 2025; puesto 82 en "
        "resultados y 72 en insumos. Chile ocupa el puesto 51, Brasil el 53, México el 65 y "
        "Colombia el 78.",
        "Dato: la POLCTI fijó como meta el puesto 67 para 2026; el puesto alcanzado está 13 "
        "posiciones por debajo de esa meta.",
        "Scopus cuenta documentos, que son un resultado de la I+D; el Índice Mundial de "
        "Innovación combina insumos y resultados de innovación. La producción se triplicó entre "
        "2018 y 2024, y el puesto en el índice fue el mismo en 2025 y en 2026; los dos periodos "
        "no son comparables.",
    ],
))

L.append(cifra(
    "vinculacion",
    "02 · Cooperación de empresas innovadoras",
    "4,7", "%",
    "de las empresas que innovan colaboró con un laboratorio público",
    "4,1 % colaboró con un centro de investigación",
    fuente="INEI y PRODUCE, ENIIMSEC 2018, citada en la POLCTI 2030",
    notas=[
        "Dato: según la Encuesta Nacional de Innovación en la Industria Manufacturera y Empresas "
        "de Servicios Intensivos en Conocimiento (ENIIMSEC 2018), el 59 % del gasto en "
        "innovación de 2017 correspondió a la adquisición o alquiler de bienes de capital.",
        "Ninguno de los dos datos de la lámina mide la colaboración con universidades.",
        "Implicación para el formulador: es probable que la empresa socia no haya colaborado "
        "antes con un laboratorio o un centro de investigación; la propuesta parte de un problema "
        "de la empresa.",
    ],
))

L.append(tarjetas(
    "restricciones",
    "02 · Restricciones del sistema peruano",
    "Financiamiento y capacidades de I+D en el *Perú*, 2023-2027",
    [
        ("−13 %", "Variación de los fondos de PROCIENCIA de 2026 a 2027"),
        ("3 de 10", "soles de gasto en I+D ejecutados por empresas, 2023"),
        ("47 %", "de los investigadores RENACYT activos se ubica en Lima, 2024"),
        ("−10 %", "presupuesto de CONCYTEC en 2026"),
    ],
    fuente="Gestión y CONCYTEC, 2026 · RICYT · CONCYTEC, RENACYT 2024",
    notas=[
        "Dato: PROCIENCIA pasa de unos S/ 60 millones propios en 2026 a S/ 52,3 millones "
        "aprobados para 2027, sin contar el componente SINACTI II. El presupuesto de CONCYTEC "
        "bajó 10 % en 2026.",
        "Dato: el 47 % corresponde a los investigadores RENACYT activos (2024); en 2015, Lima y "
        "Callao concentraban el 68 % del gasto en I+D. El PIA Multidisciplinarios exige una "
        "entidad asociada de otra región.",
        "Implicación para el formulador: revisar cada requisito de las bases al preparar la "
        "propuesta, porque su incumplimiento la excluye antes de la evaluación técnica; "
        "incorporar la empresa socia desde el inicio y, en el PIA Multidisciplinarios, la "
        "entidad asociada de otra región.",
        "Verificar antes de la clase: si los S/ 52,3 millones de PROCIENCIA 2027 incluyen "
        "préstamo.",
    ],
))

L.append(visual(
    "ley-30309",
    "02 · Beneficio tributario a la I+D",
    "Proyectos aprobados para el beneficio tributario de la *Ley 30309*, 2016 y 2019",
    pendiente("2016", 11, "8 aprobados de 72 presentados", "2019", 54, "26 aprobados de 48 presentados"),
    fuente="CONCYTEC, _Política Nacional de CTI al 2030_, Tabla 10",
    notas=[
        "Dato: la Ley 30309 permite a una empresa deducir del impuesto a la renta un porcentaje "
        "adicional de su gasto en proyectos de I+D+i si CONCYTEC califica el proyecto. En 2016 "
        "se aprobó 1 de cada 9 proyectos.",
        "Entre 2016 y 2019 el incentivo fue el mismo; subió con el DU 010-2019 (noviembre "
        "de 2019). En el mismo periodo bajaron las postulaciones y en 2019 cambió la directiva "
        "de calificación, de modo que la causa del aumento de la tasa de aprobación no está "
        "demostrada.",
        "La Ley 32539 (dic. 2025) prorrogó el beneficio hasta 2028.",
        "La calificación de la Ley 30309 no es un concurso, pero, como los concursos, exige "
        "demostrar que el proyecto es I+D+i.",
        "Verificar antes de la clase: fecha de la Directiva 001-2019-CONCYTEC-DPP.",
    ],
))

L.append(recursos(
    "recursos-indicadores",
    "02 · Recursos recomendados",
    "Recursos sobre indicadores de ciencia, tecnología e innovación",
    [
        {"tipo": "Sitio web", "titulo": "Research and Development",
         "autor": "Our World in Data, 2023",
         "detalle": "Gasto en I+D, investigadores, publicaciones y patentes por país",
         "url": "ourworldindata.org/research-and-development",
         "enlace": "https://ourworldindata.org/research-and-development"},
        {"tipo": "Base de datos", "titulo": "SCImago Journal & Country Rank: Perú",
         "autor": "SCImago, con datos de Scopus",
         "detalle": "Producción y citación científica del Perú desde 1996, por área",
         "url": "scimagojr.com/countrysearch.php?country=PE",
         "enlace": "https://www.scimagojr.com/countrysearch.php?country=PE"},
        {"tipo": "Guía", "titulo": "Manual de Valencia: indicadores de vinculación de la universidad con el entorno",
         "autor": "OCTS-OEI y RICYT, 2017",
         "detalle": "Indicadores para medir la vinculación de la universidad con su entorno",
         "url": "ricyt.org · Manual de Valencia",
         "enlace": "https://www.ricyt.org/wp-content/uploads/2017/06/files_manual_vinculacion.pdf"},
        {"tipo": "Informe", "titulo": "Informe de la UNESCO sobre la Ciencia 2021: América Latina",
         "autor": "UNESCO, 2021",
         "detalle": "Políticas, gasto, investigadores y publicaciones en América Latina",
         "url": "unesco.org/reports/science/2021/es/latin-america",
         "enlace": "https://www.unesco.org/reports/science/2021/es/latin-america"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "Our World in Data permite repetir y ampliar la comparación del gasto en I+D, con series largas para el Perú y sus vecinos. SCImago usa la misma fuente que el dato de producción científica (Scopus) y agrega citas, índice h y colaboración internacional.",
        "El Manual de Valencia define cómo medir la vinculación desde la universidad, aspecto que no cubren los datos de cooperación de las empresas. Es un documento distinto de El Estado de la Ciencia, ya citado.",
        "El capítulo de la UNESCO describe la inversión estancada, la baja demanda de conocimiento del sector productivo y los cambios frecuentes de rumbo en las políticas de la región. Sus datos llegan a 2018-2019.",
    ],
))

# ---------- U6 · Aplicación a la propuesta

L.append(pasos(
    "coherencia-propuesta",
    "02 · Revisión de elegibilidad",
    "Coherencia entre problema, tipo de I+D, *TRL* y entidad postulante",
    [
        ("Problema", "Población afectada"),
        ("Tipo", "Resultado al cierre"),
        ("TRL", "Nivel inicial y final, con evidencia"),
        ("Programa", "Entidad postulante"),
    ],
    notas=[
        "La evaluación verifica primero la coherencia entre estos cuatro elementos, en la "
        "etapa de elegibilidad y pertinencia; la calidad técnica se califica después.",
        "Error frecuente: presentar a Desarrollo Tecnológico un proyecto en TRL 4 cuyo objetivo "
        "es «entender el mecanismo», o presentar a un fondo de innovación un producto sin "
        "usuarios identificados.",
    ],
))

L.append(caso(
    "caso-qaira",
    "02 · Caso de estudio · empresa de egresados",
    "qAIRa y qHAWAX",
    "Pontificia Universidad Católica del Perú · Lima",
    [
        ("TRL 3–4", "Prototipo de dron con sensores de calidad del aire"),
        ("INDECOPI", "Modelo de utilidad solicitado con la PUCP en 2016 y concedido en 2018"),
        ("TRL 7–8", "qHAWAX: red de monitoreo con municipios de Lima, 2020"),
    ],
    icono("dron"),
    fuente="OMPI, caso de estudio, 2020 · Unión Andina, 2022 · Andina, 2020",
    notas=[
        "El caso reúne los cuatro elementos de la revisión de elegibilidad: problema, tipo de "
        "actividad, TRL y entidad.",
        "GRUPO QAIRA S.A.C. fue fundada por egresados de la PUCP (Mónica Abarca, Carlos Saito, "
        "Francisco Cuéllar y Javier CalvoPérez); la OMPI da 2015 como año de fundación. El modelo de "
        "utilidad se solicitó en 2016 junto con la PUCP y se concedió en 2018: empresa y universidad "
        "son cotitulares. Los TRL son estimaciones del docente.",
        "En 2020 la red qHAWAX tenía siete módulos con la Municipalidad de Lima, Miraflores y San "
        "Borja; la financiaron el Banco Mundial y el CONCYTEC (Andina, 3 de junio de 2020).",
        "El caso muestra una innovación, porque la red se puso en uso con municipios, y la «e» de la "
        "sigla, porque el resultado llegó al mercado mediante una empresa nueva. La sesión 2 trata la "
        "titularidad compartida y el modelo de utilidad.",
        "Verificar antes de la clase: estado actual de la empresa (Andina la presenta activa en mayo "
        "de 2025; otras bases la registran como cerrada).",
    ],
))

L.append(tarjetas(
    "entidades-uni",
    "02 · Primera entidad de destino",
    "Entidades y concursos accesibles a un equipo de la *UNI*",
    [
        ("VRI-UNI", "Concursos internos del Vicerrectorado de Investigación, dirigidos por un docente"),
        ("PROCIENCIA", "Un docente RENACYT es el responsable y un estudiante participa como tesista"),
        ("PROINNÓVATE", "Postula la empresa; la universidad participa como entidad asociada"),
        ("Red CITE", "Validación de prototipos"),
    ],
    clave=0,
    numerar=False,
    iconos=["building", "fund", "rocket", "sliders"],
    fuente="VRI-UNI · PROCIENCIA, bases y calendario 2027 · PROINNÓVATE",
    notas=[
        "Para un estudiante, la vía de acceso más directa a PROCIENCIA es participar como "
        "tesista en un proyecto ganador, porque el PIA exige al menos una tesis y Desarrollo "
        "Tecnológico, una de posgrado.",
        "Dato: la pertinencia de un proyecto se evalúa frente a prioridades publicadas, como la "
        "POLCTI 2030, los desafíos de prioridades nacionales de PROCIENCIA (S/ 20 millones en "
        "2027) o los Objetivos de Desarrollo Sostenible (ODS).",
        "Otras opciones son el beneficio tributario de la Ley 30309, con una empresa, y Horizonte "
        "Europa, programa en el que las entidades peruanas son elegibles para recibir "
        "financiamiento.",
        "Verificar antes de la clase: resolución rectoral vigente de los concursos del VRI-UNI.",
    ],
))

L.append(recursos(
    "recursos-formulacion",
    "02 · Recursos recomendados",
    "Recursos para la formulación de propuestas de I+D+i",
    [
        {"tipo": "Guía", "titulo": "Metodología del marco lógico para la planificación, el seguimiento y la evaluación de proyectos",
         "autor": "Ortegón, Pacheco y Prieto, CEPAL, 2005",
         "detalle": "Árbol de problemas, matriz de marco lógico y evaluación de proyectos",
         "url": "hdl.handle.net/11362/5607",
         "enlace": "https://hdl.handle.net/11362/5607"},
        {"tipo": "Guía", "titulo": "Tipología de proyectos de carácter científico, tecnológico o de innovación, versión 8",
         "autor": "Minciencias, Colombia, 2025",
         "detalle": "Criterios de calificación de proyectos, con TRL inicial y final",
         "url": "minciencias.gov.co · Tipología de proyectos, versión 8",
         "enlace": "https://www.minciencias.gov.co/sites/default/files/upload/paginas/tipologia_de_proyectos_version_8.pdf"},
        {"tipo": "Sitio web", "titulo": "ALICIA: Acceso Libre a Información Científica para la Innovación",
         "autor": "CONCYTEC",
         "detalle": "Tesis y artículos de los repositorios peruanos de acceso abierto",
         "url": "alicia.concytec.gob.pe",
         "enlace": "https://alicia.concytec.gob.pe/"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "El manual de la CEPAL lleva del árbol de problemas a los objetivos y a la matriz con indicadores: la misma secuencia entre problema y resultado que se revisa en la elegibilidad. Se trata en detalle en la sesión 4.",
        "La tipología de Minciencias es un caso latinoamericano de lo que se exige para calificar un proyecto: qué es y qué no es investigación, desarrollo o innovación, antecedentes, novedad y TRL inicial y final. Sirve para comparar con la calificación de la Ley 30309.",
        "ALICIA permite encontrar tesis y artículos de la UNI y de otras universidades por tema e identificar a los docentes que trabajan esos temas, vía de entrada como tesista en proyectos de PROCIENCIA.",
    ],
))

L.append(cierre(
    "sintesis-02",
    "02 · Síntesis",
    "Criterios para elegir la *entidad de destino* de una propuesta",
    [
        "Entidad postulante: define el programa",
        "TRL de partida: dentro del rango del concurso",
        "Equipo de la UNI: VRI-UNI o tesista en PROCIENCIA",
        "Cuádruple hélice: actor ausente en el equipo",
    ],
    notas=[
        "Recapitular el criterio de cada término del tema 02.",
    ],
))

# ================================================================ CIERRE (5 min)

L.append(cierre(
    "sintesis-sesion",
    "Cierre",
    "Tipo de actividad, *TRL* y entidad de destino de una propuesta",
    [
        "Tipo de actividad: I+D, innovación o ambas",
        "Madurez tecnológica: TRL acreditado con evidencia",
        "Entidad de destino: según el postulante y el TRL",
    ],
    ("Sesión 2", "_Startups_, _spin-offs_ y transferencia tecnológica"),
    notas=[
        "Recapitular los contenidos de la sesión: la clasificación de la actividad según los "
        "manuales de Frascati y Oslo, el nivel de madurez acreditado con evidencia y la elección "
        "de la entidad de destino en el sistema peruano.",
        "La sesión 2 trata las dos vías por las que un resultado llega al mercado: la creación "
        "de una empresa nueva, que es la «e» de la sigla, y la licencia a una empresa existente.",
    ],
))

L.append(referencias(
    "fuentes",
    "Referencias de la sesión",
    [
        ("definicion-id", "OCDE (2015). _Manual de Frascati 2015_. París: OECD Publishing."),
        ("cinco-criterios", "PROCIENCIA (2025). Bases E041-2026-02, Investigación Aplicada."),
        ("rutina-o-id", "PROCIENCIA (2024). Investigación Aplicada 2025-02."),
        ("tres-tipos", "PROCIENCIA. RDE 068-2025, 052-2026 y 087-2026."),
        ("definicion-innovacion", "OCDE y Eurostat (2018). _Manual de Oslo 2018_, 4.ª ed."),
        ("escala-trl", "Comisión Europea (2014). _Horizonte 2020_, Anexo G (TRL)."),
        ("nivel-probado", "CONCYTEC (2022). Directiva 001-2022-CONCYTEC-P."),
        ("caso-satelites", "nanosats.eu, Chasqui-I · Andina (2014) · Infobae (2025, 28 de octubre), UNI-SAT."),
        ("sin-trl", "Innovation Fund Denmark. _Societal Readiness Levels_."),
        ("modelos-innovacion", "Kline, S. y Rosenberg, N. (1986). An overview of innovation. En _The Positive Sum Strategy_, 275-305."),
        ("cuadruple-helice", "Carayannis, E. y Campbell, D. (2009). Mode 3 and Quadruple Helix. _IJTM_, 46(3/4), 201-234."),
        ("cuadruple-helice", "Congreso de la República (2021). Ley 31250, Ley del SINACTI."),
        ("trl-en-fondos", "PROCIENCIA (2025). Bases E041-2026-03, Desarrollo Tecnológico."),
        ("gasto-comparado", "RICYT y OEI (2025). _El Estado de la Ciencia 2025_. OCDE (2025). MSTI."),
        ("ciencia-e-innovacion", "El Peruano (2026, 11 de febrero). Producción científica peruana. OMPI (2026). _Global Innovation Index 2026_."),
        ("vinculacion", "INEI y PRODUCE (2018). Encuesta Nacional de Innovación en la Industria Manufacturera y Empresas de Servicios Intensivos en Conocimiento (ENIIMSEC)."),
        ("restricciones", "Gestión (2026, 14 de julio). CONCYTEC desembolsará más de S/ 52 millones en 2027."),
        ("ley-30309", "CONCYTEC (2025). _Política Nacional de CTI al 2030_, Tabla 10. Aprobada por DS 093-2025-PCM."),
        ("caso-qaira", "OMPI (2020). Caso de estudio qAIRa. Unión Andina (2022). qAIRa case."),
        ("entidades-uni", "PROCIENCIA (2026). Calendario de concursos 2027. Comisión Europea (2026). Países participantes en Horizonte Europa."),
    ],
))

construir("clase-01", "Sesión 1 · Fundamentos y ecosistema I+D+i+e", L)
