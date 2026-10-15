#!/usr/bin/env python3
"""Sesión 6 · Pitch y sustentación de proyectos — formato ponencia (11.ª edición).

Sesión de unos 90 minutos, la mitad que las demás: un solo bloque, sin receso y
con un único tema, «Pitch y sustentación de proyectos». Cierra el curso.

Secuencia (scratchpad/inv-s6.md, §e): U1 relato técnico y tipos de audiencia
→ U2 estructura del pitch y material de apoyo → U3 preguntas técnicas y
financieras del jurado → síntesis de la sesión y de las seis sesiones del
curso. Cada lámina lleva en el antetítulo el número del tema y el nombre del
bloque; cada unidad cierra con una lámina de recursos, como en la sesión 5, y no
hay lámina de sección por unidad. Cambio
frente a la secuencia: la lámina de los bloques del pitch compara Sequoia, la
NSF y StartUp Perú 13G, sin la guía de Y Combinator, que queda como recurso.

Ejemplos (uno por lámina de caso; ninguno usado en las sesiones 1 a 5):
PredictaMAR, resumen EGU26-22690 (relato ABT); Le Qara, Arequipa (tres
audiencias); delegación peruana en StartCo 2026 (solicitud ante inversionistas);
TRAZA, Startup UNI (demostración); Demo Day de IMPULSO 2G, Startup UNI (ronda de
preguntas). Las preguntas de la lámina de tipos de pregunta son citas textuales
de Kanze et al. (2018), sin nombre de empresa. Recursos: scratchpad/recursos-s6.md
(4 por unidad); Olson (2015) y Dahlstrom (2014) se citan en clase y se
sustituyen en la U1 por Valeiras-Jurado (2019).

Formato expositivo: la sesión no incluye actividades en el aula. Las notas
reúnen contenido de respaldo con dato y fuente, errores frecuentes y puntos
por verificar.

Antes de dictar, verificar: lista ratificada de StartUp Perú 13G; estado de la
validación de campo de PredictaMAR; monto y formato del premio Elsevier-ISC3
de Le Qara; estado de financiamiento de TRAZA.

Uso:  python3 tools/ponencia/clase-06.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from graficos import deck_portada, icono_s6, linea_tiempo, matriz_guias  # noqa: E402
from plantillas import (  # noqa: E402
    agenda, caso, cierre, cifra, construir, pasos, portada, recursos, referencias, seccion,
    tarjetas, visual,
)

FUENTE_REC = "Enlaces verificados en octubre de 2026"
SUP = "PROINNÓVATE, bases finales EIN StartUp Perú 13G"
KANZE = "Kanze, Huang, Conley y Higgins, _Academy of Management Journal_, 2018"

# Recursos recomendados por unidad (scratchpad/recursos-s6.md). Cada entrada:
# (slug, antetítulo, titular, items, notas).
RECURSOS = {
    "U1": ("recursos-relato", "01 · Recursos recomendados",
           "Recursos sobre *narrativa* y exposición oral de la investigación", [
        {"tipo": "Artículo", "titulo": "Contemos la ciencia: una revisión de ideas sobre _storytelling_…",
         "autor": "Rueda, Rosen y Crúz-Mena, Mètode Science Studies Journal, 2023",
         "detalle": "Revisión de estudios sobre narrativa en la comunicación pública de la ciencia",
         "url": "metode.es · Contemos la ciencia (Rueda et al.)",
         "enlace": "https://metode.es/wp-content/uploads/2023/12/119ES-MONO3-rueda-contemos-ciencia.pdf"},
        {"tipo": "Artículo", "titulo": "Rhetorical Analysis of a Discourse Model in the Business World…",
         "autor": "Santiago-Guervós, Círculo de Lingüística Aplicada a la Comunicación, 2019",
         "detalle": "Análisis retórico de dos _elevator pitch_ en español, uno eficaz y otro fallido",
         "url": "doi.org/10.5209/clac.66597",
         "enlace": "https://doi.org/10.5209/clac.66597"},
        {"tipo": "Artículo", "titulo": "Modal coherence in specialised discourse…",
         "autor": "Valeiras-Jurado, Ibérica, 37, 2019",
         "detalle": "Comparación multimodal de un _pitch_ de producto y una charla de divulgación",
         "url": "revistaiberica.org · Ibérica 37 (2019)",
         "enlace": "https://www.revistaiberica.org/index.php/iberica/article/view/111"},
        {"tipo": "Sitio web", "titulo": "Watch 3MT presentations from around the world",
         "autor": "Universidad de Queensland, Three Minute Thesis, desde 2008",
         "detalle": "Videos de ganadores que exponen una tesis doctoral en tres minutos",
         "url": "threeminutethesis.uq.edu.au/watch-3mt",
         "enlace": "https://threeminutethesis.uq.edu.au/watch-3mt"},
    ], [
        "El artículo de Rueda, Rosen y Crúz-Mena (UNAM), en español y con licencia CC BY-SA 4.0, "
        "identifica tres estructuras narrativas dominantes en la comunicación de la ciencia y "
        "discute la emoción y la persuasión; el QR abre el PDF de la revista Mètode.",
        "Santiago-Guervós (Universidad de Salamanca) analiza dos _elevator pitch_ en español con "
        "los cánones de la retórica clásica: estudio del destinatario, orden del discurso, léxico "
        "y puesta en escena. Valeiras-Jurado (Universidad de Gante) compara un _pitch_ de "
        "producto con una charla de divulgación de resultados de investigación y atribuye la "
        "eficacia persuasiva a la coherencia entre palabra, gesto, voz e imagen.",
        "La Tesis en Tres Minutos (3MT, _Three Minute Thesis_) nació en la Universidad de "
        "Queensland en 2008; la página reúne videos de ganadores, varios de ingeniería, "
        "expuestos ante un jurado académico y un público no especializado.",
    ]),
    "U2": ("recursos-estructura", "01 · Recursos recomendados",
           "Recursos sobre la estructura y el material de un *_pitch_*", [
        {"tipo": "Guía", "titulo": "How to build your seed round pitch deck",
         "autor": "Aaron Harris, Y Combinator, 2018",
         "detalle": "Plantilla de presentación para una ronda semilla, lámina por lámina",
         "url": "ycombinator.com · Seed round pitch deck",
         "enlace": "https://www.ycombinator.com/library/2u-how-to-build-your-seed-round-pitch-deck"},
        {"tipo": "Guía", "titulo": "Guía rápida para elaborar tu Pitch Deck",
         "autor": "Instituto Nacional de Ciberseguridad (INCIBE), España, 2024",
         "detalle": "Trece secciones de un _pitch deck_ con un caso ficticio",
         "url": "incibe.es · Guía rápida de INCIBE (2024)",
         "enlace": "https://www.incibe.es/emprendimiento/publicaciones/guias-y-estudios/guias/guia-rapida-para-elaborar-tu-pitch-deck"},
        {"tipo": "Libro", "titulo": "The Craft of Scientific Presentations, 2.ª edición",
         "autor": "Michael Alley, Springer, 2013",
         "detalle": "Láminas con titular-afirmación y evidencia visual, y preparación de la exposición",
         "url": "doi.org/10.1007/978-1-4419-8279-7",
         "enlace": "https://doi.org/10.1007/978-1-4419-8279-7"},
        {"tipo": "Guía", "titulo": "EIC Accelerator. Guide for applicants, versión 6.0",
         "autor": "Consejo Europeo de Innovación (EIC), 2025",
         "detalle": "Requisitos de la presentación, del video y de la entrevista ante el jurado",
         "url": "eic.ec.europa.eu · EIC Accelerator, guide for applicants",
         "enlace": "https://eic.ec.europa.eu/document/download/9d96fbf3-4d85-4ad0-9483-c77ce348111d_en?filename=EIC%20Accelerator%20guide%20for%20applicants_WP26.pdf"},
    ], [
        "La guía de Aaron Harris recorre las láminas de una presentación para una ronda semilla "
        "en el orden de la unidad: problema, solución, tracción, mercado, equipo y solicitud.",
        "La guía del INCIBE, en español, incluye resumen ejecutivo, proyecciones financieras y "
        "una sección de errores comunes; el caso es de ciberseguridad y la estructura sirve para "
        "cualquier proyecto de base tecnológica. El libro de Alley desarrolla el diseño de "
        "láminas con un titular en oración completa y evidencia visual; el curso usa titulares "
        "en sintagma nominal, por norma propia.",
        "La guía del Consejo Europeo de Innovación corresponde a un fondo público que pide a la "
        "empresa una presentación de láminas, un video y una entrevista con jurado; se publica "
        "con ISBN y DOI de la Oficina de Publicaciones de la Unión Europea.",
    ]),
    "U3": ("recursos-preguntas", "01 · Recursos recomendados",
           "Recursos sobre entrevistas ante *paneles* y preguntas de un jurado", [
        {"tipo": "Guía", "titulo": "ERC Starting Grant Online Interview. Notes and Tips",
         "autor": "Agencia austriaca de fomento de la investigación (FFG), abril de 2026",
         "detalle": "Preguntas habituales de los paneles europeos sobre riesgo, presupuesto y equipo",
         "url": "univie.ac.at · FFG, ERC interview notes (2026)",
         "enlace": "https://projektservice-mathematik.univie.ac.at/fileadmin/user_upload/p_projektservice_mathematik/PDFs/EU/ERC/2026/FFG_Notes_Interview_StG_Apr26.pdf"},
        {"tipo": "Guía", "titulo": "Example Interview Process and Questions for Candidates",
         "autor": "UK Research and Innovation, Future Leaders Fellowships, 2023",
         "detalle": "Exposición de cinco minutos seguida de tres bloques de preguntas del panel",
         "url": "ukri.org · FLF example interview questions",
         "enlace": "https://www.ukri.org/wp-content/uploads/2023/02/UKRI-150823-Funding-Opp-FutureLeadersFellowships-ExampleInterviewProcessQuestions.pdf"},
        {"tipo": "Artículo", "titulo": "Estrategias didácticas y recomendaciones para la defensa oral…",
         "autor": "Onieva López, REIFOP, 2016",
         "detalle": "Rúbricas de tribunales universitarios y pautas para responder en una defensa oral",
         "url": "doi.org/10.6018/reifop.19.3.206331",
         "enlace": "https://doi.org/10.6018/reifop.19.3.206331"},
        {"tipo": "Artículo", "titulo": "El perfil del emprendedor que apoyan los fondos de capital privado…",
         "autor": "Santillán Salgado et al., Contaduría y Administración, 2015",
         "detalle": "Encuesta a fondos mexicanos sobre los rasgos del emprendedor que evalúan",
         "url": "cya.unam.mx/index.php/cya/article/view/818",
         "enlace": "https://www.cya.unam.mx/index.php/cya/article/view/818"},
    ], [
        "Las notas de la FFG (Österreichische Forschungsförderungsgesellschaft), punto nacional de "
        "contacto del Consejo Europeo de Investigación (ERC) en Austria, recogen preguntas de "
        "los paneles: qué hace único al proyecto, cuál es el riesgo principal y su alternativa, "
        "qué ocurre si no se financia una parte del equipo.",
        "La ficha de UK Research and Innovation describe una entrevista en que cada miembro del "
        "panel pregunta durante 7 minutos sobre un eje fijo. El artículo de Onieva López "
        "(Revista Electrónica Interuniversitaria de Formación del Profesorado, REIFOP) compara "
        "planillas de tribunales; una de ellas asigna 12 % a la exactitud de las respuestas.",
        "Santillán Salgado, Gaona Domínguez y Hernández Perales encuestan a fondos mexicanos de "
        "capital privado y capital emprendedor sobre experiencia, liderazgo, integridad y "
        "trabajo en equipo del emprendedor: evidencia latinoamericana sobre las preguntas de "
        "equipo.",
    ]),
}

L = []


def rec(clave):
    """Lámina de recursos de la unidad."""
    slug, ceja, tit, items, notas = RECURSOS[clave]
    L.append(recursos(slug, ceja, tit, items, fuente=FUENTE_REC, notas=notas))


# ================================================================ APERTURA (4 min)

L.append(portada(
    "portada",
    "Sesión 6 · Diseño y Gestión de Proyectos {I+D+i+e}",
    "_Pitch_ y sustentación de proyectos",
    "Relato técnico de un proyecto de ciencia y tecnología según la audiencia y "
    "sustentación ante un comité o un jurado",
    ["_Pitch_ y sustentación de proyectos"],
    "Abraham Caso-Torres · OTI-UNI · CC BY-SA 4.0",
    visual=deck_portada(),
    notas=[
        "Dar la bienvenida y presentar el tema único de la sesión 6, última del curso: la "
        "presentación oral de un proyecto ante quien decide su financiamiento o su selección, "
        "con el material que la acompaña y la ronda de preguntas que la sigue.",
        "La sesión dura 90 minutos, en un bloque único, y es expositiva. Cada caso es un "
        "proyecto o un evento distinto de los usados en las sesiones 1 a 5.",
    ],
))

L.append(agenda(
    "agenda",
    "Agenda",
    "Contenidos de la *sesión 6* y cierre del curso",
    [
        ("_Pitch_ y sustentación de proyectos",
         ["Relato técnico y tipos de audiencia",
          "Estructura del _pitch_ y material de apoyo",
          "Preguntas técnicas y financieras del jurado",
          "Síntesis de la sesión y de las seis sesiones del curso"]),
    ],
    notas=[
        "Presentar las tres unidades del tema y el cierre del curso.",
        "Tiempo: apertura, 4 min; relato técnico y audiencias, 27; estructura y material de "
        "apoyo, 29; preguntas del jurado, 21; síntesis de la sesión y del curso, 9.",
        "La sesión usa material de la sesión 5: el resumen técnico, la ficha tecnológica y el "
        "video de tres minutos para la difusión de resultados que se compromete a elaborar un "
        "proyecto de Desarrollo Tecnológico de PROCIENCIA. "
        "El tema de tendencias mundiales en I+D+i+e del sílabo no se dicta en esta edición.",
    ],
))

L.append(seccion(
    "tema-01", "01", "_Pitch_ y sustentación de proyectos",
    "Relato técnico según la audiencia, estructura del _pitch_, material de apoyo y "
    "preguntas de un jurado",
    temas=1,
    notas=[
        "Presentar el tema, que trata la exposición de un proyecto de ciencia y tecnología "
        "ante inversionistas, comités de fondos públicos y jurados, y la ronda de preguntas "
        "que la sigue.",
        "Tiempo: 77 minutos; relato técnico y audiencias, 27; estructura y material de apoyo, "
        "29; preguntas del jurado, 21.",
    ],
))

# ---------- U1 · Relato técnico y tipos de audiencia (27 min)

L.append(tarjetas(
    "definiciones-pitch",
    "01 · Términos del _pitch_",
    "Términos de la presentación oral de un *proyecto* ante quien decide",
    [
        ("_Pitch_", "Exposición o argumentos para persuadir a quien decide"),
        ("_Elevator pitch_", "Exposición verbal breve, en general de menos de dos minutos"),
        ("_Pitch deck_", "Láminas que acompañan la exposición o se envían para su lectura"),
        ("_Demo day_", "Presentación pública con que culmina un programa de aceleración"),
        ("Sustentación", "Exposición ante un comité o un jurado seguida de preguntas; "
                         "«entrevista» en las bases de fondos peruanos"),
    ],
    clave=4,
    iconos=["quote", "clock", "layers", "users", "rubric"],
    fuente="_Oxford Advanced Learner's Dictionary_, 2026 · Clingingsmith y Shane, "
           "_Management Science_, 2018 · Cohen y Hochberg, SSRN 2418000, 2014 · " + SUP + ", num. 37",
    notas=[
        "El diccionario de Oxford define _pitch_ como la exposición o los argumentos con que una "
        "persona intenta vender algo o persuadir a otros de hacer algo, y da como ejemplo «a "
        "cada empresa se le dieron diez minutos para su _pitch_». El nombre _elevator pitch_ "
        "alude a la exposición que cabe en un viaje breve de ascensor con un alto directivo.",
        "Clingingsmith y Shane (2018) describen el _elevator pitch_ como una breve presentación "
        "verbal de un negocio, en general de menos de dos minutos, cuyo fin es que el "
        "inversionista quiera seguir conversando. Las duraciones de 30 a 60 segundos que dan "
        "algunas guías no tienen fuente académica.",
        "Cohen y Hochberg (2014) definen la aceleradora como un programa de duración fija, por "
        "cohortes, con mentoría y formación, que culmina en un evento público de _pitch_ o "
        "_demo day_. Las aceleradoras y sus efectos se presentaron en la sesión 3.",
        "Dato: las bases de StartUp Perú 13G no usan la palabra sustentación; el comité técnico "
        "evalúa «luego de una entrevista de obligatorio cumplimiento al Líder Emprendedor» "
        "(num. 37).",
        "Los equivalentes en español son discurso de ascensor, presentación de láminas y día "
        "de demostración. Los términos en inglés van en cursiva.",
        "Verificar antes de la clase: el texto de Cohen y Hochberg (2014), leído en citas "
        "secundarias porque el repositorio SSRN no respondió.",
    ],
))

L.append(pasos(
    "relato-abt",
    "01 · Estructura narrativa",
    "Estructura narrativa *ABT* de Olson (2015) para un relato técnico",
    [
        ("Y (_and_)", "Hechos aceptados que sitúan el problema y su magnitud"),
        ("Pero (_but_)", "Brecha o conflicto que deja el problema sin resolver"),
        ("Por lo tanto (_therefore_)", "Respuesta del proyecto y resultado esperado, con "
                                        "número y unidad"),
    ],
    clave=2,
    fuente="Olson, _Houston, We Have a Narrative_, University of Chicago Press, 2015 · "
           "Dahlstrom, _PNAS_, 111(supl. 4), 2014",
    notas=[
        "ABT es la sigla de _And, But, Therefore_, «y, pero, por lo tanto». Randy Olson, biólogo "
        "marino y cineasta, la propone en el libro _Houston, We Have a Narrative_ (2015): «y» "
        "añade contexto, «pero» introduce el conflicto y «por lo tanto» da la resolución. La "
        "adapta de una regla de los guionistas de _South Park_, que sustituyen «y» por «pero» o "
        "«por lo tanto» al encadenar escenas (dato de prensa).",
        "Dahlstrom (2014, _Proceedings of the National Academy of Sciences_, PNAS) define la "
        "narrativa por tres rasgos: relaciones de causa y efecto entre hechos, un periodo "
        "determinado y personajes concretos. En un proyecto técnico, el personaje es el usuario "
        "o el beneficiario.",
        "Dato: según Dahlstrom (2014), la narrativa se lee el doble de rápido y se recuerda el "
        "doble que el texto expositivo, con independencia de la familiaridad o el interés del "
        "lector; la cifra procede de estudios de Graesser y colaboradores (1995 y 2002), no "
        "leídos para esta sesión.",
        "Dato: en 732 resúmenes sobre cambio climático de 19 revistas, los más narrativos "
        "recibieron más citas (Hillier, Kelly y Klinger, 2016, _PLoS ONE_). La relación es "
        "correlacional y se asocia también a la revista.",
        "Dato: en prospectos de oferta pública inicial (OPI) de 1996 a 2000 en tres industrias "
        "de alta tecnología, la narrativa influyó en la obtención de recursos tras controlar "
        "otros factores (Martens, Jennings y Jennings, 2007, _Academy of Management Journal_).",
        "Error frecuente: un «por lo tanto» sin cifra ni unidad.",
    ],
))

L.append(caso(
    "caso-abt",
    "01 · Caso de estudio · relato ABT",
    "PredictaMAR",
    "Randy Warthon y Maik Valenzuela · Lima · resumen de congreso EGU26-22690, 2026",
    [
        ("Y", "Pesca artesanal con incertidumbre al elegir la zona de pesca"),
        ("Pero", "Exploración con costo de tiempo y combustible"),
        ("Por lo tanto", "Probabilidad de presencia por especie; −20 a −25 % de "
                         "combustible por viaje"),
    ],
    icono_s6("embarcacion"),
    fuente="Warthon y Valenzuela, EGU26-22690, EGU General Assembly 2026, "
           "doi.org/10.5194/egusphere-egu26-22690",
    notas=[
        "PredictaMAR es una plataforma de apoyo a la decisión para la pesca artesanal, de dos "
        "investigadores independientes de Miraflores, Lima, presentada como resumen en la "
        "sesión OS4.8 de la Asamblea General 2026 de la Unión Europea de Geociencias (EGU)."
        " La lámina reconstruye el resumen "
        "con la estructura ABT.",
        "El sistema combina clorofila, temperatura superficial del mar, batimetría, salinidad y "
        "circulación del Servicio Marino de Copernicus, programa de observación de la Tierra de la "
        "Unión Europea, con una ponderación por especie "
        "construida con literatura, incluida la del Instituto del Mar del Perú (IMARPE). Estima "
        "una probabilidad de presencia y no una predicción determinista.",
        "Dato: las estimaciones preliminares del resumen son de 15 % a 30 % menos distancia de "
        "navegación y de 20 % a 25 % menos combustible por viaje en embarcaciones pequeñas con "
        "motor fuera de borda.",
        "Un resumen de congreso no pasa por revisión por pares; las cifras son preliminares y "
        "la validación de campo con pescadores artesanales sigue en curso.",
        "Verificar antes de la clase: el estado de la validación de campo.",
    ],
))

L.append(tarjetas(
    "audiencias",
    "01 · Tipos de audiencia",
    "Audiencias de un *_pitch_* de ciencia y tecnología y objeto de su decisión",
    [
        ("Inversionista de capital de riesgo", "Retorno esperado frente al riesgo, con el "
                                               "equipo como factor más citado"),
        ("Comité o panel de un fondo público", "Cumplimiento de bases y cartilla publicadas; "
                                               "propuesta escrita, video y, en algunos "
                                               "concursos, entrevista"),
        ("Jurado académico", "Rigor del método y claridad; en una rúbrica de tribunal, 12 % "
                             "de la nota por la exactitud de las respuestas"),
    ],
    clave=1,
    iconos=["fund", "building", "users"],
    fuente="Gompers et al., _J. Financial Economics_, 2020 · " + SUP
           + ", num. 29-40 · PROCIENCIA, bases E041-2025-01-BM, Anexo 11 · Onieva López, "
           "2016",
    notas=[
        "Dato: por cada inversión cerrada, una firma de capital de riesgo considera unas 100 "
        "oportunidades; una de cada cuatro llega a una reunión con el equipo, un tercio de "
        "esas pasa a la reunión de socios, la mitad a la debida diligencia y un tercio recibe "
        "una hoja de términos (Gompers et al., 2020; tabla 6 del documento de trabajo de "
        "2016).",
        "Los criterios de los inversionistas ángeles se presentaron en la sesión 3.",
        "Dato: en un fondo público el panel puede deliberar sin exposición del postulante. En "
        "Emprendimiento Académico de PROCIENCIA, el panel de selección tiene de 4 a 6 "
        "miembros: al menos 3 expertos técnicos, 1 representante de la industria y desarrollo "
        "de negocios y 1 profesional en comercialización de resultados o gestión de "
        "tecnología, más un secretario sin voto. Las bases no prevén exposición del postulante "
        "(bases E041-2025-01-BM, Anexo 11, num. 3).",
        "Un jurado académico (tribunal de tesis, comité de un congreso o concurso de "
        "exposición) evalúa el rigor del método, la comprensión por un público no "
        "especializado y las respuestas. El recurso de la Universidad de Queensland al cierre "
        "de la unidad reúne ejemplos.",
        "Dato: en la planilla de la Facultad de Ciencias del Deporte de la Universidad de "
        "Castilla-La Mancha que reproduce Onieva López (2016), la defensa oral vale 40 % de la "
        "nota del trabajo de fin de grado y la exactitud de las respuestas al tribunal, 12 %.",
        "Implicación para el formulador: el mismo proyecto se presenta con un énfasis distinto "
        "según el objeto de la decisión de cada audiencia.",
    ],
))

L.append(caso(
    "caso-tres-audiencias",
    "01 · Caso de estudio · tres audiencias",
    "Le Qara",
    "Jacqueline e Isemar Cruz Loayza · Arequipa · biocuero producido por microorganismos "
    "con residuos vegetales y frutales",
    [
        ("2019", "StartUp Perú, 7.ª edición, una de cinco ganadoras de Arequipa"),
        ("2020", "Premio de química sostenible de la Fundación Elsevier"),
        ("2022", "K-Startup Grand Challenge, aceleradora del gobierno de Corea del Sur"),
    ],
    icono_s6("biocuero"),
    fuente="Andina, 7-10-2019 y 19-12-2020 · DPL News, 30-1-2023",
    notas=[
        "Le Qara la fundaron Jacqueline Cruz Loayza, ingeniera industrial de la Universidad "
        "Católica San Pablo (UCSP), e Isemar Cruz Loayza, biotecnóloga y diseñadora. El "
        "material es un biocuero producido por microorganismos que se alimentan de residuos "
        "vegetales y frutales.",
        "Dato: en 2019 fue una de las cinco ganadoras arequipeñas de la 7.ª edición de StartUp "
        "Perú; Andina menciona un "
        "capital semilla de S/ 50 000 sin precisar si es por proyecto. Cuatro de los cinco "
        "ganadores de esa región salían de Kaman, la incubadora de la UCSP.",
        "Dato: en diciembre de 2020 recibió el premio «Espíritu Emprendedor en Química "
        "Sostenible» de la Fundación Elsevier y el Centro Colaborativo Internacional de "
        "Química Sostenible (ISC3), frente a finalistas de Estados Unidos, Países Bajos y "
        "Nigeria. En 2022 ganó el K-Startup Grand Challenge, con apoyo del gobierno coreano "
        "para abrir una sucursal.",
        "Cada audiencia evalúa un aspecto distinto: el fondo público, el mérito innovador y el "
        "equipo; el jurado de química sostenible, el proceso; la aceleradora extranjera, el "
        "mercado y la escala. La lectura es del docente; las notas de prensa no describen el "
        "formato de cada presentación.",
        "Verificar antes de la clase: el monto del premio de 2020 y el formato del _pitch_ en "
        "las dos competencias internacionales.",
    ],
))

rec("U1")

# ---------- U2 · Estructura del pitch y material de apoyo (29 min)

L.append(visual(
    "bloques-del-pitch",
    "01 · Estructura del _pitch_",
    "Bloques de un *_pitch_* en tres guías: Sequoia, NSF y StartUp Perú 13G",
    matriz_guias(
        ["Sequoia Capital · 10 secciones", "NSF · Project Pitch, 4 secciones",
         "StartUp Perú 13G · video y evaluación"],
        [
            ("Problema", ["Problema", "Cliente y necesidad, en oportunidad de mercado",
                          "Problema (video)"]),
            ("Solución", ["Solución · por qué ahora", "Innovación tecnológica · objetivos y "
                          "desafíos técnicos", "Solución y carácter innovador (video)"]),
            ("Mercado", ["Mercado, competencia y modelo de negocio",
                         "Oportunidad de mercado", "Mercado, 10 %"]),
            ("Equipo", ["Equipo", "Empresa y equipo", "Composición y capacidad de "
                                                      "ejecución, 40 %"]),
            ("Tracción", ["Finanzas, si existen", "", "Tracción, 10 %"]),
            ("Solicitud", ["", "", "Plan de ejecución del capital semilla, 5 %"]),
        ],
        nota="GUION = LA GUÍA NO PIDE EL BLOQUE · CORRESPONDENCIA DEL DOCENTE",
        alto=60,
    ),
    fuente="Sequoia Capital, _Writing a business plan_ · Fundación Nacional de Ciencias de "
           "EE. UU. (NSF), _Project Pitch_ · " + SUP + ", num. 29.i y 33",
    notas=[
        "Los seis bloques ordenan el contenido de un _pitch_: quién tiene el problema y cuánto "
        "le cuesta; qué hace la tecnología y con qué evidencia, incluido el TRL; quién paga y "
        "cuántos son; por qué este equipo; qué avance medible existe; cuánto se pide, con qué "
        "instrumento y para qué hito. La correspondencia con cada guía es del docente.",
        "La guía de Sequoia Capital tiene diez secciones: propósito de la empresa, problema, "
        "solución, por qué ahora, potencial de mercado, competencia o alternativas, modelo de "
        "negocio, equipo, finanzas, «si las hay», y visión.",
        "El _Project Pitch_ es el primer filtro del programa SBIR/STTR (_Small Business "
        "Innovation Research / Small Business Technology Transfer_) de la NSF: innovación "
        "tecnológica (hasta 3 500 caracteres), objetivos y desafíos técnicos (3 500), "
        "oportunidad de mercado, con perfil del cliente y necesidad (1 750), y empresa y equipo "
        "(1 750). Si la propuesta encaja, la NSF invita a presentar la propuesta completa.",
        "Dato: el video de StartUp Perú 13G, de hasta 3 minutos, responde cuál es el problema, "
        "cómo se soluciona y por qué es innovador; cómo crecerá el emprendimiento y cómo "
        "ejecutará el fondo; quién es el equipo y por qué es el adecuado (num. 29.i). Si "
        "excede los 3 minutos, se revisan los primeros 3 (nota 14).",
        "Dato: la evaluación externa de StartUp Perú 13G asigna mérito innovador 30 %, modelo "
        "de negocio 15 % (tracción 10 % e impacto 5 %), escalabilidad 15 % (mercado 10 % y "
        "plan de ejecución del capital semilla 5 %) y equipo emprendedor 40 % (num. 33).",
        "La solicitud, traducción de _ask_, es el monto que se pide, el instrumento y el hito "
        "que financia. El orden de los bloques puede empezar por el más sólido del proyecto.",
    ],
))

L.append(cifra(
    "equipo-primero",
    "01 · Evidencia sobre inversionistas",
    "47", "%",
    "de las firmas de capital de riesgo encuestadas señala al equipo como el factor más "
    "importante para invertir",
    "Encuesta de 2015-2016 a 885 inversionistas de 681 firmas; 95 % menciona al equipo como "
    "factor importante",
    fuente="Gompers, Gornall, Kaplan y Strebulaev, _Journal of Financial Economics_, "
           "135(1), 2020 · tabla 7 del documento de trabajo NBER 22587, 2016",
    notas=[
        "Dato: después del equipo, los inversionistas mencionan como importantes el modelo de "
        "negocio (83 %), el producto (74 %), el mercado (68 %) y la industria (31 %); los "
        "factores del negocio en conjunto son el más importante para el 37 % (Gompers et al., "
        "2020; tabla 7 del documento de trabajo).",
        "Dato: el equipo es también la causa más citada del éxito (96 %) y del fracaso (92 %) "
        "de las inversiones de la cartera.",
        "El resumen publicado da 885 encuestados; el documento de trabajo de 2016, del que se "
        "leyeron las tablas, da 889. Los porcentajes se calculan por firma.",
        "Dato: StartUp Perú 13G asigna 40 % al equipo emprendedor en la evaluación externa "
        "(num. 33) y 30 % en el comité técnico (num. 39).",
        "Implicación para el formulador: el bloque del equipo nombra a las personas, su "
        "trayectoria verificable y su dedicación al proyecto.",
    ],
))

L.append(caso(
    "caso-solicitud",
    "01 · Caso de estudio · solicitud",
    "StartCo 2026",
    "Delegación peruana de la Comisión de Promoción del Perú para la Exportación y el "
    "Turismo (PROMPERÚ) · Medellín, 16 y 17 de abril de 2026",
    [
        ("16", "_Startups_ de Arequipa, Huancayo, Huánuco y Lima"),
        ("US$ 12 M", "Inversión buscada en conjunto"),
        ("100 000", "_Ticket_ mínimo en US$; rondas de escalamiento de hasta US$ 2,5 "
                    "millones"),
        ("Más de 70", "Reuniones con inversionistas y fondos"),
    ],
    icono_s6("ronda"),
    fuente="Infobae, 7-5-2026 · ProActivo, 2026",
    notas=[
        "StartCo es un evento de inversión en _startups_ de América Latina que se realiza en "
        "Medellín. PROMPERÚ organizó en 2026 la primera delegación peruana: 16 _startups_ que "
        "buscaban en conjunto unos US$ 12 millones, con montos por inversión (_tickets_) desde "
        "US$ 100 000 y rondas de escalamiento de hasta US$ 2,5 millones. Tuvieron más de 70 "
        "reuniones con inversionistas y fondos y más de 200 con empresas.",
        "El monto que pidió cada empresa no es público.",
        "La solicitud de un _pitch_ ante capital de riesgo se expresa como monto, instrumento y "
        "hito que financia; un fondo público fija el monto máximo en sus bases y pide el plan "
        "de uso de los recursos.",
        "Dato: los nombres de algunas empresas difieren entre las fuentes de prensa.",
    ],
))

L.append(tarjetas(
    "sustentacion-fondos",
    "01 · Sustentación en fondos peruanos",
    "Formas de *sustentación* en concursos de PROINNÓVATE y PROCIENCIA, 2026-2027",
    [
        ("StartUp Perú 13G", "Video de 3 min y entrevista al líder ante el comité"),
        ("Innovación Empresarial", "Concurso regional · video de 3 min; comité sin entrevista"),
        ("Validación de la Innovación", "Concurso regional · video de 5 min con el prototipo"),
        ("Desarrollo Tecnológico 2027", "PROCIENCIA · video de 5 min; panel sin exposición"),
    ],
    clave=0,
    iconos=["users", "play", "simulate", "rubric"],
    fuente="PROINNÓVATE, bases EIN 13G, num. 29.i y 37 · bases regionales de San Martín, "
           "2026, num. 41, 45 y 49 · PROCIENCIA, bases E041-2027-02",
    notas=[
        "Dato: en StartUp Perú 13G, el comité técnico evalúa luego de una entrevista "
        "obligatoria al líder emprendedor y valora la participación de los demás miembros "
        "(num. 37). Califica por consenso, de 1 a 4: mérito innovador 35 %, modelo de negocio y "
        "escalabilidad 35 % y equipo emprendedor 30 %; aprueba con 3 o más en el total y en "
        "los dos primeros criterios (num. 39-40). Las bases no fijan la duración de la "
        "entrevista.",
        "Dato: la bonificación de 15 % sobre el puntaje, por una propuesta de valor basada en "
        "sostenibilidad ambiental o adaptación al cambio climático, se verifica mediante una "
        "entrevista con un especialista (num. 41).",
        "Dato: en los concursos regionales de PROINNÓVATE 2026, Innovación Empresarial pide "
        "un video de hasta 3 minutos con el problema, la solución innovadora y los pasos "
        "técnicos, y el comité evalúa «luego de revisar la propuesta, evaluaciones externas y "
        "el video» (num. 41.vi y 49). Validación de la Innovación pide un video de hasta 5 "
        "minutos que muestre el prototipo, su avance y sus funcionalidades (num. 45.vi). Se "
        "leyeron las bases iniciales de San Martín, de marzo de 2026. Los dos concursos "
        "regionales de emprendimiento del mismo documento, Emprendimiento Innovador y "
        "Emprendimiento Dinámico, sí prevén entrevista.",
        "Dato: en Desarrollo Tecnológico 2027, el video de hasta cinco minutos va en un medio "
        "público, sin contraseña durante todo el concurso (num. 1.5). La evaluación por pares "
        "y el panel de selección se presentaron en la sesión 4; las bases no prevén exposición "
        "oral del postulante.",
        "En el Perú, la exposición oral con preguntas aparece en StartUp Perú, en los "
        "concursos regionales de emprendimiento de PROINNÓVATE (Emprendimiento Innovador y "
        "Emprendimiento Dinámico, con entrevista obligatoria al líder en las bases de San "
        "Martín), en los _demo days_ de las incubadoras y en concursos internacionales; los programas de "
        "PROCIENCIA revisados deciden sobre la propuesta escrita y el video.",
        "Verificar antes de la clase: las bases finales de los concursos regionales.",
    ],
))

L.append(tarjetas(
    "material-de-apoyo",
    "01 · Material de apoyo",
    "Material de apoyo de un *_pitch_* y de una sustentación",
    [
        ("_Pitch deck_", "Láminas de la exposición y una versión para lectura sin "
                         "expositor"),
        ("Video", "3 o 5 min en la postulación, según las bases"),
        ("Resumen ejecutivo", "Una página con problema, resultado, equipo y solicitud"),
        ("Demostración", "Prototipo en funcionamiento, en vivo o grabado"),
        ("Dossier del proyecto", "Bitácora, registros, publicaciones y fotografías con "
                                 "fecha"),
    ],
    clave=3,
    iconos=["layers", "play", "file", "simulate", "folder"],
    fuente="PROCIENCIA, bases E041-2027-02, num. 1.5 y Anexos 4A y 8 · " + SUP + ", num. 29.i",
    notas=[
        "En Desarrollo Tecnológico 2027 hay dos videos: el de postulación, de hasta cinco "
        "minutos (num. 1.5), y el de tres minutos para la difusión de los resultados, que la "
        "entidad se compromete a elaborar (Anexo 4A) y que es financiable como servicio de "
        "terceros (Anexo 8). La ficha tecnológica y el resumen técnico de "
        "la sesión 5 sirven de base para el resumen ejecutivo.",
        "El docente propone un video en cuatro partes: el problema con su magnitud, lo "
        "que se construyó con el prototipo a la vista, lo que se midió con número y unidad, y "
        "lo que sigue y lo que falta. Se graba durante la ejecución del proyecto y no al final.",
        "El docente propone reunir el registro cronológico del proyecto desde la bitácora "
        "durante la ejecución, con la decisión que cambió el rumbo, el "
        "ensayo fallido y lo aprendido, cada uno con fecha y número. Ningún fondo lo exige y "
        "queda como archivo del proyecto.",
        "Dato: los términos de referencia de una consultoría para el Doctorado en Ciencias con "
        "mención en Física de la UNI, programa presentado en la sesión 5, piden por cada tesis "
        "doctoral un _elevator pitch_, un resumen ejecutivo, una presentación comercial y un "
        "video, además de una propuesta de _Innovation Day_ ante empresas, entidades públicas e "
        "inversionistas (VRI-UNI, agosto de 2026).",
        "Error frecuente: abrir con la presentación de la institución, usar imágenes ajenas al "
        "proyecto o anunciar un impacto donde el proyecto entregó un producto.",
    ],
))

L.append(caso(
    "caso-demostracion",
    "01 · Caso de estudio · demostración",
    "TRAZA",
    "Maribel Agredas, CEO · _startup_ incubada en Startup UNI · trazabilidad textil con "
    "_blockchain_",
    [
        ("8-10 sep.", "Feria UNICTEC 2026, en la UNI"),
        ("DPP", "Pasaporte digital de producto de cada prenda"),
        ("QR", "Código en pijamas que llevó el equipo, escaneado por estudiantes para ver "
               "los componentes de la prenda"),
    ],
    icono_s6("prenda"),
    fuente="Startup UNI, nota del 10-9-2026",
    notas=[
        "TRAZA desarrolla un pasaporte digital de producto (DPP, por _digital product "
        "passport_) con _blockchain_ para la trazabilidad del sector textil. En la Feria "
        "Tecnológica Internacional de la UNI (UNICTEC), del 8 al 10 de septiembre de 2026, el "
        "equipo llevó pijamas con el código QR del pasaporte incorporado; los asistentes lo "
        "escanearon y vieron los componentes de la prenda.",
        "La demostración muestra el prototipo en funcionamiento ante la audiencia y permite que "
        "esta lo use.",
        "Implicación para el formulador: una demostración en vivo requiere un plan alternativo, "
        "como un video del mismo uso, por si falla la conexión o el equipo.",
        "Dato: el Reglamento (UE) 2024/1781, de diseño ecológico de productos sostenibles (en "
        "vigor desde el 18 de julio de 2024), introduce el pasaporte digital de producto en la "
        "Unión Europea; los textiles figuran entre los grupos prioritarios.",
        "Verificar antes de la clase: el estado de financiamiento de TRAZA, que no figura en "
        "la nota.",
    ],
))

rec("U2")

# ---------- U3 · Preguntas técnicas y financieras del jurado (21 min)

L.append(tarjetas(
    "tipos-de-pregunta",
    "01 · Preguntas del jurado",
    "Preguntas de un jurado por objeto y foco de *promoción* o de prevención",
    [
        ("Técnica · prevención", "«_Have you Turing tested this?_»"),
        ("De mercado · prevención", "«_Can you talk a little bit about the competitive "
                                    "environment?_»"),
        ("Financiera · promoción", "«_How do you plan to monetize this?_»"),
        ("De equipo · promoción", "«_So why you?_»"),
    ],
    iconos=["simulate", "chart", "budget", "users"],
    fuente=KANZE + ", apéndice B",
    notas=[
        "Las preguntas son citas textuales de inversionistas en la ronda de preguntas de "
        "la edición de Nueva York de TechCrunch Disrupt, concurso de _startups_, recogidas por "
        "Kanze et al. (2018). En español, las cuatro preguntas indagan si el sistema pasó una prueba de "
        "Turing, cómo es el entorno competitivo, cómo se piensa obtener ingresos y por qué ese "
        "equipo es el indicado.",
        "Kanze et al. clasifican las preguntas con la teoría del foco regulatorio: una pregunta "
        "de promoción trata de ganancias, crecimiento y logros; una de prevención, de pérdidas, "
        "seguridad y riesgos.",
        "Otras preguntas de promoción del estudio tratan del potencial de propiedad "
        "intelectual y de los hitos del año; otras de prevención, del plazo para alcanzar el "
        "punto de equilibrio, de las salvaguardas ante un riesgo y de la trayectoria del resto "
        "del equipo.",
        "Las preguntas técnicas tratan de validación, escalamiento y propiedad intelectual; las "
        "de mercado, de clientes, uso y competencia; las financieras, de precio, margen, punto "
        "de equilibrio, uso de fondos y valorización; las de equipo, de trayectoria, "
        "capacidades internas y dedicación.",
        "Dato: el estudio documenta que los inversionistas hicieron más preguntas de promoción "
        "a los emprendedores hombres y más preguntas de prevención a las mujeres.",
        "Las cuatro citas proceden de jurados de inversionistas. En un fondo público las "
        "preguntas siguen los criterios de la cartilla (StartUp Perú 13G, num. 39); en un "
        "jurado académico, los de la rúbrica del tribunal. Los recursos de la unidad reúnen "
        "preguntas de paneles del ERC y de UK Research and Innovation.",
    ],
))

L.append(cifra(
    "foco-de-la-pregunta",
    "01 · Foco de la pregunta",
    "7,2", "veces",
    "más fondos para las _startups_ con mayoría de preguntas de promoción (US$ 16,8 "
    "millones) que para las de prevención (US$ 2,3 millones)",
    "189 empresas y 1 857 preguntas de inversionistas en TechCrunch Disrupt Nueva York, "
    "2010-2016",
    fuente=KANZE + ", 61(2), pp. 594 y 598",
    notas=[
        "Dato: el estudio calcula 7,21 veces con los promedios exactos. Cada pregunta de "
        "prevención adicional se asocia con US$ 3,8 millones menos de fondos obtenidos, en una "
        "regresión sobre el monto total recaudado (p. 598).",
        "El análisis de campo es correlacional. El experimento posterior del mismo artículo "
        "confirma el sentido del efecto: inversionistas ángeles acreditados asignaron en "
        "promedio US$ 133 259 de US$ 400 000 a las condiciones con preguntas de promoción, 2,00 "
        "veces los US$ 66 741 asignados con preguntas de prevención.",
        "Dato: las empresas que respondieron preguntas de prevención con respuestas de "
        "promoción recaudaron en promedio US$ 7,9 millones, 14,03 veces los US$ 563 270 de "
        "quienes respondieron en el mismo foco. La submuestra es pequeña y la cifra se toma "
        "con esa reserva (p. 599).",
        "Implicación para el formulador: una pregunta de prevención se responde con el riesgo y "
        "su control, y se añade la ganancia que ese control protege.",
    ],
))

L.append(caso(
    "caso-demo-day",
    "01 · Caso de estudio · ronda de preguntas",
    "IMPULSO 2G",
    "Jornada final (_demo day_) de la preincubación de Startup UNI · Facultad de Ingeniería "
    "Eléctrica y Electrónica · agosto de 2026",
    [
        ("10", "Finalistas ante 4 jurados, en dos bloques de 90 min"),
        ("S/ 3 000", "Primer puesto, SORO LAB; luego Morgan Hub y PAVDRONE"),
        ("5 min", "_Pitch_ de cada equipo"),
        ("12 min", "Preguntas del jurado a cada equipo"),
    ],
    icono_s6("escenario"),
    fuente="Startup UNI, nota del 28-8-2026",
    notas=[
        "IMPULSO 2G es el programa de preincubación 2026 de Startup UNI, la incubadora de la "
        "UNI; cerró con un _demo day_ presencial en la Facultad de Ingeniería Eléctrica y "
        "Electrónica. Los 10 finalistas fueron AIintheSky, Altar Filter, Artesanía 5.0 Lab, "
        "Morgan Hub, NeoPrint, PAVDRONE, QUIPPU, Smart Painter, SORO LAB y Tech Solutions.",
        "Dato: cada equipo tuvo 5 minutos de _pitch_, 12 minutos para responder al jurado y 1 "
        "minuto para que los cuatro jurados completaran la rúbrica. SORO LAB expuso en forma "
        "presencial desde México y Tech Solutions en forma virtual. Premios: S/ 3 000, S/ 2 000 "
        "y S/ 1 000.",
        "Dato: en los concursos del experimento de Clingingsmith y Shane (2018), cada participante tuvo 90 "
        "segundos y una pregunta del panel. Los formatos varían; las bases o el reglamento del "
        "evento fijan los tiempos.",
        "El programa IMPULSO 2G se mencionó en la sesión 3 como preincubación de Startup UNI; "
        "el caso trata la jornada final y su ronda de preguntas.",
        "La nota de Startup UNI no describe qué hace cada ganador. El programa de incubación "
        "2026 de la misma incubadora cierra con una presentación ante jurado y capital "
        "semilla.",
    ],
))

L.append(pasos(
    "preparar-respuestas",
    "01 · Preparación de respuestas",
    "Preparación de las respuestas ante un *jurado* técnico o financiero",
    [
        ("Preguntas probables", "Por criterio de la cartilla o de la rúbrica"),
        ("Láminas de respaldo", "Ensayos, costos, TRL y presupuesto"),
        ("Respuesta con dato", "Cifra con su unidad y su fuente"),
        ("Riesgo y ganancia", "Control del riesgo y ganancia protegida"),
        ("Lo no medido", "Lo pendiente y su fecha de medición"),
    ],
    clave=3,
    fuente="Kanze et al., 2018 · Chen, Yao y Kotha, 2009 · Clingingsmith y Shane, 2018",
    notas=[
        "Los pasos 1, 2, 3 y 5 son criterio del docente y valen para inversionistas, comités de "
        "fondos y tribunales académicos; el paso 4 aplica el resultado de "
        "Kanze et al. (2018) sobre las respuestas de promoción a preguntas de prevención, "
        "obtenido en una submuestra pequeña.",
        "Dato: la preparación percibida del emprendedor, y no su pasión, influyó en la decisión "
        "de financiar en un experimento de laboratorio y en un estudio de campo con "
        "inversionistas (Chen, Yao y Kotha, 2009).",
        "Dato: en concursos de _pitch_ con asignación aleatoria de 271 emprendedores de 10 "
        "universidades del noreste de Ohio, la capacitación aumentó en un tercio de desviación estándar el uso de los "
        "elementos recomendados; mejoró la evaluación de jueces experimentados para las ideas "
        "de calidad alta y la empeoró para las demás (Clingingsmith y Shane, 2018).",
        "Dato: 24 inversionistas ángeles del Reino Unido evaluaron tres _pitches_; los "
        "factores de presentación pesaron más en su puntuación que los factores que ellos "
        "mismos declararon (Clark, 2008, _Venture Capital_). Los ángeles combinan análisis e "
        "intuición, con predominio de la intuición (Huang y Pearce, 2015, _Administrative "
        "Science Quarterly_).",
        "Error frecuente: responder una pregunta financiera sin el presupuesto a la vista. Las "
        "láminas de respaldo van después de la lámina final y no se proyectan si nadie lo "
        "pide.",
    ],
))

rec("U3")

# ================================================================ CIERRE (9 min)

L.append(cierre(
    "sintesis-sesion",
    "01 · Síntesis",
    "Síntesis del *_pitch_* y de la sustentación",
    [
        "Audiencia: retorno, bases o rigor según quien decide",
        "Estructura: seis bloques, del problema a la solicitud",
        "Sustentación: video, entrevista o panel según el fondo",
        "Preguntas: preparación por criterio, con dato y fuente",
    ],
    notas=[
        "Recapitular el criterio de cada término de la sesión.",
        "La audiencia determina el objeto de la decisión; la estructura y el material de apoyo "
        "se ajustan a ese objeto y a las bases, y la ronda de preguntas se prepara con los "
        "criterios de la cartilla o de la rúbrica.",
    ],
))

L.append(visual(
    "cierre-del-curso",
    "Cierre del curso",
    "Contenido de las *seis sesiones* del curso Diseño y Gestión de Proyectos I+D+i+e",
    linea_tiempo(
        [
            (1, "S1 · Fundamentos", "Tipo de actividad, TRL y entidad de destino", False),
            (2, "S2 · Transferencia", "Vías de transferencia, titularidad y protección", False),
            (3, "S3 · Financiamiento", "Instrumentos públicos y capital emprendedor", False),
            (4, "S4 · Formulación", "Problema, objetivos, marco lógico, plan y equipo", False),
            (5, "S5 · Ejecución", "Contrato, gasto, hitos, protección y valorización", False),
            (6, "S6 · Sustentación", "Relato, estructura y preguntas del jurado", True),
        ],
        escala=(0.4, 6.6, None),
        nota="SECUENCIA DE LAS SESIONES · 11.ª EDICIÓN, 2026",
    ),
    notas=[
        "Recapitular el curso en el orden de las sesiones: la sesión 1 clasifica la actividad "
        "como I+D o innovación, asigna el TRL e identifica la entidad de destino; la sesión 2 "
        "trata las vías de transferencia, la titularidad, la protección y las empresas de base "
        "tecnológica; la sesión 3, los instrumentos públicos, la contrapartida, el capital "
        "emprendedor y la cooperación internacional.",
        "La sesión 4 trata la propuesta según la cartilla del concurso: problema, objetivos, "
        "marco lógico, plan de trabajo y equipo; la sesión 5, el contrato, el gasto, los "
        "hitos, la protección, el acceso abierto y la valorización de los resultados; la "
        "sesión 6, el relato, la estructura y la sustentación ante inversionistas, fondos y "
        "jurados.",
        "En un proyecto, las sesiones corresponden a etapas sucesivas: convocatoria y elección "
        "del instrumento (sesiones 1 y 3), propuesta (sesión 4), ejecución y resultados "
        "(sesiones 2 y 5) y presentación ante quien decide (sesión 6).",
    ],
))

L.append(referencias(
    "fuentes",
    "Referencias de la sesión",
    [
        ("definiciones-pitch", "Oxford University Press (2026). _Oxford Advanced Learner's Dictionary_. "
                               "Cohen, S. y Hochberg, Y. V. (2014). SSRN 2418000."),
        ("relato-abt", "Olson, R. (2015). _Houston, We Have a Narrative_. University of Chicago Press. "
                       "Dahlstrom, M. F. (2014). _PNAS_, 111(supl. 4)."),
        ("caso-abt", "Warthon, R. y Valenzuela, M. (2026). EGU26-22690."),
        ("audiencias", "PROCIENCIA (2025). Bases E041-2025-01-BM, Anexo 11. "
                       "Onieva López, J. L. (2016). _REIFOP_, 19(3), 185-198."),
        ("caso-tres-audiencias", "Andina (7-10-2019; 19-12-2020). DPL News (30-1-2023)."),
        ("bloques-del-pitch", "Sequoia Capital. _Writing a business plan_. NSF. _Project Pitch_. "
                              "PROINNÓVATE (2025). Bases EIN StartUp Perú 13G."),
        ("equipo-primero", "Gompers, P. A., Gornall, W., Kaplan, S. N. y Strebulaev, I. A. (2020). "
                           "_J. Financial Economics_, 135(1), 169-190."),
        ("caso-solicitud", "Infobae (7-5-2026). ProActivo (2026)."),
        ("sustentacion-fondos", "PROINNÓVATE (2026). Bases iniciales regionales, San Martín. "
                                "PROCIENCIA (2026). Bases E041-2027-02."),
        ("caso-demostracion", "Startup UNI (10-9-2026). Feria UNICTEC 2026."),
        ("tipos-de-pregunta", "Kanze, D., Huang, L., Conley, M. A. y Higgins, E. T. (2018). "
                              "_Academy of Management Journal_, 61(2), 586-614."),
        ("caso-demo-day", "Startup UNI (28-8-2026). _Demo Day_ de IMPULSO 2G. "
                          "Clingingsmith, D. y Shane, S. (2018). _Management Science_, 64(11)."),
        ("preparar-respuestas", "Chen, X.-P., Yao, X. y Kotha, S. (2009). _Academy of Management "
                                "Journal_, 52(1)."),
    ],
    notas=[
        "Referencias completas: Clingingsmith y Shane (2018), https://doi.org/10.1287/mnsc.2017.2882; "
        "Dahlstrom (2014), https://doi.org/10.1073/pnas.1320645111; Gompers et al. (2020), "
        "https://doi.org/10.1016/j.jfineco.2019.06.011; Kanze et al. (2018), "
        "https://doi.org/10.5465/amj.2016.1215; Chen, Yao y Kotha (2009), "
        "https://doi.org/10.5465/amj.2009.36462018; Warthon y Valenzuela (2026), "
        "https://doi.org/10.5194/egusphere-egu26-22690; Onieva López (2016), "
        "https://doi.org/10.6018/reifop.19.3.206331.",
        "Citadas en las notas: Hillier, Kelly y Klinger (2016), _PLoS ONE_, 11(12), e0167983, "
        "https://doi.org/10.1371/journal.pone.0167983; Martens, Jennings y Jennings (2007), "
        "_Academy of Management Journal_, 50(5), 1107-1132; Clark (2008), _Venture Capital_, "
        "10(3), 257-279; Huang y Pearce (2015), _Administrative Science Quarterly_, 60(4), "
        "634-670; VRI-UNI (2026), términos de referencia del servicio especializado en gestión "
        "y procesamiento de información de investigaciones.",
    ],
))


def _sin_corte(lam):
    """Espacio de no separación en montos y cifras de los nodos de texto
    («S/ 3 000», «US$ 16,8»), para que el salto de línea no parta la cifra."""
    import re

    def fijo(txt):
        txt = re.sub(r"(S/|US\$|USD|R\$|€) (?=\d)", "\\1\u00a0", txt)
        return re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", txt)

    lam.cuerpo = re.sub(r">([^<]+)<", lambda m: ">" + fijo(m.group(1)) + "<", lam.cuerpo)
    return lam


L = [_sin_corte(lam) for lam in L]

construir("clase-06", "Sesión 6 · Pitch y sustentación de proyectos", L)
