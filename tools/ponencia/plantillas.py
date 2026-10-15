"""Plantillas de lámina de la 11.ª edición (formato ponencia · «Mezcla A + C»).

Dos modos de lámina, decididos por la plantilla:

  · BASE (estilo C, «Ingeniería ilustrada»): papel de dibujo con retícula
    milimetrada, marco con zonas, marcas de registro y cajetín técnico
    (OTI·UNI · I+D+i+e S<n> · Lámina NN/TT; el número de sesión sale del nombre de la clase). En tema oscuro, plano nocturno
    tipo blueprint. Plantillas: visual, criterios (alias circuito), tarjetas,
    duo, pasos, caso, agenda, cierre, recursos, referencias.
  · IMPACTO (estilo A, «Keynote oscuro»): noche azul, halos, grano y brillo
    en el dato. Siempre oscuras. Plantillas: portada, seccion (halo azul),
    cifra, frase, pregunta (halo rojo y cronómetro) y la variante de
    votación de `tarjetas`.

Reglas del sistema (ver src/css/ponencia.css):
  · una idea por lámina; el texto largo va en `notas` (tecla N);
  · un solo acento rojo protagonista: lo que va entre *asteriscos*, salvo que
    la evidencia ya lleve el rojo (clase `es-clave`): entonces el titular
    queda en tinta;
  · la fuente es una línea corta en el pie; la referencia completa, al final.

Todas las medidas son px de un lienzo fijo de 1600 × 900 que se escala entero
a la ventana (variable --s, que fija un script mínimo en cada lámina).
"""

from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from graficos import barras_svg, criterios_svg, ico, regla_pregunta

RAIZ = Path(__file__).resolve().parents[2]

IMPACTO = {"portada", "seccion", "cifra", "frase", "pregunta", "votacion"}


@dataclass
class Lamina:
    slug: str
    clase: str
    cuerpo: str
    titulo: str
    fuente: str = ""
    notas: list[str] = field(default_factory=list)
    modo: str = ""

    def __post_init__(self):
        if not self.modo:
            self.modo = "impacto" if self.clase in IMPACTO else "base"


# ------------------------------------------------------------------ texto


def t(s: str) -> str:
    """Escapa y convierte *palabra* en el acento rojo de la lámina."""
    s = html.escape(s, quote=False)
    s = s.replace("__", "\x00")  # casilla para rellenar en la ficha
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"_(.+?)_", r"<i>\1</i>", s)
    s = re.sub(r"\{(.+?)\}", r'<span class="nc">\1</span>', s)
    # Espacio fino de no separación entre la cifra y su unidad.
    s = re.sub(r"(\d) (%|kg|millones)", "\\1\u202f\\2", s)
    s = s.replace("\x00", '<span class="blanco" aria-label="espacio para completar"></span>')
    return s


def plano(s: str) -> str:
    return re.sub(r"[*_{}]", "", s)


def _in(i: int) -> str:
    return f'data-in style="--i:{i}"'


def _ceja(s: str, i: int = 0, cls: str = "ceja") -> str:
    return f'<p class="{cls}" {_in(i)}><span>{t(s)}</span></p>' if s else ""


def _cab(eyebrow: str, titular: str, extra: str = "") -> str:
    return (
        f'<header class="cab">{_ceja(eyebrow)}'
        f'<h1 class="titular" {_in(1)}>{t(titular)}</h1>{extra}</header>'
    )


def _zona(contenido: str, cls: str = "") -> str:
    return f'<div class="zona {cls}">{contenido}</div>'


def _halos(*specs) -> str:
    """specs: (color, x, y, ancho, alto) en px del lienzo."""
    return "".join(
        f'<div class="halo halo--{c}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>'
        for c, x, y, w, h in specs
    )


def _bloque(s: str) -> str:
    """Envuelve en <span> un texto con marcas (cursiva, acento) que va dentro
    de un contenedor flex o grid: sin el envoltorio, cada <i> sería un
    elemento aparte de la rejilla y partiría la línea. El texto sin marcas
    queda igual (las sesiones 1 a 5 no cambian)."""
    return f"<span>{s}</span>" if "<" in s else s


def _sigla(s: str) -> str:
    return s.replace("I+D+i+e", '<span class="sigla">I+D+i+e</span>', 1)


# -------------------------------------------------------- impacto (A)


