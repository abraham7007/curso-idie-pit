# Diseño y Gestión de Proyectos I+D+i+e · 11.ª edición

## Formato ponencia (rediseño en curso, octubre de 2026)

La 10.ª edición resultó pesada: unas 150 palabras por lámina, recuadros que
decían lo que el docente debía decir y conceptos repetidos entre sesiones. La
11.ª edición rehace el curso como **ponencia**: una idea por lámina, titular
corto que afirma algo, un solo acento rojo, gráficos simples y el texto de
apoyo en las **notas del docente** (tecla **N**).

| Sesión | Estado |
|---|---|
| 1 · Fundamentos y ecosistema | **Rediseñada** · 39 láminas · sesión expositiva, sin actividades · 6 láminas de recursos recomendados con QR · `tools/ponencia/clase-01.py` |
| 2 · *Startups*, *spin-offs* y transferencia | **Rediseñada** · 40 láminas · sesión expositiva · 6 láminas de recursos con QR · `tools/ponencia/clase-02.py` |
| 3 · Mapa de financiamiento e inversión | **Rediseñada** · 38 láminas · sesión expositiva · 6 láminas de recursos con QR · `tools/ponencia/clase-03.py` |
| 4 · Formulación de proyectos | **Rediseñada** · 40 láminas · sesión expositiva · 6 láminas de recursos con QR · `tools/ponencia/clase-04.py` |
| 5 · Del proyecto ganado al resultado transferido | **Rediseñada** · 40 láminas · sesión expositiva · 6 láminas de recursos con QR · `tools/ponencia/clase-05.py` |
| 6 · Pitch y sustentación de proyectos | **Rediseñada** · 24 láminas · bloque único de 90 min · 3 láminas de recursos con QR · `tools/ponencia/clase-06.py` |

```
src/css/ponencia.css            sistema visual nuevo (lienzo 16:9 escalable)
src/js/ponencia.js              deck.js + atajos N (notas), T (tema), Espacio
tools/ponencia/plantillas.py    12 plantillas: portada, sección, cifra, frase,
                                tarjetas, dúo, pasos, visual, caso, pregunta,
                                cierre, referencias
tools/ponencia/graficos.py      gráficos SVG en línea que siguen el tema
tools/ponencia/clase-01.py      guion de la sesión 1 (texto + notas + fuentes)

python3 tools/ponencia/clase-01.py     regenera las láminas de la sesión 1
```

Reglas del formato: titular de 12 palabras como máximo; 15 a 25 palabras
visibles por lámina (tope 40); `*palabra*` marca el único acento rojo; las
cifras llevan una línea de fuente en el pie y la referencia completa en la
última lámina, numerada automáticamente.

Redacción: registro impersonal (titulares en sintagma nominal, definiciones en
tercera persona, sin segunda persona, aforismos, metáforas ni preguntas
retóricas). Se verifica con la skill de usuario `correccion-anti-ia`:

```
python3 ~/.claude/skills/correccion-anti-ia/scripts/escanear.py tools/ponencia/clase-01.py --formato laminas --min MEDIA
```

Hallazgos que quedan y son correctos: las tres preguntas de investigación de
la lámina de tipos de I+D (ejemplos citados) y los pares «término: criterio»
de las síntesis.

El guion antiguo `tools/clases/clase-01.py` queda como referencia y está
bloqueado para que no sobrescriba la versión nueva. Las reglas de densidad de
`../METODOLOGIA.md` (40-48 láminas, dos recuadros por lámina, pie de figura)
no aplican al formato ponencia.

---

## Edición anterior (10.ª)

Curso del Programa de Iniciación Tecnológica (PIT) de la **OTI-UNI**. Esta
edición se construye en diapositivas HTML siguiendo
`../METODOLOGIA.md`. La 9na edición queda archivada en
`edicion-09/` y no se toca: es la referencia de contenido.

## Estructura de la carpeta

