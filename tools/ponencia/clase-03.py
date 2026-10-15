#!/usr/bin/env python3
"""Sesión 3 · Mapa de financiamiento e inversión — formato ponencia (11.ª edición).

Temas: «Instrumentos públicos de financiamiento de la I+D+i» (tema 01: formas
de financiamiento, programas nacionales, fondos sectoriales y contrapartida) y
«Capital emprendedor y financiamiento internacional» (tema 02: actores de la
inversión en etapa temprana, términos de la inversión y situación del Perú,
cooperación y fondos internacionales).

Secuencia (scratchpad/s3-auditoria-secuencia.md, §4): U1 formas → U2 programas
nacionales → U3 fondos sectoriales y contrapartida → receso → U4 actores → U5
términos y Perú → U6 cooperación internacional. Cambios frente a la secuencia:
la tasa de selección de PROCIENCIA 2026 entra como lámina de dato en la U2; el
ejemplo de dilución pasa a las notas de `contraprestacion`; la ruta de
instrumentos públicos usa `pasos` y el mapa por madurez usa `tramos_trl` (seis
filas). Ninguna sigla se usa antes de la lámina que la presenta.

Contenido: scratchpad/inv-s3.md (conceptos, programas 2026-2027, cifras y
casos). Cotejos propios: POLCTI (Tabla 14 y análisis del gasto por
instrumento), Skalicka et al. (2022, tablas 8, 11 y 13), Avnimelech et al.
(2024, figura 1), Dhiman y Arora (2024, tabla 2), Andina (8 de julio de 2020)
sobre la inversión de HAX en Tumi Robotics y APCI (cooperación de 2023, por
nota del Congreso y el folleto oficial). Recursos: scratchpad/recursos-s3.md
(4 por unidad; el informe de PECAP de la U5 se sustituye por Lerner, 2009,
porque las notas citan el diagnóstico de COFIDE y PECAP).

Formato expositivo: la sesión no incluye actividades en el aula. Las notas
reúnen contenido de respaldo con dato y fuente, errores frecuentes de los
formuladores y puntos por verificar. Los titulares y las explicaciones son
genéricos; los ejemplos concretos van en las notas y no se repiten en otras
sesiones (scratchpad/asignacion-ejemplos.md y banco-ejemplos.md): U01, tala
ilegal (subvención y contrapartida de una universidad pública); X04, Backus
(Ley 30309); X01, WAREM S.A.C. (contrapartida de una empresa); U24 y X07
(FONDOEMPLEO). El ejemplo de inversión ángel usa una empresa genérica.

Antes de dictar, verificar: generación de StartUp Perú abierta en octubre de
2026 (la 13G cerró en enero); dato del Perú en LAVCA 2025; año de los datos del
diagnóstico de COFIDE y PECAP; número y fecha del DS 116-2026-EF; artículo 38
de la Ley 32069; cooperación de EE. UU. en 2023 (US$ 128,6 M); generación de
StartUp Perú y participación cedida a HAX por Tumi Robotics; si PROCIENCIA
publicó las bases de Desafíos para la solución de prioridades nacionales.

Uso:  python3 tools/ponencia/clase-03.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from graficos import barras_valor, icono_tecnico, peldanos, tramos_trl  # noqa: E402
from plantillas import (  # noqa: E402
    agenda, caso, cierre, cifra, construir, duo, frase, pasos, portada, recursos,
    referencias, seccion, tarjetas, visual,
)

FUENTE_REC = "Enlaces verificados en octubre de 2026"

L = []

# ================================================================ APERTURA (5 min)

L.append(portada(
    "portada",
    "Sesión 3 · Diseño y Gestión de Proyectos {I+D+i+e}",
    "Mapa de financiamiento e inversión",
    "Financiamiento de proyectos de I+D+i en el Perú según la fuente y la etapa de madurez",
    ["Instrumentos públicos de financiamiento de la I+D+i",
     "Capital emprendedor y financiamiento internacional"],
    "Abraham Caso-Torres · OTI-UNI · CC BY-SA 4.0",
    visual=peldanos(),
    notas=[
        "Dar la bienvenida y presentar los dos temas de la sesión: los instrumentos con que el "
        "Estado peruano financia la I+D+i y el dinero que no proviene del presupuesto nacional, "
        "el de los inversionistas privados y el de la cooperación internacional.",
        "La sesión 2 trató la vía de transferencia (licencia, _spin-off_ o _startup_) y la "
        "titularidad fijada por escrito. Esta sesión trata las fuentes de "
        "financiamiento que admite cada vía.",
    ],
))

L.append(agenda(
    "agenda",
    "Agenda",
    "Temas y contenidos de la sesión 3",
    [
        ("Instrumentos públicos de financiamiento de la I+D+i",
         ["Formas de financiamiento",
          "Programas nacionales de CTI",
          "Fondos sectoriales y contrapartida"]),
        ("Capital emprendedor y financiamiento internacional",
         ["Actores de la inversión temprana",
          "Términos de la inversión y Perú",
          "Cooperación y fondos internacionales"]),
    ],
    franja=("Receso", "10 minutos, entre el tema 01 y el tema 02"),
    notas=[
        "Presentar los dos temas y las tres unidades de cada uno.",
        "Tiempo: apertura, 5 min; tema 01, 75 min; receso, 10 min; tema 02, 80 min; cierre, "
        "5 min; holgura para preguntas, 5 min.",
        "El presupuesto por rubros, la contrapartida durante la ejecución, el contrato con "
        "PROCIENCIA y la rendición de cuentas corresponden a la sesión 5; la redacción de la "
        "propuesta según las bases, a la sesión 4.",
    ],
))

# ============== TEMA 01 · INSTRUMENTOS PÚBLICOS DE FINANCIAMIENTO DE LA I+D+i

L.append(seccion(
    "tema-01", "01", "Instrumentos públicos de financiamiento de la I+D+i",
    "Formas en que el Estado financia la I+D+i, programas que las operan y aporte exigido a "
    "quien postula",
    notas=[
        "Presentar el tema 01, que trata el dinero del Estado peruano: las formas que adopta, "
        "los programas nacionales y sectoriales que lo administran y la contrapartida que "
        "exigen. La contrapartida es el aporte propio, en dinero o en especie, de quien "
        "postula; se define con las bases de PROCIENCIA en la unidad 3.",
        "Tiempo: 75 minutos; presentación del tema, 1; formas de financiamiento, 22; programas "
        "nacionales, 26; fondos sectoriales y contrapartida, 22; síntesis, 4.",
    ],
))

# ---------- U1 · Formas de financiamiento

L.append(frase(
    "definicion-instrumento",
    "01 · Definición de instrumento",
    "Un *instrumento de política* de CTI es el conjunto de modos y medios con que el Estado "
    "pone en práctica una política de ciencia, tecnología e innovación.",
    "Síntesis de Sagasti y Aráoz (1979), recogida en la POLCTI (CONCYTEC, 2025)",
    notas=[
        "Francisco Sagasti empleó la noción de instrumento de política en el Proyecto de "
        "Instrumentos de Política Científica y Tecnológica de los años setenta. Según Sagasti y "
        "Aráoz (1979), un instrumento comprende un dispositivo legal, una estructura de "
        "organización y un conjunto de instrumentos operacionales (POLCTI, 2025).",
        "Un programa como PROCIENCIA opera varios instrumentos. Cada uno se abre con una "
        "convocatoria, cuyas bases fijan quién postula, el monto máximo, la contrapartida y el "
        "nivel de madurez exigido; el concurso es la modalidad en que las propuestas compiten "
        "por evaluación.",
        "La POLCTI recoge la clasificación de la Red de Indicadores de Ciencia y Tecnología "
        "(RICYT), con 20 tipos de instrumentos agrupados en cinco objetivos: investigación, "
        "innovación, formación de recursos humanos, áreas estratégicas y articulación del "
        "sistema.",
    ],
))

L.append(tarjetas(
    "formas-financiamiento",
    "01 · Formas de financiamiento",
    "Formas de *financiamiento* público de la I+D+i en el Perú",
    [
        ("Subvención por concurso", "Recursos no reembolsables para ejecutar un plan aprobado"),
        ("Beneficio tributario", "Deducción adicional del impuesto a la renta por el gasto en I+D+i"),
        ("Garantía de crédito", "Respaldo público de hasta el 80 % de un préstamo de una entidad financiera"),
        ("Servicio tecnológico", "Ensayos y asistencia técnica de la Red CITE"),
        ("Compra pública de innovación", "Contrato del Estado para una solución que no existe en el mercado"),
    ],
    iconos=["fund", "scale", "budget", "workshop", "building"],
    fuente="PROCIENCIA, bases 2027 · Ley 30309 · PROINNÓVATE, Garantías Tecnológicas · BID, 2023",
    notas=[
        "La subvención no reembolsable transfiere recursos que no se devuelven, condicionados a "
        "ejecutar un plan aprobado y rendir cuentas; las bases de PROCIENCIA 2027 la describen "
        "como «recursos monetarios no reembolsables».",
        "El beneficio tributario no entrega dinero; reduce el impuesto de una empresa con "
        "utilidades. La garantía de crédito tampoco: el préstamo lo otorga una entidad del sistema financiero y el "
        "Programa de Garantías Tecnológicas de PROINNÓVATE garantiza hasta el 80 %.",
        "La compra pública de innovación contrata el desarrollo o la adquisición de una "
        "solución que no existe en el mercado; la modalidad precomercial contrata la I+D y los "
        "prototipos, sin la compra del producto (BID, 2023). La Ley 32069 (2024), Ley General de "
        "Contrataciones Públicas, regula la compra pública de innovación en su artículo 38; no "
        "se halló una compra de ese tipo aplicada a I+D. Los Desafíos Públicos de Innovación de "
        "PROINNÓVATE parten del reto de una entidad pública y se financian como subvención a "
        "una micro, pequeña o mediana empresa.",
        "La Red CITE reúne los Centros de Innovación Productiva y Transferencia Tecnológica "
        "(CITE), públicos y privados, articulados por el Instituto Tecnológico de la "
        "Producción (ITP).",
        "El financiamiento participativo financiero, mediante plataformas "
        "autorizadas por la Superintendencia del Mercado de Valores (SMV), y los fondos internos "
        "de las universidades son otras formas. La participación en el capital de una empresa es una forma "
        "privada y se trata en el tema 02.",
        "Verificar antes de la clase: el texto del artículo 38 de la Ley 32069, confirmado "
        "por comentarios jurídicos y no por el texto oficial.",
    ],
))

L.append(duo(
    "momento-del-dinero",
    "01 · Oportunidad del recurso",
    "Momento del *recurso público* por forma de financiamiento",
    {"cab": "Antes del gasto", "t": "Subvención de PROCIENCIA o PROINNÓVATE",
     "items": ["Desembolsos según el cronograma de las bases",
               "Aporte propio del equipo desde el inicio"]},
    {"cab": "Después del gasto", "t": "Deducción de la Ley 30309",
     "items": ["Proyecto ejecutado y pagado por la empresa",
               "Deducción en la declaración anual del impuesto"]},
    fuente="PROCIENCIA, bases 2027 · Ley 30309, modificada por las leyes 31659 y 32539",
    notas=[
        "Ejemplo de subvención: Chapaq Cocha, sistema de alerta temprana de bajo costo para "
        "peligros de origen glaciar del Instituto Nacional de Investigación en Glaciares y "
        "Ecosistemas de Montaña (INAIGEM), obtuvo S/ 350 000 en Proyectos de Desarrollo "
        "Tecnológico 2026-03 de PROCIENCIA, el tope del concurso (RDE 044-2026-PROCIENCIA-DE). "
        "El monto se desembolsa en una sola armada, antes de que el equipo ejecute el gasto.",
        "Ejemplo de deducción: en mayo de 2016 CONCYTEC presentó a Backus como la primera "
        "empresa con un proyecto calificado por la Ley 30309, la «Preparación de carga "
        "(Picking)» con equipos guiados por láser en su planta de Ate (Andina, 31 de mayo de "
        "2016). La empresa ejecuta y paga el proyecto, y la deducción llega con la declaración "
        "anual del impuesto. La nota no publica el monto.",
        "Según el momento del desembolso, el gasto lo adelanta el programa o la empresa. En la deducción "
        "tributaria, la empresa necesita caja propia; en la garantía de crédito, el préstamo se "
        "devuelve con intereses.",
        "Error frecuente: proponer la deducción de la Ley 30309 como fuente de la contrapartida "
        "de un concurso. La deducción llega después del gasto y no aporta dinero durante la "
        "ejecución.",
        "La ejecución del gasto y su rendición ante el programa se tratan en la sesión 5.",
    ],
))

L.append(cifra(
    "concentracion-instrumentos",
    "01 · Presupuesto público de CTI por instrumento",
    "90", "%",
    "del presupuesto público de CTI asignado a 45 de los 164 instrumentos, promedio 2012-2018",
    "Programa Nacional de Becas: 43 % del presupuesto público de CTI",
    fuente="CONCYTEC, _Política Nacional de CTI al 2030_, con datos de Rogers (2020)",
    notas=[
        "Dato: el estudio de línea base del gasto público en CTI (Rogers, 2020), recogido en la "
        "POLCTI, contó 164 instrumentos con presupuesto en el periodo 2012-2018. Trece de ellos "
        "acumularon tres cuartas partes de los recursos y 49 sumaron el 1 %.",
        "Dato: por sector, Producción operó 71 instrumentos, CONCYTEC 38, Educación 26 y "
        "Agricultura 9 (POLCTI, Tabla 14). Sin el programa de becas, 9 instrumentos de 164 "
        "acumulan la mitad del presupuesto.",
        "El análisis usa el presupuesto promedio anual de 2012 a 2018; no se halló un "
        "inventario posterior. Los montos de cada convocatoria se citan con la edición y la "
        "fecha de consulta, porque cambian cada año.",
        "Dato: en el otro extremo, otros 45 instrumentos tenían un presupuesto de US$ 150 000 o "
        "menos (POLCTI, 2025).",
    ],
))

L.append(recursos(
    "recursos-formas",
    "01 · Recursos recomendados",
    "Recursos sobre instrumentos y formas de financiamiento de la innovación",
    [
        {"tipo": "Guía", "titulo": "A Practitioner's Guide to Innovation Policy",
         "autor": "Cirera, Frias, Hill y Li, Banco Mundial, 2020",
         "detalle": "Objetivo, diseño y evidencia de cada instrumento de política de innovación",
         "url": "doi.org/10.1596/33269",
         "enlace": "https://doi.org/10.1596/33269"},
        {"tipo": "Informe", "titulo": "Financing SMEs and Entrepreneurs 2026: An OECD Scoreboard, nota del Perú",
         "autor": "OCDE, 2026",
         "detalle": "Deuda, capital y garantías para pymes peruanas, con datos hasta 2025",
         "url": "oecd.org · Financing SMEs 2026, nota Perú",
         "enlace": "https://www.oecd.org/en/publications/financing-smes-and-entrepreneurs-2026_bb7fc5c4-en/peru_11f4cae1-en.html"},
        {"tipo": "Libro", "titulo": "¿Cómo repensar el desarrollo productivo? Políticas e instituciones sólidas para la transformación económica",
         "autor": "Crespi, Fernández-Arias y Stein (eds.), BID, 2014",
         "detalle": "Razones de la intervención pública e instrumentos de desarrollo productivo",
         "url": "doi.org/10.18235/0012587",
         "enlace": "https://doi.org/10.18235/0012587"},
        {"tipo": "Artículo", "titulo": "Capital de riesgo e innovación en América Latina",
         "autor": "Luis Felipe Jiménez, Revista de la CEPAL, 2008",
         "detalle": "Instrumento de financiamiento adecuado a cada fase de la innovación",
         "url": "hdl.handle.net/11362/11287",
         "enlace": "https://hdl.handle.net/11362/11287"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía del Banco Mundial describe, para cada instrumento (subvención, bono tecnológico, crédito, garantía, incentivo fiscal), su objetivo, su diseño y la evidencia de impacto en países en desarrollo; amplía la lámina de formas de financiamiento.",
        "La nota del Perú en el informe de la OCDE da indicadores de préstamos, garantías y capital para pymes; cubre la forma reembolsable. El libro del BID explica en español por qué el Estado interviene y con qué instrumentos.",
        "Jiménez (2008) sostiene que cada fase de la innovación requiere un instrumento distinto y describe programas de Brasil y Chile; sus datos son anteriores a 2008.",
    ],
))

# ---------- U2 · Programas nacionales de CTI

L.append(visual(
    "prociencia-rutas",
    "01 · Calendario de PROCIENCIA",
    "Fondos del calendario 2027 de *PROCIENCIA* por línea de financiamiento",
    barras_valor([
        ("Prioridades nacionales", 20.0, ""),
        ("Maduración y transferencia", 19.57, "clave"),
        ("Generación de conocimiento", 8.38, ""),
        ("Capacidades habilitantes", 4.36, ""),
    ], maximo=25, paso=5, menor=1, decimales=2, xb=560,
        unidad="MILLONES DE SOLES · DESEMBOLSO PROGRAMADO PARA 2027"),
    fuente="PROCIENCIA, nota del 14 de julio de 2026 · RDE 055-2026 y RDE 092-2026",
    notas=[
        "Dato: el calendario 2027 programa 15 concursos por S/ 52 296 000 y al menos 191 "
        "subvenciones (Resolución de Dirección Ejecutiva, RDE, 055-2026-PROCIENCIA-DE, "
        "modificada por la RDE 092-2026). El total "
        "se presentó en la sesión 1.",
        "Dato: la línea de maduración y transferencia reúne siete concursos: Desarrollo "
        "Tecnológico (S/ 4,2 M), Escalamiento Tecnológico (S/ 7,2 M), Articulación con el "
        "sector productivo (S/ 4,0 M), Valorización y protección (S/ 2,1 M), Centros de "
        "Transferencia en el Sector Privado (S/ 1,6 M), Patentes PCT (S/ 0,465 M) y el "
        "concurso con el Centro para el Desarrollo Tecnológico y la Innovación (CDTI) de "
        "España, sin monto. Esa línea y la de prioridades nacionales "
        "suman el 76 % del calendario.",
        "El monto del calendario es lo que se desembolsa en el año fiscal 2027, no el costo "
        "total de cada concurso. Investigación Básica, por ejemplo, desembolsa en 2027 el 80 % "
        "de su costo.",
        "Emprendimiento Académico no figura en el calendario 2027; su fase 2 cerró el 5 de "
        "octubre de 2026 y publica resultados desde el 25 de noviembre.",
        "Verificar antes de la clase: si PROCIENCIA publicó las bases de Desafíos para la "
        "solución de prioridades nacionales (S/ 20 M); al 14 de octubre de 2026 no figuraban "
        "en su plataforma.",
    ],
))

L.append(cifra(
    "tasa-seleccion",
    "01 · Selección en PROCIENCIA",
    "18,4", "%",
    "de las 408 postulaciones a Investigación Básica 2026-01 de PROCIENCIA obtuvo financiamiento",
    "Lima: 43 de los 75 proyectos seleccionados y 61 % del monto adjudicado",
    fuente="PROCIENCIA, RDE 052-2026 · cálculo propio sobre la lista de seleccionados",
    notas=[
        "Dato: el concurso de Investigación Básica 2026-01 recibió 408 postulaciones; 261 "
        "aprobaron la evaluación y 75 resultaron seleccionadas, con 23 accesitarias (RDE "
        "052-2026). La tasa de selección se calcula sobre las postulaciones.",
        "Dato: según la columna «Región» de la lista, los proyectos de Lima recibieron "
        "S/ 9,88 millones de S/ 16,16 millones, aun con cupos reservados para regiones.",
        "Dos programas internacionales de la unidad 6 seleccionaron en 2026 a 5 de 130 y a 10 de "
        "90 propuestas.",
        "Error frecuente: interpretar la aprobación en la evaluación técnica como "
        "financiamiento. De las 261 propuestas aprobadas, 75 recibieron fondos.",
    ],
))

L.append(tarjetas(
    "proinnovate-concursos",
    "01 · Concursos de PROINNÓVATE",
    "Concursos de *PROINNÓVATE* para empresas según la etapa del proyecto, 2026",
    [
        ("Innovación Empresarial", "Prototipo de producto o proceso de una mipyme; hasta S/ 360 000"),
        ("Validación de la Innovación", "Prototipo con el riesgo tecnológico superado; hasta S/ 500 000"),
        ("Desafíos Públicos de Innovación", "Solución a un reto de una entidad pública; hasta S/ 893 000"),
        ("Innovación Abierta", "Mediana o gran empresa con mypes y _startups_; hasta S/ 2 000 000"),
        ("Garantías Tecnológicas", "Garantía de hasta el 80 % del préstamo de una mipyme"),
    ],
    clave=1,
    iconos=["bulb", "check", "target", "network", "budget"],
    fuente="PROINNÓVATE, fichas de financiamiento 2026 · DS 002-2026-PRODUCE",
    notas=[
        "El DS 002-2026-PRODUCE creó el Programa Nacional de Innovación y Desarrollo Productivo "
        "(PROINNÓVATE), adscrito al Ministerio de la Producción (PRODUCE), que absorbió por "
        "fusión al programa anterior; el relanzamiento operativo fue a inicios de junio de "
        "2026. La mipyme es la micro, pequeña o mediana empresa. La mype es la micro o pequeña "
        "empresa.",
        "Dato: Validación de la Innovación cofinancia hasta el 60 % del costo total; en los "
        "concursos regionales de 2026, Innovación Empresarial cofinanció hasta el 75 %.",
        "Dato: en 2025 PROINNÓVATE adjudicó S/ 90,7 millones en proyectos nuevos; el 49,2 % de "
        "las beneficiarias está en la macrorregión Lima (Memoria Institucional 2025).",
        "La universidad no postula a estos concursos y participa como entidad asociada de la "
        "empresa, según la regla de la sesión 1.",
        "Error frecuente: postular a Validación con un prototipo que no superó el riesgo "
        "tecnológico; ese tramo corresponde a Innovación Empresarial o a Desarrollo Tecnológico "
        "de PROCIENCIA.",
    ],
))

L.append(cifra(
    "startup-peru",
    "01 · StartUp Perú",
    "≈ 1 400", "",
    "emprendimientos impulsados por StartUp Perú entre 2014 y octubre de 2026",
    "Tope de la 13.ª generación: S/ 67 000 en Innovadores y S/ 150 000 en Dinámicos",
    fuente="PROINNÓVATE, nota del 7 de octubre de 2026 · startup.proinnovate.gob.pe",
    notas=[
        "Dato: el ministro de la Producción informó en octubre de 2026 unos 1 400 "
        "emprendimientos y unos S/ 300 millones desde 2014 (nota de PROINNÓVATE del 7 de "
        "octubre de 2026), la cifra oficial más reciente.",
        "Andina informó en noviembre de 2025 1 160 emprendimientos y más de S/ 190 millones, y la "
        "Memoria 2025 de PROINNÓVATE cuenta 434 _startups_ en el portafolio de emprendimiento. "
        "Las fuentes usan universos distintos.",
        "Dato: Emprendimientos Innovadores 13G admite empresas de hasta 18 meses con producto "
        "mínimo viable y ventas de hasta S/ 120 000; cofinancia hasta el 70 %, con al menos 10 % "
        "de aporte monetario. Los S/ 67 000 incluyen S/ 7 000 para la incubadora.",
        "Dato: en la 12G se ratificaron 176 de 548 postulaciones evaluadas, el 32 % (actas de "
        "resultados).",
        "Verificar antes de la clase: el acumulado oficial y la generación abierta en octubre de "
        "2026.",
    ],
))

L.append(duo(
    "beneficio-tributario",
    "01 · Beneficio tributario a la I+D+i",
    "Subvención y deducción tributaria de la *Ley 30309* para proyectos de I+D+i",
    {"cab": "Subvención", "t": "Recursos no reembolsables durante la ejecución",
     "items": ["Aporte propio del beneficiario desde el inicio", "Rendición de cuentas del gasto"]},
    {"cab": "Ley 30309", "t": "Deducción adicional del impuesto a la renta",
     "items": ["Deducción total de hasta 240 % del gasto con ingresos de hasta S/ 12,65 millones",
               "Tope anual de S/ 2,75 millones; vigencia hasta 2028"]},
    fuente="Ley 31659, 2022 · Ley 32539, 2025 · DS 116-2026-EF",
    notas=[
        "Dato: una empresa con ingresos netos de hasta 2 300 unidades impositivas tributarias "
        "(UIT) deduce el 240 % del gasto si ejecuta el proyecto directamente o con un centro "
        "domiciliado, y el 190 % con uno no domiciliado; por encima de ese umbral, 190 % y 160 %. "
        "La deducción adicional tiene un tope de 500 UIT al año; la UIT de 2026 es S/ 5 500.",
        "La Ley 32539 prorrogó el beneficio hasta el 31 de diciembre de 2028; los proyectos "
        "calificados que terminen después lo mantienen hasta 2030. Si el proyecto no culmina o "
        "no cumple su objetivo, la empresa rectifica y reintegra el impuesto con intereses.",
        "CONCYTEC califica el proyecto; el plazo de solicitudes de 2026 venció el 9 de octubre. "
        "Un contrato de I+D de una empresa con la UNI califica si la universidad es un centro "
        "autorizado.",
        "La serie de aprobaciones de 2016 y 2019 se presentó en la sesión 1.",
        "Verificar antes de la clase: número y fecha del DS 116-2026-EF.",
    ],
))

L.append(recursos(
    "recursos-programas",
    "01 · Recursos recomendados",
    "Recursos sobre programas nacionales e incentivos tributarios a la I+D+i",
    [
        {"tipo": "Sitio web", "titulo": "Beneficios tributarios",
         "autor": "CONCYTEC, portal vigente en 2026",
         "detalle": "Formularios, cálculo de la deducción y centros autorizados de la Ley 30309",
         "url": "portalbeneficiostributarios.concytec.gob.pe",
         "enlace": "https://portalbeneficiostributarios.concytec.gob.pe/"},
        {"tipo": "Informe", "titulo": "Peru: Strengthening the Science, Technology, and Innovation System Project. Implementation Completion and Results Report",
         "autor": "Banco Mundial, 2023",
         "detalle": "Evaluación de cierre del préstamo ejecutado por CONCYTEC y PROCIENCIA",
         "url": "worldbank.org · ICR CTI Perú 2023",
         "enlace": "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099052523122540876"},
        {"tipo": "Informe", "titulo": "Exenciones fiscales para la I+D+i: experiencias en América Latina y retos pendientes",
         "autor": "Mónica Parra Torrado, BID, 2011",
         "detalle": "Fundamento y diseño de los incentivos tributarios a la I+D+i",
         "url": "doi.org/10.18235/0007654",
         "enlace": "https://doi.org/10.18235/0007654"},
        {"tipo": "Artículo", "titulo": "Innovación y productividad en las empresas de servicios y manufactureras: el caso del Perú",
         "autor": "Mario D. Tello, Revista de la CEPAL, 2017",
         "detalle": "Inversión en innovación y productividad laboral de empresas peruanas",
         "url": "hdl.handle.net/11362/41148",
         "enlace": "https://hdl.handle.net/11362/41148"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "El portal de CONCYTEC reúne los formularios, una calculadora de la deducción, el buscador de centros autorizados y las preguntas frecuentes; no menciona la Ley 32539.",
        "El informe de cierre del Banco Mundial evalúa el préstamo de US$ 100 millones ejecutado por CONCYTEC y PROCIENCIA, origen de los concursos con sufijo «BM», y extrae lecciones sobre la asignación de fondos.",
        "Parra Torrado (2011) compara el incentivo fiscal con la subvención; es anterior a la Ley 30309. Tello (2017) estima con datos peruanos de 2004 la relación entre inversión en innovación y productividad.",
    ],
))

# ---------- U3 · Fondos sectoriales y contrapartida

L.append(tarjetas(
    "fondos-sectoriales",
    "01 · Fondos sectoriales y regionales",
    "Fondos *sectoriales* y regionales con componente de innovación en el Perú",
    [
        ("Procompite", "Gobiernos regionales y locales; planes de negocio de productores organizados"),
        ("AGROIDEAS", "Ministerio de Desarrollo Agrario; planes de negocio de organizaciones agrarias"),
        ("Turismo Emprende", "Ministerio de Comercio Exterior y Turismo; hasta S/ 100 000 por mype en 2026"),
        ("Canon minero", "5 % para universidades públicas de la zona, con uso preferente en investigación"),
        ("FONDOEMPLEO", "Remanente de utilidades; empleo, capacitación y emprendimiento, no "
                        "I+D; hasta S/ 1,5 millones y 20 % de contrapartida"),
    ],
    iconos=["users", "fund", "globe", "building", "workshop"],
    fuente="Agroideas y MINCETUR, 2026 · MEF, 2023 · DL 892 y DS 009-98-TR · FONDOEMPLEO, 2026",
    notas=[
        "Dato: Procompite ejecutó S/ 435 millones en 1 307 planes de negocio en 2025; la Ley "
        "32079 dispone que los gobiernos regionales y locales destinen entre 5 % y 15 % de sus "
        "recursos de inversión. AGROIDEAS, programa del Ministerio de Desarrollo Agrario y Riego "
        "(Midagri), ejerce la rectoría.",
        "Dato: Turismo Emprende 2026-II, del Ministerio de Comercio Exterior y Turismo "
        "(MINCETUR), llega a S/ 100 000 en la modalidad de innovación de mypes turísticas; la "
        "modalidad Experiencias en Comunidad tiene topes de S/ 60 000 y S/ 120 000.",
        "Dato: las universidades públicas de la zona productora reciben el 5 % del canon minero, "
        "con uso preferente en investigación; hasta la mitad puede ir a infraestructura y "
        "equipamiento, y no puede pagar remuneraciones (Ministerio de Economía y Finanzas, MEF, "
        "2023).",
        "Dato: el Fondo Nacional de Capacitación Laboral y de Promoción del Empleo "
        "(FONDOEMPLEO) lo crea el artículo 3 del Decreto Legislativo (DL) 892 de 1996, sobre la "
        "participación de los trabajadores en las utilidades, y lo reglamenta el DS 009-98-TR. "
        "La Ley 27564 (2001) no lo crea: modifica ese artículo para que los recursos vuelvan a "
        "la región donde se generó el remanente.",
        "El remanente es la parte de la participación en las utilidades que excede el tope de "
        "18 remuneraciones mensuales por trabajador. FONDOEMPLEO recibe hasta 2 200 UIT por "
        "región y ejercicio; el exceso pasa al gobierno regional para inversión pública. Es una "
        "persona jurídica de derecho privado (DS 017-2011-TR) y, según su memoria, no recibe "
        "presupuesto público.",
        "Dato: FONDOEMPLEO aprobó 38 proyectos por S/ 28,25 millones en el concurso 2024 y 28 "
        "por S/ 22,89 millones en el de 2025; en ACTÍVA-T 2026 aprobó 43 proyectos, sin monto "
        "total publicado. Uno es de la UNI: inserción laboral de jóvenes vulnerables en "
        "manufactureras de Lima Norte, con diagnóstico de brechas y emparejamiento ocupacional "
        "con IA (código C2635). La IA se usa para la empleabilidad, no para hacer I+D "
        "(FONDOEMPLEO, relaciones de proyectos aprobados 2024 y 2025 y de seleccionados 2026).",
        "Dato: el Instituto Tecnológico de la Producción (ITP) ejecuta desde octubre de 2025, en "
        "24 meses, un sistema de monitoreo acuícola con drones subacuáticos operados a distancia "
        "(ROV) en Puno, con S/ 997 925 de FONDOEMPLEO y 380 beneficiarios (Memoria Anual 2025).",
        "En las bases de ACTÍVA-T 2026, el criterio de innovación y sostenibilidad pesa el 7,5 % "
        "de la nota técnica. La contrapartida mínima del 20 %, con al menos 5 % monetario, se "
        "calcula sobre lo solicitado, no sobre el costo total como en PROCIENCIA. Una universidad "
        "puede postular; si es pública, como la UNI, ejecuta de forma indirecta y FONDOEMPLEO "
        "administra los recursos.",
        "Procompite y AGROIDEAS financian a organizaciones productivas; un equipo de ingeniería "
        "participa como socio técnico de una asociación de productores. FONDOEMPLEO puede "
        "financiar la capacitación o la adopción de un resultado de I+D+i, no la investigación.",
        "El Programa Nacional de Innovación en Pesca y Acuicultura (PNIPA) es de PRODUCE; no se "
        "halló convocatoria en 2026. Los estímulos del Ministerio de Cultura no son instrumentos "
        "de CTI.",
    ],
))

L.append(frase(
    "definicion-contrapartida",
    "01 · Definición de contrapartida",
    "La *contrapartida* es el aporte monetario o no monetario que las entidades participantes "
    "se comprometen a dar para cubrir el costo que no financia el programa.",
    "Síntesis de PROCIENCIA, bases de Investigación Básica 2027, num. 2.4.3",
    notas=[
        "Las bases de PROCIENCIA fijan el porcentaje máximo de financiamiento del programa sobre "
        "el costo total; el resto es la contrapartida, y el aporte no monetario no puede "
        "superar el monetario más el de PROCIENCIA (num. 2.4.3). La monetaria es dinero; la no "
        "monetaria son bienes, horas de personal e instalaciones valorizados.",
        "El porcentaje se calcula sobre el costo total del proyecto, no sobre el monto "
        "solicitado al programa.",
        "Error frecuente: comprometer como contrapartida monetaria recursos que la entidad no "
        "tiene presupuestados. La firma del aporte la respalda el representante de cada entidad "
        "participante.",
        "La valorización de la contrapartida no monetaria durante la ejecución se trata en la "
        "sesión 5.",
    ],
))

L.append(duo(
    "monetaria-o-no-monetaria",
    "01 · Tipos de contrapartida",
    "Contrapartida *monetaria* y no monetaria según la entidad participante, 2026-2027",
    {"cab": "Monetaria", "t": "Dinero depositado en la cuenta del proyecto",
     "items": ["Universidad privada societaria en Investigación Básica: al menos 30 %",
               "Emprendimiento en StartUp Perú: al menos 10 %"]},
    {"cab": "No monetaria", "t": "Horas de personal, equipos e instalaciones valorizados",
     "items": ["Universidad pública en Investigación Básica: al menos 20 %",
               "Universidad pública en Desarrollo Tecnológico: al menos 25 %"]},
    fuente="PROCIENCIA, bases E041-2027-01 y E041-2027-02 · StartUp Perú, bases 13G",
    notas=[
        "Dato: en Investigación Básica 2027, PROCIENCIA cubre hasta el 80 % para entidades "
        "públicas, sin fines de lucro y universidades asociativas, y hasta el 60 % para "
        "universidades privadas societarias, que aportan al menos 30 % monetario y 10 % no "
        "monetario; las empresas solo participan como entidades asociadas. En Desarrollo Tecnológico, con fines de "
        "lucro, cubre hasta el 65 %, con 20 % monetario y 15 % no monetario.",
        "Dato: en Escalamiento Tecnológico el porcentaje depende de la entidad adoptante; a "
        "nivel piloto, PROCIENCIA cubre el 89 % con institutos y entidades públicas y el 80 % "
        "con una gran empresa.",
        "Ejemplo en un mismo concurso, Desarrollo Tecnológico 2026-03 (RDE 044-2026): el INAIGEM, "
        "entidad pública, ganó S/ 350 000 con el sistema de alerta Chapaq Cocha y aporta "
        "0 % monetario y al menos 25 % no monetario del costo total; en el ejemplo de las bases, "
        "unos S/ 116 667, para un costo total de unos S/ 466 667. WAREM S.A.C., empresa con "
        "fines de lucro, ganó S/ 349 863 con un analizador portátil de espectroscopía en el "
        "infrarrojo cercano (NIR/SWIR) para verificar la autenticidad de maca y tarwi; PROCIENCIA le cubre como máximo el 65 % y la empresa "
        "aporta al menos 20 % monetario y 15 % no monetario (bases E041-2026-03, tablas 7 y 8). "
        "La contrapartida real de cada proyecto no es pública.",
        "Dato: en 2026 la Red CITE tiene 25 centros públicos, 12 unidades técnicas y 14 centros "
        "privados, con más de 47 000 servicios en el primer semestre (ProActivo, 2026). Las "
        "cifras varían entre documentos del Instituto Tecnológico de la Producción.",
    ],
))

L.append(pasos(
    "ruta-instrumentos-publicos",
    "01 · Secuencia de instrumentos públicos",
    "*Instrumentos* públicos de la investigación a la transferencia comercial",
    [
        ("Investigación aplicada", "PROCIENCIA; lidera un docente; TRL 2–3 a 3–4"),
        ("Desarrollo Tecnológico", "PROCIENCIA; TRL 3–4 a 5; 25 % no monetario"),
        ("Ensayo en un CITE", "Servicio tecnológico pagado o aportado por un socio"),
        ("Validación de la Innovación", "PROINNÓVATE; postula la empresa; hasta 60 %"),
        ("Garantía Tecnológica", "Crédito de la mipyme garantizado hasta el 80 %"),
    ],
    clave=3,
    fuente="PROCIENCIA, bases E041-2027-02 y E041-2027-03 · PROINNÓVATE, 2026",
    notas=[
        "Los rangos de TRL son los de las bases de 2027. Desarrollo Tecnológico cambió frente a las "
        "bases de 2026 de la sesión 1: pasó de TRL 4–5 a 6 a TRL 3–4 a 5. En cada "
        "paso cambian la entidad postulante y el tipo de contrapartida: la universidad aporta "
        "horas y equipos en los dos primeros; la empresa aporta dinero desde la validación.",
        "El paso marcado corresponde al ingreso de la empresa. PROINNÓVATE exige que postule una empresa "
        "y la universidad participa como asociada. Antes de ese paso, la titularidad del "
        "resultado se fija por escrito, según la sesión 2.",
        "Dato: la garantía de innovación exige un proyecto previo cofinanciado por "
        "PROINNÓVATE y una empresa con al menos dos años y ventas de hasta S/ 11 845 000.",
        "Escalamiento Tecnológico de PROCIENCIA (piloto TRL 5 a 6; industrial TRL 6 a 7) es una "
        "alternativa al paso de validación; el adoptante puede ser una empresa, un instituto o una "
        "entidad pública, y el porcentaje de PROCIENCIA baja cuanto más grande es la empresa.",
    ],
))

L.append(recursos(
    "recursos-contrapartida",
    "01 · Recursos recomendados",
    "Recursos sobre contrapartida y fondos sectoriales",
    [
        {"tipo": "Guía", "titulo": "EU Grants: AGA — Annotated Grant Agreement, versión 2.0",
         "autor": "Comisión Europea, 2025",
         "detalle": "Reglas de costos, cofinanciamiento y aportes en especie de subvenciones europeas",
         "url": "ec.europa.eu · AGA v2.0 (2025)",
         "enlace": "https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/common/guidance/aga_en.pdf"},
        {"tipo": "Guía", "titulo": "Bases del Concurso IDeA de I+D 2026, FONDEF",
         "autor": "ANID, Chile, 2025",
         "detalle": "Aportes incrementales y no incrementales de beneficiarias y asociadas",
         "url": "anid.cl/concursos/concurso-idea-id-2026",
         "enlace": "https://anid.cl/concursos/concurso-idea-id-2026/"},
        {"tipo": "Guía", "titulo": "Convocatoria 2026: términos de referencia",
         "autor": "FONTAGRO, 2025",
         "detalle": "Consorcio regional con contrapartida mínima del doble de lo solicitado",
         "url": "fontagro.org · Convocatoria 2026",
         "enlace": "https://fontagro.org/es/iniciativas/convocatorias/convocatoria-2026"},
        {"tipo": "Informe", "titulo": "Evaluación de impacto del Programa de Compensaciones para la Competitividad (AGROIDEAS)",
         "autor": "MEF, 2024",
         "detalle": "Evaluación cuasiexperimental del cofinanciamiento a organizaciones agrarias",
         "url": "gob.pe · Evaluación de AGROIDEAS",
         "enlace": "https://www.gob.pe/institucion/mef/informes-publicaciones/6615722-evaluacion-de-impacto-del-programa-de-compensaciones-para-la-competitividad-agroideas"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "El acuerdo anotado de la Comisión Europea distingue los aportes en especie gratuitos de terceros de los aportes contra pago y fija cómo se documentan; conviene leer los artículos 6 y 9, porque el documento tiene 431 páginas.",
        "Las bases chilenas del concurso IDeA exigen a la beneficiaria un aporte mínimo del 30 % del subsidio y a las asociadas uno del 15 %, en aportes incrementales o no incrementales; sirven para comparar con las bases peruanas.",
        "Los términos de referencia del Fondo Regional de Tecnología Agropecuaria (FONTAGRO), que se presenta en la unidad 6, piden una contrapartida del doble de lo solicitado, mayor que el aporte del fondo. La evaluación del MEF muestra qué exige y qué logra AGROIDEAS.",
    ],
))

L.append(cierre(
    "sintesis-01",
    "01 · Síntesis",
    "Instrumentos públicos y *contrapartida*",
    [
        "Forma: momento del dinero y obligación del receptor",
        "Programa: entidad postulante y tramo de TRL",
        "Contrapartida: aporte monetario o no monetario",
    ],
    ("Receso", "10 minutos · Tema 02: capital emprendedor y financiamiento internacional"),
    notas=[
        "Recapitular el criterio de cada término del tema 01 antes del receso de 10 minutos.",
        "Dato: 45 de los 164 instrumentos públicos de CTI reunieron el 90 % del presupuesto "
        "en 2012-2018 (POLCTI, 2025).",
        "El financiamiento máximo del programa baja de 80 % en Investigación Básica a 60 % en Validación de "
        "la Innovación, según las bases de 2026 y 2027.",
    ],
))

# ============== TEMA 02 · CAPITAL EMPRENDEDOR Y FINANCIAMIENTO INTERNACIONAL

L.append(seccion(
    "tema-02", "02", "Capital emprendedor y financiamiento internacional",
    "Inversionistas de cada etapa de una empresa de base tecnológica, contraprestación "
    "exigida y fuentes externas al presupuesto nacional",
    notas=[
        "Mantener esta lámina en pantalla durante el receso.",
        "Presentar el tema 02, que trata el dinero que no proviene del presupuesto nacional: la "
        "inversión privada en empresas jóvenes, lo que pide a cambio, cuánto llega al Perú y la "
        "cooperación internacional.",
        "Tiempo: 80 minutos; presentación del tema, 1; actores de la inversión temprana, 27; "
        "términos de la inversión y Perú, 22; cooperación y fondos internacionales, 26; "
        "síntesis, 4.",
    ],
))

# ---------- U4 · Actores de la inversión en etapa temprana

L.append(frase(
    "definicion-capital-riesgo",
    "02 · Definición de capital de riesgo",
    "El *capital de riesgo* es el capital que aportan firmas de inversión a empresas jóvenes "
    "no cotizadas en bolsa, a cambio de una participación en su capital.",
    "Síntesis de la definición de la OCDE (1996)",
    notas=[
        "La OCDE define el capital de riesgo (_venture capital_) como el capital que aportan "
        "firmas que invierten junto con los gestores en empresas jóvenes no cotizadas. El fondo "
        "espera un crecimiento alto y una salida por venta de su participación.",
        "El inversionista ángel es una persona con patrimonio propio que invierte directamente "
        "en empresas nuevas o en crecimiento no cotizadas (Comisión Europea, SEC(2007) 1719). "
        "Capital emprendedor es el término que agrupa a ángeles, aceleradoras y fondos; lo usa "
        "la Asociación Peruana de Capital Semilla y Emprendedor (PECAP).",
        "La deuda de riesgo (_venture debt_) son préstamos o líneas de crédito a empresas "
        "jóvenes, a menudo respaldadas por fondos de capital de riesgo; cede poca o ninguna "
        "propiedad, en general mediante opciones de compra de acciones (_warrants_) (LAVCA, "
        "2026).",
        "A diferencia del préstamo, la inversión no se devuelve: el inversionista comparte el "
        "resultado de la empresa en proporción a su participación.",
    ],
))

L.append(pasos(
    "etapas-inversion",
    "02 · Etapas de la inversión",
    "Etapas de una empresa de base tecnológica y *fuente* de financiamiento de cada una",
    [
        ("Presemilla", "Fondos propios, familia y subvenciones"),
        ("Semilla", "Inversionistas ángeles, aceleradoras y StartUp Perú"),
        ("Serie A", "Ronda liderada por un fondo de capital de riesgo"),
        ("Expansión", "Rondas siguientes y deuda de riesgo"),
        ("Salida", "Venta de la participación de los inversionistas"),
    ],
    clave=1,
    fuente="Esquema según Comisión Europea, 2007 · OCDE, 1996 · LAVCA, 2026",
    notas=[
        "Una ronda es cada operación en que la empresa recibe inversión a cambio de "
        "participación; las rondas se nombran por etapa (semilla, serie A, serie B).",
        "La inversión ángel se concentra en presemilla y semilla; el capital de riesgo, desde "
        "la semilla hasta la expansión; la deuda de riesgo, en empresas con ingresos "
        "recurrentes.",
        "La semilla corresponde en buena parte al tramo del valle de la muerte presentado en la "
        "sesión 1: el producto existe y la empresa carece de las ventas que exige un fondo de "
        "capital de riesgo.",
        "Dato: en 2025 las rondas de etapa temprana sumaron US$ 2 200 millones, el 52 % del "
        "capital de riesgo de América Latina (LAVCA, _2026 Trends in Tech_).",
    ],
))

L.append(duo(
    "incubadora-aceleradora",
    "02 · Incubadora y aceleradora",
    "Servicios de una *incubadora* y de una aceleradora de empresas",
    {"cab": "Incubadora", "t": "Recursos compartidos para empresas jóvenes",
     "items": ["Oficina, consultores y personal",
               "Acceso posible a financiamiento y soporte técnico"]},
    {"cab": "Aceleradora", "t": "Programa de plazo fijo por cohortes",
     "items": ["Mentoría, formación y redes de contacto",
               "Con frecuencia, a cambio de participación"]},
    fuente="NBIA, 2021, en Dhiman y Arora, 2024 · Avnimelech et al., 2024",
    notas=[
        "La definición de incubadora es de la National Business Incubation Association (NBIA, "
        "2021), recogida en la revisión de Dhiman y Arora (2024) sobre 259 artículos de Scopus. "
        "Avnimelech et al. (2024) definen la aceleradora como una entidad que dirige programas "
        "de plazo fijo, por cohortes, para empresas nacientes; una cohorte es el grupo que "
        "ingresa y egresa a la vez, con frecuencia una docena de empresas.",
        "La incubadora admite empresas de forma individual y la aceleradora las admite por "
        "cohortes, con fecha de inicio y de cierre.",
        "Dato: la unidad Startup UNI, del Vicerrectorado de Investigación, abrió en 2026 el programa de "
        "preincubación Impulso 2G. StartUp Perú destina S/ 7 000 de cada subvención de Innovadores "
        "a la incubadora que acompaña al ganador.",
    ],
))

L.append(cifra(
    "efecto-aceleradora",
    "02 · Resultados de las aceleradoras",
    "73", "%",
    "de 1 350 empresas graduadas de aceleradoras de Israel sin capital levantado a los 12 "
    "meses, 2010-2019",
    "39 % sin capital a los tres años, entre las 515 con datos de ese plazo",
    fuente="Avnimelech et al., _Strategic Management Journal_, 2024",
    notas=[
        "Dato: Avnimelech et al. (2024) reunieron a todas las empresas graduadas de 24 "
        "aceleradoras de Israel entre 2010 y 2019, en 158 cohortes dirigidas por 69 gestores.",
        "Dato: en su modelo, la aceleradora explica el 8,9 % de la varianza del capital "
        "levantado a los 12 meses; al incluir la cohorte y el gestor, la cifra baja a 3,6 %. "
        "El gestor del programa y la cohorte explican parte de lo que se atribuía a la "
        "aceleradora.",
        "Implicación para el formulador: el ingreso a una aceleradora no garantiza una ronda "
        "de inversión; el 73 % de las graduadas no levantó capital en el primer año.",
        "Los autores eligen Israel por el tamaño de su población de empresas emergentes y de "
        "aceleradoras; las cifras no describen el mercado peruano.",
    ],
))

L.append(visual(
    "criterios-angel",
    "02 · Criterios de los inversionistas ángeles",
    "Criterios de evaluación inicial de 31 inversionistas ángeles de la *República Checa*",
    barras_valor([
        ("Aporte propio del emprendedor", 90.32, "clave"),
        ("Potencial de expansión", 83.87, ""),
        ("Avance del proyecto", 80.65, ""),
        ("Solución nueva", 74.19, ""),
        ("Mercado en crecimiento", 64.52, ""),
    ], maximo=100, paso=20, menor=5, decimales=1, sufijo=" %", xb=600,
        unidad="PORCENTAJE DE INVERSIONISTAS QUE APLICA EL CRITERIO · 2018-2019"),
    fuente="Skalicka et al., _Economic Research-Ekonomska Istraživanja_, 2022, tablas 5, 10, 11 y 13",
    notas=[
        "Dato: Skalicka et al. (2022) entrevistaron a 31 inversionistas ángeles con sede en la "
        "República Checa entre abril de 2018 y mayo de 2019. El 90,3 % exige que el emprendedor "
        "invierta dinero propio en el proyecto; el 10 % acepta financiar sin ese aporte.",
        "Dato: la probabilidad de que un proyecto pase la evaluación inicial es del 48 % en "
        "semilla y arranque y del 84 % en etapa emergente (tabla 9).",
        "Implicación para el formulador: el aporte propio de los fundadores cumple ante un "
        "ángel una función parecida a la contrapartida monetaria de un concurso público.",
        "Las cifras son de un mercado europeo emergente; la nota técnica del BID sobre inversión "
        "ángel en América Latina, en los recursos de esta unidad, trata la región. En el Perú, "
        "las redes de ángeles y los fondos están agrupados en PECAP.",
    ],
))

L.append(recursos(
    "recursos-actores",
    "02 · Recursos recomendados",
    "Recursos sobre inversionistas ángeles, aceleradoras y capital de riesgo",
    [
        {"tipo": "Sitio web", "titulo": "Directorio de asociados y afiliados",
         "autor": "PECAP, vigente en 2026",
         "detalle": "Fondos, aceleradoras e incubadoras asociados a PECAP en el Perú",
         "url": "pecap.pe/directorio",
         "enlace": "https://www.pecap.pe/directorio"},
        {"tipo": "Informe", "titulo": "Inversión ángel en América Latina y el Caribe: perspectiva del desempeño de los emprendimientos",
         "autor": "Chaquiriand et al., BID Lab y Xcala, 2021",
         "detalle": "Desempeño de emprendimientos con inversión ángel en la región, 2014-2020",
         "url": "doi.org/10.18235/0003860",
         "enlace": "https://doi.org/10.18235/0003860"},
        {"tipo": "Artículo", "titulo": "Accelerating Entrepreneurs and Ecosystems: The Seed Accelerator Model",
         "autor": "Yael V. Hochberg, NBER, 2016",
         "detalle": "Modelo de aceleradora semilla y diferencias con la incubadora",
         "url": "nber.org · Hochberg (2016), aceleradoras",
         "enlace": "https://www.nber.org/books-and-chapters/innovation-policy-and-economy-volume-16/accelerating-entrepreneurs-and-ecosystems-seed-accelerator-model"},
        {"tipo": "Artículo", "titulo": "Venture Capital's Role in Financing Innovation: What We Know and How Much We Still Need to Learn",
         "autor": "Lerner y Nanda, Journal of Economic Perspectives, 2020",
         "detalle": "Alcance y límites del capital de riesgo para financiar innovación",
         "url": "doi.org/10.1257/jep.34.3.237",
         "enlace": "https://doi.org/10.1257/jep.34.3.237"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "El directorio de PECAP pone nombre a los actores peruanos: unos 15 asociados (fondos, aceleradoras, capital corporativo) y unos 25 afiliados, entre ellos incubadoras universitarias; no lista redes de ángeles por nombre.",
        "La nota técnica del BID da evidencia regional sobre inversión ángel, que la lámina de criterios no tiene. Hochberg (2016) describe la aceleradora como un paquete de capital, mentoría, cohorte y día de demostración; acceso por suscripción.",
        "Lerner y Nanda (2020) explican qué innovaciones financia el capital de riesgo y cuáles deja fuera, como las de ciclo largo; acceso abierto.",
    ],
))

# ---------- U5 · Términos de la inversión y situación del Perú

L.append(tarjetas(
    "contraprestacion",
    "02 · Contraprestación por fuente",
    "*Contraprestación* exigida por cada fuente de financiamiento a una empresa joven",
    [
        ("Subvención", "Contrapartida, informes y rendición de cuentas"),
        ("Garantía de crédito", "Devolución del préstamo con intereses"),
        ("Deuda de riesgo", "Devolución con intereses, a veces con opción de compra de acciones"),
        ("Inversión ángel", "Participación en el capital de la empresa"),
        ("Capital de riesgo", "Participación y salida prevista por venta"),
    ],
    clave=4,
    iconos=["fund", "budget", "file", "users", "rocket"],
    fuente="PROCIENCIA y PROINNÓVATE, bases 2026-2027 · Comisión Europea, 2007 · OCDE, 1996 · LAVCA, 2026",
    notas=[
        "La participación es la fracción de la propiedad de la empresa que recibe el "
        "inversionista. Cada ronda emite nuevas acciones y reduce la fracción de los "
        "fundadores; esa reducción se llama dilución.",
        "En un ejemplo con cifras supuestas para una empresa de base tecnológica, un ángel "
        "aporta S/ 300 000 por "
        "el 20 %, lo que valora la empresa en S/ 1,5 millones después de la inversión; si una "
        "ronda posterior entrega otro 20 %, los fundadores conservan el 64 % (80 % × 80 %).",
        "Error frecuente: ceder participación antes de fijar la titularidad del resultado. La "
        "sesión 2 fijó la titularidad por escrito antes de explotar; en una _spin-off_, la licencia "
        "o la cesión de la universidad se firma antes de recibir inversión.",
        "Las cláusulas de la hoja de términos (valoración, preferencia de liquidación, puesto "
        "en el directorio) se desarrollan en el libro _Venture Deals_ de los recursos.",
    ],
))

L.append(visual(
    "capital-riesgo-region",
    "02 · Capital de riesgo en América Latina",
    "Capital de riesgo invertido en el *Perú* y en cinco países de la región, 2024",
    barras_valor([
        ("Brasil", 2013, ""),
        ("México", 1176, ""),
        ("Colombia", 513, ""),
        ("Argentina", 399, ""),
        ("Chile", 178, ""),
        ("Perú", 30, "clave"),
    ], maximo=2500, paso=500, menor=100, decimales=0,
        unidad="MILLONES DE US$",
        nota="0,7 % DE US$ 4 500 MILLONES EN LA REGIÓN", nota_fila=5),
    fuente="LAVCA, _2025 Trends in Tech_, pp. 3 y 8",
    notas=[
        "Dato: la Asociación para la Inversión de Capital Privado en América Latina (LAVCA) "
        "registró US$ 4 500 millones de capital de riesgo en 751 operaciones en 2024. El Perú "
        "recibió US$ 30 millones; la proporción (0,7 %) es cálculo propio. La sesión 2 citó el "
        "dato en las notas.",
        "El total de 2025 es de unos US$ 4 200 millones, cálculo propio con el 52 % de la etapa "
        "temprana citado en la lámina de etapas. El dato del Perú en 2025 no es público.",
        "Dato: según el diagnóstico de COFIDE y PECAP (nota de junio de 2026), las _startups_ "
        "peruanas recibieron US$ 76,5 millones en 23 operaciones; el 72 % fue deuda y el 97 % "
        "provino del exterior. La cifra incluye deuda y otro universo de operaciones; LAVCA "
        "cuenta solo capital de riesgo, de modo que las dos cifras no son comparables. El Fondo de Capital para Emprendimientos Innovadores (FCEI), "
        "fondo de fondos de PRODUCE administrado por la Corporación Financiera de Desarrollo "
        "(COFIDE), suma US$ 25 millones e invirtió más de US$ 14 millones en 5 fondos.",
        "Verificar antes de la clase: el dato del Perú en 2025 (una nota de prensa da US$ 35 "
        "millones en 8 rondas, sin acceso al informe) y el año del diagnóstico de COFIDE y "
        "PECAP, que la nota no indica.",
    ],
))

L.append(caso(
    "caso-tumi-financiamiento",
    "02 · Caso de estudio · fuentes por etapa",
    "Tumi Robotics",
    "Empresa nacida en laboratorios de la PUCP · Lima",
    [
        ("Público", "Cofinanciamiento de StartUp Perú, Innovación Empresarial y apoyo a la internacionalización"),
        ("2020", "Aceleradora HAX: US$ 250 000, de ellos US$ 100 000 en efectivo"),
        ("2026", "Selección por un centro espacial de Luxemburgo"),
    ],
    icono_tecnico("robot"),
    fuente="PROINNÓVATE, 2026 · Andina, 8 de julio de 2020",
    notas=[
        "El caso retoma la empresa de robots de inspección minera de la sesión 2 y ordena sus "
        "fuentes: subvenciones públicas con contrapartida y capital semilla de una aceleradora "
        "privada.",
        "Dato: Tumi Robotics recibió cofinanciamiento de StartUp Perú, Innovación Empresarial y "
        "el Programa de Apoyo a la Internacionalización de PROINNÓVATE; según su director, ese "
        "financiamiento permitió escalar sus prototipos (PROINNÓVATE, mayo de 2026).",
        "Dato: Andina informó en julio de 2020 que HAX, aceleradora de empresas de _hardware_ con "
        "sede en Shenzhen y San Francisco, entregó US$ 250 000: US$ 100 000 en efectivo y "
        "US$ 150 000 en servicios de consultoría, diseño e ingeniería. La nota no indica la "
        "participación cedida.",
        "Dato: en mayo de 2026 el Centro Europeo de Innovación en Recursos Espaciales (ESRIC) la "
        "seleccionó para adaptar sus robots al suelo lunar.",
        "Verificar antes de la clase: la generación de StartUp Perú, el año de cada "
        "cofinanciamiento y la participación que recibió HAX.",
    ],
))

L.append(recursos(
    "recursos-inversion",
    "02 · Recursos recomendados",
    "Recursos sobre términos de inversión y capital de riesgo en América Latina",
    [
        {"tipo": "Libro", "titulo": "Venture Deals: Be Smarter Than Your Lawyer and Venture Capitalist, 4.ª edición",
         "autor": "Brad Feld y Jason Mendelson, Wiley, 2019",
         "detalle": "Cláusulas de la hoja de términos: valoración, dilución, control y salida",
         "url": "venturedeals.com",
         "enlace": "https://venturedeals.com/"},
        {"tipo": "Artículo", "titulo": "El desarrollo del capital de riesgo en América Latina y el Caribe: una perspectiva comparada",
         "autor": "Wagner y Stein, Revista de la CEPAL, 2019",
         "detalle": "Rasgos del capital de riesgo latinoamericano frente a otras regiones",
         "url": "hdl.handle.net/11362/44737",
         "enlace": "https://hdl.handle.net/11362/44737"},
        {"tipo": "Informe", "titulo": "Cinco palancas para acelerar el ecosistema de _startups_ en Perú",
         "autor": "Castillo Leska et al., BID, 2026",
         "detalle": "Cuellos de botella del ecosistema peruano, incluida la movilización de capital",
         "url": "doi.org/10.18235/0014508",
         "enlace": "https://doi.org/10.18235/0014508"},
        {"tipo": "Libro", "titulo": "Boulevard of Broken Dreams: Why Public Efforts to Boost Entrepreneurship and Venture Capital Have Failed",
         "autor": "Josh Lerner, Princeton University Press, 2009",
         "detalle": "Evaluación de programas públicos de fomento del capital de riesgo",
         "url": "doi.org/10.1515/9781400831630",
         "enlace": "https://doi.org/10.1515/9781400831630"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "_Venture Deals_ explica la hoja de términos, la preferencia de liquidación, la protección contra la dilución y la nota convertible; la 4.ª edición es la vigente y es de pago.",
        "Wagner y Stein (2019) muestran que en la región las rondas son más grandes, menos tecnológicas y más financiadas desde el exterior; sus datos son de 2005 a 2011. El informe del BID de septiembre de 2026 diagnostica el ecosistema peruano con datos recientes.",
        "Lerner (2009) analiza por qué fracasan muchos programas públicos de capital de riesgo; sirve para leer el diseño del fondo de fondos FCEI. Es de pago.",
    ],
))

# ---------- U6 · Cooperación y fondos internacionales

L.append(visual(
    "cooperacion-internacional",
    "02 · Cooperación técnica internacional",
    "Cooperación técnica internacional ejecutada en el *Perú* según su origen, 2023",
    barras_valor([
        ("Oficial bilateral", 304.8, "clave"),
        ("No gubernamental", 132.6, ""),
        ("Oficial multilateral", 78.9, ""),
    ], maximo=350, paso=50, menor=10, decimales=1, xb=520,
        unidad="MILLONES DE US$",
        nota="TOTAL: 516,3 MILLONES DE US$ · OFICIAL: 383,7"),
    fuente="APCI, _Cifras de la cooperación técnica internacional en el Perú 2023_",
    notas=[
        "Dato: la Agencia Peruana de Cooperación Internacional (APCI) registró US$ 516,3 "
        "millones ejecutados en 2023: US$ 383,7 millones de cooperación oficial (bilateral y "
        "multilateral) y US$ 132,6 millones de entidades no gubernamentales. La cifra de 2021 "
        "era de US$ 472,1 millones.",
        "La cooperación oficial bilateral se acuerda entre gobiernos y llega sobre todo a "
        "entidades públicas; un equipo universitario accede a ella mediante convocatorias de "
        "programas como los de la lámina siguiente.",
        "La Agencia de los Estados Unidos para el Desarrollo Internacional (USAID) dejó de "
        "ejecutar asistencia exterior el 1 de julio de 2025, según prensa que cita al "
        "Departamento de Estado; las cifras de 2025 reflejarán ese cambio.",
        "Verificar antes de la clase: el monto de Estados Unidos, primer cooperante en 2023 "
        "(US$ 128,6 millones), en el folleto de la APCI; la extracción del PDF no permitió "
        "confirmarlo.",
    ],
))

L.append(tarjetas(
    "fuentes-internacionales",
    "02 · Fuentes internacionales",
    "Programas internacionales de financiamiento de la *I+D* abiertos a entidades peruanas",
    [
        ("Horizonte Europa", "Consorcio con socios europeos; entidades peruanas elegibles para financiamiento"),
        ("CYTED", "Redes de al menos seis países iberoamericanos; financia coordinación y movilidad"),
        ("FONTAGRO", "Consorcios regionales de I+D agroalimentaria; 5 de 130 propuestas en 2026"),
        ("SATREPS", "Investigación conjunta con Japón; 10 de 90 propuestas en 2026"),
        ("Fondo Verde para el Clima", "Acceso mediante una entidad acreditada, como Profonanpe"),
    ],
    iconos=["globe", "network", "users", "agreement", "sun"],
    fuente="Comisión Europea, 2026 · CYTED, 2026 · FONTAGRO, 2026 · JST, 2026 · GCF",
    notas=[
        "Un consorcio es la asociación de entidades de varios países que postula y ejecuta un "
        "proyecto conjunto. Una entidad acreditada es la organización nacional autorizada por "
        "un fondo para presentar y administrar sus proyectos.",
        "Dato: en la lista de países participantes de Horizonte Europa (versión 4.2, 7 de "
        "octubre de 2026), el Perú figura entre los países de ingreso bajo y medio con "
        "financiamiento automático; Brasil, México y Chile no. La expresión indica que sus "
        "entidades pueden recibir fondos sin justificación adicional; el consorcio compite igual "
        "en la convocatoria.",
        "Dato: las Redes Temáticas del Programa Iberoamericano de Ciencia y Tecnología para el "
        "Desarrollo (CYTED) pueden solicitar hasta € 20 000 el primer año y hasta € 25 000 anuales hasta el "
        "cuarto; no financian investigación. El Fondo Regional de Tecnología Agropecuaria "
        "(FONTAGRO), del BID y el Instituto "
        "Interamericano de Cooperación para la Agricultura (IICA), asignó unos US$ 5 millones a "
        "5 consorcios en 2026.",
        "Dato: SATREPS (Science and Technology Research Partnership for Sustainable "
        "Development), de la Agencia de Ciencia y Tecnología de Japón (JST) y la Agencia de "
        "Cooperación Internacional del Japón (JICA), requiere un investigador japonés y la "
        "solicitud oficial del gobierno peruano. El Centro Peruano Japonés de Investigaciones "
        "Sísmicas y Mitigación de Desastres (CISMID) de la UNI firmó en junio de 2021 un "
        "proyecto SATREPS de 60 meses de estimación de daños en la infraestructura de Lima.",
        "El Fondo de Promoción de las Áreas Naturales Protegidas del Perú (Profonanpe) está "
        "acreditado ante el Fondo Verde para el Clima (GCF) desde 2015, con categoría B, y fue "
        "reacreditado en 2022. BID Lab, del Grupo BID, "
        "ofrece capital, préstamos y cooperación técnica no reembolsable a empresas.",
    ],
))

L.append(visual(
    "mapa-fuentes-madurez",
    "02 · Fuentes por nivel de madurez",
    "Tramo de madurez (*TRL*) que cubre cada fuente de financiamiento",
    tramos_trl([
        ("Investigación aplicada", "PROCIENCIA · bases 2027", 2.5, 3.5, False, False),
        ("Desarrollo Tecnológico", "PROCIENCIA · bases 2027", 3.5, 5, False, False),
        ("Escalamiento Tecnológico", "PROCIENCIA · bases 2027", 5, 7, False, False),
        ("Validación de la Innovación", "PROINNÓVATE · empresa postulante", 6, 7.5, True, True),
        ("StartUp Perú y aceleradoras", "Producto mínimo viable con usuarios", 7, 8, False, True),
        ("Capital de riesgo", "Empresa con ventas y crecimiento", 8, 9, False, True),
    ]),
    fuente="PROCIENCIA, bases E041-2027-02, E041-2027-03 y E067-2027-01 · estimación del docente",
    notas=[
        "Las tres primeras filas toman el TRL de entrada y de salida de las bases de 2027, "
        "distinto del de 2026 en Desarrollo Tecnológico. Las "
        "tres últimas son estimaciones del docente, porque PROINNÓVATE, las aceleradoras y los "
        "fondos no usan un TRL numérico: Validación pide un prototipo con el riesgo tecnológico "
        "superado y StartUp Perú, un producto mínimo viable con tracción.",
        "La fila marcada es la entrada de la empresa, en el tramo del valle de la muerte de la "
        "sesión 1. Ninguna de las seis fuentes cubre por sí sola el tramo completo de la figura.",
        "Las filas posibles dependen de la vía de transferencia de la sesión 2: con una licencia, la empresa "
        "licenciataria postula a Validación; las aceleradoras, los ángeles y los fondos invierten "
        "en _spin-offs_ o _startups_, no en una licencia.",
        "La cooperación internacional no ocupa un tramo fijo: Horizonte Europa abarca desde la "
        "investigación hasta la demostración según la convocatoria, y CYTED financia redes, no "
        "proyectos.",
    ],
))

L.append(recursos(
    "recursos-internacional",
    "02 · Recursos recomendados",
    "Recursos sobre cooperación y fondos internacionales de I+D",
    [
        {"tipo": "Sitio web", "titulo": "EU Funding & Tenders Portal",
         "autor": "Comisión Europea",
         "detalle": "Convocatorias europeas, búsqueda de socios y guías de postulación",
         "url": "ec.europa.eu · EU Funding & Tenders Portal",
         "enlace": "https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home"},
        {"tipo": "Sitio web", "titulo": "Programa Iberoamericano de Ciencia y Tecnología para el Desarrollo",
         "autor": "CYTED, guía del solicitante 2026",
         "detalle": "Redes temáticas y cooperación iberoamericana en ciencia y tecnología",
         "url": "cyted.org",
         "enlace": "https://www.cyted.org/"},
        {"tipo": "Sitio web", "titulo": "Productos de financiamiento",
         "autor": "BID Lab, vigente en 2026",
         "detalle": "Inversión, préstamos y cooperación técnica para _startups_ y ecosistemas",
         "url": "bidlab.org/es/productos/financiamiento",
         "enlace": "https://bidlab.org/es/productos/financiamiento"},
        {"tipo": "Base de datos", "titulo": "CORDIS: resultados de investigaciones de la UE",
         "autor": "Oficina de Publicaciones de la Unión Europea",
         "detalle": "Proyectos financiados por la Unión Europea, con socios y resultados",
         "url": "cordis.europa.eu/es",
         "enlace": "https://cordis.europa.eu/es"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "El portal de la Comisión Europea da acceso a las convocatorias de Horizonte Europa y a la búsqueda de socios para consorcios; la postulación exige registro. CORDIS muestra proyectos ya financiados y sus participantes, punto de partida para identificar socios.",
        "El sitio de CYTED reúne las convocatorias de redes temáticas; la de 2026 cerró el 15 de mayo y la de 2027 suele abrir en abril.",
        "La página de BID Lab describe capital semilla de US$ 0,2 a 0,5 millones, inversión de serie A y B de US$ 1 a 3 millones, préstamos y proyectos de ecosistema con contrapartida mínima del 50 %.",
    ],
))

L.append(cierre(
    "sintesis-02",
    "02 · Síntesis",
    "Inversión privada y *cooperación*",
    [
        "Capital de riesgo: participación con salida prevista",
        "Aceleradora: 73 % de graduadas en Israel sin capital a 12 meses",
        "Perú: US$ 30 millones de capital de riesgo en 2024",
        "Cooperación: consorcio o entidad acreditada",
    ],
    notas=[
        "Recapitular el criterio de cada término del tema 02.",
    ],
))

# ================================================================ CIERRE (5 min)

L.append(cierre(
    "sintesis-sesion",
    "Cierre",
    "Fuentes de *financiamiento* por etapa",
    [
        "Instrumento público: forma, postulante y contrapartida",
        "Inversión privada: participación según la etapa",
        "Cooperación internacional: programa, socio exigido y entidad acreditada",
    ],
    ("Sesión 4", "Formulación de proyectos"),
    notas=[
        "Recapitular los contenidos de la sesión: las formas del financiamiento público y sus "
        "programas, la contrapartida, los inversionistas de cada etapa de la empresa y las "
        "fuentes internacionales.",
        "La sesión 4 toma la convocatoria elegida y redacta la propuesta según sus bases: "
        "problema, objetivos, marco lógico, metodología e hitos verificables.",
    ],
))

L.append(referencias(
    "fuentes",
    "Referencias de la sesión",
    [
        ("definicion-instrumento", "Sagasti, F. y Aráoz, A. (1979), en CONCYTEC (2025). _Política Nacional de CTI al 2030_."),
        ("formas-financiamiento", "BID (2023). _Guía práctica para la implementación de proyectos de compra pública de innovación_. Ley 32069 (2024), Ley General de Contrataciones Públicas."),
        ("concentracion-instrumentos", "Rogers, M. (2020). Línea base del gasto público en CTI en el Perú."),
        ("prociencia-rutas", "PROCIENCIA (2026). RDE 055-2026 y 092-2026, calendario 2027."),
        ("tasa-seleccion", "PROCIENCIA (2026). RDE 052-2026, Investigación Básica 2026-01."),
        ("proinnovate-concursos", "PROINNÓVATE (2026). Fichas de financiamiento. DS 002-2026-PRODUCE."),
        ("startup-peru", "PROINNÓVATE (2026, 7 de octubre). Nota sobre StartUp Perú."),
        ("beneficio-tributario", "Leyes 30309, 31659 y 32539. MEF (2026). DS 116-2026-EF."),
        ("fondos-sectoriales", "Agroideas (2026). MEF (2023). DL 892 y DS 009-98-TR. FONDOEMPLEO (2026). Bases ACTÍVA-T."),
        ("definicion-contrapartida", "PROCIENCIA (2026). Bases E041-2027-01 y E041-2027-02."),
        ("definicion-capital-riesgo", "OCDE (1996). _Venture capital and innovation_. Comisión Europea (2007). SEC(2007) 1719."),
        ("etapas-inversion", "LAVCA (2026). _2026 LAVCA Trends in Tech_, resumen público."),
        ("incubadora-aceleradora", "Dhiman, V. y Arora, M. (2024). _LBS Journal of Management & Research_, 22(1)."),
        ("efecto-aceleradora", "Avnimelech, G. et al. (2024). _Strategic Management Journal_."),
        ("criterios-angel", "Skalicka, M. et al. (2022). _Economic Research-Ekonomska Istraživanja_, 36(1)."),
        ("capital-riesgo-region", "LAVCA (2025). _2025 LAVCA Trends in Tech_."),
        ("caso-tumi-financiamiento", "PROINNÓVATE (2026, mayo). Andina (2020, 8 de julio)."),
        ("cooperacion-internacional", "APCI. _Cifras de la cooperación técnica internacional en el Perú 2023_."),
        ("fuentes-internacionales", "Comisión Europea (2026). Horizonte Europa, países participantes, v4.2. CYTED (2026). FONTAGRO (2026). JST (2026)."),
        ("mapa-fuentes-madurez", "PROCIENCIA (2026). Bases E041-2027-02, E041-2027-03 y E067-2027-01."),
    ],
))


def _sin_corte(lam):
    """Espacio de no separación en montos de los nodos de texto («S/ 150 000»,
    «US$ 250 000»), para que el salto de línea no parta la cifra."""
    import re

    def fijo(txt):
        txt = re.sub(r"(S/|US\$|€) (?=\d)", "\\1\u00a0", txt)
        return re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", txt)

    lam.cuerpo = re.sub(r">([^<]+)<", lambda m: ">" + fijo(m.group(1)) + "<", lam.cuerpo)
    return lam


L = [_sin_corte(lam) for lam in L]

construir("clase-03", "Sesión 3 · Mapa de financiamiento e inversión", L)