def portada(slug, sesion, titulo, subtitulo, temas, autor, visual="", notas=()):
    temas_html = "".join(f"<li><b>{n:02d}</b>{_bloque(t(x))}</li>" for n, x in enumerate(temas, 1))
    cuerpo = (
        _halos(("azul", -260, -260, 1100, 820), ("rojo", 1080, 120, 560, 620))
        + visual
        + '<div class="portada">'
        + _ceja(sesion)
        + f'<h1 class="display" {_in(1)}>{_sigla(t(titulo))}</h1>'
        + f'<p class="lead" {_in(2)}>{t(subtitulo)}</p>'
        + f'<ol class="portada__temas" {_in(3)}>{temas_html}</ol>'
        + f'<p class="credito" {_in(4)}>{t(autor)}</p>'
        + "</div>"
    )
    return Lamina(slug, "portada", cuerpo, plano(titulo), "", list(notas))


def seccion(slug, numero, titulo, promesa="", notas=(), temas=2):
    """`temas`: número de temas de la sesión que muestra la pista (2 en las
    sesiones 1 a 5; 1 en la sesión 6, de un solo tema)."""
    n = int(numero) if str(numero).isdigit() else 1
    # Un título con una palabra muy larga («Institucionalidad») no puede
    # partirse y, a 108 px, invade el número decorativo: se reduce el cuerpo.
    largo = max((len(p) for p in plano(titulo).split()), default=0) >= 15
    pista = "".join(
        f'<li class="{"es-actual" if k == n else ""}"><span></span>{k:02d}</li>' for k in range(1, temas + 1)
    )
    cuerpo = (
        _halos(("azul", -200, -240, 1200, 900), ("azul", 900, 260, 900, 760))
        + f'<p class="seccion__num" aria-hidden="true" {_in(0)}>{t(numero)}</p>'
        + f'<div class="seccion{" seccion--largo" if largo else ""}">'
        + f'<h1 class="display" {_in(1)}>{t(titulo)}</h1>'
        + (f'<p class="lead" {_in(2)}>{t(promesa)}</p>' if promesa else "")
        + f'<ol class="pista" {_in(3)}>{pista}</ol>'
        + "</div>"
    )
    return Lamina(slug, "seccion", cuerpo, plano(titulo), "", list(notas))


def _instrumento_cifra(valor: str, unidad: str, lectura: str) -> str:
    """Panel de vidrio que mide la cifra: 1 000 puntos para un %, o la
    comparación de dos barras para un múltiplo (×N)."""
    v = valor.replace(",", ".").replace("\u202f", "")
    if unidad.strip() == "%":
        try:
            n = round(float(v) * 10)
        except ValueError:
            return ""
        cols, filas, p = 40, 25, 11
        pts = []
        for k in range(cols * filas):
            f, c = divmod(k, cols)
            x, y = 14 + c * p, 14 + f * p
            if k < n:
                pts.append(f'<circle class="pt pt--on" cx="{x}" cy="{y}" r="3.6" style="--k:{k}"/>')
            else:
                pts.append(f'<circle class="pt" cx="{x}" cy="{y}" r="2.2"/>')
        w, h = 28 + (cols - 1) * p, 28 + (filas - 1) * p
        return (
            f'<div class="instrumento vidrio" {_in(3)}><svg viewBox="0 0 {w} {h}" class="puntos" aria-hidden="true">'
            f'{"".join(pts)}</svg><p class="instrumento__ley">1 punto = 0,1 %</p></div>'
        )
    m = re.match(r"[×x](\d+)", v)
    if m:
        k = int(m.group(1))
        anios = re.findall(r"\b(19\d\d|20\d\d)\b", lectura)
        a0, a1 = (anios + ["", ""])[:2]
        u = 120
        barras = (
            f'<text class="i-etq" x="0" y="54">{a0}</text>'
            f'<rect class="i-barra" x="110" y="26" width="{u}" height="40" rx="3"/>'
            f'<text class="i-etq i-etq--on" x="0" y="164">{a1}</text>'
            f'<rect class="i-barra i-barra--on" x="110" y="136" width="{u * k}" height="40" rx="3"/>'
        )
        guias = "".join(
            f'<path class="i-guia" d="M{110 + u * j} 96V194"/>' for j in range(1, k)
        )
        cota = (
            f'<path class="i-cota" d="M110 226H{110 + u * k}M110 216V236M{110 + u * k} 216V236"/>'
            f'<text class="i-cota-t" x="{110 + u * k / 2}" y="262" text-anchor="middle">{html.escape(valor)}</text>'
        )
        return (
            f'<div class="instrumento vidrio" {_in(3)}><svg viewBox="0 0 {130 + u * k} 280" class="multiplo" '
            f'aria-hidden="true">{barras}{guias}{cota}</svg></div>'
        )
    return ""