```
README.md                       este archivo

../METODOLOGIA.md               documento único de metodología del curso

presentar.html                  contenedor de pantalla completa
package.json  vite.config.js    servidor de desarrollo y verificadores
src/css/                        sistema de diseño (5 hojas)
src/js/                         mazo y contenedor
src/slides/clase-NN/            las láminas generadas — NO se editan a mano
src/paper/clase-NN/             los PDF de las fuentes de esa sesión
src/paper/fuentes.json          artículos: metadatos de Crossref, estado y licencia
src/paper/fuentes-externas.json los que no se pudieron descargar + fuentes
                                institucionales, con su ruta de acceso
public/                         iconos y figuras servidos en la raíz
tools/                          generador, verificadores y auditorías
tools/clases/clase-NN.py        los guiones de sesión — AQUÍ se edita

edicion-09/clases/              6 mazos .pptx + .pdf de la edición anterior
edicion-09/evaluacion/          4 quizzes + examen final (.docx y GIFT)
edicion-09/documentos/          sílabo PIT 2026 y los tres temarios

institucional/encuestas/        reporte docente junio 2026 (440 respuestas)
institucional/charlas/          ponencias externas
```

## Órdenes

```
npm run dev              servidor en http://localhost:5174
npm run check            verifica desborde, recortes, figuras y enlaces
npm run check:fullscreen verifica las dos rutas de pantalla completa
npm run figuras          regenera public/figures/*.svg
npm run audit:lexico     barrido de léxico que delata redacción automática
npm run audit:editorial  siglas, comillas, consistencia interna

python3 tools/clases/clase-01.py            regenera las láminas de la sesión 1
python3 tools/buscar-oa.py "consulta" 6     busca fuentes de acceso abierto
python3 tools/get-paper.py clase-01 DOI slug  descarga y verifica el título
```

`buscar-oa.py` consulta **título y resumen**, no el texto completo. Con el
parámetro general de OpenAlex, «national innovation system Latin America»
devolvía estudios de carga de enfermedad que contienen esas palabras sueltas
por separado.

El puerto es **5174** y no el 5173 por omisión de Vite: en esta máquina el 5173
lo ocupa el servidor del curso anterior, y con el puerto compartido el
verificador cargaba las láminas de otro curso y las daba por buenas.

Antes de capturar nada, **reiniciar el servidor** si se creó o renombró una
lámina (METODOLOGIA.md §11): el generador de estilos solo examina los archivos que
existían al arrancar.

## Diferencias respecto de la 9na edición

| | 9na edición | 10ma edición |
|---|---|---|
| Sesiones | 6 | 6 |
| Duración | 16 h · 5 sesiones de 3 h + 1 de 1 h | **18 h · 6 sesiones de 3 h** |
| Formato | PowerPoint | Diapositivas HTML verificadas |
| Sesión 6 | bloque corto de 1 h sobre pitch | **sesión completa de 3 h con dos temas: Pitch Elevator · tendencias mundiales en I+D+i+e (visión prospectiva)** |
| Práctica | ejercicios sueltos | **24 talleres de formulación numerados** |
| Fuentes | citas al pie | **6 láminas de fuente por sesión** |

## Tabla de sustituciones (METODOLOGIA.md §13)

Lo único propio del tema. Resuelta antes de escribir la primera lámina.

| Qué | En el curso de ESP32 fue | En este curso |
|---|---|---|
| Objeto central dibujado en las portadas | La placa de desarrollo | El mapa del ecosistema: academia, empresa, mercado, estado y fondos alrededor del proyecto |
| Color de acento | Rojo institucional | `#c8102e` — rojo UNI |
| Color secundario | Azul institucional | `#1f3864` — azul UNI |
| Familia monoespaciada | IBM Plex Mono | IBM Plex Mono |
| Familia de palo seco | IBM Plex Sans | IBM Plex Sans |
| Bloque de práctica | La hora del código | **Taller de formulación asistida** |
| Herramienta de proyecto | Entorno de compilación cruzada | Documento de propuesta creado desde cero |
| Herramienta de simulación | Simulador de placa | Hoja de cálculo de presupuesto y cronograma |
| Herramienta de diagramas | Pizarra de bocetos | Excalidraw · Mermaid |
| Número de sesiones | 12 | 6 |
| Temas por sesión | 2 | 2 |
| Prefijos de traza | `[ADC]`, `[FSM]`, `[MQTT]` | `[TRL]`, `[RUBRICA]`, `[PRESUP]`, `[HITO]` |
| Excepciones de la auditoría de siglas | Nombre del módulo, identificadores | Organismos, programas y normas — la lista vive en `tools/audit-editorial.py` |

