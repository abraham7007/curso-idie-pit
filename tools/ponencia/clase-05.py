#!/usr/bin/env python3
"""Sesión 5 · Ejecución del proyecto y transferencia de resultados — formato ponencia (11.ª edición).

Temas: «Ejecución, presupuesto y rendición del proyecto» (tema 01: ciclo del
contrato, documentos de gestión, transferencia a una entidad pública, rubros y
topes, elegibilidad del gasto, compras de una universidad pública, aporte no
monetario, revisión de hitos, cambios y cierre) y «Registro, difusión,
valorización y transferencia de resultados» (tema 02: resultados exigidos,
reporte de viabilidad de patente, calendario de protección, tasas, software,
acceso abierto, plan de gestión de datos, paquete tecnológico, valorización y
licencia).

Secuencia (scratchpad/s5-auditoria-secuencia.md, §4): U1 del concurso al
contrato → U2 presupuesto por rubros y contrapartida → U3 seguimiento, cambios
y cierre → receso → U4 resultados exigidos y protección → U5 publicación,
repositorio y datos abiertos → U6 paquete tecnológico, valorización y
transferencia. Cambios frente a la secuencia: entra una lámina sobre las
modalidades de compra de la Ley 32069 (U2); la ejecución de la UNI en 2024 y
el dato de Hamilton et al. (2023) pasan a las notas; la U4 suma un caso de
solicitud por la vía del PCT y la U6 un caso de licencia con términos
publicados (Unicamp) en lugar del diplomado de vinculación.

Concurso de referencia: Proyectos de Desarrollo Tecnológico E041-2027-02 de
PROCIENCIA (bases integradas, Anexos 8, 11, 12, 14, 15 y 16, modelo de
contrato firmado el 10 de septiembre de 2026), la guía de soporte, seguimiento
y evaluación de los concursos 2027 (26 de agosto de 2026) y las bases de
Investigación Aplicada E041-2027-03. Contenido: scratchpad/inv-s5.md.

Ejemplos (uno distinto por lámina de caso o de ejemplo; ninguno usado en las
sesiones 1 a 4): U13, fotocatálisis solar de efluentes textiles (arranque);
Doctorado en Ciencias con mención en Física de la UNI (transferencia a una
entidad pública); U15, gemelos digitales sísmicos (aporte no monetario,
cálculo ilustrativo); desionización capacitiva y fotocatálisis, Básica 2022
(cierre); sensor electroquímico de metales pesados con residuos de PET (vía
PCT); U18, electrodos de coronta de maíz morado (publicación después de la
solicitud); red acelerográfica REDACIS del CISMID (registros de libre descarga); U06, fibra
acrílica con CuO (valorización por costo); licencia exclusiva de la Unicamp
(términos publicados). Recursos: scratchpad/recursos-s5.md (4 por unidad).

Formato expositivo: la sesión no incluye actividades en el aula. Las notas
reúnen contenido de respaldo con dato y fuente, errores frecuentes y puntos
por verificar.

Antes de dictar, verificar: estado del contrato y del POP de U13; regla de
contrapartida de Investigación Aplicada 2025-02 (U15) y de Desarrollo
Tecnológico 2024-02 (U06); oficio de cierre del proyecto de Básica 2022;
estado de las solicitudes PE20260953A1, WO2026038966A1 y PE20240417A1;
certificación de la UNI para el art. 55.1 g) de la Ley 32069; licencia de uso
de los registros de REDACIS.

Uso:  python3 tools/ponencia/clase-05.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from graficos import (  # noqa: E402
    barras_apiladas, barras_valor, criterios_svg, cronograma_portada, icono_s5, linea_tiempo,
)
from plantillas import (  # noqa: E402
    agenda, caso, cierre, construir, duo, pasos, portada, recursos, referencias, seccion,
    tarjetas, visual,
)

FUENTE_REC = "Enlaces verificados en octubre de 2026"
GUIA = "PROCIENCIA, guía de soporte, seguimiento y evaluación, concursos 2027"
CONTRATO = "PROCIENCIA, modelo de contrato E041-2027-02"
BASES = "PROCIENCIA, bases integradas E041-2027-02"

# Recursos recomendados por unidad (scratchpad/recursos-s5.md). Cada entrada:
# (slug, antetítulo, titular, items, notas). Se rellenan al recibir el archivo.
RECURSOS = {
    "U1": ("recursos-arranque", "01 · Recursos recomendados",
           "Recursos sobre contratos y condiciones de una subvención de I+D", [
        {"tipo": "Guía", "titulo": "Guía de ejecución de proyectos de investigación y desarrollo, adenda 2",
         "autor": "CONACYT, Paraguay · PROCIENCIA II, 2025",
         "detalle": "Firma, desembolso, reprogramaciones y cierre en un programa paraguayo",
         "url": "conacyt.gov.py · Guía de ejecución I+D (2025)",
         "enlace": "https://www.conacyt.gov.py/sites/default/files/GUIA%20DE%20EJECUCI%C3%93N_adenda%202_PINV01-INIC01.pdf"},
        {"tipo": "Guía", "titulo": "Terms and conditions for research grants",
         "autor": "UK Research and Innovation, actualizada en 2026",
         "detalle": "Condiciones estándar que acepta la institución al recibir una subvención",
         "url": "ukri.org · Terms and conditions for research grants",
         "enlace": "https://www.ukri.org/publications/terms-and-conditions-for-research-grants/"},
        {"tipo": "Artículo", "titulo": "Good Financial Grant Practice: A Tool for Developing and Demonstrating Institutional Financial and Grant Management Capacity in Global Health",
         "autor": "Harste et al., Clinical Infectious Diseases, 2021",
         "detalle": "Estándar de gestión financiera de subvenciones y verificación previa de la entidad",
         "url": "pmc.ncbi.nlm.nih.gov/articles/PMC8634540",
         "enlace": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8634540/"},
        {"tipo": "Sitio web", "titulo": "Búsquedas El Peruano: normas legales",
         "autor": "Editora Perú, actualización diaria",
         "detalle": "Buscador de resoluciones de transferencia y de resultados de concursos",
         "url": "busquedas.elperuano.pe",
         "enlace": "https://busquedas.elperuano.pe/"},
    ], [
        "La guía del CONACYT del Paraguay corresponde a un programa homónimo de PROCIENCIA: documentos de firma, póliza de fiel cumplimiento, contrapartida y reprogramaciones; sirve para contrastar con la guía 2027.",
        "Las condiciones de UK Research and Innovation (UKRI) cubren inicio, cambios, informes y propiedad intelectual de una subvención británica, que reconoce el costo económico completo, a diferencia de PROCIENCIA.",
        "El artículo de Harste et al. (2021) presenta el estándar de buena práctica financiera de subvenciones (GFGP). El buscador de El Peruano ubica por número o entidad las resoluciones de transferencia del CONCYTEC.",
    ]),
    "U2": ("recursos-presupuesto", "01 · Recursos recomendados",
           "Recursos sobre rendición del gasto y ejecución presupuestal", [
        {"tipo": "Guía", "titulo": "Instructivo General de Rendición de Cuentas de la ANID",
         "autor": "ANID, Chile, 2026",
         "detalle": "Ítems financiables, documentos de respaldo y aportes institucionales",
         "url": "udec.cl · Instructivo de rendición ANID 2026",
         "enlace": "https://vrid.udec.cl/wp-content/uploads/2026/03/REX-7-Instructivo-General-Rendiciones-ANID-2026.pdf"},
        {"tipo": "Guía", "titulo": "Guía para la presentación de informes de ejecución financiera de los contratos y convenios de CTeI",
         "autor": "Minciencias, Colombia, s. f.",
         "detalle": "Informe financiero por rubro y fuente, incluida la contrapartida",
         "url": "minciencias.gov.co · Guía de informes financieros",
         "enlace": "https://minciencias.gov.co/sites/default/files/m801pr15g02_guia_presentacion_informes_ejecucion_financiera_v00_0.pdf"},
        {"tipo": "Sitio web", "titulo": "Seguimiento de la ejecución presupuestal: Consulta Amigable",
         "autor": "Ministerio de Economía y Finanzas, actualización diaria",
         "detalle": "Presupuesto y ejecución de cada entidad pública por fuente",
         "url": "gob.pe/802",
         "enlace": "https://www.gob.pe/802-seguimiento-de-la-ejecucion-presupuestal-consulta-amigable"},
        {"tipo": "Guía", "titulo": "Proposal & Award Policies & Procedures Guide (PAPPG) 24-1, Budget and Budget Justification",
         "autor": "National Science Foundation, 2024",
         "detalle": "Partidas, costos indirectos y reglas de contrapartida de la NSF",
         "url": "nsf.gov · PAPPG 24-1, Budget",
         "enlace": "https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ch2D2f"},
    ], [
        "El instructivo de la Agencia Nacional de Investigación y Desarrollo (ANID) de Chile detalla ítems, respaldos y aportes institucionales, equivalentes a la contrapartida; el QR abre la copia publicada por la Universidad de Concepción.",
        "La guía de Minciencias exige soportar la contrapartida con el mismo rigor que los recursos del ministerio. La Consulta Amigable del MEF muestra el presupuesto y el devengado de la UNI en la fuente Donaciones y Transferencias.",
        "La guía de la NSF financia costos indirectos y prohíbe la contrapartida voluntaria comprometida; PROCIENCIA exige contrapartida y no paga gastos administrativos generales.",
    ]),
    "U3": ("recursos-seguimiento", "01 · Recursos recomendados",
           "Recursos sobre seguimiento, informes y archivo de un proyecto", [
        {"tipo": "Guía", "titulo": "SmartSig. Manual de instrucciones. Responsable Técnico (V2)",
         "autor": "PROCIENCIA, 2023",
         "detalle": "Registro del POP, medios de verificación, actas de hito y saldos",
         "url": "prociencia.gob.pe · Manual de SmartSIG",
         "enlace": "https://prociencia.gob.pe/wp-content/uploads/documentos%20prociencia/Manual%20de%20Instrucciones%20de%20SMART%20SIG_V2%282%29%2021-07-2023%20%281%29.pdf"},
        {"tipo": "Guía", "titulo": "Normas de Control Interno",
         "autor": "Contraloría General de la República, 2006",
         "detalle": "Rendición de cuentas, documentación de procesos y archivo en entidades públicas",
         "url": "gob.pe · Normas de Control Interno (2006)",
         "enlace": "https://cdn.www.gob.pe/uploads/document/file/2914323/Normas%20de%20Control%20Interno%2C%20aprobadas%20por%20R.C.%20N%C2%B0%20320-2006-CG%20de%2030.OCT.2006%2C%20publicada%20el%2003.NOV.2006.pdf"},
        {"tipo": "Guía", "titulo": "Guía para la presentación de informes técnicos de avance y final de programas y proyectos de CTeI",
         "autor": "Minciencias, Colombia, s. f.",
         "detalle": "Contenido de los informes técnicos de avance y del informe final",
         "url": "minciencias.gov.co · Guía de informes técnicos",
         "enlace": "https://minciencias.gov.co/sites/default/files/m801pr15g01_guia_presentacion_de_informes_tecnicos_de_ctei_v00_0.pdf"},
        {"tipo": "Artículo", "titulo": "The post-award effort of managing and reporting on funded research: a scoping review",
         "autor": "Crane, Blatch-Jones y Fackrell, F1000Research, 2023",
         "detalle": "Revisión del esfuerzo de gestión e informes después de la adjudicación",
         "url": "doi.org/10.12688/f1000research.133263.2",
         "enlace": "https://doi.org/10.12688/f1000research.133263.2"},
    ], [
        "El manual de SmartSIG muestra paso a paso el registro del POP, los medios de verificación y las actas; es de 2023 y la interfaz pudo cambiar.",
        "Las Normas de Control Interno de la Contraloría (Resolución 320-2006-CG) fijan la rendición de cuentas, la documentación de procesos y el archivo institucional (normas 3.7, 3.8 y 4.6).",
        "La guía de informes técnicos de Minciencias distingue el informe de avance del informe final. La revisión de Crane et al. (2023) identifica dónde los informes duplican esfuerzo.",
    ]),
    "U4": ("recursos-proteccion", "02 · Recursos recomendados",
           "Recursos sobre solicitudes de patente y búsqueda de antecedentes", [
        {"tipo": "Guía", "titulo": "Guía del solicitante del PCT",
         "autor": "OMPI, actualización continua",
         "detalle": "Presentación, búsqueda, publicación internacional y fase nacional",
         "url": "wipo.int/es/web/pct-system/guide",
         "enlace": "https://www.wipo.int/es/web/pct-system/guide/index"},
        {"tipo": "Libro", "titulo": "Manual de la OMPI de redacción de solicitudes de patente, 2.ª edición",
         "autor": "OMPI, edición en español, 2024",
         "detalle": "Estructura de la solicitud, reivindicaciones y descripción",
         "url": "wipo.int · Manual de redacción de patentes",
         "enlace": "https://www.wipo.int/edocs/pubdocs/es/wipo-pub-867-23-es-wipo-patent-drafting-manual.pdf"},
        {"tipo": "Base de datos", "titulo": "PATENTSCOPE",
         "autor": "OMPI, actualización continua",
         "detalle": "Solicitudes PCT y colecciones nacionales de patentes",
         "url": "patentscope.wipo.int",
         "enlace": "https://patentscope.wipo.int/search/es/search.jsf"},
        {"tipo": "Sitio web", "titulo": "Centros de Apoyo a la Tecnología y la Innovación (CATI)",
         "autor": "OMPI, vigente en 2026",
         "detalle": "Red mundial de centros que apoyan búsquedas de patentes",
         "url": "wipo.int/es/web/tisc",
         "enlace": "https://www.wipo.int/es/web/tisc"},
    ], [
        "La guía del solicitante del PCT tiene una introducción a la fase internacional y otra a la fase nacional; los anexos por oficina están en inglés y francés.",
        "El manual de redacción de la OMPI (licencia CC BY 4.0) es el paso siguiente a un reporte de viabilidad positivo. PATENTSCOPE publica las solicitudes PCT y sus entradas en fase nacional, con búsqueda por CIP.",
        "La página de la OMPI sobre los CATI describe la red internacional e incluye un buscador de centros.",
    ]),
    "U5": ("recursos-datos", "02 · Recursos recomendados",
           "Recursos sobre gestión, licencia y depósito de datos de investigación", [
        {"tipo": "Sitio web", "titulo": "Chooser: selector de licencias Creative Commons",
         "autor": "Creative Commons, vigente en 2026",
         "detalle": "Elección de la licencia de una obra o de un conjunto de datos",
         "url": "creativecommons.org/chooser",
         "enlace": "https://creativecommons.org/chooser/"},
        {"tipo": "Guía", "titulo": "Practical Guide to the International Alignment of Research Data Management, Extended Edition",
         "autor": "Science Europe, 2021",
         "detalle": "Requisitos mínimos de un plan de gestión de datos y rúbrica",
         "url": "doi.org/10.5281/zenodo.4915862",
         "enlace": "https://doi.org/10.5281/zenodo.4915862"},
        {"tipo": "Base de datos", "titulo": "Zenodo",
         "autor": "CERN y OpenAIRE, desde 2013",
         "detalle": "Repositorio general de datos, código y documentos con DOI",
         "url": "zenodo.org",
         "enlace": "https://zenodo.org/"},
        {"tipo": "Sitio web", "titulo": "Open policy finder",
         "autor": "Jisc, Reino Unido, desde 2024",
         "detalle": "Políticas editoriales de versión depositable, embargo y licencia",
         "url": "openpolicyfinder.jisc.ac.uk",
         "enlace": "https://openpolicyfinder.jisc.ac.uk/"},
    ], [
        "El selector de Creative Commons ayuda a elegir la licencia; los resúmenes de cada licencia están en español. La guía de Science Europe resume seis temas comunes a los planes de datos europeos, cercanos a las secciones del Anexo 14.",
        "Zenodo asigna DOI, admite versiones y licencias abiertas y publica código desde GitHub; no reemplaza el depósito en el repositorio institucional que exige la Ley 30035.",
        "Open policy finder sustituye a Sherpa Romeo e indica si una revista permite depositar el manuscrito aceptado y con qué embargo.",
    ]),
    "U6": ("recursos-transferencia", "02 · Recursos recomendados",
           "Recursos sobre valorización y contratos de transferencia", [
        {"tipo": "Guía", "titulo": "Recomendación (UE) 2023/499 sobre un Código de buenas prácticas en la gestión de los activos intelectuales para la valorización del conocimiento",
         "autor": "Comisión Europea, 2023",
         "detalle": "Gestión de activos intelectuales para valorizar resultados públicos",
         "url": "boe.es/doue/2023/069/L00075-00084.pdf",
         "enlace": "https://www.boe.es/doue/2023/069/L00075-00084.pdf"},
        {"tipo": "Artículo", "titulo": "Dificultades de la valoración de tecnologías en el ámbito universitario",
         "autor": "Medellín y Arellano, Contaduría y Administración, 2019",
         "detalle": "Dificultades de gestores mexicanos al valorar tecnologías universitarias",
         "url": "doi.org/10.22201/fca.24488410e.2019.1811",
         "enlace": "https://doi.org/10.22201/fca.24488410e.2019.1811"},
        {"tipo": "Informe", "titulo": "Final Report from the Expert Group on Intellectual Property Valuation",
         "autor": "Comisión Europea, 2014",
         "detalle": "Métodos de valorización de la propiedad intelectual, obstáculos y recomendaciones",
         "url": "doi.org/10.2777/72196",
         "enlace": "https://doi.org/10.2777/72196"},
        {"tipo": "Guía", "titulo": "Modelos de contratos de transferencia de tecnología",
         "autor": "Oficina Española de Patentes y Marcas, 2017",
         "detalle": "Modelos de licencia, confidencialidad e I+D con guías de uso",
         "url": "oepm.es · Modelos de contratos de transferencia",
         "enlace": "https://oepm.es/es/conoce-la-propiedad-industrial/transferencia-de-tecnologia/modelos-de-contratos"},
    ], [
        "La Recomendación (UE) 2023/499 no es vinculante y trata la estrategia de gestión de activos intelectuales y su paso al mercado; el QR abre la copia del Diario Oficial de la Unión Europea en el BOE.",
        "Medellín y Arellano (2019) agrupan las dificultades de valorar tecnologías universitarias en información, métodos, madurez de la tecnología y práctica empresarial. El grupo de expertos de la Comisión Europea (2014) atribuye el problema a la poca difusión de los métodos.",
        "Los modelos de la Oficina Española de Patentes y Marcas incluyen una licencia entre organismo público de investigación y empresa; están escritos para el derecho español y se adaptan a la Decisión 486 y al reglamento de propiedad intelectual de la UNI.",
    ]),
}

L = []


def rec(clave):
    """Lámina de recursos de la unidad, si ya se cargaron."""
    if clave in RECURSOS:
        slug, ceja, tit, items, notas = RECURSOS[clave]
        L.append(recursos(slug, ceja, tit, items, fuente=FUENTE_REC, notas=notas))


# ================================================================ APERTURA (5 min)

L.append(portada(
    "portada",
    "Sesión 5 · Diseño y Gestión de Proyectos {I+D+i+e}",
    "Ejecución del proyecto y transferencia de resultados",
    "Ejecución de un proyecto subvencionado por PROCIENCIA y destino de sus resultados al cierre",
    ["Ejecución, presupuesto y rendición del proyecto",
     "Registro, difusión, valorización y transferencia de resultados"],
    "Abraham Caso-Torres · OTI-UNI · CC BY-SA 4.0",
    visual=cronograma_portada(),
    notas=[
        "Dar la bienvenida y presentar los dos temas de la sesión: la ejecución del contrato "
        "desde el resultado del concurso hasta el oficio de cierre, y los resultados que el "
        "proyecto entrega, protege, deposita y transfiere.",
        "La sesión usa los documentos del concurso de la sesión 4, Proyectos de Desarrollo "
        "Tecnológico 2027-02 de PROCIENCIA: el modelo de contrato, las bases con sus anexos y la "
        "guía de soporte, seguimiento y evaluación de los concursos 2027. Cada caso es un "
        "proyecto distinto, de la UNI salvo uno.",
    ],
))

L.append(agenda(
    "agenda",
    "Agenda",
    "Temas y contenidos de la sesión 5",
    [
        ("Ejecución, presupuesto y rendición del proyecto",
         ["Resultado del concurso y firma del contrato",
          "Presupuesto por rubros y contrapartida",
          "Seguimiento, cambios y cierre"]),
        ("Registro, difusión, valorización y transferencia de resultados",
         ["Resultados y protección",
          "Publicación y datos abiertos",
          "Valorización y transferencia"]),
    ],
    notas=[
        "Presentar los dos temas y las tres unidades de cada uno.",
        "Tiempo: apertura, 5 min; tema 01, 76 min; receso, 10 min; tema 02, 79 min; cierre, "
        "5 min; holgura para preguntas, 5 min.",
        "La sesión parte de dos productos de la sesión 4: la matriz de marco lógico con sus "
        "medios de verificación y el cronograma con hitos. La contrapartida y el momento del "
        "desembolso se definieron en la sesión 3; la titularidad, las figuras de protección y "
        "el plazo de gracia, en la sesión 2.",
    ],
))

# ============== TEMA 01 · EJECUCIÓN, PRESUPUESTO Y RENDICIÓN DEL PROYECTO

L.append(seccion(
    "tema-01", "01", "Ejecución, presupuesto y rendición del proyecto",
    "Documentos y plazos desde el resultado del concurso, reglas del gasto y de la "
    "contrapartida, revisión de hitos y cierre del contrato",
    notas=[
        "Presentar el tema 01, que sigue la vida del contrato de subvención: lo que se firma y "
        "se aprueba al inicio, lo que se puede pagar y con qué tope, lo que se revisa en cada "
        "hito y lo que se entrega para cerrar.",
        "Tiempo: 76 minutos; presentación del tema, 1; resultado del concurso y firma del contrato, 24; "
        "presupuesto por rubros y contrapartida, 25; seguimiento, cambios y cierre, 23; "
        "síntesis, 3.",
    ],
))

# ---------- U1 · Resultado del concurso y firma del contrato

L.append(visual(
    "ciclo-de-ejecucion",
    "01 · Ciclo de ejecución",
    "Etapas de ejecución de un contrato de *PROCIENCIA*, del resultado al oficio de cierre",
    linea_tiempo(
        [
            (0, "Resolución de resultados", "Lista de seleccionados del concurso", False),
            (1, "Firma del contrato", "Carta fianza del 10 % antes del desembolso, si es privada", False),
            (2, "POP aprobado", "Hasta 60 días desde la firma", False),
            (3, "Primer desembolso", "Inicio del plazo de ejecución", True),
            (4, "Revisión de hitos", "Acta (ARAP) al vencer cada hito", False),
            (5, "Fin de la ejecución", "Vencimiento del último hito del POP", False),
            (6, "Informe final (IFR)", "Hasta 60 días tras el fin de la ejecución", False),
            (7, "Oficio de cierre", "Fin de la vigencia del contrato", False),
        ],
        tramos=[(1, 7, "Vigencia del contrato", False), (3, 5, "Plazo de ejecución", True)],
        nota="ESQUEMA, SIN ESCALA",
    ),
    fuente=GUIA + ", num. 2.1-2.3 y 3.1 · " + CONTRATO + ", cl. 4.ª y 11.ª",
    notas=[
        "El contrato rige desde el día siguiente a su firma hasta el oficio de cierre. El plazo "
        "de ejecución corre desde el día siguiente al primer desembolso, con la fecha en que el "
        "monto figura como girado, hasta el vencimiento del último hito del plan operativo del "
        "proyecto (POP) (guía 2027, num. 2.1-2.2; contrato, cl. 4.ª).",
        "La guía de soporte, seguimiento y evaluación de los concursos 2027, firmada el 26 de "
        "agosto de 2026, rige el seguimiento de los proyectos de ese año. El informe final de "
        "resultados (IFR) lo presenta el responsable técnico con los resultados, los "
        "indicadores del POP y el estado de los planes de gestión ambiental y social y de "
        "gestión de datos.",
        "Dato: en Desarrollo Tecnológico 2027, PROCIENCIA desembolsa el 100 % en una sola "
        "armada; en Investigación Básica y Aplicada 2027, el 80 % del monto, de manera "
        "referencial, en la primera armada (bases E041-2027-01, -02 y -03, num. 2.4.1). El hito "
        "y el acta de acompañamiento y revisión de avances (ARAP) se presentaron en la sesión 4.",
        "Dato: la carta fianza o póliza de caución por el 10 % del financiamiento se exige a "
        "personas jurídicas de régimen privado; para instituciones del Estado no es obligatoria "
        "(contrato, cl. 11.ª; guía, num. 2.3). El taller de inducción, obligatorio para el "
        "responsable técnico y el gestor, se dicta hasta 30 días después de recibido el "
        "expediente de seleccionados (num. 3.1.1).",
        "Dato: se reconocen los gastos posteriores a la aprobación del POP. Si el POP no se "
        "aprueba, el contrato puede resolverse con devolución total (guía, num. 3.2 y 4). Las "
        "autorizaciones de colecta, de acceso a recursos genéticos o del comité de ética "
        "figuran al menos en trámite al aprobar el POP y se obtienen en el primer hito "
        "(num. 3.1.2).",
        "Error frecuente: contar el plazo de ejecución desde la firma del contrato.",
    ],
))

L.append(tarjetas(
    "documentos-de-gestion",
    "01 · Documentos de gestión",
    "Documentos que rigen la ejecución de un *contrato* de subvención de PROCIENCIA",
    [
        ("Contrato", "Diecisiete cláusulas firmadas por la entidad ejecutora y PROCIENCIA"),
        ("Bases del concurso", "Rubros, topes, resultados exigidos y plazos"),
        ("Guía de seguimiento 2027", "Hitos, visitas, cambios, cierre e incumplimiento"),
        ("Plan operativo (POP)", "Hitos, programación técnica y financiera, desembolsos, "
                                 "visitas y plan de gestión de datos"),
        ("Ficha y resumen técnico", "Presentación del proyecto al inicio y de sus resultados al "
                                    "cierre"),
    ],
    clave=3,
    iconos=["agreement", "file", "rubric", "gantt", "book"],
    fuente=CONTRATO + ", cl. 4.ª, 13.ª y 17.ª · " + GUIA + ", glosario y num. 3.7",
    notas=[
        "El contrato lo conforman sus cláusulas, las bases, la guía de soporte, seguimiento y "
        "evaluación y el POP aprobado (cl. 17.ª). Las modificaciones técnicas verificadas por "
        "la Sub Unidad de Soporte, Seguimiento y Evaluación (SUSSE) de PROCIENCIA no requieren "
        "adenda al contrato, pero sí la aceptación expresa de ambas partes (cl. 4.ª; "
        "Resolución de Dirección Ejecutiva, RDE, 085-2022-PROCIENCIA-DE). La ficha técnica, "
        "que complementa el POP al inicio, y el resumen técnico, que se elabora al cierre, son "
        "documentos de gestión con fines de difusión (guía, glosario), pero no integran el "
        "contrato.",
        "El POP es el principal documento de gestión. Reúne los hitos, el plan de gestión "
        "ambiental y social (PGAS), el plan de gestión de datos (PGD), la programación técnica, "
        "técnico-financiera, monetaria y no monetaria, y los cronogramas de desembolsos y de "
        "visitas. Lo elabora el responsable técnico en SmartSIG, el sistema de seguimiento de "
        "PROCIENCIA, y lo aprueba el monitor técnico (guía, glosario).",
        "La SUSSE asigna un monitor técnico y un monitor financiero. El gestor del proyecto, de "
        "la oficina de gestión de la investigación de la entidad, actualiza la ejecución en "
        "SmartSIG; el gestor tecnológico responde por el paquete tecnológico, la ficha "
        "tecnológica y la propiedad intelectual.",
        "Dato: PROCIENCIA reconoce los acuerdos de propiedad intelectual entre los participantes "
        "según la normativa de la entidad ejecutora y, cuando corresponde, exige un acuerdo de "
        "buena fe entre ellos (contrato, cl. 13.ª; guía, num. 3.7).",
        "Dato: el modelo 2027 se titula contrato; las bases lo llaman convenio en un pasaje "
        "(num. 2.2.1) y, para una entidad pública, la resolución de transferencia del CONCYTEC "
        "lo registra con un número de convenio (Ley 31250, 12.ª disposición complementaria "
        "final), como se ve en esta unidad.",
        "Error frecuente: tramitar una adenda para un cambio técnico.",
    ],
))

L.append(caso(
    "caso-arranque",
    "01 · Caso de estudio · arranque",
    "Efluentes textiles con fotocatálisis",
    "UNI · Investigación Aplicada 2026-02 de PROCIENCIA, modalidad multidisciplinaria",
    [
        ("S/ 500 000", "Subvención de PROCIENCIA"),
        ("86 de 375", "Propuestas seleccionadas en el concurso"),
        ("9 sep. 2026", "Resolución de resultados; siguen el contrato y el POP"),
    ],
    icono_s5("fotorreactor"),
    fuente="PROCIENCIA, RDE 087-2026-PROCIENCIA-DE, 9 de septiembre de 2026",
    notas=[
        "El proyecto «Catalizadores fotocatalíticos inmovilizados de ZnO codopado con Ce, Sm y "
        "Tb para el tratamiento continuo de efluentes textiles a escala piloto y con energía "
        "solar», de la UNI, con responsable técnico Juan Martín Rodríguez Rodríguez, figura "
        "entre los seleccionados de Investigación Aplicada 2026-02 (RDE "
        "087-2026-PROCIENCIA-DE).",
        "Dato: el concurso recibió 375 postulaciones; 234 aprobaron la evaluación por pares "
        "externos, 219 resultaron aptas y trece paneles seleccionaron 86, con 8 accesitarias "
        "(RDE 087-2026).",
        "A la fecha de la clase, el proyecto está en la etapa que sigue a la resolución: "
        "expediente de seleccionados, firma del contrato y elaboración del POP. La etapa se "
        "estima con las fechas publicadas; el estado real del contrato no es público.",
        "Dato: con la regla de Investigación Aplicada 2027, una entidad pública recibe hasta "
        "el 80 % del costo total y aporta al menos 20 % no monetario, y PROCIENCIA desembolsa "
        "de manera referencial el 80 % en la primera armada (bases E041-2027-03, num. 2.4.1 y "
        "2.4.3). Las bases del concurso 2026-02 no se cotejaron.",
        "Verificar antes de la clase: la fecha de firma del contrato y de aprobación del POP "
        "del proyecto.",
    ],
))

L.append(pasos(
    "transferencia-entidad-publica",
    "01 · Entidad pública ejecutora",
    "Transferencia del *CONCYTEC* al Doctorado en Física de la UNI, ejemplo",
    [
        ("Convenio", "Firmado por PROCIENCIA y la UNI"),
        ("Presupuesto", "Informe favorable previo"),
        ("Resolución", "RP 088-2026-CONCYTEC-P por S/ 1 000 000"),
        ("Publicación", "_El Peruano_, 27 de junio de 2026"),
        ("Ejecución", "Cuenta Única del Tesoro"),
    ],
    clave=2,
    fuente="Ley 31250, 12.ª disposición complementaria final · CONCYTEC, RP "
           "088-2026-CONCYTEC-P, 25 de junio de 2026 · " + GUIA + ", num. 2.3",
    notas=[
        "La duodécima disposición complementaria final de la Ley 31250 autoriza al CONCYTEC, "
        "de manera excepcional, a transferir recursos a entidades públicas para cofinanciar "
        "programas y proyectos de CTI. La transferencia se aprueba por resolución del titular "
        "del pliego, previa firma de un convenio e informe favorable de la oficina de "
        "presupuesto, y la resolución se publica en El Peruano. El convenio del ejemplo es "
        "el PE501084296-2023-PROCIENCIA-BM.",
        "Dato: la Resolución de Presidencia (RP) 088-2026-CONCYTEC-P, del 25 de junio de 2026, "
        "aprobó siete transferencias a cinco entidades públicas por S/ 7 250 000. A la UNI le "
        "correspondieron S/ 1 000 000 para el Doctorado en Ciencias con mención en Física y "
        "S/ 1 000 000 para el Doctorado en Ciencias con mención en Química.",
        "Dato: en una entidad pública, el gasto se registra en la Cuenta Única del Tesoro con "
        "cargo a la transferencia de PROCIENCIA, y los saldos no ejecutados se devuelven por el "
        "Sistema Integrado de Administración Financiera (SIAF) (guía, num. 2.3 y 3.2). La "
        "entidad privada recibe el subsidio en una cuenta del proyecto.",
        "Dato: el doctorado se financia con el préstamo BIRF 9334-PE del Banco Internacional "
        "de Reconstrucción y Fomento, del Grupo Banco Mundial, al Perú. Con fondos de "
        "préstamo, las compras siguen las regulaciones de adquisiciones del Banco Mundial "
        "(guía, num. 3.2, nota 9); el Vicerrectorado de Investigación (VRI) de la UNI publica "
        "los procesos del programa con esas reglas.",
        "Verificar antes de la clase: la resolución rectoral con que la UNI incorporó la "
        "transferencia a su presupuesto.",
    ],
))

rec("U1")

# ---------- U2 · Presupuesto por rubros y contrapartida

L.append(visual(
    "rubros-financiables",
    "01 · Rubros financiables",
    "Tope de cada rubro sobre el monto de *PROCIENCIA*, concursos 2027",
    barras_valor([
        ("Recursos humanos", 60, "clave"),
        ("Equipos y bienes duraderos", 40, ""),
        ("Servicios de terceros", 25, ""),
        ("Pasajes y viáticos", 15, ""),
        ("Gastos logísticos de operación", 10, ""),
    ], maximo=70, paso=10, menor=2, decimales=0, sufijo=" %", xb=560,
        unidad="PORCENTAJE MÁXIMO DEL MONTO DE PROCIENCIA",
        nota="MATERIALES E INSUMOS · SIN TOPE"),
    fuente=BASES + ", num. 2.4.2, tabla 6 y Anexo 8",
    notas=[
        "Dato: los topes se calculan sobre el monto que financia PROCIENCIA y no sobre el costo "
        "total del proyecto; la suma de los rubros es 100 %. Materiales e insumos no tienen "
        "tope. Los topes son iguales en Investigación Básica, Desarrollo Tecnológico e "
        "Investigación Aplicada 2027 (num. 2.4.2).",
        "Recursos humanos cubre el incentivo al responsable técnico y a los coinvestigadores y "
        "el estipendio de tesistas, técnicos, asistentes y gestor tecnológico, nunca beneficios "
        "sociales ni costo laboral. El estipendio de un tesista de posgrado es de al menos "
        "S/ 1 200 mensuales (Anexo 8).",
        "Dato: un equipo es un bien de costo unitario mayor a un cuarto de UIT, S/ 1 375 en "
        "2026 con la UIT de S/ 5 500 (DS 301-2025-EF); por debajo de ese monto es material o "
        "insumo (bases, nota 33).",
        "Servicios de terceros incluye el taller de cierre, la publicación en acceso abierto, "
        "el video de tres minutos, las tasas de propiedad intelectual nacionales y del Tratado "
        "de Cooperación en materia de Patentes (PCT), el "
        "reporte de viabilidad de patente y el seguro de viaje, hasta S/ 2 000 por viaje. "
        "Gastos logísticos incluye el incentivo al gestor del proyecto, hasta S/ 1 500 "
        "mensuales, y no cubre gastos administrativos generales (_overhead_) (Anexo 8).",
        "Dato: la Ley de Presupuesto 2026 autoriza a las entidades públicas que ejecutan "
        "transferencias de PROCIENCIA a otorgar a sus investigadores un incentivo económico no "
        "remunerativo ni pensionable (Ley 32513, art. 60.1 y 60.4). La nota 18 del Anexo 8 aún "
        "cita el art. 74 de la Ley 31953, de 2024.",
        "Implicación para el formulador: el presupuesto se construye desde las actividades del "
        "POP. Cada medio de verificación de la matriz de la sesión 4 tiene un costo que entra "
        "en uno de estos rubros.",
    ],
))

L.append(visual(
    "elegibilidad-del-gasto",
    "01 · Elegibilidad del gasto",
    "Condiciones de un gasto *elegible* según la guía y las bases 2027",
    criterios_svg([
        ("Vínculo", "Actividad del POP y rubro financiable de las bases"),
        ("Fecha", "Posterior al POP aprobado y dentro del plazo de ejecución"),
        ("Comprobante", "A nombre de la entidad, visado por el responsable técnico y el gestor"),
        ("Proveedor", "Sin vínculo familiar ni societario con el equipo o la entidad"),
        ("Bien", "Nuevo, sin inmuebles ni vehículos, sin equipos en los últimos 6 meses"),
    ]).replace("Actividad de I+D", "Gasto elegible"),
    fuente=GUIA + ", num. 3.1.3 y 3.2 · " + BASES + ", Anexo 8",
    notas=[
        "Las cinco condiciones se cumplen a la vez. La guía reconoce los gastos posteriores a "
        "la aprobación del POP y, por excepción, los sustentados desde la vigencia del "
        "contrato; ningún gasto puede tener fecha posterior al fin de la ejecución (num. 3.2).",
        "Dato: el Anexo 8 prohíbe comprar inmuebles, vehículos, bienes usados o con impacto "
        "ambiental negativo y equipos en los últimos seis meses de ejecución, y contratar "
        "proveedores vinculados al equipo o a la entidad hasta el cuarto grado de "
        "consanguinidad y el segundo de afinidad.",
        "Dato: los originales de comprobantes, declaraciones juradas y documentos de compra se "
        "conservan al menos cinco años, con un archivo de copias para la auditoría externa. En "
        "cada hito, los monitores revisan comprobantes originales elegidos al azar (num. 3.1.3 "
        "y 3.2).",
        "Las consultorías se contratan por producto y no con pagos mensuales; al proveedor no "
        "domiciliado se le retiene el impuesto a la renta. Los gastos bancarios corren por "
        "cuenta de la entidad (Anexo 8; guía, num. 3.2).",
        "Error frecuente: un comprobante a nombre de un integrante del equipo. El gasto no se "
        "reconoce aunque el bien esté en el laboratorio.",
    ],
))

L.append(tarjetas(
    "compras-entidad-publica",
    "01 · Compras de una entidad pública",
    "Modalidades de compra de una universidad pública según la *Ley 32069*",
    [
        ("Contrato menor", "Hasta 8 UIT, S/ 44 000 en 2026, sin procedimiento de selección"),
        ("Contratación directa para I+D+i", "Bienes y servicios de uso directo en I+D+i, con "
                                            "certificación del CONCYTEC o de un programa"),
        ("Compra pública de innovación", "Solución que no está en el mercado y requiere I+D"),
        ("Procedimiento competitivo", "Regla general para montos mayores a 8 UIT"),
        ("Fondos de préstamo", "Excluidos por el art. 7.1 f); reglas del Banco Mundial"),
    ],
    clave=1,
    iconos=["check", "search", "target", "rubric", "building"],
    fuente="Ley 32069, arts. 7.1 f), 34, 38 y 55.1 g) · DS 301-2025-EF · " + GUIA + ", num. 3.2",
    notas=[
        "La Ley 32069, Ley General de Contrataciones Públicas, sustituyó a la Ley 30225 y se "
        "aplica a las universidades públicas (art. 3). La guía de PROCIENCIA dispone que las "
        "compras sigan las normas de la entidad ejecutora; con fondos de un préstamo externo, "
        "las del organismo financiador, que la guía llama «prestatario» (num. 3.2, notas 8 y "
        "9). La Ley 32069 excluye esas compras de su ámbito, salvo sus principios (art. 7.1 f).",
        "Dato: el contrato menor, de hasta 8 UIT vigentes al contratar, no requiere "
        "procedimiento de selección; se publica en la Plataforma Digital para las "
        "Contrataciones Públicas (Pladicop) y lo supervisa el Organismo Especializado para las "
        "Contrataciones Públicas Eficientes (OECE) (art. 34).",
        "La contratación directa del art. 55.1 g) cubre la adquisición de bienes y servicios "
        "usados directamente en actividades de I+D+i por entidades públicas del nivel de "
        "ejecución del SINACTI que cuentan con una certificación de los programas nacionales de "
        "CTI o del CONCYTEC.",
        "La compra pública de innovación (art. 38) se usa cuando la solución no está disponible "
        "en el mercado o requiere adaptaciones con elementos innovadores, y asume los riesgos "
        "del proceso de innovación.",
        "Dato: la nota 8 de la guía 2027 de PROCIENCIA remite al Texto Único Ordenado "
        "de la Ley 30225, derogada.",
        "Dato: la Ley 32069 rige desde el 22 de abril de 2025, 90 días después de la "
        "publicación de su reglamento (29.ª disposición complementaria final).",
        "Implicación para el formulador: los plazos de compra de la entidad se declaran al "
        "postular y se reflejan en el cronograma, porque el plazo de ejecución corre desde el "
        "desembolso.",
        "Verificar antes de la clase: si la UNI cuenta con la certificación del art. 55.1 g).",
    ],
))

L.append(duo(
    "aporte-no-monetario",
    "01 · Contrapartida no monetaria",
    "Valorización del aporte no monetario: monitoreo con *gemelos digitales*, ejemplo",
    {"cab": "Regla de valorización", "t": "Aporte de la entidad en los rubros financiables",
     "items": ["Horas del personal según su remuneración bruta",
               "Equipos propios según su vida útil",
               "Materiales y servicios a precio de mercado"]},
    {"cab": "Ejemplo ilustrativo", "t": "Gemelos digitales sísmicos · UNI, Investigación "
                                        "Aplicada 2025-02",
     "items": ["S/ 499 500 de PROCIENCIA",
               "Costo total de S/ 624 375 con la regla 80/20",
               "Aporte no monetario de S/ 124 875"]},
    fuente="PROCIENCIA, bases E041-2027-03 y seleccionados de 2025-02 · cálculo ilustrativo",
    notas=[
        "La contrapartida y sus porcentajes por tipo de entidad se presentaron en la sesión 3. "
        "Durante la ejecución, el aporte se valoriza en los mismos rubros del Anexo 8 y el "
        "monitor financiero verifica la ejecución monetaria y no monetaria en cada hito.",
        "Dato: en Investigación Aplicada 2027, una entidad pública recibe hasta el 80 % del "
        "costo total y aporta al menos 20 % no monetario, sin aporte monetario; el aporte no "
        "monetario no puede exceder el financiamiento de PROCIENCIA (bases E041-2027-03, "
        "num. 2.4.3, tabla 13).",
        "Dato: en la entidad pública, el tesista, el técnico, el asistente o el gestor que es "
        "servidor público se registra como contrapartida no monetaria por la fracción de su "
        "remuneración dedicada al proyecto, y no como incentivo (notas 47 y 49).",
        "El proyecto «Integración de tecnologías de observación sísmica en gemelos digitales "
        "para el diagnóstico de la salud estructural de infraestructura y líneas vitales», con "
        "responsable técnico Miguel Augusto Díaz Figueroa, del Centro Peruano Japonés de "
        "Investigaciones Sísmicas y Mitigación de Desastres (CISMID) de la UNI, fue "
        "seleccionado en Investigación Aplicada 2025-02 con S/ 499 500. El cálculo aplica la "
        "regla de 2027 y es ilustrativo; la contrapartida real no es pública.",
        "Dato: el proyecto trabaja con la Universidad de Tokio y la Universidad Privada de "
        "Tacna; según una presentación del CISMID de junio de 2026, levantó cerca de 1 500 "
        "lotes en Villa El Salvador y cerca de 460 en Alto de la Alianza (Tacna).",
        "Error frecuente: calcular el porcentaje de contrapartida sobre el monto solicitado y "
        "no sobre el costo total.",
        "Verificar antes de la clase: la regla de contrapartida de las bases de Investigación "
        "Aplicada 2025-02.",
    ],
))

rec("U2")

# ---------- U3 · Seguimiento, cambios y cierre

L.append(tarjetas(
    "revision-de-hito",
    "01 · Revisión de hito",
    "Contenido de la revisión de un *hito* en el acta de acompañamiento (ARAP)",
    [
        ("Avance técnico", "Indicadores del POP con sus medios de verificación en SmartSIG"),
        ("Avance financiero", "Comprobantes visados y ejecución monetaria y no monetaria"),
        ("Datos y salvaguardas", "Plan de gestión de datos y plan ambiental y social"),
        ("Observaciones", "Subsanación a más tardar en el hito siguiente"),
    ],
    clave=0,
    iconos=["target", "chart", "file", "check"],
    fuente=GUIA + ", num. 3.1.3-3.1.4 y 3.2",
    notas=[
        "Al vencer cada hito, los monitores revisan el avance en una visita o reunión, de "
        "preferencia presencial. Los medios de verificación se cargan en SmartSIG antes del "
        "vencimiento y el hito se cierra a más tardar 30 días después; el acta cerrada no "
        "admite modificaciones (num. 3.1.3).",
        "Dato: el gestor del proyecto actualiza la ejecución financiera en SmartSIG cada "
        "quince días, desde el día siguiente al primer desembolso (num. 3.1.3 y 3.2).",
        "La calificación del hito, aprobado con 70 % o más de indicadores cumplidos, aprobado "
        "con reserva entre 50 % y 70 % y desaprobado por debajo de 50 % o por uso indebido de "
        "fondos, se presentó en la sesión 4.",
        "Dato: los monitores pueden hacer visitas intermedias, anunciadas o no, que constan en "
        "el acta de visita intermedia (AVIRAP); verifican la participación del equipo y el "
        "avance y pueden condicionar los desembolsos pendientes en los concursos con más de "
        "una armada (num. 3.1.4).",
        "Error frecuente: cargar los medios de verificación después del vencimiento del hito.",
    ],
))

L.append(tarjetas(
    "gestion-de-cambios",
    "01 · Gestión de cambios",
    "Cambios admitidos durante la ejecución y su *trámite* ante PROCIENCIA",
    [
        ("Entre partidas", "Solicitud al monitor financiero antes de ejecutar, dentro de los "
                           "topes"),
        ("Ampliación de plazo", "Una por proyecto, hasta la mitad del plazo inicial y sin más "
                                "presupuesto"),
        ("Responsable técnico", "Reemplazo propuesto por la entidad con los requisitos de las "
                                "bases"),
        ("Integrantes y asociadas", "Cartas y anexos firmados por las entidades"),
        ("Contrapartida", "Cambio que respeta los mínimos de las bases"),
    ],
    clave=1,
    iconos=["chart", "calendar", "users", "agreement", "rubric"],
    fuente=GUIA + ", num. 3.3.1-3.3.4 · " + CONTRATO + ", cl. 4.ª y 8.ª",
    notas=[
        "Dato: el cambio entre partidas se solicita al monitor financiero, con copia al monitor "
        "técnico, antes de ejecutarlo; se evalúan su contribución a los objetivos, los topes "
        "por rubro y la elegibilidad, lo aprueba el coordinador de la SUSSE y se actualiza en "
        "SmartSIG (num. 3.3.4). La guía no fija un porcentaje de cambio exento de solicitud.",
        "Dato: la ampliación de plazo procede por fuerza mayor, razón técnica sustentada o "
        "embarazo de la responsable técnica, y se pide al menos 20 días antes del vencimiento "
        "(num. 3.3.1).",
        "Dato: en un proyecto de más de un año, el responsable técnico puede ausentarse hasta "
        "tres meses con un coinvestigador a cargo;el reemplazo no puede tener deudas con PROCIENCIA (num. 3.3.2-3.3.3).",
        "Los cambios técnicos verificados por la SUSSE no requieren adenda al contrato, pero sí "
        "la aceptación expresa de ambas partes (cl. 4.ª).",
        "Error frecuente: ejecutar el cambio y comunicarlo después. La guía exige enviar la "
        "solicitud antes de ejecutar la modificación (num. 3.3) y el contrato obliga a "
        "comunicar los cambios para su aprobación (cl. 8.ª, num. 15).",
    ],
))

L.append(pasos(
    "cierre-del-proyecto",
    "01 · Cierre del proyecto",
    "Etapas del *cierre* de un proyecto de PROCIENCIA, del último hito al oficio",
    [
        ("Último hito", "Acta del último hito del POP"),
        ("Taller de difusión", "Presentación pública de resultados"),
        ("Informe final (IFR)", "Hasta 60 días tras el fin de la ejecución"),
        ("Saldos", "Devolución por SIAF o papeleta T-6"),
        ("Oficio de cierre", "Emitido por la SUSSE"),
    ],
    clave=2,
    fuente=GUIA + ", num. 3.1.5-3.1.6, 3.2 y 4 · " + CONTRATO + ", cl. 8.ª-10.ª",
    notas=[
        "El IFR se presenta hasta 60 días calendario después del fin de la ejecución, plazo "
        "prorrogable por un periodo similar si se sustenta antes del vencimiento. Los "
        "monitores lo evalúan en el reporte al informe final (RIFR); con su aprobación, la "
        "SUSSE emite el oficio de cierre, que concluye la vigencia del contrato y habilita la "
        "devolución de la garantía y del monto retenido, si lo hubo (num. 3.1.6 y apartado «Cierre del proyecto»).",
        "Dato: sin IFR, la SUSSE puede recomendar la ejecución de la carta fianza de la entidad "
        "privada y la inscripción del responsable técnico o de la entidad en el Registro de No "
        "Elegibles (RENOES), y PROCIENCIA puede resolver el contrato (num. 3.1.6).",
        "Dato: la resolución del contrato por incumplimiento obliga a devolver lo desembolsado "
        "más los intereses de ley y puede llevar a la calificación de no apto y al "
        "procedimiento sancionador del CONCYTEC (contrato, cl. 9.ª-10.ª; Ley 31250, art. 15 q).",
        "Dato: la entidad pública devuelve los saldos no elegibles por el módulo de "
        "operaciones en línea del SIAF; la privada, con la papeleta de depósito T-6. La entidad "
        "conserva los documentos y responde a PROCIENCIA hasta cinco años después del cierre "
        "(guía, num. 3.1.6 y 3.2; contrato, cl. 8.ª).",
        "Error frecuente: dar por cerrado el proyecto al terminar el plazo de ejecución. El "
        "contrato sigue vigente hasta el oficio de cierre.",
    ],
))

L.append(caso(
    "caso-cierre",
    "01 · Caso de estudio · cierre",
    "Desionización capacitiva de agua",
    "UNI · Investigación Básica 2022-01 de PROCIENCIA, contrato PE501078335-2022",
    [
        ("32 meses", "Plazo de ejecución, del 3 sep. 2022 al 2 may. 2025"),
        ("S/ 100 179", "Ejecutados en 2024"),
        ("En cierre", "Estado del proyecto en el informe del VRI-UNI de 2024"),
    ],
    icono_s5("cdi"),
    fuente="VRI-UNI, _Ejecución del financiamiento de proyectos de investigación con recursos "
           "externos, año 2024_, 2025 · PROCIENCIA, RDE 055-2022-PROCIENCIA-DE",
    notas=[
        "El proyecto «Fabricación, caracterización y evaluación de electrodos nanoestructurados "
        "basados en materiales carbonosos y óxidos semiconductores (ZnO, TiO2) para la "
        "degradación y eliminación simultánea de contaminantes en agua por medio de un sistema "
        "híbrido desionización capacitiva-fotocatálisis heterogénea», con responsable técnico "
        "Luis Alberto Sánchez Rodas, figura como «en proceso de cierre» en el informe del "
        "VRI de la UNI. Fue seleccionado en Investigación Básica 2022-01, modalidad "
        "multidisciplinaria, con S/ 500 000 (RDE 055-2022-PROCIENCIA-DE).",
        "La desionización capacitiva retira iones del agua al aplicar una diferencia de "
        "potencial entre dos electrodos porosos; la fotocatálisis heterogénea degrada "
        "contaminantes con un semiconductor activado por luz.",
        "Dato: el informe lista 29 proyectos con recursos externos vigentes en 2024, 28 de "
        "PROCIENCIA en la fuente Donaciones y Transferencias y uno de Erasmus+. Cinco proyectos "
        "de 2022, rotulados como Básica en el informe, figuran en proceso de cierre. Siete "
        "proyectos no registran ejecución en 2024; seis de ellos empezaron entre noviembre y "
        "diciembre de ese año.",
        "Dato: el mismo responsable técnico ejecuta un proyecto de Investigación Aplicada "
        "2024-01 sobre desalinización por desionización capacitiva "
        "(PE501086421-2024-PROCIENCIA, S/ 500 000) y un proyecto posdoctoral de 2024 sobre "
        "reactores de desionización capacitiva.",
        "Verificar antes de la clase: si PROCIENCIA emitió el oficio de cierre, si los "
        "productos del proyecto están en el repositorio institucional de la UNI y el origen "
        "de los 32 meses de ejecución, que superan los 24 meses de la modalidad en las bases "
        "2022-01.",
    ],
))

rec("U3")

L.append(cierre(
    "sintesis-01",
    "01 · Síntesis",
    "Ejecución y *cierre* del proyecto",
    [
        "Plazo: del primer desembolso al último hito",
        "Gasto: vínculo, fecha, comprobante, proveedor y bien",
        "Hito: avance técnico y financiero en SmartSIG",
        "Cierre: informe final en 60 días y oficio de cierre",
    ],
    ("Receso", "10 minutos · Tema 02: registro, difusión, valorización y transferencia de "
               "resultados"),
    notas=[
        "Recapitular el criterio de cada término del tema 01.",
        "Dato: la vigencia del contrato es más larga que el plazo de ejecución; empieza con la "
        "firma y termina con el oficio de cierre (guía 2027, num. 2.1-2.2).",
    ],
))

# ============== TEMA 02 · REGISTRO, DIFUSIÓN, VALORIZACIÓN Y TRANSFERENCIA

L.append(seccion(
    "tema-02", "02", "Registro, difusión, valorización y transferencia de resultados",
    "Resultados que exigen las bases, orden de su protección y publicación, y documentos con "
    "que el resultado llega a un usuario",
    notas=[
        "Presentar el tema 02, que trata los productos que el proyecto entrega al cierre y el "
        "orden en que se protegen, se publican y se ofrecen a un usuario.",
        "Tiempo: 79 minutos; presentación del tema, 1; resultados exigidos y protección, 31; "
        "publicación, repositorio y datos abiertos, 22; paquete tecnológico, valorización y "
        "transferencia, 22; síntesis, 3.",
    ],
))

# ---------- U4 · Resultados exigidos y protección

L.append(tarjetas(
    "resultados-exigidos",
    "02 · Resultados exigidos",
    "Resultados exigidos al cierre de un proyecto de *Desarrollo Tecnológico* 2027",
    [
        ("Resultado validado", "TRL 5 o superior, con informe de pruebas"),
        ("Actividad con usuarios", "Validación con potenciales adoptantes"),
        ("Reporte de viabilidad", "Patentabilidad; si es positiva, solicitud de protección"),
        ("Paquete tecnológico", "Información para madurar y transferir"),
        ("Planes y ficha", "Uso, escalamiento y ficha tecnológica"),
    ],
    clave=2,
    iconos=["check", "users", "patent", "file", "rubric"],
    fuente=BASES + ", num. 1.6, tabla 2 y notas 3-7",
    notas=[
        "La tabla 2 de las bases añade una tesis de posgrado opcional. Si el producto es un "
        "software, la solicitud de protección puede ser el registro de derechos de autor ante "
        "el INDECOPI.",
        "La actividad con usuarios puede ser una prueba en entorno relevante, una sesión "
        "demostrativa, una mesa técnica o una rueda de negocios; se documenta en un informe "
        "«cuidando no afectar la novedad ni la estrategia de propiedad intelectual» (nota 3).",
        "Dato: en Investigación Aplicada 2027 los resultados exigidos son artículos "
        "científicos originales, tesis y ponencias en congresos (bases E041-2027-03, tablas 3 "
        "y 4).",
        "El video de tres minutos para la difusión de los resultados, que la entidad se "
        "compromete a elaborar (Anexo 4A), es financiable como servicio de terceros (Anexo 8) "
        "y es material para el _pitch_ de la sesión 6. El video de postulación, de hasta cinco "
        "minutos (num. 1.5), no es un gasto financiable.",
    ],
))

L.append(pasos(
    "reporte-viabilidad",
    "02 · Reporte de viabilidad de patente",
    "Contenido del *reporte de viabilidad* de patente, Anexo 12 de las bases 2027",
    [
        ("Materia patentable", "Arts. 15 y 20 de la Decisión 486; recursos genéticos"),
        ("Estrategia de búsqueda", "Palabras clave y clasificaciones CIP y CPC"),
        ("Documentos citados", "Categorías X, Y, A, O y T según su relevancia"),
        ("Novedad y ventaja técnica", "Comparación con el estado de la técnica"),
        ("Resultado", "Recomendación de patente o de modelo de utilidad"),
    ],
    clave=4,
    fuente=BASES + ", num. 1.6 y Anexos 12 y 15",
    notas=[
        "El reporte de viabilidad de patente lo elabora o gestiona el gestor tecnológico y lo "
        "emite el INDECOPI, un Centro de Apoyo a la Tecnología y la Innovación (CATI), la "
        "oficina de transferencia de la entidad o un tercero con un especialista en propiedad "
        "intelectual (num. 1.6). El Anexo 12 aclara que es una opinión a una fecha determinada "
        "y no un adelanto del examen de la Dirección de Invenciones y Nuevas Tecnologías.",
        "La Clasificación Internacional de Patentes (CIP) y la Clasificación Cooperativa de "
        "Patentes (CPC) ordenan los documentos por campo técnico. X marca un documento "
        "relevante por sí solo; Y, uno relevante combinado con otros; A, el estado de la "
        "técnica general; O, una divulgación oral; T, un documento posterior a la fecha de "
        "presentación que se cita por la teoría o el principio en que se basa la invención.",
        "Dato: el Anexo 15 lista 57 CATI de la red que coordina el INDECOPI; el de la UNI es "
        "el n.º 28.",
        "Dato: el Programa Patenta del INDECOPI ofrece asistencia gratuita para el reporte de "
        "viabilidad y la redacción de la solicitud, en cinco ciclos al año (Andina, 26 de enero "
        "de 2026).",
        "La búsqueda declarada de la sesión 4 era de literatura científica; la del reporte de "
        "viabilidad es de documentos de patente.",
    ],
))

L.append(visual(
    "calendario-proteccion",
    "02 · Calendario de protección",
    "Plazos de una solicitud de patente en la *Comunidad Andina* y en el PCT, en meses",
    linea_tiempo(
        [
            (-12, "Inicio del plazo de gracia", "Divulgación propia admitida (art. 17)", False),
            (0, "Solicitud nacional", "Presentación ante el INDECOPI", True),
            (12, "Fin de la prioridad", "Solicitud PCT o en el exterior", False),
            (18, "Publicación", "Art. 40; oposición en 60 días", False),
            (24, "Pedido de examen", "Hasta 6 meses tras la publicación (art. 44)", False),
            (30, "Fase nacional PCT", "En general, desde la fecha de prioridad", False),
        ],
        tramos=[(-12, 0, "Gracia · 12 meses", False), (0, 12, "Prioridad · 12 meses", False),
                (0, 30, "Reserva en el repositorio · 12 + 18 meses", True)],
        escala=(-12, 36, 6), unidad="MES",
    ),
    fuente="Decisión 486, arts. 9, 17, 40, 42 y 44 · OMPI, preguntas frecuentes del PCT, "
           "2026 · DS 006-2015-PCM, art. 13.2",
    notas=[
        "Dato: la Decisión 486, art. 17, dispone: «Para efectos de determinar la "
        "patentabilidad, no se tomará en consideración la divulgación ocurrida dentro del año "
        "precedente a la fecha de la presentación de la solicitud en el País Miembro o dentro "
        "del año precedente a la fecha de prioridad, si ésta hubiese sido invocada, siempre que "
        "tal divulgación hubiese provenido de a) el inventor o su causahabiente; b) una oficina "
        "nacional competente que, en contravención de la norma que rige la materia, publique el "
        "contenido de la solicitud […]; o, c) un tercero que hubiese obtenido la información "
        "directa o indirectamente del inventor o su causahabiente».",
        "El plazo de gracia no rige igual en todas las oficinas. La Oficina Europea de Patentes "
        "exime las divulgaciones de los seis meses previos por abuso evidente o por exhibición "
        "en una exposición internacional reconocida (Convenio sobre la Patente Europea, "
        "art. 55); Estados Unidos admite un año para la divulgación del inventor (35 U.S.C. "
        "102(b)(1)(A)). Un artículo del propio inventor publicado dentro de los 12 meses "
        "previos a la solicitud queda cubierto en la Comunidad Andina y en Estados Unidos, pero "
        "destruye la novedad ante la Oficina Europea.",
        "Dato: la solicitud se publica a los 18 meses (art. 40); la oposición se presenta "
        "dentro de 60 días de la publicación, prorrogables por 60 (art. 42); el examen de fondo "
        "se pide dentro de los seis meses siguientes a la publicación, bajo pena de abandono "
        "(art. 44). La patente dura 20 años desde la presentación (art. 50); el modelo de "
        "utilidad, 10 años (art. 84).",
        "Dato: el PCT, que administra la Organización Mundial de la Propiedad Intelectual "
        "(OMPI), tiene 159 Estados contratantes, con Bahamas obligada desde el 19 de agosto de 2026; el Perú es parte "
        "desde el 6 de junio de 2009. La fase nacional se inicia, en general, antes del mes 30 "
        "desde la fecha de prioridad (OMPI, 2026).",
        "Dato: el Reglamento de la Ley 30035 permite reservar del repositorio un resultado "
        "patentable 12 meses desde su entrega, ampliables 18 meses si se presentó la solicitud "
        "ante el INDECOPI (DS 006-2015-PCM, art. 13.2). La lámina supone que la entrega "
        "coincide con el mes de la solicitud.",
        "Error frecuente: confiar en el plazo de gracia para publicar primero. La práctica "
        "prudente es solicitar antes de divulgar; la ficha tecnológica del Anexo 11 se completa "
        "después de presentar la solicitud.",
    ],
))

L.append(caso(
    "caso-pct",
    "02 · Caso de estudio · vía PCT",
    "Sensor de metales pesados con PET",
    "UNI, Facultad de Ciencias · solicitudes peruana y PCT, agosto de 2024",
    [
        ("Ago. 2024", "Solicitud internacional PCT/PE2024/050016"),
        ("May. 2026", "Publicación de la solicitud peruana PE20260953A1"),
        ("Mes 30", "Entrada en fases nacionales, hacia febrero de 2027 (estimación)"),
    ],
    icono_s5("electrodo"),
    fuente="Google Patents, PE20260953A1 y WO2026038966A1, consulta de octubre de 2026 · "
           "OMPI, preguntas frecuentes del PCT, 2026",
    notas=[
        "Un grupo de la Facultad de Ciencias de la UNI, el de la investigadora Angélica Baena "
        "Moncada, presentó el 12 de agosto de 2024 una solicitud internacional por la vía del "
        "PCT y el 13 de agosto de 2024 la solicitud peruana, para un sensor electroquímico de "
        "metales pesados elaborado con residuos de tereftalato de polietileno (PET). La UNI "
        "figura como titular; la solicitud internacional se publicó como WO2026038966A1 el 19 "
        "de febrero de 2026.",
        "Con la solicitud internacional, la fecha de presentación vale en todos los Estados "
        "contratantes del PCT a esa fecha, 157 en agosto de 2024 (hoy son 159, con Uruguay "
        "desde 2025 y Bahamas desde 2026), y la concesión sigue a cargo de cada oficina "
        "nacional o regional. No existe una patente internacional.",
        "La fecha de febrero de 2027 es una estimación del docente: supone que la solicitud de "
        "agosto de 2024 es la primera y aplica el plazo general de 30 meses.",
        "Dato: PROCIENCIA financia por concurso la fase internacional del PCT. En Registro de "
        "Patentes PCT 2025-01 hubo 91 postulaciones y 11 seleccionadas, por S/ 259 060 en "
        "total; la convocatoria E062-2027-01 otorga hasta S/ 15 000 por propuesta y cierra el "
        "30 de octubre de 2026 (RDE 069-2025-PROCIENCIA-DE; bases E062-2027-01).",
        "Verificar antes de la clase: el estado de las dos solicitudes en el buscador del "
        "INDECOPI y en PATENTSCOPE, y si la solicitud internacional reivindica una prioridad "
        "anterior.",
    ],
))

L.append(visual(
    "tasas-indecopi",
    "02 · Tasas de protección",
    "Tasas del *INDECOPI* para patente, modelo de utilidad, software y PCT, 2026",
    barras_apiladas([
        ("Patente de invención", [396.0, 324.0], "clave", "S/ 720,00"),
        ("Modelo de utilidad", [226.8, 97.2], "", "S/ 324,00"),
        ("Registro de software", [357.7], "", "S/ 357,70"),
        ("Transmisión de la solicitud PCT", [233.3], "", "S/ 233,30"),
        ("Búsqueda de información tecnológica", [201.6], "", "S/ 201,60"),
    ], maximo=800, paso=100, menor=20, unidad="SOLES POR TRÁMITE", xb=600,
        leyenda=("PRESENTACIÓN O TRÁMITE", "EXAMEN DE FONDO")),
    fuente="INDECOPI, listado de aranceles actualizado al 1 de enero de 2026 (Banco de la "
           "Nación) · Programa Patenta, tasas",
    notas=[
        "Dato: la patente de invención suma S/ 396,00 de presentación y S/ 324,00 de examen de "
        "fondo; el modelo de utilidad, S/ 226,80 y S/ 97,20. La tasa del modelo de utilidad es "
        "el 45 % de la de la patente.",
        "Dato: la anualidad de una patente es de S/ 116,60 por año antes de la concesión y de "
        "S/ 139,50 por año de vigencia después; en el plazo de gracia, S/ 180,50.",
        "Las tasas de presentación internacional y de búsqueda del PCT las cobra la oficina "
        "receptora, que las transfiere a la OMPI y a la administración de búsqueda (Reglamento "
        "del PCT, reglas 15.1 y 16.1); el INDECOPI, como oficina receptora, cobra además la "
        "tasa de transmisión.",
        "Dato: las tasas y los servicios de propiedad intelectual, nacionales y del PCT, son "
        "financiables como servicios de terceros en las bases 2027 (Anexo 8). El listado del "
        "INDECOPI no prevé descuentos para universidades.",
        "Dato: en 2026 una universidad pública puede destinar hasta el 20 % de sus recursos de "
        "canon, sobrecanon y regalías a gasto corriente de proyectos de investigación y hasta "
        "el 10 % a software, licencias y patentes, entre otros fines (Ley 32513, art. 80.1 c "
        "y d).",
        "Implicación para el formulador: las anualidades y la fase nacional en otros países se "
        "pagan después del cierre del proyecto; quién las paga se acuerda con la oficina de "
        "transferencia antes de presentar la solicitud.",
    ],
))

L.append(duo(
    "software-registro-y-deposito",
    "02 · Software",
    "Registro y depósito del *software* de un proyecto con fondos públicos",
    {"cab": "Registro", "t": "Derecho de autor desde la creación",
     "items": ["Registro declarativo (DL 822)",
               "Tasa de S/ 357,70 en 2026",
               "Resultado admitido en Desarrollo Tecnológico"]},
    {"cab": "Depósito", "t": "Difusión completa en el repositorio nacional",
     "items": ["Programas y archivos del proyecto",
               "Metadatos si está protegido",
               "Código fuente y manuales"]},
    fuente="DL 822, arts. 3, 69 y 170-171 · " + CONTRATO + ", cl. 12.ª · DS 006-2015-PCM",
    notas=[
        "El Decreto Legislativo 822, Ley sobre el Derecho de Autor, protege el programa de "
        "ordenador como obra literaria, sin registro ni formalidad (arts. 3 y 69). El registro "
        "es facultativo y no constitutivo; sirve de publicidad y de prueba de anterioridad "
        "(arts. 170-171).",
        "El contrato 2027 obliga a difundir de manera completa los archivos digitales y los "
        "programas informáticos del proyecto en el Repositorio Nacional Digital de Ciencia, "
        "Tecnología e Innovación; si están protegidos por derechos de propiedad, la entidad "
        "entrega los metadatos (cl. 12.ª). PROCIENCIA puede usar los resultados sin requerir "
        "autorización.",
        "Dato: el Reglamento de la Ley 30035 exige a la entidad incluir en sus contratos una "
        "cesión no exclusiva de derechos patrimoniales y, cuando la obra es un software, la "
        "entrega del código fuente, el código objeto, la documentación técnica y los manuales "
        "(art. 10.2).",
        "Implicación para el formulador: la licencia del código y la decisión de protegerlo se "
        "toman antes del depósito. Un secreto empresarial no es compatible con la difusión "
        "completa del código.",
        "Verificar antes de la clase: las modificaciones del DL 822 por el DL 1724 (2026), que "
        "no se cotejaron.",
    ],
))

rec("U4")

# ---------- U5 · Publicación, repositorio y datos abiertos

L.append(pasos(
    "deposito-acceso-abierto",
    "02 · Acceso abierto",
    "Depósito de los resultados en acceso abierto según la *Ley 30035* y su reglamento",
    [
        ("Productos", "Artículo o manuscrito, tesis, datos y plan de gestión de datos"),
        ("Repositorio institucional", "De la entidad o, si no es posible, del CONCYTEC"),
        ("Cosecha nacional", "ALICIA, Repositorio Nacional Digital"),
        ("Acceso abierto", "Lectura y descarga sin registro, suscripción ni pago"),
    ],
    clave=1,
    fuente="Ley 30035 · DS 006-2015-PCM, arts. 2, 3, 11 y 13 · " + CONTRATO + ", cl. 8.ª · " +
           GUIA + ", num. 3.5-3.6",
    notas=[
        "El Reglamento de la Ley 30035 define el acceso abierto como el acceso inmediato y "
        "gratuito a una obra, a datos procesados o a estadísticas de monitoreo, sin registro, "
        "suscripción ni pago, con autorización para leer, descargar, reproducir, distribuir, "
        "imprimir, buscar y enlazar (art. 2.1). Rige para las entidades públicas y para los "
        "privados que usan fondos del Estado (art. 3).",
        "Dato: lo financiado con fondos públicos se publica en el repositorio institucional "
        "para que lo recolecte el Repositorio Nacional Digital (art. 11). La exclusividad "
        "editorial permite postergar el depósito hasta 24 meses; un resultado patentable, 12 "
        "meses, ampliables 18 si se presentó la solicitud (art. 13).",
        "Dato: el contrato 2027 obliga a depositar el PGD y los productos según la Ley 30035 "
        "(cl. 8.ª). La guía pide reconocer el financiamiento con la fórmula «Este trabajo fue "
        "subvencionado por el CONCYTEC a través del programa PROCIENCIA en el marco del "
        "concurso […], según contrato [número]» (num. 3.6).",
        "ALICIA (Acceso Libre a Información Científica para la Innovación) es el repositorio "
        "nacional que cosecha los repositorios institucionales. El cargo de publicación en una revista de acceso abierto es "
        "financiable como servicio de terceros (Anexo 8).",
        "Verificar antes de la clase: si el repositorio de la UNI está integrado en la red "
        "nacional que cosecha ALICIA.",
    ],
))

L.append(caso(
    "caso-articulo",
    "02 · Caso de estudio · publicación",
    "Electrodos de coronta de maíz",
    "UNI, Facultad de Ciencias · artículo en _ACS Environmental Au_, 2024",
    [
        ("Ago. 2022", "Solicitudes de patente peruana e internacional, titular UNI"),
        ("Ago. 2023", "Envío del manuscrito a la revista"),
        ("Ene. 2024", "Artículo en acceso abierto con el contrato del financiador"),
    ],
    icono_s5("moneda"),
    fuente="Huarote-García et al., _ACS Environmental Au_, 4(2), 80-88, 2024 · Google Patents, "
           "PE20240417A1",
    notas=[
        "El artículo «Activated Carbon Electrodes for Supercapacitors from Purple Corncob (_Zea "
        "mays_ L.)» (Huarote-García et al., 2024), del grupo de Angélica Baena Moncada, declara "
        "el financiamiento del CONCYTEC y del FONDECYT con el Banco Mundial mediante el "
        "contrato 026-2019 FONDECYT-BM-INC.INV.",
        "Dato: la solicitud peruana del grupo sobre electrodos de coronta de maíz morado se "
        "presentó el 4 de agosto de 2022 y se publicó como PE20240417A1 el 7 de marzo de 2024; "
        "la internacional, PCT/PE2022/050015, el 18 de agosto de 2022. La revista recibió el "
        "manuscrito el 15 de agosto de 2023 y lo publicó el 5 de enero de 2024.",
        "Dato: el artículo se publicó con la licencia Creative Commons CC BY-NC-ND 4.0, que "
        "permite leer y redistribuir con atribución, sin uso comercial ni obras derivadas. "
        "OpenAlex atribuye el código de financiamiento a un fondo homónimo de Chile; el nombre "
        "completo del programa en el agradecimiento evita esa confusión.",
        "El grupo ganó después Investigación Aplicada 2024-01 con un banco de supercapacitores "
        "de coronta de maíz morado para scooters eléctricos (PE501086503-2024-PROCIENCIA), que "
        "ejecutó S/ 22 000 entre junio y diciembre de 2024 (VRI-UNI).",
        "Verificar antes de la clase: si el artículo está depositado en el repositorio "
        "institucional de la UNI.",
    ],
))

L.append(tarjetas(
    "plan-gestion-datos",
    "02 · Plan de gestión de datos",
    "Contenido del *plan de gestión de datos* según la guía del CONCYTEC, 2025",
    [
        ("Creación y organización", "Datos que se generan, carpetas, nombres y versiones"),
        ("Documentación", "Recopilación y análisis descritos con metadatos"),
        ("Aspectos éticos y legales", "Licencia CC BY 4.0 como estándar"),
        ("Conservación y reutilización", "Copias, riesgos, datos que se abren y responsables"),
    ],
    clave=2,
    iconos=["file", "book", "rubric", "globe"],
    fuente=BASES + ", Anexo 14 (guía del plan de gestión de datos de investigación) · " +
           GUIA + ", num. 3.5",
    notas=[
        "El plan de gestión de datos describe qué datos se recogen o generan, con qué "
        "metodología y estándares, y cómo se comparten, abren, conservan y preservan. Se "
        "presenta al postular, se actualiza durante la ejecución y "
        "se deposita según la Ley 30035 (guía 2027, glosario y num. 3.5).",
        "La guía del Anexo 14 tiene diez secciones, de la información general del proyecto a "
        "las responsabilidades y los recursos. Recomienda la licencia Creative Commons "
        "Atribución 4.0 (CC BY) como estándar y adopta los principios FAIR: datos localizables, "
        "accesibles, interoperables y reutilizables (Wilkinson et al., 2016).",
        "La guía define el cuaderno de laboratorio como el registro primario de la "
        "investigación, en papel o electrónico, con protocolos, hipótesis, resultados y "
        "análisis iniciales. El paquete tecnológico exige además el control de versiones de "
        "los archivos técnicos (Anexo 16).",
        "Dato: una revisión de 105 estudios sobre 2 121 580 artículos de medicina y ciencias "
        "de la salud estimó que, entre 2016 y 2021, el 8 % declaró sus datos disponibles y el "
        "2 % los tenía disponibles de hecho; el código compartido no llegó al 0,5 % (Hamilton "
        "et al., 2023). El dato no es de ingeniería.",
        "Implicación para el formulador: el costo de almacenar y publicar los datos se incluye "
        "en el presupuesto del proyecto.",
    ],
))

L.append(caso(
    "caso-datos-abiertos",
    "02 · Caso de estudio · datos de libre descarga",
    "Red acelerográfica del CISMID",
    "UNI, Facultad de Ingeniería Civil · sismo de Ica del 4 de julio de 2025",
    [
        ("M5,3", "Sismo con epicentro a 106 km al suroeste de Ica"),
        ("49", "Estaciones con registro; 38 de la red REDACIS"),
        ("Descarga", "Registros sin filtrar en el sitio del CISMID"),
    ],
    icono_s5("acelerografo"),
    fuente="CISMID-FIC-UNI, informe acelerográfico del sismo del 4 de julio de 2025 · "
           "cismid.uni.edu.pe/ceois/redacis",
    notas=[
        "El Centro de Observación para la Ingeniería Sísmica (CEOIS) del CISMID publica un "
        "informe por cada sismo relevante con los registros de la Red Nacional de Acelerógrafos "
        "del CISMID (REDACIS).",
        "Dato: del sismo de magnitud 5,3 del 4 de julio de 2025 se obtuvieron registros en 49 "
        "estaciones: 38 de REDACIS, 7 de la red del Centro de Investigación en Transformación "
        "Digital en Ingeniería (CITDI) de la Facultad de Ingeniería Civil y 4 en convenio con el "
        "Servicio Nacional de Capacitación para la Industria de la Construcción (SENCICO). La "
        "aceleración máxima, 6,49 cm/s², se registró en la estación de la Universidad Nacional "
        "San Luis Gonzaga de Ica.",
        "El informe declara el procesamiento: los registros se filtraron con un pasa banda "
        "entre 0,04 s y 10 s y se corrigieron por línea base, y los registros sin filtrar se "
        "descargan del sitio de REDACIS. Esa descripción es el tipo de metadato que pide un plan "
        "de gestión de datos.",
        "Los registros sirven para el diseño sismorresistente y para la investigación en "
        "ingeniería sísmica de otros grupos.",
        "Sin una licencia declarada, los registros son de libre descarga pero no datos abiertos "
        "en sentido estricto; la guía del Anexo 14 pide declarar la licencia, con CC BY 4.0 "
        "como estándar.",
        "Verificar antes de la clase: la licencia y las condiciones de uso de los registros de "
        "REDACIS.",
    ],
))

rec("U5")

# ---------- U6 · Paquete tecnológico, valorización y transferencia

L.append(tarjetas(
    "paquete-tecnologico",
    "02 · Paquete tecnológico",
    "Documentos de *transferencia* exigidos en Desarrollo Tecnológico, Anexos 11 y 16",
    [
        ("Paquete tecnológico", "Arquitectura, planos, desempeño, propiedad intelectual y "
                                "trazabilidad documental"),
        ("Plan de uso o transferencia", "Usuarios, mecanismo, condiciones y evidencias de "
                                        "interés"),
        ("Plan de escalamiento", "Brechas desde TRL 5 hacia TRL 6, ruta regulatoria e "
                                 "inversiones"),
        ("Ficha tecnológica", "Registro público después de solicitar la protección"),
    ],
    clave=0,
    iconos=["file", "agreement", "chart", "globe"],
    fuente=BASES + ", Anexos 11 y 16",
    notas=[
        "Las bases definen el paquete tecnológico para transferencia como un conjunto "
        "organizado de documentos técnicos que sistematiza el conocimiento generado, las "
        "condiciones de reproducción, operación y validación del resultado y lo necesario para "
        "continuar su maduración, escalamiento y transferencia (Anexo 16, num. 1).",
        "El índice del paquete incluye la trazabilidad y gestión documental: inventario de "
        "productos y archivos técnicos, control de versiones, ubicación y estado de la "
        "documentación, repositorios y medidas de respaldo (Anexo 16, 1.1 i).",
        "El plan de uso, transferencia o adopción identifica usuarios y el mecanismo previsto, "
        "que puede ser licencia, codesarrollo o adopción; el plan de escalamiento fija la ruta "
        "desde TRL 5 hacia TRL 6 o superior, con las brechas técnicas, regulatorias, "
        "productivas y financieras.",
        "La ficha tecnológica se completa después de presentar la solicitud de protección y se "
        "difunde en Vincúlate, la plataforma de vinculación del CONCYTEC, que prioriza "
        "tecnologías de TRL 4 o superior (Anexo 11).",
    ],
))

L.append(tarjetas(
    "metodos-valorizacion",
    "02 · Valorización",
    "Enfoques de valorización de la propiedad intelectual según la *OMPI*, 2025",
    [
        ("Costo", "Recursos para reproducir o sustituir el activo; no predice ingresos"),
        ("Mercado", "Transacciones comparables, escasas en tecnología temprana"),
        ("Ingresos", "Flujos futuros descontados, con el riesgo concentrado en la tasa"),
    ],
    iconos=["chart", "search", "target"],
    fuente="OMPI, _IP Valuation Basics for Technology Transfer Professionals_, 2025, caps. 4-6",
    notas=[
        "La guía de la OMPI de 2025 describe los tres enfoques clásicos y advierte que la "
        "propiedad intelectual académica suele valorarse en TRL 1 a 4, donde los métodos "
        "tradicionales dan rangos amplios e inciertos (cap. 2). Las opciones reales y la "
        "simulación de Monte Carlo complementan esos enfoques (caps. 7-8).",
        "La regla del 25 % asigna al licenciante cerca de un cuarto de la utilidad operativa "
        "esperada del licenciatario; proviene de un estudio de fines de los años cincuenta "
        "(Goldscheider, Jarosz y Mulhern, 2002). En _Uniloc USA v. Microsoft_ (2011), el "
        "Tribunal de Apelaciones del Circuito Federal de Estados Unidos rechazó la regla como "
        "base para fijar la regalía razonable en un litigio por infracción de patente y declaró inadmisible la prueba que se apoya en ella.",
        "Dato: en 1 533 licencias entre empresas, de fines de los ochenta a 2000, la regalía "
        "mediana fue 4,5 %; por sector, 6,8 % en software, 5,1 % en farmacéutica y "
        "biotecnología, 4,8 % en productos de salud, 4,0 % en electrónica y 3,6 % en química "
        "(Goldscheider, Jarosz y Mulhern, 2002). La guía de licencias de la OMPI indica que "
        "muchos licenciantes cobran entre 0,5 % y 5 % de los ingresos (OMPI, 2015).",
        "Error frecuente: presentar un valor único. Los tres enfoques dan un rango que sirve "
        "como posición de negociación.",
    ],
))

L.append(duo(
    "valorizacion-por-costo",
    "02 · Valorización por costo",
    "Piso de valor por costo de una *fibra acrílica* antimicrobiana, ejemplo",
    {"cab": "Componentes del costo", "t": "Inversión para reproducir el resultado",
     "items": ["S/ 350 000 de PROCIENCIA, Desarrollo Tecnológico 2024-02",
               "Contrapartida no monetaria de la UNI",
               "Tasas de protección y ensayos del proyecto"]},
    {"cab": "Fuera del costo", "t": "Valor de uso para un licenciatario",
     "items": ["Mercado de fibras antimicrobianas",
               "Regalías de licencias comparables",
               "Riesgo y costo del escalamiento industrial"]},
    fuente="PROCIENCIA, seleccionados de Desarrollo Tecnológico 2024-02 · OMPI, 2025, cap. 4",
    notas=[
        "El proyecto «Síntesis del compuesto de fibras acrílicas hiladas en seco con "
        "nanopartículas de CuO, inyectadas en el proceso de extrusión, para la obtención de "
        "propiedades antimicrobianas», con responsable técnico "
        "José Luis Solís Véliz, fue seleccionado en Desarrollo Tecnológico 2024-02 con "
        "S/ 350 000.",
        "El enfoque del costo estima el valor por los recursos necesarios para recrear el "
        "activo (reproducción) o para obtener uno equivalente (reemplazo). En TRL bajo sirve "
        "como piso o línea de base de la negociación (OMPI, 2025, cap. 4).",
        "Dato: con la regla de Desarrollo Tecnológico 2027 para una entidad pública, 75 % de "
        "PROCIENCIA y al menos 25 % no monetario, el costo total sería S/ 466 667. El cálculo es "
        "ilustrativo; la regla de 2024-02 y la contrapartida real no se verificaron.",
        "Error frecuente: tomar el costo del proyecto como precio de la licencia.",
    ],
))

L.append(caso(
    "caso-licencia",
    "02 · Caso de estudio · licencia",
    "Licencia exclusiva de la Unicamp",
    "Universidad Estatal de Campinas, Brasil · solicitud de patente BR102020011648-7",
    [
        ("3,0 %", "Regalía mínima sobre la facturación líquida mensual"),
        ("R$ 10 000", "Tasa de acceso mínima a la tecnología"),
        ("18 meses", "Plazo para invertir sin perder la exclusividad"),
    ],
    icono_s5("magnetica"),
    fuente="Inova Unicamp, extracto de oferta tecnológica 02/2025, 17 de diciembre de 2025, y "
           "resultado Inova 4/2026, 19 de febrero de 2026",
    notas=[
        "La Universidad Estatal de Campinas (Unicamp) ofreció en diciembre de 2025 la licencia "
        "exclusiva de la solicitud de patente BR102020011648-7, presentada en 2020, sobre un "
        "proceso que reduce la sacarosa de bebidas con nanopartículas magnéticas recubiertas de "
        "sílice y la enzima invertasa inmovilizada. En febrero de 2026 seleccionó a la empresa "
        "Bugar Labs, con 34 de 80 puntos.",
        "Dato: el extracto fijó una regalía mínima de 3,0 % sobre la facturación líquida "
        "mensual de los productos con la tecnología y una tasa de acceso mínima de R$ 10 000; "
        "estimó en cerca de R$ 80 000 el desarrollo complementario. Si el licenciatario no "
        "inicia la inversión en 18 meses desde la firma, la licencia pasa a no exclusiva. La "
        "búsqueda de libertad de operación corre por cuenta del licenciatario.",
        "En los criterios de regalía y de tasa de acceso, la empresa obtuvo cero puntos, que "
        "la tabla asigna a la oferta igual al mínimo; la lectura de que aceptó los mínimos es "
        "una inferencia del docente.",
        "La ley brasileña de innovación (Ley 10.973/2004) y su reglamento (Decreto 9.283/2018) "
        "obligan a publicar el extracto de la oferta cuando la licencia es exclusiva (Ley "
        "10.973, art. 6, § 1). No se hallaron licencias de universidades peruanas con términos "
        "publicados.",
        "Un contrato de licencia fija objeto, titularidad, exclusividad por campo, territorio o "
        "tiempo, sublicencias, plazo, pagos, mejoras, asistencia técnica, confidencialidad y "
        "solución de controversias (OMPI, 2015).",
    ],
))

rec("U6")

L.append(cierre(
    "sintesis-02",
    "02 · Síntesis",
    "Protección y *transferencia* de resultados",
    [
        "Resultados: tabla 2 de las bases de Desarrollo Tecnológico",
        "Protección: solicitud antes de la divulgación",
        "Depósito: repositorio institucional, licencia y metadatos",
        "Valorización: rango entre costo, mercado e ingresos",
    ],
    notas=[
        "Recapitular el criterio de cada término del tema 02.",
        "Dato: el Reglamento de la Ley 30035 permite reservar un resultado patentable hasta "
        "12 + 18 meses, de modo que el depósito obligatorio no compromete la solicitud "
        "(DS 006-2015-PCM, art. 13.2).",
    ],
))

# ================================================================ CIERRE (5 min)

L.append(cierre(
    "sintesis-sesion",
    "Cierre",
    "Ejecución del contrato de subvención y *transferencia* del resultado",
    [
        "Ejecución: contrato, POP, gasto elegible, hitos y oficio de cierre",
        "Resultados: protección, acceso abierto, paquete y valorización",
    ],
    ("Sesión 6", "_Pitch_ y sustentación de proyectos"),
    notas=[
        "Recapitular la sesión: el contrato y sus documentos, el gasto y sus reglas, la "
        "revisión de hitos y el cierre; los resultados exigidos, su protección, su depósito en "
        "acceso abierto y los documentos con que se ofrecen a un usuario.",
        "La sesión 5 cierra el bloque de formulación y ejecución iniciado con el financiamiento "
        "(sesión 3) y la redacción de la propuesta (sesión 4).",
        "La sesión 6, de 90 minutos, trata el _pitch_ y la sustentación de proyectos. "
        "El resumen técnico, la ficha tecnológica y el video de tres minutos del proyecto son "
        "material para el _pitch_.",
    ],
))

L.append(referencias(
    "fuentes",
    "Referencias de la sesión",
    [
        ("ciclo-de-ejecucion", "PROCIENCIA (2026). _Guía de soporte, seguimiento y evaluación_, concursos 2027."),
        ("documentos-de-gestion", "PROCIENCIA (2026). _Modelo de contrato_, E041-2027-02."),
        ("caso-arranque", "PROCIENCIA (2026). RDE 087-2026-PROCIENCIA-DE."),
        ("transferencia-entidad-publica", "CONCYTEC (2026). RP 088-2026-CONCYTEC-P. Ley 31250."),
        ("rubros-financiables", "PROCIENCIA (2026). _Bases y anexos_, E041-2027-02 y -03. Ley 32513."),
        ("compras-entidad-publica", "Ley 32069 (2024). Ley General de Contrataciones Públicas."),
        ("caso-cierre", "VRI-UNI (2025). _Ejecución con recursos externos, año 2024_. PROCIENCIA (2022). RDE 055-2022-PROCIENCIA-DE."),
        ("reporte-viabilidad", "Comunidad Andina (2000). Decisión 486."),
        ("calendario-proteccion", "OMPI (2026). _PCT FAQs_. DS 006-2015-PCM."),
        ("caso-pct", "PROCIENCIA (2025). RDE 069-2025-PROCIENCIA-DE."),
        ("tasas-indecopi", "INDECOPI (2026). _Listado de aranceles_, 01-01-2026."),
        ("software-registro-y-deposito", "Decreto Legislativo 822 (1996)."),
        ("deposito-acceso-abierto", "Ley 30035 (2013). DS 006-2015-PCM (2015)."),
        ("caso-articulo", "Huarote-García, E. et al. (2024). _ACS Environ. Au_, 4(2), 80-88."),
        ("plan-gestion-datos", "CONCYTEC (2025). _Guía del plan de gestión de datos de investigación_. Hamilton, D. G. et al. (2023). _BMJ_, 382, e075767. Wilkinson, M. D. et al. (2016). _Sci. Data_, 3."),
        ("caso-datos-abiertos", "CISMID-FIC-UNI (2025). Informe acelerográfico, 04-07-2025."),
        ("metodos-valorizacion", "OMPI (2025). _IP Valuation Basics_. Goldscheider, R. et al. (2002). _les Nouvelles_, 37."),
        ("caso-licencia", "Inova Unicamp (2025-2026). Extracto 02/2025. OMPI (2015). Pub. 903."),
    ],
    notas=[
        "Referencias completas: Huarote-García et al. (2024), https://doi.org/10.1021/acsenvironau.3c00048; "
        "Hamilton et al. (2023), https://doi.org/10.1136/bmj-2023-075767; Wilkinson et al. (2016), "
        "https://doi.org/10.1038/sdata.2016.18; OMPI (2025), https://doi.org/10.34667/tind.50113; "
        "Goldscheider, Jarosz y Mulhern (2002), les Nouvelles, 37, 123-133; Uniloc USA v. Microsoft, "
        "632 F.3d 1292 (Fed. Cir. 2011); RP 088-2026-CONCYTEC-P, El Peruano, 27 de junio de 2026.",
    ],
))


def _sin_corte(lam):
    """Espacio de no separación en montos y cifras de los nodos de texto
    («S/ 300 000», «R$ 10 000»), para que el salto de línea no parta la cifra."""
    import re

    def fijo(txt):
        txt = re.sub(r"(S/|US\$|R\$|€) (?=\d)", "\\1\u00a0", txt)
        return re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", txt)

    lam.cuerpo = re.sub(r">([^<]+)<", lambda m: ">" + fijo(m.group(1)) + "<", lam.cuerpo)
    return lam


L = [_sin_corte(lam) for lam in L]

construir("clase-05", "Sesión 5 · Ejecución del proyecto y transferencia de resultados", L)