def cifra(slug, eyebrow, valor, unidad, lectura, contexto="", fuente="", oscuro=False, notas=()):
    u = f"<small>{t(unidad)}</small>" if unidad else ""
    inst = _instrumento_cifra(valor, unidad, lectura)
    cuerpo = (
        _halos(("azul", -240, -260, 1000, 760), ("rojo", 40, 180, 760, 560))
        + _ceja(eyebrow, 0, "ceja ceja--luz")
        + f'<div class="cifra-blk{" cifra-blk--solo" if not inst else ""}">'
        + f'<p class="cifra es-clave" {_in(1)}>{t(valor)}{u}</p>'
        + f'<p class="lead" {_in(2)}>{t(lectura)}</p>'
        + (f'<p class="cifra__contexto" {_in(3)}>{t(contexto)}</p>' if contexto else "")
        + "</div>"
        + inst
    )
    titulo = " ".join(x for x in (valor, unidad, lectura) if x)
    return Lamina(slug, "cifra", cuerpo, plano(titulo), fuente, list(notas))


def frase(slug, eyebrow, texto, autor="", fuente="", notas=()):
    grande = " frase--grande" if len(plano(texto)) <= 64 else ""
    cuerpo = (
        _halos(("azul", -260, -280, 1100, 800), ("rojo", 980, 420, 700, 560))
        + _ceja(eyebrow, 0, "ceja ceja--luz")
        + f'<figure class="frase-blk{grande}" {_in(1)}>'
        + '<span class="reg reg--a"></span><span class="reg reg--b"></span>'
        + f'<blockquote class="frase">{t(texto)}</blockquote>'
        + (f'<figcaption class="frase__autor">{t(autor)}</figcaption>' if autor else "")
        + "</figure>"
    )
    return Lamina(slug, "frase", cuerpo, plano(texto), fuente, list(notas))


def _cronometro(minutos: int, i: int) -> str:
    r = 128
    marcas = []
    import math

    for k in range(60):
        a = math.radians(k * 6 - 90)
        r0 = r - (14 if k % 5 == 0 else 7)
        marcas.append(
            f"M{160 + math.cos(a) * r0:.1f} {160 + math.sin(a) * r0:.1f}L{160 + math.cos(a) * r:.1f} {160 + math.sin(a) * r:.1f}"
        )
    seg = minutos * 60
    return (
        f'<button type="button" class="crono" data-segundos="{seg}" {_in(i)} '
        f'aria-label="Cronómetro de {minutos} minutos; se inicia o se detiene con un clic o con la tecla C">'
        '<svg viewBox="0 0 320 320" aria-hidden="true">'
        f'<circle class="crono__pista" cx="160" cy="160" r="{r + 14}"/>'
        f'<circle class="crono__arco" cx="160" cy="160" r="{r + 14}" pathLength="1000" transform="rotate(-90 160 160)"/>'
        f'<path class="crono__marcas" d="{"".join(marcas)}"/></svg>'
        f'<span class="crono__t">{minutos:02d}:00</span><span class="crono__u">min · C</span></button>'
    )


def pregunta(slug, eyebrow, texto, instruccion="", notas=(), regla_trl=False):
    m = re.search(r"(\d+)\s*minutos?", eyebrow)
    minutos = int(m.group(1)) if m else 0
    cuerpo = (
        _halos(("rojo", 820, 120, 900, 760), ("azul", -300, -300, 1000, 700))
        + f'<p class="chip vidrio" {_in(0)}>{ico("clock", "chip__ico")}<span>{t(eyebrow)}</span></p>'
        + '<div class="pregunta-blk">'
        + f'<h1 class="pregunta" {_in(1)}>{t(texto)}</h1>'
        + (f'<p class="pregunta__sub" {_in(2)}>{t(instruccion)}</p>' if instruccion else "")
        + "</div>"
        + (_cronometro(minutos, 3) if minutos else "")
        + (f'<div class="regla-q" {_in(4)}>{regla_pregunta()}</div>' if regla_trl else "")
    )
    lam = Lamina(slug, "pregunta", cuerpo, plano(texto), "", list(notas))
    if regla_trl:
        lam.cuerpo = lam.cuerpo.replace('class="crono"', 'class="crono crono--alto"')
    return lam