### El hilo conductor de los talleres

Los 24 talleres **no se anclan a una convocatoria concreta**. El curso se llama
*Diseño y **Gestión** de Proyectos I+D+i+e*, no «formulación para el concurso X».
El hilo conductor es el **ciclo del proyecto**, aplicado a un proyecto de
investigación aplicada o formativa de nivel universitario, con equipo mixto de
alumnos y docentes — la situación real del público.

Tres reglas que se derivan de eso y que hay que respetar en cada taller:

1. **Un caso de un campo distinto en cada taller.** El público viene de muchas
   carreras; un único proyecto de ejemplo sesga el curso entero.
2. **Los criterios de las bases entran como principios generales** —qué mira un
   evaluador y por qué—, nunca como los anexos y formularios de una convocatoria.
3. **Se enseña la herramienta y qué hacer en cada paso**, no a rellenar una
   plantilla.

### Adaptaciones de la metodología que este curso impuso

1. **«La hora del código» → «Taller de formulación asistida».** El esqueleto
   de §4 no cambia —los tres entregables van antes del prompt, y «por qué se
   pide así» es lo que enseña—, pero los entregables son ficha de proyecto,
   borrador de propuesta y diagrama en vez de firmware, simulación y esquema.
2. **«Lámina de artículo» → «lámina de fuente».** Aquí las fuentes
   autorizadas no son solo artículos revisados por pares: también manuales
   metodológicos (Frascati 2015, Oslo 2018), informes de organismos (Global
   Innovation Index, BID Lab, OCDE) y bases legales de convocatoria. La
   sección central deja de llamarse «procedimiento experimental» y pasa por
   argumento: un manual no experimenta, fija una definición.
3. **Excepciones de la auditoría léxica.** «Ecosistema», «panorama»,
   «fundamental», «sustentar» y «en el marco de» son vocabulario de este campo
   y la lista cerrada los marca igual. No se han borrado de la lista —eso
   perdería el aviso cuando sí son relleno—: se informan aparte, para leerlos
   caso por caso.
4. **Seis fuentes por sesión, no tres.** La metodología fija 3 por sesión
   sobre sesiones más cortas; aquí cada sesión son 3 horas y las fuentes se
   discuten a medida que avanza el tema, repartidas entre los dos temas. La
   comprobación de cierre pasa a ser `ls src/slides/clase-NN/*fuente*.html |
   wc -l` = 6.
5. **Gamificación y temporización, fuera del mazo.** El reporte de encuestas
   pide ambas, y §8 prohíbe los cuestionarios dentro de la lámina y el
   andamiaje de tiempos en pantalla. Los cuestionarios viven en Moodle
   (`edicion-09/evaluacion/*_GIFT.txt`) y los bloques de 45-60 minutos en el
   guion del docente.

## Estado

- [x] Fase 0 · andamiaje instalado y verificado de extremo a extremo
- [x] Fase 0.1 · iconografía, auditorías, mapa del ecosistema y portada
- [x] Pasada 1 · fuentes — **cerrada**. 36 artículos revisados por pares,
      6 por sesión, verificados contra Crossref y descargados en
      `src/paper/clase-NN/`, más 5 fuentes institucionales. Cada fuente sin
      licencia Creative Commons lleva en `fuentes.json` los campos
      `licencia_verificada` y `nota_de_acceso`: cuando la copia abierta está
      en un repositorio y no en el editor, **la lámina debe enlazar al
      repositorio, no al DOI**. Otras 6 fuentes institucionales son portales
      sin PDF único y se consultan al escribir la lámina.
- [ ] Sesiones 1 a 6 · pasadas 2 a 8 de METODOLOGIA.md §10
