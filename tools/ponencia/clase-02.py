#!/usr/bin/env python3
"""Sesión 2 · Startups, spin-offs y transferencia — formato ponencia (11.ª edición).

Temas: «Transferencia y protección de resultados de investigación»
(tema 01: vía de transferencia, titularidad y protección del resultado) y
«Creación de empresas derivadas y de base tecnológica» (tema 02: oficina de
transferencia, empresas de base tecnológica y deep tech, factores asociados y
situación del Perú).

Secuencia (scratchpad/s2-auditoria-secuencia.md, §4): U1 vías de transferencia
→ U2 titularidad → U3 protección → receso → U4 oficina de transferencia → U5
empresas de base tecnológica → U6 factores asociados y situación del Perú. La
lámina `cesion-o-licencia` de la secuencia pasa a las notas de
`inventor-y-titular` para no superar las 40 láminas. Ninguna sigla se usa antes
de la lámina que la presenta.

Contenido: scratchpad/inv-s2.md (conceptos, cifras, casos y marco normativo).
Las cifras del informe del BID (Peña y Jenik, 2023) se cotejaron además en la
copia local del PDF (edicion-10/src/paper/clase-02/deep-tech-nueva-ola-bid.pdf),
porque el sitio del BID devuelve 403. Recursos: scratchpad/recursos-s2.md (4 por
unidad; ninguno se cita en clase).

Formato expositivo: la sesión no incluye actividades en el aula. Las notas
reúnen contenido de respaldo con dato y fuente, errores frecuentes de los
formuladores y puntos por verificar. Ejemplos (scratchpad/asignacion-ejemplos.md
y banco-ejemplos.md): cada concepto se ilustra con un proyecto distinto; los
titulares y las explicaciones conceptuales no nombran proyectos. El caso qAIRa
viene de la sesión 1.

Antes de dictar, verificar: estado actual de qAIRa, número del modelo de
utilidad y año de fundación; titularidad actual de la patente HB4; vigencia en
2026 de los reglamentos de PI de la UNI (2019), la PUCP (2011) y la UPCH (2012);
votación en el Pleno del dictamen sobre transferencia tecnológica (mayo de
2026); si una universidad pública puede participar en el capital de una
spin-off; si PROCIENCIA abrió la fase 2 de Emprendimiento Académico.

Uso:  python3 tools/ponencia/clase-02.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from graficos import icono, icono_tecnico, peldanos  # noqa: E402
from plantillas import (  # noqa: E402
    agenda, caso, cierre, cifra, construir, criterios, duo, frase, pasos, portada,
    recursos, referencias, seccion, tarjetas,
)

FUENTE_REC = "Enlaces verificados en octubre de 2026"

L = []


def resultado_verificacion(lam, texto_html):
    """La lista de verificación de `criterios()` rotula su resultado como
    «Actividad de I+D» (sesión 1). Aquí se sustituye ese rótulo sin modificar
    la plantilla ni el gráfico."""
    lam.cuerpo = lam.cuerpo.replace(
        '<p class="vf-res__t">Actividad de I+D</p>', f'<p class="vf-res__t">{texto_html}</p>'
    )
    return lam


# ================================================================ APERTURA (5 min)

L.append(portada(
    "portada",
    "Sesión 2 · Diseño y Gestión de Proyectos {I+D+i+e}",
    "_Startups_, _spin-offs_ y transferencia",
    "Transferencia de resultados de investigación universitaria a empresas existentes "
    "y a empresas nuevas",
    ["Transferencia y protección de resultados de investigación",
     "Creación de empresas derivadas y de base tecnológica"],
    "Abraham Caso-Torres · OTI-UNI · CC BY-SA 4.0",
    visual=peldanos(),
    notas=[
        "Dar la bienvenida y presentar los dos temas de la sesión: las vías por las que un "
        "resultado de investigación llega a una empresa, con su titularidad y su protección, y "
        "la creación de empresas a partir de esos resultados.",
        "La sesión 1 presentó la «e» de la sigla I+D+i+e como la creación de una empresa nueva y "
        "anunció la comparación con la licencia a una empresa existente; esa comparación abre el "
        "tema 01.",
    ],
))

L.append(agenda(
    "agenda",
    "Agenda",
    "Temas y contenidos de la sesión 2",
    [
        ("Transferencia y protección de resultados de investigación",
         ["Vías de transferencia",
          "Titularidad de resultados",
          "Formas de protección"]),
        ("Creación de empresas derivadas y de base tecnológica",
         ["Oficina de transferencia",
          "Empresas de base tecnológica",
          "Factores asociados y Perú"]),
    ],
    notas=[
        "Presentar los dos temas y las tres unidades de cada uno.",
        "Tiempo: apertura, 5 min; tema 01, 75 min; receso, 10 min; tema 02, 80 min; cierre, "
        "5 min; holgura para preguntas, 5 min.",
        "Los instrumentos de financiamiento de cada vía (StartUp Perú, capital de riesgo, "
        "inversionistas ángeles) corresponden a la sesión 3; el trámite de patentes, las tasas y "
        "el Tratado de Cooperación en materia de Patentes (PCT), a la sesión 5.",
    ],
))

# ===================== TEMA 01 · TRANSFERENCIA Y PROTECCIÓN DE RESULTADOS DE INVESTIGACIÓN

L.append(seccion(
    "tema-01", "01", "Transferencia y protección de resultados de investigación",
    "Vías por las que un resultado de investigación llega a un tercero, titularidad del "
    "resultado y formas de protección",
    notas=[
        "Presentar el tema 01, que trata el resultado de investigación: la vía por la que llega a "
        "quien lo explota, quién decide sobre él y cómo se protege.",
        "Tiempo: 75 minutos; presentación del tema, 1; vías de transferencia, 26; titularidad, "
        "19; protección, 25; síntesis, 4.",
    ],
))

# ---------- U1 · Vías de transferencia

L.append(frase(
    "definicion-transferencia",
    "01 · Definición de transferencia tecnológica",
    "La *transferencia tecnológica* es la transmisión de conocimientos, medios y derechos de "
    "explotación a terceros para que produzcan un bien, desarrollen un proceso o presten un "
    "servicio.",
    "Síntesis de la Ley 31250, glosario, n.º 56 (2021)",
    notas=[
        "El glosario de la Ley 31250 define la transferencia tecnológica como el «proceso de "
        "transmisión de información científica y tecnológica, conocimientos, medios y derechos "
        "de explotación hacia terceros». Repite la definición del Programa Especial de "
        "Transferencia y Extensión Tecnológica de CONCYTEC (2016).",
        "La Organización Mundial de la Propiedad Intelectual (OMPI) enumera como medios formales "
        "de transferencia la licencia, la cesión, los contratos de colaboración y de "
        "investigación, la consultoría, los acuerdos de transferencia de material y la creación "
        "de empresas derivadas y emergentes. La licencia y la creación de empresas derivadas o "
        "emergentes son las vías que se comparan en esta unidad.",
        "Según el Manual de Oslo, un resultado pasa a ser innovación cuando llega a los usuarios; la "
        "transferencia es uno de los caminos para que eso ocurra cuando el resultado nace en una "
        "universidad.",
    ],
))

L.append(tarjetas(
    "vias-transferencia",
    "01 · Vías de transferencia",
    "Vías de *transferencia* de un resultado de investigación universitaria",
    [
        ("Licencia", "Autorización a una empresa existente para explotar el resultado, sin cambio de titular"),
        ("_Spin-off_", "Empresa nueva que deriva de una universidad o centro de investigación y explota su resultado"),
        ("_Startup_ de base tecnológica", "Empresa nueva que no explota un resultado de la universidad"),
    ],
    numerar=False,
    iconos=["agreement", "building", "rocket"],
    fuente="Comunidad Andina, Decisión 486, art. 57 · Ley 31250, glosario, n.º 18 y 54",
    notas=[
        "La Decisión 486 de la Comunidad Andina (CAN), régimen común de propiedad industrial de "
        "Bolivia, Colombia, Ecuador y el Perú, define la licencia en su artículo 57 como la "
        "autorización del titular a terceros para explotar la invención.",
        "La Ley 31250 define la _spin-off_ como una organización con estructura jurídica propia "
        "que nace de otra ya estructurada, como una universidad o un centro de investigación, y "
        "transfiere conocimiento al ámbito empresarial (n.º 54). En la literatura, la _spin-off_ "
        "académica exige además un vínculo formal con la universidad: licencia, cesión o "
        "participación (Klofsten y Jones-Evans, 2000, recogido en Pattnaik y Pandey, 2014).",
        "La empresa de base tecnológica (n.º 18 de la ley) no necesita originarse en la "
        "universidad ni explotar un resultado suyo; por eso no arrastra la cuestión de "
        "titularidad que tiene la _spin-off_.",
        "La Ley Universitaria (Ley 30220, art. 52) encarga a las universidades promover pequeñas "
        "y microempresas de propiedad de los estudiantes, con asesoría docente y uso de equipos.",
        "La OMPI usa en español «empresa derivada» para la _spin-off_ y «empresa emergente» para "
        "la _startup_.",
        "Los contratos de I+D por encargo, la consultoría y los servicios científicos y "
        "tecnológicos (Ley 31250, n.º 53) son otras formas de transferencia.",
    ],
))

L.append(duo(
    "licencia-o-spinoff",
    "01 · Licencia y _spin-off_",
    "Reparto del riesgo y del ingreso en la licencia y en la *_spin-off_*",
    {"cab": "Licencia", "t": "Empresa existente autorizada por el titular",
     "items": ["Riesgo del licenciatario", "Ingreso por regalías"]},
    {"cab": "_Spin-off_", "t": "Empresa nueva con licencia, cesión o participación",
     "items": ["Riesgo del equipo fundador", "Ingreso por regalías o por participación"]},
    fuente="Comunidad Andina, Decisión 486, arts. 56 y 57 · Klofsten y Jones-Evans, 2000",
    notas=[
        "La regalía es el pago del licenciatario al titular por explotar la invención; el "
        "contrato fija su base de cálculo, por ejemplo, las unidades vendidas.",
        "La licencia conviene cuando existe una empresa con capacidad de producir y vender el "
        "resultado. La _spin-off_ se forma cuando el resultado requiere un desarrollo adicional "
        "que ninguna empresa existente asume y el equipo decide asumirlo.",
        "Error frecuente: suponer que la _spin-off_ prescinde de la universidad. Si el resultado "
        "se obtuvo con recursos de la universidad, la empresa nueva necesita una licencia, una "
        "cesión o un acuerdo de participación.",
        "Verificar antes de la clase: si la normativa vigente permite a una universidad pública "
        "como la UNI participar en el capital de una _spin-off_. El dictamen de la Comisión de "
        "Ciencia, Innovación y Tecnología del Congreso (mayo de 2026) prevé bonificaciones por "
        "transferencia que incluyen la participación en empresas de base tecnológica, pero no es "
        "ley vigente.",
    ],
))

L.append(duo(
    "spinoff-o-startup",
    "01 · _Spin-off_ y _startup_",
    "Vía de transferencia según el origen del resultado: *_spin-off_* y _startup_ en la UNI",
    {"cab": "_Spin-off_ posible", "t": "Teñido de fibra de alpaca con CO₂ supercrítico, desarrollado con un fondo de PROCIENCIA",
     "items": ["Derechos de la universidad (art. 11)", "Acuerdo previo a la empresa"]},
    {"cab": "_Startup_", "t": "Yakuscan, Kalman Robotics y Zeia, incubadas en StartUp UNI",
     "items": ["Cofinanciamiento de PROINNÓVATE", "Titularidad del estudiante sobre lo creado con medios propios (art. 18)"]},
    fuente="Reglamento de PI de la UNI, 2019, arts. 11 y 18 · PROCIENCIA, 2024 · ProActivo, 2026",
    notas=[
        "Entre las dos columnas cambia el origen de los recursos con que se obtuvo el resultado, "
        "y con él la vía.",
        "Dato: «Innovación sostenible en teñido de fibra de alpaca con CO₂ supercrítico para "
        "reducir el consumo de agua», de Beatriz Orcon Basilio (UNI), ganó el concurso "
        "Emprendimiento Académico 2024 de PROCIENCIA y el Banco Mundial, con S/ 400 000 y "
        "ejecución entre noviembre de 2024 y mayo de 2026. El concurso prevé como salida una "
        "empresa de base tecnológica; si se constituye, la empresa necesita un acuerdo con la "
        "UNI sobre el resultado.",
        "Dato: Yakuscan (escaneo 3D de embarcaciones con drones con escáner láser e inteligencia "
        "artificial), Kalman Robotics y Zeia son empresas incubadas por StartUp UNI con "
        "cofinanciamiento de PROINNÓVATE (StartUp Perú, Capital Semilla), según la presentación "
        "de la ruta ProInnóvaTECH en la UNI (ProActivo, abril de 2026). Las fuentes consultadas "
        "no indican que exploten un resultado de la universidad; los montos de cada una no son "
        "públicos.",
        "El reglamento de propiedad intelectual de la UNI (RR 1632, 2019) asigna a la universidad "
        "la totalidad de los derechos económicos sobre lo creado en ejercicio de funciones o con "
        "sus recursos, salvo pacto (art. 11). Los estudiantes son titulares de lo que crean "
        "íntegramente, sin perjuicio de los derechos de la universidad (art. 18).",
        "Error frecuente: constituir la empresa antes de resolver la propiedad del resultado. El "
        "informe del BID sobre _deep tech_ (Peña y Jenik, 2023) incluye la estructura accionaria "
        "comprometida y las barreras institucionales para licenciar la propiedad intelectual "
        "entre los obstáculos de las empresas que no consiguen inversión.",
        "Verificar antes de la clase: vigencia en 2026 del reglamento de la UNI de 2019.",
    ],
))

L.append(caso(
    "caso-hb4",
    "01 · Caso de estudio · licencia de una patente",
    "Trigo y soja HB4",
    "Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET) y Universidad "
    "Nacional del Litoral (UNL) · Argentina",
    [
        ("2004", "Patente de la construcción genética, con el CONICET y la UNL como cotitulares"),
        ("20 años", "Licencia a la empresa Bioceres, con regalías por cada semilla vendida"),
        ("2020", "Aprobación del trigo HB4 en la Argentina"),
    ],
    icono_tecnico("planta"),
    fuente="UNL, 2012 y 2020 · CONICET",
    notas=[
        "El grupo de Raquel Chan, de la Facultad de Bioquímica y Ciencias Biológicas de la UNL, "
        "aisló el gen HaHB4 del girasol, que confiere tolerancia a la sequía. El CONICET y la UNL "
        "patentaron la construcción genética en 2004 y licenciaron su uso y explotación a "
        "Bioceres por 20 años (UNL, 2012). La colaboración público-privada superó los 15 años "
        "(UNL, 2020).",
        "Dato: el Departamento de Agricultura de los Estados Unidos (USDA) desreguló el trigo HB4 "
        "el 27 de agosto de 2024. La venta comercial depende de la aceptación de los países "
        "importadores.",
        "El caso muestra la vía de licencia: el resultado no se convirtió en empresa nueva, lo "
        "explota una empresa existente y la titularidad sigue siendo pública. Bioceres figura en "
        "el informe del BID (2023) entre las empresas de _deep tech_ de mayor valoración de la "
        "región.",
        "Verificar antes de la clase: titularidad actual de la patente; una fuente secundaria la "
        "atribuye a Trigall Genetics.",
    ],
))

L.append(recursos(
    "recursos-vias",
    "01 · Recursos recomendados",
    "Recursos sobre vías de transferencia y licencias",
    [
        {"tipo": "Sitio web", "titulo": "Preguntas frecuentes: transferencia de tecnología y propiedad intelectual",
         "autor": "OMPI, División de Transferencia de Tecnología",
         "detalle": "Modos de transferencia, empresas derivadas y titularidad de la propiedad intelectual",
         "url": "wipo.int/es/web/technology-transfer/faq",
         "enlace": "https://www.wipo.int/es/web/technology-transfer/faq"},
        {"tipo": "Guía", "titulo": "Intercambiar valor. Negociación de acuerdos de licencia de tecnología",
         "autor": "OMPI y Centro de Comercio Internacional, 2005",
         "detalle": "Preparación, valoración y negociación de licencias de tecnología, con casos prácticos",
         "url": "wipo.int · Intercambiar valor (OMPI y CCI)",
         "enlace": "https://www.wipo.int/edocs/pubdocs/es/licensing/906/wipo_pub_906.pdf"},
        {"tipo": "Guía", "titulo": "Manual para la comercialización de inventos patentados",
         "autor": "Zelada y Fernandini, INDECOPI, 2020",
         "detalle": "Venta, licencia o empresa propia para explotar una patente",
         "url": "patenta.pe · Manual de comercialización",
         "enlace": "https://www.patenta.pe/wp-content/uploads/2025/05/MANUAL-PARA-LA-COMERCIALIZACION-DE-INVENTOS-PATENTADOS-1.pdf"},
        {"tipo": "Artículo", "titulo": "Tipología de las _spin-offs_ en un contexto universitario: una propuesta de clasificación",
         "autor": "Beraza y Rodríguez, Cuadernos de Gestión, 2012",
         "detalle": "Cuatro tipos de _spin-off_ universitaria según tres criterios",
         "url": "doi.org/10.5295/cdg.090181jb",
         "enlace": "https://doi.org/10.5295/cdg.090181jb"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "Las preguntas frecuentes de la OMPI tratan los modos y tipos de transferencia, entre ellos las licencias, las empresas derivadas y las emergentes; las preguntas 11 a 19 tratan la titularidad de la propiedad intelectual de empleados, estudiantes y proyectos con empresas, tema de la unidad siguiente.",
        "El manual de la OMPI y el Centro de Comercio Internacional cubre la preparación previa a una licencia, la valoración de la tecnología, las cláusulas del acuerdo y la negociación, con casos prácticos. El manual del INDECOPI compara la venta, la licencia y el emprendimiento propio desde la posición del inventor independiente; sus cifras son de 2015 a 2019.",
        "Beraza y Rodríguez (2012) distinguen la _spin-off_ independiente, la vinculada, la _joint venture_ y la subsidiaria según quién emprende, qué conocimiento se transfiere y si hay socios externos. Se basa en la experiencia española.",
    ],
))

# ---------- U2 · Titularidad de los resultados

L.append(pasos(
    "inventor-y-titular",
    "01 · Inventor y titular",
    "Funciones del inventor, el *titular* y el licenciatario de una invención",
    [
        ("Inventor", "Concibe la invención y conserva el derecho a ser mencionado"),
        ("Titular", "Persona natural o jurídica que decide, licencia o cede"),
        ("Licenciatario", "Explota la invención con autorización del titular"),
        ("Usuario", "Adquiere y usa el producto"),
    ],
    clave=1,
    fuente="Comunidad Andina, Decisión 486, arts. 22, 24, 56 y 57",
    notas=[
        "La propiedad intelectual (PI) comprende los derechos sobre las creaciones intelectuales; "
        "la patente y el modelo de utilidad, que se presentan en la unidad siguiente, son derechos "
        "de propiedad industrial.",
        "Según la Decisión 486, el derecho a la patente pertenece en origen al inventor y puede "
        "transferirse; quienes inventan en conjunto son cotitulares (art. 22). El inventor tiene "
        "derecho a ser mencionado en la patente (art. 24).",
        "La cesión (art. 56) transfiere la titularidad, y el cesionario pasa a ser el titular. La "
        "licencia (art. 57) autoriza la explotación sin cambiar de titular. Las dos se registran "
        "por escrito para tener efectos frente a terceros.",
        "El art. 23 remite a la legislación nacional las invenciones hechas bajo relación laboral "
        "y dispone que las entidades con financiamiento estatal reinviertan parte de las regalías "
        "en investigación y hagan partícipes a los investigadores.",
        "El DL 1727 (2026) tipifica como infracción incluir como inventores a quienes no "
        "contribuyeron a la invención (art. 34.d de la Ley 31250 modificada).",
        "Error frecuente: considerar al inventor como titular cuando el resultado se obtuvo con "
        "recursos de la universidad; en ese caso decide el titular que fija el reglamento.",
    ],
))

L.append(tarjetas(
    "documento-titularidad",
    "01 · Documentos de titularidad",
    "Documentos que fijan la *titularidad* de un resultado universitario en el Perú",
    [
        ("Bases y contrato del fondo", "PROCIENCIA reconoce los acuerdos de PI entre los participantes"),
        ("Reglamento de PI", "Derechos de la universidad sobre lo creado con sus recursos"),
        ("Convenio con terceros", "Cláusula de titularidad con la empresa o entidad asociada"),
        ("Convenio con los autores", "Reparto de regalías y reconocimiento de la autoría"),
    ],
    iconos=["fund", "rubric", "agreement", "users"],
    fuente="PROCIENCIA, contrato E72-2024-01-BM · Reglamento de PI de la UNI · Ley 30220",
    notas=[
        "El orden de las fichas es el de precedencia práctica. La Ley 31250 no regula la "
        "titularidad de los resultados; la ley fija la mención del inventor (Decisión 486) y la "
        "participación mínima de la universidad en las regalías (Ley 30220, art. 53).",
        "PROCIENCIA no se atribuye la titularidad: reconoce los acuerdos de PI entre los "
        "participantes según la normativa de la entidad ejecutora y, cuando corresponde, exige un "
        "acuerdo de buena fe entre ellos (contrato modelo E72-2024-01-BM, cláusula 14). Las bases "
        "de Emprendimiento Académico 2025 exigen una delimitación clara de la PI entre la entidad "
        "proponente y las asociadas.",
        "El reglamento de la UNI obliga a incluir una cláusula de titularidad en los convenios "
        "(arts. 12 y 23).",
        "En un proyecto financiado por PROCIENCIA con una empresa asociada intervienen los cuatro "
        "documentos, y cada uno añade un firmante.",
        "Error frecuente: negociar la titularidad después de obtener el resultado; los convenios "
        "y el reglamento se revisan al formular el proyecto.",
    ],
))

L.append(cifra(
    "regalias-universidad",
    "01 · Regalías de las invenciones universitarias",
    "20", "%",
    "mínimo de las regalías por invenciones que corresponde a la universidad",
    "Participación de los inventores: 70 % en la UNI y 50 % en la Pontificia Universidad "
    "Católica del Perú (PUCP)",
    fuente="Ley 30220, art. 53 · Reglamentos de PI de la UNI (2019) y de la PUCP (2011)",
    notas=[
        "Dato: la Ley Universitaria (Ley 30220, art. 53) dispone que las regalías se fijen por "
        "convenio con los autores según sus aportes, con un mínimo del 20 % para la universidad.",
        "Dato: el reglamento de la UNI reparte las regalías en 70 % para los inventores, 5 % para "
        "el grupo, 10 % para la facultad, 5 % para la oficina de transferencia y 10 % para la "
        "universidad; por encima de US$ 100 000 al año, el reparto pasa a 50, 5, 15, 10 y 20 % "
        "(art. 32). La UNI tiene 6 meses de preferencia para proteger; si no actúa, los "
        "partícipes pueden hacerlo y la universidad retiene el 30 % (art. 29).",
        "Dato: la PUCP asigna 50 % a los inventores, 25 % a la unidad y 25 % a la universidad "
        "(art. 20); si renuncia a proteger, el creador registra a su nombre y la PUCP conserva el "
        "10 % de los beneficios netos (art. 54). La Universidad Peruana Cayetano Heredia (UPCH) "
        "asigna 50 % a los inventores y puede ceder la titularidad a cambio de al menos el 20 % "
        "de las ganancias durante 3 años.",
        "El dictamen de la Comisión de Ciencia, Innovación y Tecnología del Congreso (mayo de "
        "2026) propone entre 20 % y 50 % para la institución; es un proyecto, no una ley vigente.",
        "Verificar antes de la clase: vigencia de los reglamentos de la UNI (2019), la PUCP "
        "(2011) y la UPCH (2012), y posibles modificaciones del art. 53 en el Sistema Peruano de "
        "Información Jurídica (SPIJ).",
    ],
))

L.append(recursos(
    "recursos-titularidad",
    "01 · Recursos recomendados",
    "Recursos sobre titularidad y reglamentos de propiedad intelectual",
    [
        {"tipo": "Guía", "titulo": "Guía para la elaboración de reglamentos de propiedad intelectual en universidades y centros de investigación en el Perú",
         "autor": "Luis Enrique Sánchez Gavidia, INDECOPI, 2018",
         "detalle": "Etapas y contenido de un reglamento universitario de propiedad intelectual",
         "url": "patenta.pe · Guía de reglamentos de PI",
         "enlace": "https://www.patenta.pe/wp-content/uploads/2025/05/GUIA-RPI.pdf"},
        {"tipo": "Guía", "titulo": "Guía Metodológica Tangüis: convenios y contratos de I+D+i para la vinculación academia-industria",
         "autor": "Claudia Fernandini, CONCYTEC, 2020",
         "detalle": "Modelos peruanos de convenios y contratos con cláusulas de propiedad intelectual",
         "url": "vinculate.concytec.gob.pe · Guía Tangüis",
         "enlace": "https://vinculate.concytec.gob.pe/wp-content/uploads/2025/07/GUIA-TANGUIS.pdf"},
        {"tipo": "Sitio web", "titulo": "Políticas de PI para universidades e instituciones de investigación",
         "autor": "OMPI, modelo de política de 2019",
         "detalle": "Modelo de política de PI, lista de verificación y base de datos",
         "url": "wipo.int · Políticas de PI para universidades",
         "enlace": "https://www.wipo.int/es/web/technology-transfer/ip-policies"},
        {"tipo": "Guía", "titulo": "University and business collaboration agreements: Lambert Toolkit",
         "autor": "Intellectual Property Office, Reino Unido, 2016",
         "detalle": "Modelos de acuerdo universidad-empresa con distintos repartos de titularidad",
         "url": "gov.uk · Lambert Toolkit",
         "enlace": "https://www.gov.uk/guidance/university-and-business-collaboration-agreements-lambert-toolkit"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía del INDECOPI explica por qué una universidad reglamenta la PI, cómo se construye el reglamento y qué contiene (titularidad, regalías, licencia y cesión), con referencia a la Ley 30220. Es de 2018: conviene contrastarla con el reglamento vigente de la UNI.",
        "La Guía Tangüis de CONCYTEC trae modelos de convenio marco y específico, contratos de servicios de I+D, acuerdos de confidencialidad y de transferencia de materiales, con un capítulo de PI; los formatos se descargan sueltos en la plataforma Vincúlate.",
        "El modelo de política de la OMPI regula la titularidad y los derechos de uso (art. 5) y los incentivos y el reparto de ingresos (art. 10). El Lambert Toolkit reúne once modelos de acuerdo británicos en los que la titularidad queda en la institución, en la empresa o se reparte; se rige por el derecho inglés y sirve para comparar cláusulas.",
    ],
))

# ---------- U3 · Protección de los resultados

L.append(frase(
    "definicion-patente",
    "01 · Definición de patente",
    "La *patente* es el derecho exclusivo y temporal que el Estado concede sobre una invención "
    "nueva, con nivel inventivo y aplicación industrial, cuya descripción se publica.",
    "Síntesis de la Decisión 486 de la Comunidad Andina, arts. 14 y 50",
    notas=[
        "La Decisión 486 exige tres requisitos de patentabilidad: novedad, nivel inventivo y "
        "aplicación industrial (art. 14). La patente dura 20 años desde la fecha de presentación "
        "de la solicitud (art. 50). En el Perú la otorga el INDECOPI.",
        "El derecho es territorial: rige en el país que concede la patente. La familia de "
        "patentes reúne las solicitudes que protegen una misma invención en varios países.",
        "Dato: el Tratado de Cooperación en materia de Patentes (PCT) de la OMPI permite una "
        "solicitud internacional con efecto en 159 Estados contratantes desde el 19 de agosto de "
        "2026.",
        "Dato: en enero de 2024 se informó que el INDECOPI concedió a la UNI una patente de 20 "
        "años por un prototipo de celdas de combustible microbianas que genera electricidad a "
        "partir de agua residual, con electrodos con nanopartículas de oro y sin membrana "
        "separadora, hasta 500 mV. Los inventores son Adolfo La Rosa-Toro, Angélica Baena y la "
        "estudiante Sandy Calderón, del Grupo de Electroquímica Aplicada; la I+D la financiaron "
        "CONCYTEC y PROINNÓVATE (Infobae, 2024).",
        "Error frecuente: describir la patente como un premio a la investigación. Es un derecho "
        "de exclusión que el titular ejerce frente a terceros, y su descripción queda pública.",
    ],
))

L.append(tarjetas(
    "formas-proteccion",
    "01 · Formas de protección",
    "Formas de protección de un resultado de investigación según la *Decisión 486*",
    [
        ("Patente de invención", "Producto o procedimiento nuevo con nivel inventivo; 20 años desde la solicitud"),
        ("Modelo de utilidad", "Nueva forma o configuración de un objeto que mejora su funcionamiento; 10 años"),
        ("Secreto empresarial", "Información no divulgada con valor comercial; protección mientras se mantenga reservada"),
    ],
    iconos=["patent", "layers", "folder"],
    fuente="Comunidad Andina, Decisión 486, arts. 14, 50, 81, 84 y 260",
    notas=[
        "El modelo de utilidad protege una nueva forma, configuración o disposición de elementos "
        "de un artefacto, herramienta o instrumento que mejora su funcionamiento o su utilización "
        "(art. 81) y dura 10 años (art. 84). El secreto empresarial no se registra y se protege "
        "mientras la información siga siendo secreta, tenga valor comercial y esté sujeta a "
        "medidas razonables de reserva (art. 260).",
        "Dato: en 2025 las universidades peruanas presentaron 722 solicitudes de modelo de "
        "utilidad y 246 de patente de invención (INDECOPI, citado por Energiminas, 2026).",
        "Dato: el INDECOPI otorgó a nombre de la UNI un modelo de utilidad por una impresora 3D "
        "que dosifica nutrientes en gel a partir de cartuchos de fruta liofilizada, para la "
        "desnutrición infantil; lo inventaron Walter Gonzales Arnao y Benito Juárez Vélez, del "
        "FABLAB UNI. Rige 10 años desde la solicitud, presentada el 31 de diciembre de 2019 "
        "(VRI-UNI, 2021). Según el VRI, de las 147 patentes de la UNI entre 1993 y 2023, 129 "
        "son modelos de utilidad y 18 de invención.",
        "La elección depende del resultado. Un procedimiento que no se puede deducir del producto "
        "vendido admite el secreto; un dispositivo que cualquiera puede desarmar y copiar requiere "
        "patente o modelo de utilidad.",
        "El diseño industrial, la marca y el derecho de autor son otras formas de propiedad "
        "intelectual, con objetos de protección distintos.",
    ],
))

L.append(frase(
    "divulgacion-y-novedad",
    "01 · Divulgación y novedad",
    "La divulgación de una invención antes de la solicitud compromete su *novedad*, salvo la "
    "del propio inventor dentro de los 12 meses previos.",
    "Síntesis de la Decisión 486, art. 17",
    fuente="Comunidad Andina, Decisión 486, art. 17 · OMPI, cuadro de plazos de gracia",
    notas=[
        "El plazo de gracia de la Decisión 486 cubre la divulgación hecha en los 12 meses "
        "anteriores a la solicitud por el inventor o su derechohabiente, por la oficina nacional "
        "en una publicación indebida o por un tercero que obtuvo la información del inventor "
        "(art. 17; cuadro de plazos de gracia de la OMPI).",
        "La Oficina Europea de Patentes y otras oficinas no reconocen ese plazo; una invención "
        "divulgada antes de solicitar puede quedar sin protección en esos países. Por eso la "
        "práctica prudente es solicitar antes de divulgar.",
        "Son divulgación un artículo, una tesis en un repositorio abierto, un póster o una "
        "demostración en una feria. El contrato de PROCIENCIA reserva su derecho a publicar los "
        "resultados «siempre y cuando no vulnere la novedad».",
        "Error frecuente: publicar la tesis en el repositorio institucional antes de presentar la "
        "solicitud de patente.",
    ],
))

L.append(caso(
    "caso-qaira",
    "01 · Caso de estudio · titularidad compartida",
    "qAIRa",
    "Empresa qAIRa y Pontificia Universidad Católica del Perú · Lima",
    [
        ("2016", "Solicitud conjunta de un modelo de utilidad por la empresa y la PUCP"),
        ("2018", "Concesión del modelo de utilidad: módulo intercambiable de medición del aire para drones"),
        ("Vía", "Empresa de egresados con la PUCP como cotitular; sin licencia publicada"),
    ],
    icono("dron"),
    fuente="OMPI, 2020 · Unión Andina, 2022 · Andina, 2020",
    notas=[
        "El caso trata la vía de transferencia y la titularidad de la empresa. qAIRa (GRUPO QAIRA S.A.C.) la fundaron Mónica Abarca, Carlos Saito, "
        "Francisco Cuéllar y Javier CalvoPérez; la OMPI da 2015 como año de fundación.",
        "En 2016 la empresa y la PUCP solicitaron juntas el modelo de utilidad «Módulo "
        "intercambiable para la medición de la calidad del aire en vehículos aéreos no "
        "tripulados», concedido en 2018 (Unión Andina, 2022). La empresa y la universidad son "
        "cotitulares. La OMPI registra solicitudes ante el INDECOPI en 2014 y 2016.",
        "La invención es una nueva configuración de un objeto existente, el dron, que mejora su "
        "función; por eso corresponde a un modelo de utilidad.",
        "En 2020 la red qHAWAX operaba 7 módulos con la Municipalidad Metropolitana de Lima, "
        "Miraflores y San Borja, con financiamiento del Banco Mundial y CONCYTEC y ejecución de "
        "la PUCP, la Universidad Católica San Pablo y qAIRa (Andina, 2020): un contrato de I+D "
        "colaborativo.",
        "El caso está en el límite entre la _spin-off_ de la Ley 31250 y la _startup_ "
        "independiente: empresa nueva de egresados con la universidad como cotitular y sin un "
        "contrato de licencia publicado.",
        "Verificar antes de la clase: estado actual de la empresa (Andina la presenta activa en "
        "mayo de 2025; CB Insights la marca como cerrada), número de registro del modelo de "
        "utilidad y año de fundación (2015 o 2016).",
    ],
))

L.append(recursos(
    "recursos-proteccion",
    "01 · Recursos recomendados",
    "Recursos sobre patentes, modelos de utilidad y secretos empresariales",
    [
        {"tipo": "Guía", "titulo": "Guía de patentes para investigadores",
         "autor": "Mauricio Osorio Icochea, INDECOPI, 2017",
         "detalle": "Patente de invención, modelo de utilidad y requisitos de patentabilidad en el Perú",
         "url": "patenta.pe · Guía de patentes (2017)",
         "enlace": "https://www.patenta.pe/wp-content/uploads/2025/05/GUIA-DE-PATENTES-PARA-INVESTIGADORES.pdf"},
        {"tipo": "Guía", "titulo": "Guía práctica para la protección mediante secretos empresariales",
         "autor": "Deyra Chuquitapa Cuno, INDECOPI, 2020",
         "detalle": "Concepto, alcance y violación del secreto empresarial",
         "url": "patenta.pe · Guía de secretos empresariales",
         "enlace": "https://www.patenta.pe/wp-content/uploads/2025/03/Guia-de-secretos-empresariales.pdf"},
        {"tipo": "Sitio web", "titulo": "Programa Patenta",
         "autor": "INDECOPI, edición 2026",
         "detalle": "Asesoría gratuita para preparar solicitudes de patente o de modelo de utilidad",
         "url": "patenta.pe/programa-patenta",
         "enlace": "https://www.patenta.pe/programa-patenta/"},
        {"tipo": "Curso en línea", "titulo": "DL-170: curso de especialización sobre los conceptos básicos de las patentes",
         "autor": "Academia de la OMPI, 2026",
         "detalle": "Curso gratuito en español, de autoaprendizaje y con certificado",
         "url": "wipo.int · Academia de la OMPI, curso DL-170",
         "enlace": "https://www.wipo.int/es/web/wipo-academy/programs/ip-elearning/index"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía de patentes del INDECOPI explica las dos modalidades de patente del Perú y sus requisitos, y menciona el período de gracia de un año de la Decisión 486; no trata tasas ni plazos de trámite. La guía de secretos empresariales desarrolla la tercera forma de protección y la relación entre inventos y secretos.",
        "El Programa Patenta asesora en la redacción y presentación de solicitudes de patente o de modelo de utilidad, admite universidades y exige prototipo, modelo computarizado, planos o experimentación. La quinta convocatoria de 2026 cerró el 11 de octubre; se presenta como programa anual.",
        "El curso DL-170 de la Academia de la OMPI dura 12 horas; la edición en español admite inscripciones hasta el 14 de noviembre de 2026 y se dicta del 15 de noviembre al 16 de diciembre.",
    ],
))

L.append(cierre(
    "sintesis-01",
    "01 · Síntesis",
    "Vía de transferencia, titularidad y *protección* de un resultado de investigación",
    [
        "Vía: según quién explota el resultado y con qué recursos se obtuvo",
        "Titularidad: fijada por escrito antes de explotar",
        "Protección: solicitud previa a la divulgación",
    ],
    ("Receso", "10 minutos · Tema 02: creación de empresas derivadas y de base tecnológica"),
    notas=[
        "Recapitular el criterio de cada término del tema 01 antes del receso de 10 minutos.",
        "El plazo de gracia de 12 meses rige en la Comunidad Andina y no en todas las oficinas de "
        "patentes; la solicitud previa a la divulgación evita depender de él.",
    ],
))

# ============== TEMA 02 · CREACIÓN DE EMPRESAS DERIVADAS Y DE BASE TECNOLÓGICA

L.append(seccion(
    "tema-02", "02", "Creación de empresas derivadas y de base tecnológica",
    "Oficina de transferencia, empresas de base tecnológica y factores asociados a la creación "
    "de _spin-offs_",
    notas=[
        "Mantener esta lámina en pantalla durante el receso.",
        "Presentar el tema 02, que trata la unidad que gestiona la transferencia en la "
        "universidad, las empresas de base tecnológica y _deep tech_, los factores asociados a la "
        "creación de _spin-offs_ y la situación del Perú.",
        "Tiempo: 80 minutos; presentación del tema, 1; oficina de transferencia, 22; empresas de "
        "base tecnológica, 25; factores asociados y situación del Perú, 28; síntesis, 4.",
    ],
))

# ---------- U4 · Oficina de transferencia tecnológica

L.append(frase(
    "definicion-ott",
    "02 · Definición de oficina de transferencia",
    "La *oficina de transferencia tecnológica* (OTT) gestiona la propiedad intelectual de una "
    "universidad y su transferencia a las empresas.",
    "Síntesis de la definición de la OMPI",
    notas=[
        "La OTT gestiona lo tratado en el tema 01: recibe la comunicación de invención del "
        "investigador, decide la protección, negocia la licencia o el acuerdo con la _spin-off_ y "
        "administra el reparto de regalías.",
        "Recibe otros nombres: Oficina de Licencias Tecnológicas, Núcleo de Innovación "
        "Tecnológica (Brasil) u Oficina de Transferencia de Resultados de Investigación (OTRI, "
        "España).",
        "El dictamen peruano sobre transferencia tecnológica (mayo de 2026, no vigente) la define "
        "como la unidad que explota la PI y los resultados de I+D en nombre de la institución y "
        "propone que dependa, de preferencia, del Vicerrectorado de Investigación.",
        "Error frecuente: confundir la comunicación de invención, que es un aviso interno a la "
        "OTT, con la divulgación pública que compromete la novedad.",
    ],
))

L.append(pasos(
    "ruta-ott",
    "02 · Modelo lineal de transferencia",
    "Recorrido de un resultado en la *oficina de transferencia* según el modelo lineal",
    [
        ("Comunicación de invención", "Aviso del investigador a la OTT"),
        ("Evaluación y protección", "Revisión del resultado y solicitud antes de divulgar"),
        ("Búsqueda y negociación", "Empresa interesada o equipo fundador"),
        ("Licencia o _spin-off_", "Regalías, participación u otra contraprestación"),
    ],
    fuente="Bradley, Hayter y Link, 2013",
    notas=[
        "Bradley, Hayter y Link (2013) sintetizan el modelo lineal «tradicional» de la "
        "transferencia universitaria a partir de Siegel et al. (2004): descubrimiento, "
        "comunicación de invención, evaluación, solicitud de patente, búsqueda de interesados, "
        "negociación, licencia y adaptación por la empresa.",
        "Los autores presentan el modelo como un punto de partida para ordenar la literatura; en "
        "la práctica el proceso tiene retroalimentación y etapas que se superponen.",
        "Dato: el reglamento de la UNI da a la universidad 6 meses de preferencia para proteger "
        "una invención comunicada (art. 29); si la OTT no interviene, lo comunica en 60 días "
        "(art. 30).",
        "El grupo de investigación aporta el ensayo documentado y la descripción técnica, sin los "
        "cuales la OTT no puede evaluar ni proteger el resultado.",
    ],
))

L.append(tarjetas(
    "factores-ott",
    "02 · Factores organizativos de la OTT",
    "Factores organizativos asociados al desempeño de una *OTT*",
    [
        ("Sistema de recompensas", "Retribución por el resultado transferido"),
        ("Gestión del personal", "Dirección y metas del equipo de la oficina"),
        ("Política institucional", "Norma interna que promueve la transferencia"),
        ("Personal calificado", "Competencias en propiedad intelectual y negociación"),
        ("Barreras culturales", "Obstáculos culturales y de información en la universidad"),
    ],
    iconos=["budget", "users", "scale", "workshop", "network"],
    fuente="Siegel, Waldman y Link, 2003, en Odei y Novák, 2022",
    notas=[
        "Siegel, Waldman y Link (2003) proponen cinco factores organizativos y de gestión que "
        "favorecen la actividad de la OTT; Odei y Novák (2022) los recogen como marco de su "
        "estudio sobre la creación de _spin-offs_.",
        "Cada factor se comprueba en documentos de la universidad: el reglamento publica el "
        "reparto de regalías, la oficina tiene una jefatura con dedicación declarada, la política "
        "de transferencia está aprobada y fechada, el perfil del puesto exige formación en PI y "
        "existe un procedimiento de comunicación de invenciones.",
    ],
))

L.append(tarjetas(
    "ott-peru",
    "02 · Oficinas de transferencia en el Perú",
    "Capacidades de transferencia de las universidades e institutos del *Perú*, 2024",
    [
        ("44 %", "sin oficina o unidad de transferencia"),
        ("80 %", "sin política específica de transferencia"),
        ("30 %", "sin transferencia de tecnología por ningún mecanismo"),
        ("70 %", "de los responsables de OTT con 3 años o menos de experiencia"),
    ],
    fuente="CONCYTEC, encuesta a OTT 2024 · Osorio, 2025 · Maldonado, _El Peruano_, 2026",
    notas=[
        "Dato: el Primer Estudio Nacional de la Gestión de la Transferencia Tecnológica de "
        "CONCYTEC encuestó entre septiembre y octubre de 2024 a universidades licenciadas e "
        "institutos públicos de investigación (IPI); la muestra fue de 67 de 106 instituciones "
        "(Osorio, 2025). Más de la mitad no tiene una cartera tecnológica identificada.",
        "Dato: el 44 % y el 80 % los informó la subdirectora de Innovación y Transferencia "
        "Tecnológica de CONCYTEC (Maldonado, 2026). Casi el 70 % de los responsables de OTT tiene "
        "3 años o menos de experiencia en transferencia; el proyecto de ley 14361 da 70,2 %.",
        "CONCYTEC clasifica la capacidad de transferencia de una institución en cinco niveles, "
        "desde la ausencia de OTT y de I+D hasta la OTT consolidada con personal especializado.",
        "En 2016, de 142 universidades, unas 10 tenían política de PI y 3 tenían OTT (CONCYTEC, "
        "2016). El universo no es comparable con el de 2024.",
        "Dato: el concurso de Fortalecimiento de OTT 2025 de PROCIENCIA seleccionó cinco "
        "oficinas: Universidad de Piura, Universidad Nacional Agraria La Molina, Instituto "
        "Tecnológico de la Producción, PUCP y Universidad Nacional Hermilio Valdizán. El "
        "beneficio es un servicio de acompañamiento de 18 meses, no un monto en dinero.",
        "Verificar antes de la clase: el 44 % y el 80 % en el informe de CONCYTEC (el PDF "
        "enlazado devolvía error 404), la diferencia entre la muestra de 67 y la ficha «58 "
        "universidades + 5 IPI», y la votación en el Pleno del dictamen que haría obligatoria una "
        "unidad de transferencia en las instituciones públicas.",
    ],
))

L.append(recursos(
    "recursos-ott",
    "02 · Recursos recomendados",
    "Recursos sobre oficinas de transferencia tecnológica",
    [
        {"tipo": "Guía", "titulo": "Incentivos en la transferencia de tecnología",
         "autor": "OMPI, 2024",
         "detalle": "Incentivos monetarios y no monetarios para investigadores y personal de transferencia",
         "url": "wipo.int · Incentivos en la transferencia",
         "enlace": "https://www.wipo.int/edocs/pubdocs/es/wipo-pub-2002-es-incentives-in-technology-transfer.pdf"},
        {"tipo": "Artículo", "titulo": "Technology transfer offices and commercialization of university intellectual property: performance and policy implications",
         "autor": "Siegel, Veugelers y Wright, Oxford Review of Economic Policy, 2007",
         "detalle": "Revisión de la evidencia sobre el desempeño de las oficinas de transferencia",
         "url": "doi.org/10.1093/oxrep/grm036",
         "enlace": "https://doi.org/10.1093/oxrep/grm036"},
        {"tipo": "Informe", "titulo": "ASTP 2024 Annual Survey on the European Knowledge Transfer Landscape",
         "autor": "ASTP, 2025 (datos de 2022)",
         "detalle": "Personal, patentes, licencias y _spin-offs_ de oficinas europeas de transferencia",
         "url": "astp4kt.eu/kt-metrics",
         "enlace": "https://astp4kt.eu/resources/executive-data-report-2024-fy2022.pdf"},
        {"tipo": "Informe", "titulo": "Informe sobre la situación actual de universidades públicas y privadas en el Perú en torno a la propiedad intelectual",
         "autor": "Felipe Zucchetti, INDECOPI, 2018",
         "detalle": "Encuesta a universidades peruanas sobre oficinas y políticas de propiedad intelectual",
         "url": "patenta.pe · Universidades y PI, 2018",
         "enlace": "https://www.patenta.pe/wp-content/uploads/2025/05/Guia-universidades-publicas-y-privadas.pdf"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "La guía de la OMPI sobre incentivos desarrolla el sistema de recompensas: incentivos monetarios y no monetarios para investigadores y personal de la OTT, y reparto de ingresos, el aspecto que se comprueba en un reglamento.",
        "Siegel, Veugelers y Wright (2007) describen la OTT como intermediaria que licencia a empresas existentes o a empresas nuevas y revisan estudios sobre la productividad de oficinas, parques e incubadoras. Es un artículo distinto del de Siegel, Waldman y Link (2003) citado en clase.",
        "El informe de la ASTP da magnitudes de oficinas europeas: tamaño, comunicaciones de invención, solicitudes, licencias y _spin-offs_ por oficina; según su portada, reúne datos de 481 OTT de 22 países. La encuesta del INDECOPI de 2018 es el antecedente peruano de la encuesta de CONCYTEC de 2024.",
    ],
))

# ---------- U5 · Empresas de base tecnológica y deep tech

L.append(frase(
    "definicion-ebt",
    "02 · Definición de empresa de base tecnológica",
    "Una *empresa de base tecnológica* comercializa productos o servicios generados con uso "
    "intensivo de conocimiento científico y tecnológico.",
    "Síntesis de la Ley 31250, glosario, n.º 18 (2021)",
    notas=[
        "La Ley 31250 añade que la empresa de base tecnológica (EBT) basa su actividad en la "
        "innovación tecnológica orientada al mercado y cuenta con personal investigador y técnico "
        "de alta cualificación.",
        "Una EBT puede ser _spin-off_, si deriva de una universidad, o _startup_ independiente. "
        "La literatura llama _deep tech_ a las empresas cuyo producto nace de un avance científico "
        "o de ingeniería (Nguyen, Kowalski y Dzienis, 2024).",
        "En términos de madurez tecnológica, estas empresas suelen constituirse con la tecnología en "
        "niveles bajos de TRL y recorren como empresa el tramo del valle de la muerte.",
    ],
))

L.append(duo(
    "deep-tech-frente-digital",
    "02 · _Deep tech_ y empresa digital",
    "Rasgos de una empresa de *_deep tech_* frente a una empresa digital",
    {"cab": "Empresa digital", "t": "Ciclo de desarrollo rápido e iterativo",
     "items": ["Barrera de entrada baja", "Inversión inicial menor"]},
    {"cab": "_Deep tech_", "t": "Producto que nace de un avance científico o de ingeniería",
     "items": ["Desarrollo secuencial, largo y costoso", "Fundadores con doctorado o posgrado técnico",
               "Inversión inicial elevada"]},
    fuente="Nguyen, Kowalski y Dzienis, _Sustainability_, 2024",
    notas=[
        "Nguyen, Kowalski y Dzienis (2024) describen la empresa de _deep tech_ como una "
        "organización impulsada por la ciencia que genera avances tecnológicos y de ingeniería. "
        "Frente a la empresa digital, tiene una barrera de entrada alta, un proceso de I+D más "
        "largo, una inversión inicial mayor y menos casos de referencia.",
        "Sus campos incluyen la biotecnología, la inteligencia artificial, la nanotecnología, la "
        "robótica, las tecnologías agrícolas y los dispositivos médicos.",
        "Error frecuente: citar una tasa de fracaso del 90 % para estas empresas. Nguyen et al. "
        "la toman de fuentes secundarias y no la miden en sus casos; no se usa en clase.",
    ],
))

L.append(pasos(
    "proceso-deep-tech",
    "02 · Proceso emprendedor en _deep tech_",
    "Fases del proceso emprendedor en seis empresas de *_deep tech_*, 2024",
    [
        ("Idea", "Fundadores con formación técnica"),
        ("Oportunidad", "Reconocimiento y evaluación"),
        ("Constitución", "Creación de la empresa"),
        ("Desarrollo", "Producto y financiamiento en paralelo"),
        ("Escalamiento", "Crecimiento de la empresa"),
    ],
    clave=3,
    fuente="Nguyen, Kowalski y Dzienis, _Sustainability_, 2024",
    notas=[
        "El modelo tiene cinco fases y seis actividades; la cuarta fase reúne el desarrollo del "
        "producto y el financiamiento, que ocurren en paralelo. Se construyó con seis casos de "
        "empresas de _deep tech_ orientadas a problemas sociales y ambientales.",
        "En los seis casos, el desarrollo del producto ocurrió después de constituir la empresa y "
        "concentró el esfuerzo de los primeros uno a tres años. Todos los fundadores tenían "
        "formación técnica previa.",
        "Implicación para el formulador: un plan que prevé constituir la empresa al terminar el "
        "desarrollo difiere del patrón observado en los seis casos.",
    ],
))

L.append(caso(
    "caso-tumi",
    "02 · Caso de estudio · _spin-off_ académica",
    "Tumi Robotics",
    "Empresa nacida en laboratorios de la PUCP · Lima",
    [
        ("2016", "Constitución por dos ingenieros, con origen en laboratorios de la PUCP"),
        ("400 m", "Profundidad de descenso de sus robots de inspección en socavones mineros"),
        ("2026", "Selección por un centro espacial de Luxemburgo para adaptar sus robots al suelo lunar"),
    ],
    icono_tecnico("robot"),
    fuente="PROINNÓVATE, 2026 · Descubre.vc, 2025",
    notas=[
        "Tumi Robotics la constituyeron en 2016 Francisco Cuéllar, también cofundador de qAIRa, "
        "y Claudia Akamine. Fabrica robots terrestres, acuáticos y aéreos con escáner láser "
        "(LiDAR) para inspeccionar instalaciones mineras, petroquímicas y de energía.",
        "Dato: en mayo de 2026 el Centro Europeo de Innovación en Recursos Espaciales (ESRIC), de "
        "Luxemburgo, la seleccionó para adaptar sus robots al suelo lunar, con una prueba en un "
        "laboratorio análogo hacia fines de 2026 (PROINNÓVATE, 2026).",
        "Recibió fondos de StartUp Perú, Innovación Empresarial y el Programa de Apoyo a la "
        "Internacionalización de PROINNÓVATE.",
        "TRL estimado por el docente: 9 en inspección minera, por su operación comercial; 4 a 6 "
        "en la línea lunar.",
        "Tumi Robotics cumple la definición de _spin-off_ de la Ley 31250, porque nace de una "
        "universidad. La definición de la literatura exige además un vínculo formal (licencia, "
        "cesión o participación).",
        "Dato: en julio de 2021 la PUCP y Tumi Robotics firmaron dos contratos de licencia de "
        "patentes de la universidad, un robot submarino y un bote para monitorear lagunas, "
        "bofedales y otros cuerpos de agua continentales; la empresa explota las tecnologías a "
        "cambio de regalías (PUCP, Vicerrectorado de Investigación, 2021). Es el vínculo formal "
        "que pide la literatura.",
        "Verificar antes de la clase: las «4 tecnologías patentadas» que menciona Descubre.vc "
        "(no cotejadas con el INDECOPI).",
    ],
))

L.append(cifra(
    "deeptech-region",
    "02 · _Deep tech_ en América Latina",
    "5", "",
    "empresas de _deep tech_ con inversión institucional en el Perú, de 340 en América Latina "
    "y el Caribe",
    "Argentina 103 · Brasil 101 · Chile 65 · México 30",
    fuente="Peña y Jenik, _Deep Tech: The New Wave_, BID Lab, 2023",
    notas=[
        "Dato: el informe del BID Lab identificó 340 empresas de _deep tech_ con inversión de "
        "fondos de capital de riesgo o de aceleradoras en 14 países de América Latina y el "
        "Caribe; captaron unos US$ 2 000 millones y el conjunto se valoró en unos US$ 8 000 "
        "millones. Argentina, Brasil y Chile reúnen el 79 % de las empresas.",
        "Dato: las 5 empresas del Perú tienen un valor conjunto inferior a US$ 20 millones. La "
        "biotecnología reúne el 61 % de las empresas de la región.",
        "Dato: el _Deep Tech Radar Latam 2025_ (Emerge y Cubo Itaú) contó 1 316 empresas de _deep "
        "tech_ en la región, 952 de ellas en Brasil, 145 en Argentina y 73 en Chile (Agência "
        "FAPESP, 2025). Usa otra metodología, porque incluye empresas sin inversión "
        "institucional, y sus cifras no son comparables con las del BID.",
        "Los datos del BID corresponden a 2022. Las cifras se cotejaron en el PDF del informe "
        "(resumen ejecutivo y capítulo 3).",
    ],
))

L.append(recursos(
    "recursos-deeptech",
    "02 · Recursos recomendados",
    "Recursos sobre empresas de base tecnológica y _deep tech_",
    [
        {"tipo": "Informe", "titulo": "What is «Deep Tech» and what are Deep Tech Ventures?",
         "autor": "Basilio Ruiz de Apodaca, Murray y Frolund, MIT REAP, 2023",
         "detalle": "Definición de _deep tech_ y criterios para identificar sus empresas",
         "url": "reap.mit.edu · MIT REAP, 2023",
         "enlace": "https://reap.mit.edu/assets/What_is_Deep_Tech_MIT_2023.pdf"},
        {"tipo": "Artículo", "titulo": "Critical junctures in the development of university high-tech spinout companies",
         "autor": "Vohora, Wright y Lockett, Research Policy, 2004",
         "detalle": "Fases y coyunturas críticas de las _spin-offs_ universitarias",
         "url": "doi.org/10.1016/S0048-7333(03)00107-0",
         "enlace": "https://doi.org/10.1016/S0048-7333(03)00107-0"},
        {"tipo": "Informe", "titulo": "Emprendimientos de base científico-tecnológica en América Latina",
         "autor": "Kantis y Angelelli, BID, 2020",
         "detalle": "Casos, condiciones y políticas para empresas científico-tecnológicas en la región",
         "url": "doi.org/10.18235/0002156",
         "enlace": "https://doi.org/10.18235/0002156"},
        {"tipo": "Informe", "titulo": "Diagnóstico del ecosistema _Deep Tech_ de emprendimiento e inversión en etapas tempranas en Chile",
         "autor": "Díaz et al., BID, 2026",
         "detalle": "Capacidades, actores y brechas del _deep tech_ chileno",
         "url": "doi.org/10.18235/0013888",
         "enlace": "https://doi.org/10.18235/0013888"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "El documento del programa MIT REAP define el _deep tech_ como soluciones tecnológicas de base científica asociadas a dimensiones críticas de incertidumbre y propone criterios para reconocer sus empresas. No tiene revisión por pares.",
        "Vohora, Wright y Lockett (2004) describen las fases de la _spin-off_ universitaria y las coyunturas críticas que separan una fase de la siguiente (reconocimiento de la oportunidad, compromiso emprendedor, umbral de credibilidad y umbral de sostenibilidad); sirve para comparar con el proceso de Nguyen et al. De pago: consultar en la biblioteca.",
        "Los dos informes del BID son distintos del de 2023 citado en clase: Kantis y Angelelli (2020) tratan los emprendimientos científico-tecnológicos de la región, y Díaz et al. (2026) diagnostican el ecosistema chileno. El portal del BID bloquea las comprobaciones automáticas: abrir los enlaces en un navegador antes de la clase.",
    ],
))

# ---------- U6 · Factores asociados y situación del Perú

L.append(tarjetas(
    "determinantes-spinoffs",
    "02 · Factores asociados a las _spin-offs_",
    "Creación de *_spin-offs_* y factores asociados en 164 universidades del Reino Unido",
    [
        ("Cartera de patentes", "Factor con la asociación de mayor tamaño"),
        ("Financiamiento de I+D", "Asociación directa y a través de la cartera de patentes"),
        ("Recompensas al personal", "Asociación significativa de menor tamaño"),
    ],
    clave=0,
    iconos=["patent", "fund", "budget"],
    fuente="Odei y Novák, 2022, con datos de la encuesta HE-BCI 2017/18",
    notas=[
        "Dato: Odei y Novák (2022) analizaron 164 universidades del Reino Unido con datos de la "
        "Higher Education Business and Community Interaction Survey (HE-BCI) del curso 2017/18. "
        "Su modelo explica el 70 % de la variación en la creación de _spin-offs_.",
        "Es un estudio de corte transversal: muestra asociaciones, no causas. Los autores "
        "destacan las recompensas al personal; en su modelo, el tamaño de efecto mayor "
        "corresponde a la cartera de patentes.",
        "Dato: la media por universidad fue de 26,72 comunicaciones de invención, 12,91 "
        "solicitudes de patente, 10,41 patentes concedidas y 5,57 _spin-offs_ con participación "
        "de la universidad, con un rango de 0 a 70 _spin-offs_. La media no describe a una "
        "universidad cualquiera.",
        "En Europa, Hunady et al. (2019) hallaron, en 2 465 instituciones de educación superior, "
        "relaciones no lineales entre la creación de _spin-offs_, la especialización y la "
        "proporción de doctorandos.",
    ],
))

L.append(tarjetas(
    "barreras-colaboracion",
    "02 · Colaboración universidad-empresa",
    "Barreras de la colaboración universidad-empresa en un consorcio de *Irlanda*",
    [
        ("Acuerdo de PI ausente", "Barrera en los años 1 a 3; acuerdo firmado en los años 4 a 7"),
        ("Falta de confianza", "Fuerte en la fase inicial"),
        ("Temor a la fuga de conocimiento", "Fuerte en las dos primeras fases"),
        ("Renuencia a compartir recursos", "Presente desde la fase inicial"),
        ("Percepción de escaso valor", "Presente en las dos primeras fases"),
    ],
    clave=0,
    fuente="O’Dwyer, Filieri y O’Malley, _The Journal of Technology Transfer_, 2022",
    notas=[
        "Dato: O’Dwyer, Filieri y O’Malley (2022) reconstruyeron con entrevistas la evolución del "
        "consorcio farmacéutico irlandés SSPC, con 18 miembros fundadores entre universidades y "
        "empresas multinacionales, en cuatro fases: embrionaria (antes del año 1), de inicio "
        "(años 1 a 3), de compromiso (años 4 a 7) y de consolidación.",
        "La confianza por la reputación de quien convocó el consorcio precedió a la confianza "
        "por la integridad observada en el trabajo conjunto. El acuerdo de "
        "PI se firmó en la fase de compromiso; mientras tanto, los socios trabajaron sobre un "
        "compuesto genérico sin cuestiones de PI.",
        "Dato: el número de facilitadores identificados pasó de 7 en la fase embrionaria a 17 en "
        "la de compromiso.",
        "Implicación para el formulador: un convenio con una empresa asociada incluye la "
        "cláusula de titularidad desde el inicio, aunque el acuerdo completo de PI se negocie "
        "después.",
    ],
))

L.append(pasos(
    "situacion-peru",
    "02 · Transferencia universitaria en el Perú",
    "Solicitudes, títulos, licencias y empresas derivadas de las universidades del *Perú*, 2025",
    [
        ("968 solicitudes", "Patentes y modelos de utilidad, ante el INDECOPI"),
        ("≈ 336 títulos", "Concedidos a universidades (cálculo)"),
        ("Licencias", "Sin registro público; un caso difundido (PUCP, 2021)"),
        ("Empresas derivadas", "Sin registro público"),
    ],
    clave=2,
    fuente="INDECOPI, 2026 · Energiminas, 2026 · CONCYTEC, encuesta a OTT 2024 · PUCP, 2021",
    notas=[
        "Dato: en 2025 las universidades peruanas presentaron 968 solicitudes de patente de "
        "invención y de modelo de utilidad, el 79 % de las solicitudes de residentes en el Perú y "
        "34 % más que en 2024 (Energiminas, 2026, con datos del INDECOPI).",
        "Dato: el INDECOPI otorgó 1 050 títulos en 2025; el 41 % fue para solicitantes "
        "nacionales, y de estos el 78 % para universidades. El cálculo da unos 336 títulos "
        "universitarios (1 050 × 0,41 × 0,78).",
        "No existe un registro público de licencias universitarias. Un caso difundido es el de "
        "la PUCP, que en 2021 licenció dos patentes a Tumi Robotics; no se halló ninguno de la "
        "UNI. CONCYTEC informa que «muy pocas» instituciones transfieren por "
        "licencia o por creación de empresas de base tecnológica (encuesta de 2024).",
        "Dato: el Perú recibió US$ 30 millones de capital de riesgo en 2024, de US$ 4 500 "
        "millones en América Latina (Asociación para la Inversión de Capital Privado en América "
        "Latina, LAVCA, 2025).",
        "Error frecuente: afirmar que el 79 % de las patentes del país son universitarias; es el "
        "79 % de las solicitudes nacionales, sin contar las extranjeras.",
    ],
))

L.append(caso(
    "caso-uni",
    "02 · Caso de estudio · proyecto previo a la empresa",
    "Equipo SPT",
    "Universidad Nacional de Ingeniería · PROCIENCIA, 2025",
    [
        ("S/ 400 000", "Subvención de Emprendimiento Académico, fase 1, por 18 meses"),
        ("TRL 5–7", "Nivel exigido al postular; las bases piden subir al menos un nivel"),
        ("EBT", "Salida prevista: empresa de base tecnológica o transferencia del paquete tecnológico"),
    ],
    icono_tecnico("spt"),
    fuente="PROCIENCIA, bases E041-2025-01-BM y tabla de seleccionados",
    notas=[
        "El proyecto desarrolla un equipo de medición con tecnología propia e inteligencia "
        "artificial para medir la energía de caída del martillo en el ensayo de penetración "
        "estándar (SPT), un ensayo geotécnico de campo, con miras a su transferencia a la "
        "industria de la construcción. Responsable técnica: Carmen Eleana Ortiz Salas.",
        "El concurso Emprendimiento Académico de PROCIENCIA financia en la fase 1 la validación "
        "tecnológica y la estimación de la demanda, y en la fase 2 la preparación para la "
        "inversión. En 2025 seleccionó 8 proyectos; en 2024, 16 propuestas por "
        "S/ 6 162 017.",
        "El caso muestra el tramo anterior a la empresa: el proyecto no ha constituido una "
        "_spin-off_ y las bases exigen delimitar la PI entre la entidad proponente y las "
        "asociadas.",
        "Verificar antes de la clase: si PROCIENCIA abrió la fase 2; el calendario 2027 "
        "publicado no incluye Emprendimiento Académico (Gestión, 14 de julio de 2026).",
    ],
))

L.append(resultado_verificacion(criterios(
    "condiciones-previas",
    "02 · Condiciones previas a la transferencia",
    "Condiciones previas a la *_spin-off_* o la licencia de un resultado universitario",
    [
        ("Comunicación", "Invención comunicada a la oficina de transferencia"),
        ("Titularidad", "Titular fijado por escrito con la universidad y los socios"),
        ("Solicitud", "Patente o modelo de utilidad solicitado antes de divulgar"),
        ("Receptor", "Empresa licenciataria o equipo fundador con dedicación"),
    ],
    notas=[
        "La lista reúne cuatro condiciones: comunicación a la OTT, titularidad por escrito, "
        "solicitud antes de divulgar y un receptor identificado.",
        "Ejemplo: las redes de nylon con nanopartículas de óxidos semiconductores contra la "
        "bioincrustación, para la acuicultura de concha de abanico, de José Luis Solís Véliz "
        "(UNI), ganaron el concurso de Desarrollo Tecnológico 2023-03 de PROCIENCIA con "
        "S/ 350 000 (PROCIENCIA, página del concurso, 2022). Si un resultado así se obtiene con equipos del laboratorio, la UNI tiene los "
        "derechos económicos (reglamento, art. 11) y 6 meses de preferencia para protegerlo "
        "(art. 29); la vía es la licencia a un fabricante de redes o a una empresa "
        "acuícola, o la _spin-off_ con acuerdo previo.",
        "Error frecuente: buscar inversionistas o fondos para la empresa antes de cumplir estas "
        "condiciones.",
    ],
), "Licencia o <i>spin-off</i>"))

L.append(recursos(
    "recursos-determinantes",
    "02 · Recursos recomendados",
    "Recursos sobre la creación de _spin-offs_ y la colaboración universidad-empresa",
    [
        {"tipo": "Libro", "titulo": "Academic Entrepreneurship: University Spinoffs and Wealth Creation",
         "autor": "Scott Shane, Edward Elgar, 2004",
         "detalle": "Factores que explican la creación de _spin-offs_ universitarias",
         "url": "doi.org/10.4337/9781843769828",
         "enlace": "https://doi.org/10.4337/9781843769828"},
        {"tipo": "Artículo", "titulo": "University spin-offs creation in the Latin American region: An exploratory study",
         "autor": "Héctor Montiel-Campos, 2018",
         "detalle": "Factores asociados a la creación de _spin-offs_ en universidades latinoamericanas",
         "url": "doi.org/10.1108/JEEE-02-2018-0011",
         "enlace": "https://doi.org/10.1108/JEEE-02-2018-0011"},
        {"tipo": "Artículo", "titulo": "Academic engagement: A review of the literature 2011-2019",
         "autor": "Perkmann et al., Research Policy, 2021",
         "detalle": "Revisión sobre la vinculación de académicos con organizaciones externas",
         "url": "doi.org/10.1016/j.respol.2020.104114",
         "enlace": "https://doi.org/10.1016/j.respol.2020.104114"},
        {"tipo": "Informe", "titulo": "ICSEd-Prodem 2021: condiciones sistémicas para el emprendimiento dinámico",
         "autor": "Kantis, Federico e Ibarra García, Prodem, 2021",
         "detalle": "Índice de condiciones para emprender por país, incluido el Perú",
         "url": "prodem.ungs.edu.ar/icsed",
         "enlace": "https://prodem.ungs.edu.ar/wp-content/uploads/2021/12/informe-2021_VF.pdf"},
    ],
    fuente=FUENTE_REC,
    notas=[
        "Shane (2004) dedica capítulos a la variación entre instituciones, el entorno, el tipo de tecnología, las industrias y las personas; la cartera de patentes y el financiamiento son una parte de esos factores. De pago: consultar en la biblioteca.",
        "Montiel-Campos (2018) estudia 52 universidades latinoamericanas: la orientación emprendedora, las incubadoras o programas de apoyo y la eficiencia del mercado de bienes se asocian con más _spin-offs_. Contrasta con el estudio británico de la clase. De pago.",
        "Perkmann et al. (2021) revisan la investigación colaborativa, por contrato y la consultoría, con sus antecedentes y efectos; acceso abierto. En el índice ICSEd-Prodem 2021 el Perú ocupa el puesto 10 de 12 en América Latina, con datos de 2020-2021.",
    ],
))

L.append(cierre(
    "sintesis-02",
    "02 · Síntesis",
    "Oficina de transferencia y *empresas de base tecnológica*",
    [
        "OTT: comunicación, protección y negociación",
        "_Deep tech_: desarrollo tras la constitución",
        "Patentes: factor más asociado a las _spin-offs_",
        "Perú: 968 solicitudes y licencias sin registro público",
    ],
    notas=[
        "Recapitular el criterio de cada término del tema 02.",
    ],
))

# ================================================================ CIERRE (5 min)

L.append(cierre(
    "sintesis-sesion",
    "Cierre",
    "Transferencia de un *resultado* universitario a una empresa",
    [
        "Vía: según el origen de los recursos y el receptor",
        "Titularidad y protección: previas a la explotación",
        "Oficina de transferencia: protección y negociación",
    ],
    ("Sesión 3", "Mapa de financiamiento e inversión"),
    notas=[
        "Recapitular los contenidos de la sesión: las vías de transferencia, la titularidad "
        "fijada por escrito, la protección solicitada antes de divulgar y la oficina que gestiona "
        "ese recorrido en la universidad.",
        "La sesión 3 trata los instrumentos públicos y los inversionistas que admite cada vía y "
        "lo que exigen a cambio.",
    ],
))

L.append(referencias(
    "fuentes",
    "Referencias de la sesión",
    [
        ("definicion-transferencia", "Congreso de la República (2021). Ley 31250, Anexo."),
        ("vias-transferencia", "Comunidad Andina (2000). Decisión 486."),
        ("licencia-o-spinoff", "Klofsten, M. y Jones-Evans, D. (2000). _Small Business Economics_, 14(4), 299-309. En Pattnaik y Pandey (2014), _TIM Review_, 4(12)."),
        ("spinoff-o-startup", "UNI (2019). Reglamento de PI, RR 1632. PROCIENCIA (2024). Emprendimiento Académico. ProActivo (2026)."),
        ("caso-hb4", "UNL (2012 y 2020). Notas sobre la tecnología HB4. CONICET (s. f.)."),
        ("documento-titularidad", "PROCIENCIA (2024). Contrato modelo E72-2024-01-BM."),
        ("regalias-universidad", "Congreso de la República (2014). Ley 30220. PUCP (2011)."),
        ("divulgacion-y-novedad", "OMPI, SCP. Plazos de gracia en las legislaciones nacionales."),
        ("caso-qaira", "OMPI (2020). Unión Andina (2022). Andina (2020)."),
        ("definicion-ott", "OMPI (s. f.). Organizaciones de transferencia de tecnología."),
        ("ruta-ott", "Bradley, S., Hayter, C. y Link, A. (2013). UNCG, Working Paper 13-10."),
        ("factores-ott", "Siegel, D., Waldman, D. y Link, A. (2003). _Research Policy_, 32(1)."),
        ("ott-peru", "Osorio, M. (2025), CONCYTEC. Maldonado, K. (2026), _El Peruano_."),
        ("deep-tech-frente-digital", "Nguyen, N., Kowalski, A. y Dzienis, A. (2024). _Sustainability_, 16(19)."),
        ("caso-tumi", "PROINNÓVATE (2026, 21 de mayo). Descubre.vc (2025). PUCP (2021)."),
        ("deeptech-region", "Peña, I. y Jenik, M. (2023). _Deep Tech: The New Wave_. BID Lab."),
        ("determinantes-spinoffs", "Odei, M. A. y Novák, P. (2022). _Economic Research-Ekonomska Istraživanja_."),
        ("barreras-colaboracion", "O’Dwyer, M., Filieri, R. y O’Malley, L. (2022). _The Journal of Technology Transfer_."),
        ("situacion-peru", "INDECOPI (2026, 18 de febrero). Energiminas (2026, 9 de febrero)."),
        ("caso-uni", "PROCIENCIA (2025). Emprendimiento Académico E041-2025-01-BM."),
    ],
))

construir("clase-02", "Sesión 2 · Startups, spin-offs y transferencia", L)