# ------------------------------------------------------------ base (C)


def tarjetas(slug, eyebrow, titular, items, clave=None, numerar=True, fuente="", notas=(),
             iconos=None, estilo=""):
    """Fichas técnicas. items: (titulo, descripcion). `clave`: índice en rojo.
    `iconos`: nombres de public/course-icons.svg, uno por ficha.
    estilo="votacion": lámina de impacto; el titular «1 X · 2 Y…» se dibuja
    como teclas de voto y las fichas se rotulan A, B, C…"""
    if estilo == "votacion":
        return _votacion(slug, eyebrow, titular, items, fuente, notas)
    cards = []
    for i, (tt, dd) in enumerate(items):
        cls = "ficha"
        if i == clave:
            cls += " ficha--clave es-clave"
        if re.match(r"^[−\-+×\d]", tt):
            cls += " ficha--cifra"
        n = f'<span class="ficha__n">{i + 1:02d}</span>' if numerar else f'<span class="ficha__n">{chr(65 + i)}</span>'
        ic = ico(iconos[i], "ficha__ico") if iconos and i < len(iconos) and iconos[i] else ""
        d = f'<p class="ficha__d">{t(dd)}</p>' if dd else ""
        cards.append(
            f'<div class="{cls}" {_in(i + 2)}><div class="ficha__cab">{n}{ic}</div>'
            f'<p class="ficha__t">{t(tt)}</p>{d}</div>'
        )
    cuerpo = _cab(eyebrow, titular) + _zona(
        f'<div class="fichas" style="--n:{len(items)}">{"".join(cards)}</div>'
    )
    return Lamina(slug, "tarjetas", cuerpo, plano(titular), fuente, list(notas))


def _votacion(slug, eyebrow, titular, items, fuente, notas):
    opciones = re.findall(r"(\d)\s+([^·]+)", titular)
    teclas = "".join(
        f'<span class="tecla" {_in(k + 1)}><b>{n}</b><span>{t(x.strip())}</span></span>'
        for k, (n, x) in enumerate(opciones)
    )
    cards = "".join(
        f'<div class="caso-v vidrio" {_in(i + 6)}><p class="caso-v__l">{chr(65 + i)}</p>'
        f'<p class="caso-v__t">{t(tt)}</p><p class="caso-v__d">{t(dd)}</p></div>'
        for i, (tt, dd) in enumerate(items)
    )
    cuerpo = (
        _halos(("rojo", 300, -380, 1100, 700), ("azul", -300, 400, 1000, 700))
        + f'<p class="chip vidrio" {_in(0)}>{ico("users", "chip__ico")}<span>{t(eyebrow)}</span></p>'
        + f'<h1 class="teclas es-clave">{teclas}</h1>'
        + f'<div class="casos-v" style="--n:{len(items)}">{cards}</div>'
    )
    return Lamina(slug, "votacion", cuerpo, plano(titular), fuente, list(notas))


def duo(slug, eyebrow, titular, a, b, fuente="", notas=()):
    """a, b: dict con cab, t, y opcionalmente d (texto) o items (lista)."""

    def lado(x, cls, letra, i):
        extra = ""
        if x.get("d"):
            extra = f'<p class="duo__d">{t(x["d"])}</p>'
        if x.get("items"):
            extra += '<ul class="duo__items">' + "".join(f"<li>{t(it)}</li>" for it in x["items"]) + "</ul>"
        return (
            f'<div class="duo__lado duo__lado--{cls}" {_in(i)}>'
            f'<p class="duo__cab"><span class="globo">{letra}</span>{t(x["cab"])}</p>'
            f'<div class="duo__cuerpo"><p class="duo__t">{t(x["t"])}</p>{extra}</div></div>'
        )

    cuerpo = _cab(eyebrow, titular) + _zona(
        '<div class="duo">' + lado(a, "a", "A", 2)
        + f'<div class="duo__eje" {_in(3)}><span>≠</span></div>'
        + lado(b, "b", "B", 4) + "</div>"
    )
    return Lamina(slug, "duo", cuerpo, plano(titular), fuente, list(notas))


def pasos(slug, eyebrow, titular, items, clave=None, marcas=None, fuente="", notas=()):
    """Diagrama de flujo de proceso. items: (titulo, descripcion)."""
    ps = []
    for i, (tt, dd) in enumerate(items):
        cls = "paso paso--clave es-clave" if i == clave else "paso"
        marca = marcas[i] if marcas else f"{i + 1:02d}"
        d = f'<p class="paso__d">{t(dd)}</p>' if dd else ""
        ps.append(
            f'<div class="{cls}" {_in(i + 2)}><p class="paso__n{" paso__n--letra" if marcas else ""}">{t(marca)}</p>'
            f'<p class="paso__ref">{"P" if not marcas else "F"}-{i + 1:02d}</p>'
            f'<p class="paso__t">{t(tt)}</p>{d}</div>'
        )
    cuerpo = _cab(eyebrow, titular) + _zona(
        f'<div class="pasos" style="--n:{len(items)}">{"".join(ps)}</div>'
    )
    return Lamina(slug, "pasos", cuerpo, plano(titular), fuente, list(notas))


def visual(slug, eyebrow, titular, svg, lado=None, fuente="", notas=()):
    """Titular-afirmación + una evidencia dibujada en coordenadas de lámina."""
    cuerpo = _cab(eyebrow, titular) + f'<div class="evidencia" {_in(2)}>{svg}</div>'
    return Lamina(slug, "visual", cuerpo, plano(titular), fuente, list(notas))


def criterios(slug, eyebrow, titular, items, fuente="", notas=()):
    """Criterios que deben cumplirse a la vez: lista de verificación
    (criterio × descripción × casilla) cuyas filas agrupa una llave que
    conduce al resultado. items: (nombre, descripcion)."""
    cuerpo = _cab(eyebrow, titular) + f'<div class="evidencia" {_in(2)}>{criterios_svg(items)}</div>'
    return Lamina(slug, "visual", cuerpo, plano(titular), fuente, list(notas))


# Nombre anterior, que conserva clase-01.py (antes se dibujaba un circuito).
circuito = criterios


# Icono de public/course-icons.svg según el tipo de recurso.
ICONO_RECURSO = {
    "sitio web": "globe",
    "libro": "book",
    "artículo": "paper",
    "articulo": "paper",
    "informe": "file",
    "guía": "rubric",
    "guia": "rubric",
    "base de datos": "chart",
}


def _qr(enlace: str, lado: int) -> str:
    """Código QR del enlace como SVG en línea. Módulos y fondo salen de
    variables CSS (--qr-mod, --qr-fondo), así que el mismo código se lee en
    el papel y en el plano nocturno; el fondo es siempre claro para que el
    código no quede invertido (algunas cámaras no leen QR en negativo)."""
    import segno

    qr = segno.make(enlace, error="m", micro=False)
    borde = 2
    filas = list(qr.matrix_iter(border=borde))
    n = len(filas)
    trazo = []
    for y, fila in enumerate(filas):
        x = 0
        while x < n:
            if fila[x]:
                x0 = x
                while x < n and fila[x]:
                    x += 1
                trazo.append(f"M{x0} {y}h{x - x0}v1h{x0 - x}z")
            else:
                x += 1
    return (
        f'<svg class="qr" viewBox="0 0 {n} {n}" width="{lado}" height="{lado}" '
        f'shape-rendering="crispEdges" role="img" aria-label="Código QR de {html.escape(enlace)}">'
        f'<rect class="qr__fondo" width="{n}" height="{n}"/>'
        f'<path class="qr__mod" d="{"".join(trazo)}"/></svg>'
    )


def _url_corta(url: str) -> str:
    """Permite el corte de línea tras «/», «.», «-» y «_» (sin partir palabras)."""
    s = html.escape(url, quote=False)
    return re.sub(r"([/._-])", r"\1<wbr>", s)


def recursos(slug, eyebrow, titular, items, fuente="", notas=()):
    """Recursos recomendados al cierre de una unidad (lámina BASE).

    items: 3 o 4 dict con las claves
      tipo     «Sitio web», «Libro», «Artículo», «Informe», «Guía» o «Base de datos»
      titulo   título del recurso
      autor    autor o institución y año
      detalle  una línea de descripción (máx. 14 palabras)
      url      URL corta que se muestra
      enlace   URL completa (destino del enlace y del código QR)
    Cada recurso es un renglón de una lista técnica (filetes, como una lista
    de piezas): número, icono y tipo; título, descripción, autor y URL; y el
    código QR, legible desde el aula. Título, URL y QR son enlaces que se
    abren en otra pestaña."""
    n = len(items)
    if not 3 <= n <= 4:
        raise ValueError(f"{slug}: recursos() admite 3 o 4 recursos, no {n}")
    lado = 122 if n == 4 else 150
    fichas = []
    for i, it in enumerate(items):
        tipo = it["tipo"]
        enlace = it["enlace"]
        a = f'href="{html.escape(enlace)}" target="_blank" rel="noopener"'
        icono = ICONO_RECURSO.get(tipo.strip().lower(), "link")
        fichas.append(
            f'<article class="rec" {_in(i + 2)}>'
            '<div class="rec__id"><div class="rec__id-l">'
            f'<span class="ficha__n">{i + 1:02d}</span>{ico(icono, "rec__ico")}</div>'
            f'<p class="rec__tipo">{t(tipo)}</p></div>'
            '<div class="rec__txt">'
            f'<h2 class="rec__t"><a {a}>{t(it["titulo"])}</a></h2>'
            f'<p class="rec__d">{t(it["detalle"])}</p>'
            f'<p class="rec__meta"><span class="rec__autor">{t(it["autor"])}</span>'
            f'<a class="rec__url" {a}>{ico("link", "rec__url-ico")}<span>{_url_corta(it["url"])}</span></a></p>'
            "</div>"
            f'<a class="rec__qr" {a} tabindex="-1">{_qr(enlace, lado)}</a>'
            "</article>"
        )
    cuerpo = _cab(eyebrow, titular) + (
        f'<div class="recursos" style="--n:{n}">{"".join(fichas)}</div>'
    )
    return Lamina(slug, "recursos", cuerpo, plano(titular), fuente, list(notas))


def caso(slug, eyebrow, nombre, quien, datos, icono_svg, fuente="", notas=()):
    """datos: lista de (cifra, explicacion). El último dato es el desenlace."""
    ds = "".join(
        f'<li class="hito{" hito--clave es-clave" if k == len(datos) - 1 else ""}" {_in(k + 3)}>'
        f"<b>{t(c)}</b><span>{t(x)}</span></li>"
        for k, (c, x) in enumerate(datos)
    )
    cuerpo = (
        '<header class="cab cab--caso">' + _ceja(eyebrow)
        + f'<h1 class="titular titular--caso" {_in(1)}>{t(nombre)}</h1>'
        + f'<p class="caso__quien" {_in(2)}>{t(quien)}</p></header>'
        + f'<ol class="hitos">{ds}</ol>'
        + f'<div class="detalle" {_in(2)}><span class="detalle__tag">A</span>{icono_svg}</div>'
    )
    return Lamina(slug, "caso", cuerpo, plano(nombre), fuente, list(notas))


def _franja(franja, i):
    if not franja:
        return ""
    return (
        f'<p class="franja" {_in(i)}><b>{t(franja[0])}</b><span>{t(franja[1])}</span></p>'
    )


def agenda(slug, eyebrow, titular, bloques, franja=None, notas=()):
    """bloques: lista de (titulo, [items]). Con un solo bloque (sesión 6, sin
    receso), el bloque ocupa el ancho completo y sus puntos van en dos
    columnas."""
    bs = []
    for i, (tt, items) in enumerate(bloques):
        li = "".join(f"<li><b>{i + 1}.{k + 1}</b>{_bloque(t(x))}</li>" for k, x in enumerate(items))
        bs.append(
            f'<div class="bloque-ag" {_in(i + 2)}><p class="bloque-ag__n">{i + 1:02d}</p>'
            f'<div><p class="bloque-ag__t">{t(tt)}</p><ul class="bloque-ag__lista">{li}</ul></div></div>'
        )
    cuerpo = (
        _cab(eyebrow, titular)
        + _zona(
            f'<div class="agenda">{"".join(bs)}</div>' if len(bloques) > 1 else
            '<div class="agenda" style="grid-template-columns:1fr">'
            + "".join(bs).replace('class="bloque-ag__lista"',
                                  'class="bloque-ag__lista" style="grid-template-columns:1fr 1fr;column-gap:48px"')
            + "</div>",
            "zona--con-franja")
        + _franja(franja, len(bloques) + 2).replace('class="franja"', 'class="franja franja--clave es-clave"')
    )
    return Lamina(slug, "agenda", cuerpo, plano(titular), "", list(notas))


def cierre(slug, eyebrow, titular, ideas, franja=None, notas=()):
    li = "".join(
        f'<li {_in(i + 2)}><b>{i + 1:02d}</b><span>{t(x)}</span><i class="casilla"></i></li>'
        for i, x in enumerate(ideas)
    )
    cuerpo = (
        _cab(eyebrow, titular)
        + _zona(f'<ol class="llevar">{li}</ol>', "zona--con-franja" if franja else "")
        + _franja(franja, len(ideas) + 2)
    )
    return Lamina(slug, "cierre", cuerpo, plano(titular), "", list(notas))


def referencias(slug, titular, refs, notas=()):
    """refs: lista de (slug de la lámina que la cita, texto APA). El slug se
    sustituye por el número real de lámina al construir."""
    li = "".join(f"<li><b>§{s}§</b><span>{t(x)}</span></li>" for s, x in refs)
    cuerpo = _cab("Fuentes", titular) + f'<ol class="refs" {_in(2)}>{li}</ol>'
    return Lamina(slug, "refs", cuerpo, plano(titular), "", list(notas))


# ------------------------------------------------------------ gráficos


def barras(datos, maximo=None, ancho=None, fila=None, etq_w=None, unidad="", decimales=2,
           guia=None, nota=None):
    """Barras con espesor sobre regla milimetrada (ver graficos.barras_svg).
    datos: (etiqueta, valor, rol) con rol en {"", "clave", "ref"}."""
    return barras_svg(datos, unidad, decimales, guia, None)


# ---------------------------------------------------------------- hoja


def _hoja() -> str:
    def T(x, y, s):
        return f'<text class="zona-t" x="{x}" y="{y}" text-anchor="middle">{s}</text>'

    z = []
    for i in range(8):
        cx = 40 + 190 * i + 95
        z += [T(cx, 32, i + 1), T(cx, 878, i + 1)]
        if i:
            x = 40 + 190 * i
            z.append(f'<path class="marco-t" d="M{x} 16V40M{x} 860V884"/>')
    for i, letra in enumerate("ABCD"):
        cy = 40 + 205 * i + 102.5
        z += [T(28, cy + 4, letra), T(1572, cy + 4, letra)]
        if i:
            y = 40 + 205 * i
            z.append(f'<path class="marco-t" d="M16 {y}H40M1560 {y}H1584"/>')

    def reg(x, y):
        return (
            f'<g class="registro"><circle cx="{x}" cy="{y}" r="9"/>'
            f'<path d="M{x - 15} {y}H{x + 15}M{x} {y - 15}V{y + 15}"/></g>'
        )

    return (
        '<svg class="hoja" viewBox="0 0 1600 900" aria-hidden="true"><defs>'
        '<pattern id="g-menor" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" class="g1"/></pattern>'
        '<pattern id="g-mayor" width="100" height="100" patternUnits="userSpaceOnUse">'
        '<rect width="100" height="100" fill="url(#g-menor)"/><path d="M100 0H0V100" class="g2"/></pattern></defs>'
        '<rect x="40" y="40" width="1520" height="820" fill="url(#g-mayor)"/>'
        '<rect class="marco-ext" x="16" y="16" width="1568" height="868"/>'
        '<rect class="marco-int" x="40" y="40" width="1520" height="820"/>'
        + "".join(z) + reg(40, 40) + reg(1560, 40) + reg(40, 860) + "</svg>"
    )


HOJA = _hoja()


def _cajetin(num: int, total: int, sesion: int = 1) -> str:
    return (
        '<div class="cajetin" aria-hidden="true">'
        "<div><span>Entidad</span><b>OTI · UNI</b></div>"
        f'<div><span>Curso</span><b>I+D+i+e · S{sesion}</b></div>'
        f"<div><span>Lámina</span><b>{num:02d} / {total:02d}</b></div></div>"
    )


# ---------------------------------------------------------------- escritura

FUENTES = (
    "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700"
    "&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap"
)

DOC = """<!doctype html>
<html lang="es">
	<head>
		<meta charset="UTF-8" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>{titulo_doc}</title>
		<link rel="preconnect" href="https://fonts.googleapis.com" />
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
		<link href="{fuentes}" rel="stylesheet" />
		<link rel="stylesheet" href="../../css/ponencia.css" />
	</head>
	<body data-deck-total="{total}" class="modo-{modo}">
		<main class="pz pz--{clase} pz--{modo}" aria-label="Lámina {num} de {total}">
			<div class="pz__lienzo">
				{fondo}
				{cuerpo}
				<footer class="pz__pie">{fuente}{sello}</footer>
			</div>
		</main>
		<script>(function(){{var r=document.documentElement;function a(){{r.style.setProperty("--s",Math.min(innerWidth/1600,innerHeight/900))}}a();addEventListener("resize",a)}})();</script>
		<aside class="pz__notas">{notas}</aside>
		<nav class="slide-nav" aria-label="Navegación">
			<a class="slide-nav__link" href="{prev}" aria-label="Anterior"><svg class="icon" aria-hidden="true"><use href="/course-icons.svg#i-arrow-left" /></svg><span>Anterior</span></a>
			<a class="slide-nav__link" href="{next}" aria-label="Siguiente"><svg class="icon" aria-hidden="true"><use href="/course-icons.svg#i-arrow-right" /></svg><span>Siguiente</span></a>
		</nav>
		<script type="module" src="../../js/ponencia.js"></script>
	</body>
</html>
"""


def construir(clase: str, nombre_sesion: str, laminas: list[Lamina]) -> None:
    destino = RAIZ / "src" / "slides" / clase
    if destino.exists():
        shutil.rmtree(destino)
    destino.mkdir(parents=True)

    archivos = [f"{i:02d}-{lam.slug}.html" for i, lam in enumerate(laminas, 1)]
    total = len(laminas)
    numero = {lam.slug: f"{i:02d}" for i, lam in enumerate(laminas, 1)}
    for lam in laminas:
        for slug, n in numero.items():
            lam.cuerpo = lam.cuerpo.replace(f"§{slug}§", n)
        if lam.clase == "refs":
            # Las referencias se listan en el orden en que aparecen en el mazo.
            items = re.findall(r"<li>.*?</li>", lam.cuerpo)
            orden = sorted(items, key=lambda li: re.search(r"<b>(\d+)</b>", li).group(1))
            lam.cuerpo = lam.cuerpo.replace("".join(items), "".join(orden))
        if "§" in lam.cuerpo:
            raise SystemExit(f"{lam.slug}: referencia a una lámina que no existe")
    for i, (lam, arch) in enumerate(zip(laminas, archivos)):
        prev = archivos[i - 1] if i > 0 else "/index.html"
        nxt = archivos[i + 1] if i + 1 < total else "/index.html"
        notas = "".join(f"<p>{t(n)}</p>" for n in lam.notas)
        fuente = (
            f'<p class="fuente"><span>Fuente</span>{t(lam.fuente)}</p>' if lam.fuente else ""
        )
        if lam.modo == "base":
            fondo, sello = HOJA, _cajetin(i + 1, total, int(re.sub(r"\D", "", clase) or 1))
        else:
            fondo = '<div class="noche" aria-hidden="true"></div>'
            sello = "" if lam.clase == "portada" else (
                f'<p class="folio" aria-hidden="true"><span>{i + 1:02d}</span> / {total:02d}</p>'
            )
        (destino / arch).write_text(
            DOC.format(
                titulo_doc=html.escape(f"{nombre_sesion} · {lam.titulo}"),
                fuentes=FUENTES,
                total=total,
                clase=lam.clase,
                modo=lam.modo,
                num=i + 1,
                fondo=fondo,
                cuerpo=lam.cuerpo,
                fuente=fuente,
                sello=sello,
                notas=notas,
                prev=prev,
                next=nxt,
            ),
            encoding="utf-8",
        )
    print(f"{total} láminas escritas en {destino.relative_to(RAIZ)}")
