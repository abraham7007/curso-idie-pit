"""Gráficos SVG en línea para las láminas de ponencia («Mezcla A + C»).

Todos los gráficos de lámina se dibujan en coordenadas del lienzo de
referencia (1600 × 900): devuelven un `<svg class="fig">` que cubre la lámina
entera, de modo que 24 unidades del SVG son 24 px en la lámina. Así se
portaron tal cual las piezas del prototipo C («Ingeniería ilustrada»).

Ningún color va fijo: cada trazo y relleno sale de una clase (`.fig .xx` en
ponencia.css) que lee variables del modo de la lámina. El mismo SVG se dibuja
como plano sobre papel (tema claro), como plano nocturno tipo blueprint (tema
oscuro) o con trazo luminoso sobre la noche de las láminas de impacto.

Zona útil para la evidencia: y ≈ 300…790 (por debajo del titular y por
encima del pie con la fuente y el cajetín).
"""

from __future__ import annotations

import math
import re
from html import escape as _esc

C30 = math.cos(math.pi / 6)
S30 = 0.5


def r1(n: float) -> str:
    v = round(n * 10) / 10
    return str(int(v)) if v == int(v) else str(v)


def e(s) -> str:
    return _esc(str(s), quote=False)


def T(x, y, s, cls="", anchor="start", extra=""):
    a = "" if anchor == "start" else f' text-anchor="{anchor}"'
    return f'<text class="{cls}" x="{r1(x)}" y="{r1(y)}"{a} {extra}>{e(s)}</text>'


def pts(arr):
    return " ".join(f"{r1(x)},{r1(y)}" for x, y in arr)


def fig(cuerpo: str, html: str = "", cls: str = "") -> str:
    """Envuelve un dibujo en coordenadas de lámina (1600 × 900)."""
    svg = (
        f'<svg class="fig {cls}" viewBox="0 0 1600 900" aria-hidden="true" '
        f'preserveAspectRatio="xMidYMid meet">{cuerpo}</svg>'
    )
    return svg + (f'<div class="fig-html">{html}</div>' if html else "")


def ico(nombre: str, cls: str = "ico") -> str:
    return f'<svg class="{cls}" aria-hidden="true"><use href="/course-icons.svg#i-{nombre}"/></svg>'


# ------------------------------------------------------------ isometría


def escalera(ox, oy, w, d, hs, caras, numeros=True, num_cls=None):
    """Nueve bloques isométricos (de atrás adelante). Devuelve (svg, info, P)."""

    def P(x, y, z):
        return (ox + (x - y) * C30, oy + (x + y) * S30 - z)

    out, info = [], [None] * len(hs)
    for i in range(len(hs) - 1, -1, -1):
        h = hs[i]
        y0, y1 = -(i + 1) * w, -i * w
        ct, cf, cr = caras[i]
        top = [P(0, y0, h), P(d, y0, h), P(d, y1, h), P(0, y1, h)]
        der = [P(d, y0, 0), P(d, y1, 0), P(d, y1, h), P(d, y0, h)]
        fre = [P(0, y1, 0), P(d, y1, 0), P(d, y1, h), P(0, y1, h)]
        g = f'<g class="bloque" style="--i:{i}">'
        g += f'<polygon class="{cf}" points="{pts(fre)}"/>'
        g += f'<polygon class="{cr}" points="{pts(der)}"/>'
        g += f'<polygon class="{ct}" points="{pts(top)}"/>'
        if numeros:
            px, py = P(d, (y0 + y1) / 2, min(h - 26, 34))
            nc = (num_cls or [""] * 9)[i]
            g += (
                f'<text class="iso-num {nc}" transform="matrix({C30:.3f},{-S30},0,1,{r1(px)},{r1(py)})" '
                f'text-anchor="middle" y="10">{i + 1}</text>'
            )
        g += "</g>"
        out.append(g)
        info[i] = {
            "topFL": P(0, y1, h), "topBL": P(0, y0, h), "topFR": P(d, y1, h),
            "topC": P(d / 2, (y0 + y1) / 2, h),
        }
    return "".join(out), info, P


# ------------------------------------------------------------- portada


def peldanos():
    """Portada: la escala TRL como torre isométrica en trazo de plano sobre la
    noche; el nivel 9, en rojo encendido. Cota vertical «TRL 1 → 9»."""
    hs = [34 + 27 * i for i in range(9)]
    caras = [("p-top9", "p-fre9", "p-der9") if i == 8 else ("p-top", "p-fre", "p-der") for i in range(9)]
    svg, info, P = escalera(985, 712, 58, 96, hs, caras, numeros=False)
    piso = []
    for k in range(-1, 6):
        a, b = P(k * 40, 90, 0), P(k * 40, -9 * 58 - 70, 0)
        piso.append(f'<line class="piso" x1="{r1(a[0])}" y1="{r1(a[1])}" x2="{r1(b[0])}" y2="{r1(b[1])}"/>')
    for k in range(-1, 11):
        a, b = P(-60, -k * 58, 0), P(240, -k * 58, 0)
        piso.append(f'<line class="piso" x1="{r1(a[0])}" y1="{r1(a[1])}" x2="{r1(b[0])}" y2="{r1(b[1])}"/>')
    a, b = info[0]["topFR"], info[8]["topFR"]
    xc = 1530
    cota = (
        '<g class="cota-luz">'
        f'<path class="ext" d="M{r1(b[0] + 14)} {r1(b[1])}H{xc + 12}M{r1(a[0] + 14)} {r1(a[1])}H{xc + 12}"/>'
        f'<path d="M{xc} {r1(b[1])}V{r1(a[1])}"/>'
        f'<path d="M{xc - 7} {r1(b[1] + 14)}L{xc} {r1(b[1])}L{xc + 7} {r1(b[1] + 14)}'
        f'M{xc - 7} {r1(a[1] - 14)}L{xc} {r1(a[1])}L{xc + 7} {r1(a[1] - 14)}"/></g>'
        + T(xc + 24, (a[1] + b[1]) / 2, "TRL 1 → 9", "mono-luz", "middle",
            f'transform="rotate(-90 {xc + 24} {r1((a[1] + b[1]) / 2)})"')
    )
    nodos = "".join(
        f'<circle class="nodo-luz" cx="{r1(info[i]["topBL"][0])}" cy="{r1(info[i]["topBL"][1])}" r="4"/>'
        for i in (0, 8)
    )
    num = []
    for i in range(9):
        x, y = info[i]["topC"]
        if i in (0, 8):
            num.append(T(x, y + 6, str(i + 1), "iso-n" + (" iso-n--9" if i == 8 else ""), "middle"))
    cuerpo = (
        '<defs><radialGradient id="piso-m" cx=".45" cy=".55" r=".55">'
        '<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>'
        '<mask id="m-piso"><rect x="760" y="300" width="840" height="600" fill="url(#piso-m)"/></mask>'
        '<filter id="glow-9" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
        f'<g class="anim-fade" mask="url(#m-piso)">{"".join(piso)}</g>'
        + '<g class="torre">' + svg.replace('<g class="bloque" style="--i:8">', '<g class="bloque bloque--9" style="--i:8" filter="url(#glow-9)">') + '</g>'
        + cota + nodos + "".join(num)
    )
    return fig(cuerpo, cls="fig--portada")


# ------------------------------------------------------------- gancho


def pendiente(a_lbl, a_val, a_det, b_lbl, b_val, b_det, alto=None):
    """Dos placas de celdas (1 celda = 1 proyecto): el antes y el después."""

    def cuenta(det):
        n = [int(x) for x in re.findall(r"\d+", det)]
        return n[0], n[1]

    la, ta = cuenta(a_det)
    lb, tb = cuenta(b_det)
    cell, gap, cols = 30, 8, 12
    paso = cell + gap
    base = 712

    def placa(x0, total, llenos, cls):
        filas = math.ceil(total / cols)
        s = []
        for k in range(total):
            fila, col = divmod(k, cols)
            x, y = x0 + col * paso, base - (fila + 1) * paso + gap
            c = cls if k < llenos else "celda"
            s.append(f'<rect class="{c}" style="--k:{k}" x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2"/>')
        w, h = cols * paso - gap, filas * paso - gap
        s.append(f'<rect class="placa-marco" x="{x0 - 14}" y="{base - h - 14}" width="{w + 28}" height="{h + 28}"/>')
        return "".join(s), w, h

    def nivel(x, total, llenos, cls):
        h = math.ceil(total / cols) * paso - gap
        y_top, y_n = base - h, base - llenos / total * h
        return (
            f'<g class="nivel {cls}"><path d="M{x} {base}V{r1(y_top)}"/>'
            f'<path d="M{x - 8} {base}H{x + 8}M{x - 8} {r1(y_top)}H{x + 8}"/>'
            f'<path class="nivel-m" d="M{x - 16} {r1(y_n)}L{x - 2} {r1(y_n)}M{x - 12} {r1(y_n - 6)}L{x - 2} {r1(y_n)}L{x - 12} {r1(y_n + 6)}"/></g>'
        )

    xa, xb = 190, 930
    A, wa, ha = placa(xa, ta, la, "celda-a")
    B, wb, hb = placa(xb, tb, lb, "celda-b")
    cuerpo = (
        A + B + nivel(xa - 30, ta, la, "nivel--a") + nivel(xb - 30, tb, lb, "nivel--b")
        + T(xa - 4, 348, a_lbl, "anio")
        + T(xb - 4, 348, b_lbl, "anio anio--b")
        + f'<text class="cifra-svg cifra-svg--a" x="{xa - 8}" y="452">{a_val}<tspan class="pct" dx="8">%</tspan></text>'
        + f'<text class="cifra-svg cifra-svg--b es-clave" x="{xb - 10}" y="470">{b_val}<tspan class="pct" dx="10">%</tspan></text>'
        + T(xa - 4, base + 50, a_det, "det")
        + T(xb - 4, base + 50, b_det, "det")
        + f'<g class="salto"><path class="salto-l" d="M{xa + wa + 50} 420 C {xa + wa + 130} 420, {xb - 170} 398, {xb - 56} 398"/>'
        f'<path class="salto-p" d="M{xb - 70} 388 L{xb - 50} 398 L{xb - 70} 408"/></g>'
        + T(xb + wb + 14, base - hb - 26, "1 CELDA = 1 PROYECTO", "etq-mono", "end")
    )
    return fig(cuerpo)


# ------------------------------------------------------ cinco criterios

_CUANTOS = {2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete"}


def criterios_svg(items):
    """Lista de verificación de criterios que deben cumplirse a la vez.

    Tabla criterio × descripción con una casilla «cumple» por fila; una llave
    agrupa todas las filas y conduce al resultado («Actividad de I+D»), con
    la condición escrita tal cual: cumplimiento simultáneo de los N criterios.
    items: (nombre, descripcion)."""
    n = len(items)
    y0 = 340                      # primera fila (bajo la cabecera de columnas)
    h = min(84, 420 / n)          # alto de fila
    y1 = y0 + n * h
    yc = (y0 + y1) / 2
    # Llave «}» que agrupa las n filas y apunta al resultado.
    xb, w, rr = 1100, 30, 16
    xm, xt = xb + w / 2, xb + w
    yt, yb = y0 + 10, y1 - 10
    llave = (
        f'<path class="vf-llave" d="M{xb} {r1(yt)}Q{r1(xm)} {r1(yt)} {r1(xm)} {r1(yt + rr)}'
        f'V{r1(yc - rr)}Q{r1(xm)} {r1(yc)} {xt} {r1(yc)}Q{r1(xm)} {r1(yc)} {r1(xm)} {r1(yc + rr)}'
        f'V{r1(yb - rr)}Q{r1(xm)} {r1(yb)} {xb} {r1(yb)}"/>'
    )
    xr = 1190                     # borde izquierdo del recuadro de resultado
    flecha = (
        f'<path class="vf-flecha" d="M{xt + 10} {r1(yc)}H{xr - 8}"/>'
        f'<path class="vf-punta" d="M{xr - 22} {r1(yc - 9)}L{xr - 6} {r1(yc)}L{xr - 22} {r1(yc + 9)}"/>'
    )
    filas = []
    for i, (nom, desc) in enumerate(items):
        filas.append(
            f'<div class="vf-fila" style="height:{r1(h)}px">'
            f'<span class="vf-ref">C{i + 1}</span><b class="vf-nom">{e(nom)}</b>'
            f'<span class="vf-desc">{e(desc)}</span>'
            f'<span class="vf-casilla"><svg viewBox="0 0 36 36" aria-hidden="true">'
            f'<path class="check" style="--i:{i}" d="M8 18.5l6.5 6.5L28 10.5"/></svg></span></div>'
        )
    cuantos = _CUANTOS.get(n, str(n))
    html = (
        '<div class="verif">'
        '<div class="vf-cab"><span></span><span>Criterio</span><span>Descripción</span><span>Cumple</span></div>'
        + "".join(filas) + "</div>"
        + f'<div class="vf-res es-clave" style="top:{r1(yc - 84)}px">'
        f'<p class="vf-res__n">{n} de {n} criterios</p><p class="vf-res__t">Actividad de I+D</p></div>'
        + f'<p class="vf-cond" style="top:{r1(yc + 100)}px">Cumplimiento simultáneo de los {cuantos} criterios</p>'
    )
    return fig(f'<g class="vf-grupo">{llave}{flecha}</g>', html)


# Nombre anterior (la lámina se dibujaba como un circuito en serie).
circuito_svg = criterios_svg


# ---------------------------------------------------------- escala TRL

TRAMOS_TRL = [
    (1, 4, "Laboratorio", "De principios básicos a validación en laboratorio"),
    (5, 6, "Entorno relevante", "Validado fuera del laboratorio"),
    (7, 9, "Entorno operacional", "Sistema probado en operación"),
]


def escalera_trl(resaltar=None, alto=None):
    """Escalera isométrica de nueve niveles en tres tramos, con cotas rojas
    sobre el piso (TRL 1–4, 5–6, 7–9) y una leyenda con líneas guía."""

    def tramo(i):
        n = i + 1
        return next(k for k, (a, b, *_r) in enumerate(TRAMOS_TRL) if a <= n <= b)

    hs = [44 + 16 * i for i in range(9)]
    caras = [(f"t{tramo(i)}-top", f"t{tramo(i)}-fre", f"t{tramo(i)}-der") for i in range(9)]
    num_cls = ["iso-num--osc" if tramo(i) == 0 else "" for i in range(9)]
    w, d = 64, 104
    svg, info, P = escalera(770, 716, w, d, hs, caras, num_cls=num_cls)
    piso = []
    for k in range(-2, 7):
        a, b = P(k * 40, 120, 0), P(k * 40, -9 * w - 70, 0)
        piso.append(f'<line class="piso-c" x1="{r1(a[0])}" y1="{r1(a[1])}" x2="{r1(b[0])}" y2="{r1(b[1])}"/>')
    for k in range(-1, 11):
        a, b = P(-80, -k * w, 0), P(d + 140, -k * w, 0)
        piso.append(f'<line class="piso-c" x1="{r1(a[0])}" y1="{r1(a[1])}" x2="{r1(b[0])}" y2="{r1(b[1])}"/>')
    xd = d + 52
    cotas = []
    for a_, b_, _n, _d in TRAMOS_TRL:
        a, b = a_ - 1, b_
        pa, pb = P(xd, -a * w, 0), P(xd, -b * w, 0)
        ea, ea2 = P(d + 8, -a * w, 0), P(xd + 12, -a * w, 0)
        eb, eb2 = P(d + 8, -b * w, 0), P(xd + 12, -b * w, 0)
        m = P(xd + 24, -(a + b) / 2 * w, 0)
        cotas.append(
            f'<path class="cota-ext" d="M{r1(ea[0])} {r1(ea[1])}L{r1(ea2[0])} {r1(ea2[1])}M{r1(eb[0])} {r1(eb[1])}L{r1(eb2[0])} {r1(eb2[1])}"/>'
            f'<path class="cota-r" d="M{r1(pa[0])} {r1(pa[1])}L{r1(pb[0])} {r1(pb[1])}"/>'
        )
        for p in (pa, pb):
            cotas.append(f'<path class="cota-r" d="M{r1(p[0] - 7)} {r1(p[1] + 7)}L{r1(p[0] + 7)} {r1(p[1] - 7)}"/>')
        lbl = f"TRL {a_}–{b_}"
        cotas.append(
            f'<text class="cota-t" transform="matrix({C30:.3f},{-S30},0,1,{r1(m[0])},{r1(m[1])})" text-anchor="middle" y="8">{lbl}</text>'
        )
    # Leyenda: un renglón por tramo, del más alto (operacional) al más bajo.
    ys = {2: 360, 1: 488, 0: 616}
    ancla = {0: 1, 1: 4, 2: 7}
    ley, lid = [], []
    for k, (a_, b_, nom, desc) in enumerate(TRAMOS_TRL):
        y = ys[k]
        p = info[ancla[k]]["topBL"]
        clave = " es-clave" if resaltar == k else ""
        ley.append(
            f'<div class="tramo t{k}{clave}" style="top:{y - 30}px;--i:{k}"><p class="tramo__n">TRL {a_}–{b_}</p>'
            f"<b>{e(nom)}</b><span>{e(desc)}</span></div>"
        )
        xk = 600
        lid.append(
            f'<path class="lider" d="M{xk - 50} {y + 2}H{xk}L{r1(p[0] - 30)} {r1(p[1] - 14)}L{r1(p[0] - 6)} {r1(p[1] - 14)}"/>'
            f'<circle class="lider-p" cx="{r1(p[0] - 2)}" cy="{r1(p[1] - 14)}" r="5"/>'
        )
    cuerpo = (
        '<defs><clipPath id="c-piso"><rect x="40" y="40" width="1520" height="752"/></clipPath></defs>'
        f'<g class="anim-fade" clip-path="url(#c-piso)">{"".join(piso)}</g>' + svg + "".join(cotas) + "".join(lid)
    )
    return fig(cuerpo, f'<div class="leyenda-trl">{"".join(ley)}</div>')


# ---------------------------------------------------- valle de la muerte


def _bez(p0, p1, p2, p3):
    def f(t):
        u = 1 - t
        return (
            u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1],
        )

    return f


def valle(alto=None):
    """Esquema de dos curvas sobre el eje TRL: fondos de investigación que
    caen e inversión privada que sube. El tramo en que ambas son bajas
    (TRL 4 a 7, rayado) es el llamado valle de la muerte."""
    x0, x1, top, base = 200, 1400, 380, 656
    fondo = 680

    def X(t):
        return x0 + (t - 1) / 8 * (x1 - x0)

    pubP = [(X(1), top + 20), (X(3.5), top + 20), (X(4.5), base - 30), (X(6.5), base - 10)]
    priP = [(X(3), base - 10), (X(5.5), base - 10), (X(6.5), top + 20), (X(9), top + 20)]
    sp = [_bez(*pubP)(i / 400) for i in range(401)]
    sq = [_bez(*priP)(i / 400) for i in range(401)]

    def y_at(arr, x, fl, fr):
        if x <= arr[0][0]:
            return fl
        if x >= arr[-1][0]:
            return fr
        for i in range(1, len(arr)):
            if arr[i][0] >= x:
                (ax, ay), (bx, by) = arr[i - 1], arr[i]
                return ay + (by - ay) * (x - ax) / ((bx - ax) or 1)
        return fr

    # Mayor de las dos fuentes en cada TRL; su punto más bajo es el cruce.
    env = []
    x = X(1)
    while x <= X(9) + 0.1:
        env.append((x, min(y_at(sp, x, top + 20, base - 10), y_at(sq, x, base - 10, top + 20))))
        x += 5
    min_pt = max(env, key=lambda p: p[1])
    pub_d = "M{},{} C{},{} {},{} {},{}".format(*[r1(v) for p in pubP for v in p])
    pri_d = "M{},{} C{},{} {},{} {},{}".format(*[r1(v) for p in priP for v in p])
    ejes = []
    for n in range(1, 10):
        ejes.append(f'<path class="tick" d="M{r1(X(n))} {fondo}V{fondo + 12}"/>')
        ejes.append(T(X(n), fondo + 44, str(n), "eje-n" + (" en-valle" if 4 <= n <= 7 else ""), "middle"))
    y_rim = top + 20
    xe = x0 - 30                  # eje vertical (financiamiento, sin escala)
    ye = top - 30
    cuerpo = (
        '<defs><pattern id="h-valle" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<path d="M0 0V12" class="hatch"/></pattern></defs>'
        f'<rect x="{r1(X(4))}" y="{top - 26}" width="{r1(X(7) - X(4))}" height="{fondo - top + 26}" fill="url(#h-valle)"/>'
        f'<path class="curva pub" d="{pub_d}"/><path class="curva pri" d="{pri_d}"/>'
        f'<path class="eje" d="M{xe} {fondo}V{ye}"/>'
        f'<path class="eje" d="M{xe - 7} {ye + 14}L{xe} {ye}L{xe + 7} {ye + 14}"/>'
        + T(xe - 22, (fondo + ye) / 2, "Financiamiento", "eje-t", "middle",
            f'transform="rotate(-90 {xe - 22} {r1((fondo + ye) / 2)})"')
        + f'<path class="eje" d="M{xe} {fondo}H{x1 + 30}"/>' + "".join(ejes)
        + T(800, fondo + 84, "Nivel de madurez tecnológica (TRL)", "eje-t", "middle")
        + '<g class="cota-valle es-clave">'
        f'<path class="ext" d="M{r1(X(4))} {y_rim - 50}V{fondo}M{r1(X(7))} {y_rim - 50}V{fondo}"/>'
        f'<path class="dim" d="M{r1(X(4))} {y_rim - 38}H{r1(X(7))}"/>'
        f'<path class="dim" d="M{r1(X(4) - 7)} {y_rim - 31}L{r1(X(4) + 7)} {y_rim - 45}M{r1(X(7) - 7)} {y_rim - 31}L{r1(X(7) + 7)} {y_rim - 45}"/>'
        f'<path class="dim" d="M{r1(min_pt[0])} {y_rim + 62}V{r1(min_pt[1] - 8)}M{r1(min_pt[0] - 7)} {r1(min_pt[1] - 20)}L{r1(min_pt[0])} {r1(min_pt[1] - 6)}L{r1(min_pt[0] + 7)} {r1(min_pt[1] - 20)}"/>'
        "</g>"
        + T((X(4) + X(7)) / 2, y_rim + 30, "Valle de la muerte", "valle-t", "middle")
        + f'<circle class="cruce" cx="{r1(min_pt[0])}" cy="{r1(min_pt[1])}" r="7"/>'
        + T(X(1), top - 4, "Fondos de investigación", "curva-t pub")
        + T(X(9), top - 4, "Inversión privada", "curva-t pri", "end")
        + T(1500, 330, "ESQUEMA, SIN ESCALA", "etq-mono", "end")
    )
    return fig(cuerpo)


# ------------------------------------------ rangos de TRL por convocatoria


def rangos_trl(filas, alto=None):
    """Regla TRL 1–9 con un rango por concurso, dibujado como cota:
    ○ nivel de entrada, ● nivel de salida. filas: (etiqueta, detalle,
    trl_entrada, trl_salida, clave)."""
    x0, x1 = 700, 1460
    y_r = 424
    fila = 118
    y1 = y_r + 40

    def X(t):
        return x0 + (t - 1) / 8 * (x1 - x0)

    c = [f'<path class="rt-M" d="M{x0 - 20} {y_r}H{x1 + 20}"/>']
    v = 1.0
    while v <= 9.0001:
        x = X(v)
        mayor = abs(v - round(v)) < 1e-3
        medio = abs(v * 2 - round(v * 2)) < 1e-3
        c.append(f'<path class="{"rt-M" if mayor else "rt-m"}" d="M{r1(x)} {y_r}V{y_r + (16 if mayor else 10 if medio else 6)}"/>')
        if mayor:
            c.append(T(x, y_r - 16, str(round(v)), "regla-n", "middle"))
            c.append(f'<path class="guia" d="M{r1(x)} {y_r + 22}V{y1 + fila * len(filas) - 40}"/>')
        v += 0.25
    c.append(T(x0 - 44, y_r + 6, "TRL", "etq-mono", "end"))
    html = []
    for i, (etq, det, a, b, clave) in enumerate(filas):
        y = y1 + i * fila
        cy = y + 44
        k = " es-clave" if clave else ""
        g = f'<g class="rango{" rango--clave es-clave" if clave else ""}" style="--i:{i}">'
        g += f'<path class="r-ext" d="M{r1(X(a))} {cy - 34}V{cy + 22}M{r1(X(b))} {cy - 34}V{cy + 22}"/>'
        g += f'<path class="r-dim" d="M{r1(X(a) + 14)} {cy}H{r1(X(b) - 15)}"/>'
        g += f'<circle class="r-in" cx="{r1(X(a))}" cy="{cy}" r="12"/>'
        g += f'<circle class="r-out" cx="{r1(X(b))}" cy="{cy}" r="14"/>'
        g += "</g>"
        c.append(g)
        html.append(
            f'<div class="rango-etq{k}" style="top:{y + 6}px;--i:{i}"><b>{e(etq)}</b><span>{e(det)}</span></div>'
        )
    ley = (
        f'<circle class="r-in" cx="{x0 - 2}" cy="{y_r - 74}" r="10"/>'
        + T(x0 + 18, y_r - 67, "ENTRADA", "etq-mono")
        + f'<circle class="r-out" cx="{x0 + 160}" cy="{y_r - 74}" r="11"/>'
        + T(x0 + 180, y_r - 67, "SALIDA", "etq-mono")
    )
    return fig("".join(c) + ley, "".join(html))


# ---------------------------------------------------- cuádruple hélice


def cuadruple_helice(helices, alto=None):
    """Modelo de cuádruple hélice como cuatro conjuntos superpuestos (un
    círculo por actor). Las zonas superpuestas son las interacciones entre
    actores; la zona común a los cuatro es el proyecto. helices: lista de 4
    (nombre, [funciones]) en orden: Estado, Academia, Empresa, Sociedad. El
    conjunto de la sociedad, en rojo."""
    cx, cy, d, r = 800, 556, 64, 152
    centros = [(cx - d, cy - d), (cx + d, cy - d), (cx - d, cy + d), (cx + d, cy + d)]
    angulos = [-135, -45, 135, 45]
    letras = "ABCD"
    clips, fondos, bordes, marcas, lideres, etqs = [], [], [], [], [], []
    for i, ((nom, act), (x, y), ang) in enumerate(zip(helices, centros, angulos)):
        clave = i == len(helices) - 1
        kc = " clave" if clave else ""
        clips.append(f'<clipPath id="cq-{i}"><circle cx="{x}" cy="{y}" r="{r}"/></clipPath>')
        fondos.append(f'<circle class="conj{kc}" style="--i:{i}" cx="{x}" cy="{y}" r="{r}"/>')
        bordes.append(f'<circle class="conj-b{kc}" style="--i:{i}" cx="{x}" cy="{y}" r="{r}"/>')
        rad = math.radians(ang)
        ux, uy = math.cos(rad), math.sin(rad)
        lx, ly = x + ux * r * 0.6, y + uy * r * 0.6
        marcas.append(
            f'<g class="conj-l{kc}"><circle cx="{r1(lx)}" cy="{r1(ly)}" r="17"/>'
            + T(lx, ly + 6, letras[i], "", "middle") + "</g>"
        )
        borde = (x + ux * r, y + uy * r)
        izq = ux < 0
        y_l = 400 if uy < 0 else 700
        x_l = 548 if izq else 1052
        codo = x_l + (30 if izq else -30)
        lideres.append(
            f'<path class="lider{kc}" d="M{r1(borde[0])} {r1(borde[1])}L{codo} {y_l}H{x_l}"/>'
            f'<circle class="lider-p{kc}" cx="{r1(borde[0])}" cy="{r1(borde[1])}" r="5"/>'
        )
        acts = "".join(f'<p class="h-act">{e(a)}</p>' for a in act)
        etqs.append(
            f'<div class="helice {"izq" if izq else "der"}{kc}{" es-clave" if clave else ""}" '
            f'style="top:{y_l - 26}px;--i:{i}"><p class="h-nom"><span class="globo-t">{letras[i]}</span>'
            f"{e(nom)}</p>{acts}</div>"
        )
    # Zona común a los cuatro conjuntos: el último círculo recortado por los
    # otros tres.
    x3, y3 = centros[3]
    nucleo = f'<circle class="nucleo" cx="{x3}" cy="{y3}" r="{r}"/>'
    for i in (2, 1, 0):
        nucleo = f'<g clip-path="url(#cq-{i})">{nucleo}</g>'
    cuerpo = (
        f'<defs>{"".join(clips)}</defs>'
        f'<g class="conjuntos">{"".join(fondos)}<g class="nucleo-g">{nucleo}</g>{"".join(bordes)}</g>'
        + "".join(marcas)
        + T(cx, cy + 9, "Proyecto", "nucleo-t", "middle")
        + "".join(lideres)
    )
    return fig(cuerpo, f'<div class="helices">{"".join(etqs)}</div>')


# -------------------------------------------------------------- barras


def _num(v, decimales):
    return f"{v:,.{decimales}f}".replace(",", " ").replace(".", ",")


def barras_svg(datos, unidad="", decimales=2, guia=None, maximo=None):
    """Barras horizontales con espesor sobre una regla milimetrada. Las
    referencias (rol «ref») van rayadas; el dato clave, en rojo; `guia`
    (valor, texto) traza una línea guía vertical."""
    top_v = maximo or 5.0
    xb, x_fin = 470, 1390
    kx = (x_fin - xb) / top_v
    n = len(datos)
    fila = 50 if n > 6 else 58
    bh, dz = 28, 9
    y_r = 392
    y0 = y_r + 46
    s, regla = [], []
    v = 0.0
    while v <= top_v + 1e-4:
        x = xb + v * kx
        mayor = abs(v - round(v)) < 1e-3
        medio = abs(v * 2 - round(v * 2)) < 1e-3
        regla.append(f'<path class="{"rt-M" if mayor else "rt-m"}" d="M{r1(x)} {y_r}V{y_r - (22 if mayor else 13 if medio else 7)}"/>')
        if mayor:
            regla.append(T(x, y_r - 32, f"{round(v)}{' %' if abs(v - top_v) < 1e-3 else ''}", "regla-n", "middle"))
            if v > 0:
                s.append(f'<path class="guia" d="M{r1(x)} {y_r + 8}V{y0 + fila * n - 16}"/>')
        v += 0.1
    regla.insert(0, f'<path class="rt-M" d="M{xb} {y_r}H{r1(xb + top_v * kx)}"/>')
    for i, (nom, val, rol) in enumerate(datos):
        y = y0 + i * fila
        w = max(3, val * kx)
        cls = {"clave": "b-clave es-clave", "ref": "b-ref"}.get(rol, "b-pais")
        s.append(T(xb - 28, y + bh / 2 + 9, nom, f"b-nom {rol}", "end"))
        s.append(
            f'<g class="barra {cls}" style="--i:{i}">'
            f'<polygon class="b-sup" points="{pts([(xb, y), (xb + dz, y - dz), (xb + w + dz, y - dz), (xb + w, y)])}"/>'
            f'<polygon class="b-fin" points="{pts([(xb + w, y), (xb + w + dz, y - dz), (xb + w + dz, y + bh - dz), (xb + w, y + bh)])}"/>'
            f'<rect class="b-fre" x="{xb}" y="{y}" width="{r1(w)}" height="{bh}"/></g>'
        )
        s.append(T(xb + w + dz + 16, y + bh / 2 + 9, _num(val, decimales) + " %", f"b-val {rol}"))
    if guia:
        gx = xb + guia[0] * kx
        y_fin = y0 + fila * n - 10
        s.append(
            f'<g class="guia-meta"><path class="gm-l" d="M{r1(gx)} {y_r - 52}V{y_fin}"/>'
            f'<path class="gm-p" d="M{r1(gx - 6)} {y_r - 52}H{r1(gx + 6)}M{r1(gx - 6)} {y_fin}H{r1(gx + 6)}"/></g>'
        )
        s.append(T(gx + 14, y_r - 58, guia[1], "gm-t"))
    cuerpo = (
        '<defs><pattern id="h-ref" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<path d="M0 0V10" class="hatch-ref"/></pattern></defs>' + "".join(regla) + "".join(s)
    )
    return fig(cuerpo)


# -------------------------------------------------------------- pausa


def regla_pregunta(y=748, x0=880, x1=1440):
    """Regla TRL 1–9 con un cursor «?» que busca su nivel (lámina de pausa)."""

    def X(n):
        return x0 + (n - 1) / 8 * (x1 - x0)

    c = [f'<path class="v-base" d="M{x0 - 30} {y}H{x1 + 30}"/>']
    v = 1.0
    while v <= 9.0001:
        x = X(v)
        mayor = abs(v - round(v)) < 0.01
        c.append(f'<path class="{"v-M" if mayor else "v-m"}" d="M{r1(x)} {y}V{y + (22 if mayor else 10)}"/>')
        if mayor:
            c.append(T(x, y + 54, str(round(v)), "v-n", "middle"))
        v += 0.25
    c.append(
        f'<g class="cursor-q" style="--x0:{r1(X(1))}px;--dx:{r1(X(9) - X(1))}px">'
        f'<path class="c-tri" d="M0 {y - 4}l-13 -20h26z"/>'
        f'<path class="c-lin" d="M0 {y - 24}V{y - 58}"/>'
        f'<circle class="c-glo" cx="0" cy="{y - 86}" r="27"/>'
        + T(0, y - 74, "?", "c-q", "middle") + "</g>"
    )
    c.append(T(x0 - 50, y + 6, "TRL", "mono-luz", "end"))
    return fig("".join(c), cls="fig--regla")


# ------------------------------------------------------ iconos de caso


def icono(nombre: str) -> str:
    """Dibujos de línea técnica (vista de planta / alzado) con ejes y cotas
    para el panel visual de la plantilla «caso». viewBox 0 0 420 420."""
    if nombre == "dron":
        rot = []
        for cx, cy in ((110, 110), (310, 110), (110, 310), (310, 310)):
            rot.append(
                f'<circle class="t-barrido" cx="{cx}" cy="{cy}" r="74"/>'
                f'<circle class="t-pieza" cx="{cx}" cy="{cy}" r="16"/>'
                f'<path class="t-pieza" d="M{cx - 64} {cy + 8}L{cx + 64} {cy - 8}"/>'
                f'<path class="t-eje" d="M{cx - 88} {cy}H{cx + 88}M{cx} {cy - 88}V{cy + 88}"/>'
            )
        cuerpo = (
            '<path class="t-eje t-eje--m" d="M20 210H400M210 20V400"/>'
            + "".join(rot)
            + '<path class="t-pieza" d="M126 126L176 176M294 126L244 176M126 294L176 244M294 294L244 244"/>'
            + '<rect class="t-cuerpo" x="168" y="168" width="84" height="84" rx="10"/>'
            + '<rect class="t-pieza" x="186" y="186" width="48" height="48" rx="4"/>'
            + '<circle class="t-sensor" cx="210" cy="210" r="11"/>'
            + '<path class="t-cota" d="M110 404H310M110 396V412M310 396V412"/>'
            + '<path class="t-cota" d="M118 400L110 404L118 408M302 400L310 404L302 408"/>'
        )
    elif nombre == "satelite":
        celdas = []
        for x0 in (28, 278):
            for k in range(4):
                celdas.append(f'<rect class="t-panel" x="{x0 + k * 28.5}" y="176" width="26" height="68"/>')
        cuerpo = (
            '<path class="t-eje t-eje--m" d="M10 210H410M210 30V400"/>'
            + "".join(celdas)
            + '<rect class="t-pieza" x="26" y="174" width="118" height="72"/><rect class="t-pieza" x="276" y="174" width="118" height="72"/>'
            + '<path class="t-pieza" d="M144 210H166M254 210H276"/>'
            + '<rect class="t-cuerpo" x="166" y="122" width="88" height="176" rx="4"/>'
            + '<path class="t-pieza" d="M166 210H254M180 136H240M180 284H240"/>'
            + '<circle class="t-sensor" cx="210" cy="166" r="12"/>'
            + '<path class="t-pieza" d="M210 122V70"/><circle class="t-pieza" cx="210" cy="64" r="6"/>'
            + '<path class="t-onda" d="M188 52a32 32 0 0 1 44 0M176 38a50 50 0 0 1 68 0"/>'
            + '<path class="t-cota" d="M290 122H330M290 298H330M320 122V298"/>'
            + '<path class="t-cota" d="M316 130L320 122L324 130M316 290L320 298L324 290"/>'
            + T(336, 216, "2U", "t-etq t-etq--cota")
        )
    else:  # hidrógeno u otros: gota con símbolo
        cuerpo = '<path class="t-cuerpo" d="M210 40C150 130 120 180 120 230a90 90 0 0 0 180 0c0-50-30-100-90-190z"/>'
    return f'<svg class="tecnico" viewBox="0 0 420 420" aria-hidden="true">{cuerpo}</svg>'


def icono_tecnico(nombre: str) -> str:
    """Dibujos de línea técnica añadidos para los casos de la sesión 2, con
    las mismas clases t-* y el mismo viewBox (0 0 420 420) que `icono()`:
    «robot» (robot de inspección sobre orugas con escáner láser, alzado),
    «planta» (planta de trigo con espiga y raíces, alzado) y «spt» (ensayo de
    penetración estándar instrumentado, alzado). Cualquier otro nombre pasa a
    `icono()`, que no se modifica."""
    if nombre == "robot":
        ruedas = "".join(
            f'<circle class="t-pieza" cx="{x}" cy="300" r="{r}"/>'
            for x, r in ((122, 26), (184, 15), (236, 15), (298, 26))
        )
        suelo = "".join(f'<path class="t-cota" d="M{x} 344l-12 12"/>' for x in range(52, 392, 24))
        cuerpo = (
            '<path class="t-eje t-eje--m" d="M40 300H380M256 52V368"/>'
            + '<path class="t-pieza" d="M30 332H390"/>' + suelo
            + '<rect class="t-pieza" x="92" y="270" width="236" height="60" rx="30"/>'
            + ruedas
            + '<rect class="t-cuerpo" x="112" y="196" width="196" height="70" rx="6"/>'
            + '<path class="t-pieza" d="M132 214H220M132 232H220M132 250H220"/>'
            + '<circle class="t-pieza" cx="290" cy="231" r="10"/>'
            + '<path class="t-pieza" d="M256 196V136"/>'
            + '<rect class="t-cuerpo" x="232" y="108" width="48" height="28" rx="4"/>'
            + '<circle class="t-sensor" cx="256" cy="122" r="7"/>'
            + '<path class="t-onda" d="M292 104a26 26 0 0 1 0 36M308 92a44 44 0 0 1 0 60M324 80a62 62 0 0 1 0 84"/>'
            + '<path class="t-cota" d="M92 384H328M92 376V392M328 376V392"/>'
            + '<path class="t-cota" d="M100 380L92 384L100 388M320 380L328 384L320 388"/>'
        )
    elif nombre == "planta":
        granos = []
        for k in range(7):
            y = 150 - k * 13
            for lado in (-1, 1):
                cx = 210 + lado * 9
                granos.append(
                    f'<ellipse class="t-cuerpo" cx="{cx}" cy="{y}" rx="8" ry="12" '
                    f'transform="rotate({lado * 18} {cx} {y})"/>'
                    f'<path class="t-pieza" d="M{cx + lado * 4} {y - 10}L{cx + lado * 20} {y - 50}"/>'
                )
        suelo = "".join(f'<path class="t-cota" d="M{x} 312l-12 12"/>' for x in range(56, 380, 24))
        cuerpo = (
            '<path class="t-eje" d="M210 30V400"/>'
            + '<path class="t-pieza" d="M40 300H380"/>' + suelo
            + '<path class="t-barrido" d="M210 300c-6 28-26 48-52 66M210 300c6 30 24 50 50 64'
            'M210 300v84M210 316c-20 10-44 14-70 12M210 316c20 10 44 14 70 12"/>'
            + '<path class="t-pieza" d="M210 300C207 250 213 204 210 162"/>'
            + '<path class="t-pieza" d="M209 262C186 250 158 226 132 184M209 262C190 246 168 226 150 196"/>'
            + '<path class="t-pieza" d="M211 222C236 208 262 186 286 146M211 222C230 206 250 186 268 158"/>'
            + "".join(granos)
            + '<path class="t-cota" d="M330 300V60M322 300H338M322 60H338"/>'
            + '<path class="t-cota" d="M326 68L330 60L334 68M326 292L330 300L334 292"/>'
        )
    elif nombre == "spt":
        suelo = "".join(f'<path class="t-cota" d="M{x} 262l-12 12"/>' for x in range(44, 392, 24))
        cuerpo = (
            '<path class="t-eje" d="M210 40V412"/>'
            + '<path class="t-pieza" d="M24 250H396"/>' + suelo
            + '<path class="t-pieza" d="M210 52L124 250M210 52L296 250"/>'
            + '<circle class="t-pieza" cx="210" cy="52" r="10"/>'
            + '<path class="t-pieza" d="M210 62V96"/>'
            + '<rect class="t-cuerpo" x="184" y="96" width="52" height="56" rx="3"/>'
            + '<path class="t-pieza" d="M210 152V194"/>'
            + '<rect class="t-pieza" x="190" y="194" width="40" height="14"/>'
            + '<rect class="t-cuerpo" x="200" y="208" width="20" height="30"/>'
            + '<circle class="t-sensor" cx="210" cy="223" r="6"/>'
            + '<path class="t-onda" d="M230 212a16 16 0 0 1 0 22M242 202a30 30 0 0 1 0 42"/>'
            + '<rect class="t-panel" x="300" y="196" width="76" height="46" rx="3"/>'
            + '<path class="t-pieza" d="M312 210H364M312 226H348"/>'
            + '<path class="t-pieza" d="M204 238V352M216 238V352"/>'
            + '<rect class="t-cuerpo" x="196" y="352" width="28" height="44"/>'
            + '<path class="t-pieza" d="M196 396L210 410L224 396"/>'
            + '<path class="t-cota" d="M88 96H112M88 194H112M100 96V194"/>'
            + '<path class="t-cota" d="M96 104L100 96L104 104M96 186L100 194L104 186"/>'
            + T(88, 150, "CAÍDA", "t-etq", "end")
        )
    else:
        return icono(nombre)
    return f'<svg class="tecnico" viewBox="0 0 420 420" aria-hidden="true">{cuerpo}</svg>'


# ------------------------------------------------ sesión 3: montos y tramos


def barras_valor(datos, maximo, paso, unidad="", sufijo="", decimales=1, menor=None,
                 xb=470, nota=None, nota_fila=None):
    """Barras horizontales con espesor para montos o porcentajes de cualquier
    escala (la versión de la sesión 1, `barras_svg`, está fijada en 0–5 %).
    Misma construcción y mismas clases: regla milimetrada con marcas mayores
    cada `paso` y menores cada `menor`; dato clave en rojo, referencias
    rayadas. `unidad` rotula la regla (p. ej., «MILLONES DE SOLES»); `sufijo`
    acompaña cada valor (« %»). `nota` es una línea literal bajo las barras o, con
    `nota_fila`, a la derecha de la barra de esa fila (para un valor muy pequeño).
    datos: (etiqueta, valor, rol) con rol en {"", "clave", "ref"}."""
    menor = menor or paso / 5
    x_fin = 1390
    kx = (x_fin - xb) / maximo
    n = len(datos)
    fila = 50 if n > 6 else 54 if n > 4 else 72
    bh, dz = 30, 9
    y_r = 392
    y0 = y_r + 52
    s, regla = [], []
    v = 0.0
    while v <= maximo + 1e-6:
        x = xb + v * kx
        mayor = abs(v / paso - round(v / paso)) < 1e-6
        regla.append(f'<path class="{"rt-M" if mayor else "rt-m"}" d="M{r1(x)} {y_r}V{y_r - (22 if mayor else 11)}"/>')
        if mayor:
            regla.append(T(x, y_r - 32, _num(v, 0), "regla-n", "middle"))
            if v > 0:
                s.append(f'<path class="guia" d="M{r1(x)} {y_r + 8}V{y0 + fila * n - 16}"/>')
        v += menor
    regla.insert(0, f'<path class="rt-M" d="M{xb} {y_r}H{r1(xb + maximo * kx)}"/>')
    if unidad:
        regla.append(T(xb, y_r - 66, unidad, "etq-mono"))
    for i, (nom, val, rol) in enumerate(datos):
        y = y0 + i * fila
        w = max(3, val * kx)
        cls = {"clave": "b-clave es-clave", "ref": "b-ref"}.get(rol, "b-pais")
        s.append(T(xb - 28, y + bh / 2 + 9, nom, f"b-nom {rol}", "end"))
        s.append(
            f'<g class="barra {cls}" style="--i:{i}">'
            f'<polygon class="b-sup" points="{pts([(xb, y), (xb + dz, y - dz), (xb + w + dz, y - dz), (xb + w, y)])}"/>'
            f'<polygon class="b-fin" points="{pts([(xb + w, y), (xb + w + dz, y - dz), (xb + w + dz, y + bh - dz), (xb + w, y + bh)])}"/>'
            f'<rect class="b-fre" x="{xb}" y="{y}" width="{r1(w)}" height="{bh}"/></g>'
        )
        s.append(T(xb + w + dz + 16, y + bh / 2 + 9, _num(val, decimales) + sufijo, f"b-val {rol}"))
    if nota and nota_fila is not None:
        w = max(3, datos[nota_fila][1] * kx)
        s.append(T(xb + w + 120, y0 + nota_fila * fila + bh / 2 + 7, nota, "etq-mono"))
    elif nota:
        s.append(T(xb, y0 + fila * n + 34, nota, "etq-mono"))
    cuerpo = (
        '<defs><pattern id="h-ref" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<path d="M0 0V10" class="hatch-ref"/></pattern></defs>' + "".join(regla) + "".join(s)
    )
    return fig(cuerpo)


def tramos_trl(filas, nota=None):
    """Regla TRL 1–9 con un tramo por fuente de financiamiento, en filas
    compactas (hasta 6; `rangos_trl` admite 3). Misma construcción que
    `rangos_trl`: ○ nivel de entrada, ● nivel de salida. El tramo fijado en
    bases se traza continuo; el estimado, discontinuo. filas: (etiqueta,
    detalle, trl_entrada, trl_salida, clave, estimado)."""
    x0, x1 = 700, 1460
    y_r = 384
    fila = 62
    y1 = y_r + 34

    def X(t):
        return x0 + (t - 1) / 8 * (x1 - x0)

    c = [f'<path class="rt-M" d="M{x0 - 20} {y_r}H{x1 + 20}"/>']
    v = 1.0
    while v <= 9.0001:
        x = X(v)
        mayor = abs(v - round(v)) < 1e-3
        medio = abs(v * 2 - round(v * 2)) < 1e-3
        c.append(f'<path class="{"rt-M" if mayor else "rt-m"}" d="M{r1(x)} {y_r}V{y_r + (16 if mayor else 10 if medio else 6)}"/>')
        if mayor:
            c.append(T(x, y_r - 16, str(round(v)), "regla-n", "middle"))
            c.append(f'<path class="guia" d="M{r1(x)} {y_r + 22}V{y1 + fila * len(filas) - 12}"/>')
        v += 0.25
    c.append(T(x0 - 44, y_r + 6, "TRL", "etq-mono", "end"))
    html = []
    for i, (etq, det, a, b, clave, estimado) in enumerate(filas):
        y = y1 + i * fila
        cy = y + 30
        k = " es-clave" if clave else ""
        trazo = ' stroke-dasharray="12 9" stroke-linecap="butt"' if estimado else ""
        g = f'<g class="rango{" rango--clave es-clave" if clave else ""}" style="--i:{i}">'
        g += f'<path class="r-ext" d="M{r1(X(a))} {cy - 22}V{cy + 18}M{r1(X(b))} {cy - 22}V{cy + 18}"/>'
        g += f'<path class="r-dim" d="M{r1(X(a) + 12)} {cy}H{r1(X(b) - 13)}"{trazo}/>'
        g += f'<circle class="r-in" cx="{r1(X(a))}" cy="{cy}" r="10"/>'
        g += f'<circle class="r-out" cx="{r1(X(b))}" cy="{cy}" r="12"/>'
        g += "</g>"
        c.append(g)
        html.append(
            f'<div class="rango-etq{k}" style="top:{y + 2}px;width:540px;--i:{i}">'
            f'<b style="font-size:27px">{e(etq)}</b>'
            f'<span style="margin-top:2px;font-size:19px">{e(det)}</span></div>'
        )
    ley = (
        f'<circle class="r-in" cx="{x0 - 2}" cy="{y_r - 66}" r="9"/>'
        + T(x0 + 16, y_r - 59, "ENTRADA", "etq-mono")
        + f'<circle class="r-out" cx="{x0 + 150}" cy="{y_r - 66}" r="10"/>'
        + T(x0 + 168, y_r - 59, "SALIDA", "etq-mono")
        + f'<path class="r-dim" d="M{x0 + 300} {y_r - 66}H{x0 + 352}"/>'
        + T(x0 + 366, y_r - 59, "BASES", "etq-mono")
        + f'<path class="r-dim" d="M{x0 + 460} {y_r - 66}H{x0 + 512}" stroke-dasharray="12 9" stroke-linecap="butt"/>'
        + T(x0 + 526, y_r - 59, "ESTIMACIÓN", "etq-mono")
    )
    if nota:
        ley += T(x1 + 20, y1 + fila * len(filas) + 22, nota, "etq-mono", "end")
    return fig("".join(c) + ley, "".join(html))


# Compatibilidad con llamadas antiguas (no se usan en la sesión 1).


# `linea_tiempo` se implementa en la sección de la sesión 5, al final del
# módulo (ninguna sesión anterior la usaba).


def meta(*_a, **_k):  # pragma: no cover
    return ""


# --------------------------------------- sesión 4: formulación de proyectos
#
# Gráficos nuevos de la sesión 4. Ninguna función anterior se modifica. Los
# trazos usan clases ya definidas en ponencia.css (gm-p, gm-l, vf-flecha,
# vf-punta, rt-M, rt-m, guia, cruce, barra, b-pais, b-clave, anio, eje-t,
# etq-mono…); las cajas con texto son <div> de `.fig-html` con estilo en
# línea que solo lee variables del modo de la lámina (--card, --card-line,
# --uni, --red, --ink…), con el mismo aspecto que las fichas: fondo de
# tarjeta, filete y cabecera de 5 px. Todo el texto de contenido mide 24 px o
# más en el lienzo de 1600 × 900.


def _caja(x, y, w, h, texto, clave=False, punteado=False, tam=24, peso=500, etiqueta="",
          alinear="center", fondo="var(--card)"):
    """Caja de texto con el aspecto de una ficha técnica, en px del lienzo."""
    color = "var(--red)" if clave else "var(--uni)"
    borde = "dashed" if punteado else "solid"
    linea = "var(--red)" if clave else "var(--card-line)"
    tag = (
        f'<span style="display:block;margin-bottom:4px;font:700 24px/1 var(--f-mono);'
        f'letter-spacing:0.08em;color:var(--red)">{e(etiqueta)}</span>' if etiqueta else ""
    )
    just = "center" if alinear == "center" else "flex-start"
    return (
        f'<div style="position:absolute;left:{r1(x)}px;top:{r1(y)}px;width:{r1(w)}px;height:{r1(h)}px;'
        f'box-sizing:border-box;display:flex;flex-direction:column;justify-content:center;'
        f'align-items:{just};text-align:{alinear};padding:6px 16px 8px;background:{fondo};'
        f'border:1.4px {borde} {linea};border-top:5px {borde} {color};'
        f'font:{peso} {tam}px/1.18 var(--f-sans);letter-spacing:-0.005em;color:var(--ink);'
        f'text-wrap:balance">{tag}<span>{e(texto)}</span></div>'
    )


def _flecha_arriba(x, y, cls="gm-p"):
    """Punta de flecha hacia arriba con vértice en (x, y)."""
    return f'<path class="{cls}" fill="none" d="M{r1(x - 8)} {r1(y + 12)}L{r1(x)} {r1(y)}L{r1(x + 8)} {r1(y + 12)}"/>'


def arbol(problema, causas, efectos, modo="problemas", supuestos=()):
    """Árbol de problemas (o de objetivos) del marco lógico, en tres niveles:
    efectos (o fines) arriba, problema central (u objetivo central) al centro y
    causas (o medios) abajo, unidos por conectores ortogonales con punta hacia
    el nivel superior. Las causas cuyo índice está en `supuestos` se dibujan
    con trazo discontinuo y el rótulo «SUPUESTO»: quedan fuera del alcance del
    proyecto (ILPES, 2005). Admite tres causas y tres efectos."""
    obj = modo == "objetivos"
    rot = (("FINES",), ("OBJETIVO", "CENTRAL"), ("MEDIOS",)) if obj else \
          (("EFECTOS",), ("PROBLEMA", "CENTRAL"), ("CAUSAS",))
    x0, w, gap = 330, 362, 36
    cxs = [x0 + w / 2 + i * (w + gap) for i in range(3)]
    ye, he = 312, 112
    yp, hp = 482, 100
    yc, hc = 640, 112
    xp0, wp = 529, 760
    cx = xp0 + wp / 2
    s, h = [], []
    # Conectores: de cada causa al problema y del problema a cada efecto.
    bus_e, bus_c = ye + he + 26, yc - 26
    s.append(f'<path class="gm-p" d="M{r1(cx)} {yp}V{bus_e}M{r1(cxs[0])} {bus_e}H{r1(cxs[2])}"/>')
    for x in cxs:
        s.append(f'<path class="gm-p" d="M{r1(x)} {bus_e}V{ye + he + 2}"/>')
        s.append(_flecha_arriba(x, ye + he + 2))
    s.append(f'<path class="gm-p" d="M{r1(cxs[0])} {bus_c}H{r1(cxs[2])}M{r1(cx)} {bus_c}V{yp + hp + 2}"/>')
    s.append(_flecha_arriba(cx, yp + hp + 2))
    for i, x in enumerate(cxs):
        extra = ' stroke-dasharray="7 6"' if i in supuestos else ""
        s.append(f'<path class="gm-p" d="M{r1(x)} {yc}V{bus_c}"{extra}/>')
    # Rótulos de nivel, a la izquierda.
    for k, (lineas, yc_) in enumerate(zip(rot, (ye + he / 2, yp + hp / 2, yc + hc / 2))):
        y0 = yc_ + 8 - (len(lineas) - 1) * 15
        for j, ln in enumerate(lineas):
            s.append(T(112, y0 + j * 30, ln, "anio" + (" anio--b" if k == 1 else "")))
    for i, x in enumerate(cxs):
        h.append(_caja(x - w / 2, ye, w, he, efectos[i]))
        sup = i in supuestos
        h.append(_caja(x - w / 2, yc, w, hc, causas[i], punteado=sup,
                       etiqueta="SUPUESTO" if sup else "",
                       fondo="transparent" if sup else "var(--card)"))
    h.append(_caja(xp0, yp, wp, hp, problema, clave=True, tam=27, peso=600))
    s.append(T(1488, 790, "ESQUEMA · SE LEE DE ABAJO ARRIBA", "etq-mono", "end"))
    return fig("".join(s), "".join(h))


def arbol_portada():
    """Portada de la sesión 4: un árbol de problemas en trazo de plano sobre
    la noche (cajas vacías con renglones de texto simulados), con el problema
    central en rojo encendido y una cota «CAUSAS → EFECTOS»."""

    def caja(x, y, w, h, cls, renglones=2):
        g = f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/>'
        for k in range(renglones):
            yy = y + 24 + k * 18
            g += f'<path class="piso" d="M{x + 16} {yy}H{x + w - 16 - k * 30}"/>'
        return g

    def linea(d):
        return f'<path class="p-fre" fill="none" d="{d}"/>'

    xs = [1006, 1182, 1358]
    cw, ch = 150, 74
    ye, yp, yc, y2 = 262, 430, 598, 724
    cxs = [x + cw / 2 for x in xs]
    pcx = 1256
    g = []
    g.append(linea(f"M{pcx} {yp}V{ye + ch + 28}"))
    g.append(linea(f"M{cxs[0]} {ye + ch + 28}H{cxs[2]}"))
    for x in cxs:
        g.append(linea(f"M{x} {ye + ch + 28}V{ye + ch}"))
    g.append(linea(f"M{cxs[0]} {yc - 28}H{cxs[2]}"))
    g.append(linea(f"M{pcx} {yc - 28}V{yp + 84}"))
    for x in cxs:
        g.append(linea(f"M{x} {yc}V{yc - 28}"))
    g.append(linea(f"M{cxs[1] - 60} {y2 - 22}H{cxs[1] + 60}M{cxs[1]} {yc + ch}V{y2 - 22}"))
    for x in (cxs[1] - 60, cxs[1] + 60):
        g.append(linea(f"M{x} {y2 - 22}V{y2}"))
    cajas = "".join(caja(x, ye, cw, ch, "p-top") for x in xs)
    cajas += caja(1056, yp, 400, 84, "p-top9", 0)
    cajas += "".join(caja(x, yc, cw, ch, "p-top") for x in xs)
    cajas += "".join(caja(int(x) - 52, y2, 104, 52, "p-fre", 1) for x in (cxs[1] - 60, cxs[1] + 60))
    xc = 1546
    cota = (
        '<g class="cota-luz">'
        f'<path class="ext" d="M{xs[2] + cw + 10} {ye}H{xc + 10}M{xs[2] + cw + 10} {yc + ch}H{xc + 10}"/>'
        f'<path d="M{xc} {ye}V{yc + ch}"/>'
        f'<path d="M{xc - 7} {ye + 14}L{xc} {ye}L{xc + 7} {ye + 14}"/></g>'
        + T(xc + 24, (ye + yc + ch) / 2, "CAUSAS → EFECTOS", "mono-luz", "middle",
            f'transform="rotate(-90 {xc + 24} {r1((ye + yc + ch) / 2)})"')
    )
    nodos = "".join(
        f'<circle class="nodo-luz" cx="{x}" cy="{y}" r="4"/>' for x, y in ((pcx, yp), (pcx, yp + 84))
    )
    cuerpo = (
        '<defs><filter id="glow-pc" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="12" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
        f'<g class="anim-fade">{"".join(g)}</g>'
        + cajas.replace('class="p-top9"', 'class="p-top9" filter="url(#glow-pc)"')
        + cota + nodos
    )
    return fig(cuerpo, cls="fig--portada")


def matriz_ml(filas, resaltar=None):
    """Matriz de marco lógico de cuatro por cuatro (ILPES, 2005): filas Fin,
    Propósito, Componentes y Actividades; columnas Resumen narrativo,
    Indicadores, Medios de verificación y Supuestos. filas: 4 tuplas
    (nivel, resumen, indicador, medio, supuesto). `resaltar`: índice de la
    fila que se marca en rojo."""
    cols = ("Resumen narrativo", "Indicadores", "Medios de verificación", "Supuestos")
    x0, wn, x1 = 112, 200, 1488
    wc = (x1 - x0 - wn) / 4
    y0, hc, hf = 300, 50, 108
    y1 = y0 + hc + hf * len(filas)
    s, h = [], []
    s.append(f'<rect class="rt-M" fill="none" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/>')
    if resaltar is not None:
        yr = y0 + hc + resaltar * hf
        s.append(f'<rect x="{x0}" y="{yr}" width="{x1 - x0}" height="{hf}" style="fill:var(--red-soft)"/>')
    for k in range(1, 5):
        x = x0 + wn + (k - 1) * wc
        s.append(f'<path class="rt-m" d="M{r1(x)} {y0}V{y1}"/>')
    for k in range(len(filas)):
        y = y0 + hc + k * hf
        s.append(f'<path class="{"rt-M" if k == 0 else "rt-m"}" d="M{x0} {y}H{x1}"/>')
    if resaltar is not None:
        yr = y0 + hc + resaltar * hf
        s.append(f'<rect class="vf-flecha" fill="none" x="{x0}" y="{yr}" width="{x1 - x0}" height="{hf}"/>')
    for k, c in enumerate(cols):
        x = x0 + wn + k * wc
        h.append(
            f'<div style="position:absolute;left:{r1(x)}px;top:{y0}px;width:{r1(wc)}px;height:{hc}px;'
            f'display:flex;align-items:center;padding:0 14px;font:600 24px/1.1 var(--f-sans);'
            f'color:var(--uni)">{e(c)}</div>'
        )
    for i, (nivel, *celdas) in enumerate(filas):
        y = y0 + hc + i * hf
        clave = i == resaltar
        h.append(
            f'<div style="position:absolute;left:{x0}px;top:{y}px;width:{wn}px;height:{hf}px;'
            f'display:flex;align-items:center;padding:0 18px;font:700 26px/1.1 var(--f-sans);'
            f'color:{"var(--red)" if clave else "var(--ink)"}">{e(nivel)}</div>'
        )
        for k, txt in enumerate(celdas):
            x = x0 + wn + k * wc
            h.append(
                f'<div style="position:absolute;left:{r1(x)}px;top:{y}px;width:{r1(wc)}px;height:{hf}px;'
                f'display:flex;align-items:center;padding:4px 14px;font:400 24px/1.16 var(--f-sans);'
                f'color:var(--ink-2)">{e(txt)}</div>'
            )
    return fig("".join(s), "".join(h))


def gantt(tareas, hitos, meses=24, leyenda=("Ruta crítica", "Cierre de hito")):
    """Diagrama de Gantt sobre una regla de meses. tareas: (grupo, etiqueta,
    mes_inicio, mes_fin, critica); el grupo se rotula una vez («OE1»). La ruta
    crítica va en rojo. hitos: (mes_inicio, mes_fin, rótulo): cada hito es un
    periodo, dibujado como franja sobre la regla, con un rombo y una línea
    guía en el mes de cierre."""
    xa, xb = 640, 1480
    kx = (xb - xa) / meses
    y_b, h_b = 300, 44
    y_r = 392
    y0, fila, bh = 418, 40, 22
    n = len(tareas)
    y_fin = y0 + n * fila

    def X(m):
        return xa + m * kx

    s, h = [], []
    # Franja de hitos (periodos).
    for k, (a, b, rot) in enumerate(hitos):
        x, w = X(a - 1), (b - a + 1) * kx
        s.append(f'<rect x="{r1(x + 2)}" y="{y_b}" width="{r1(w - 4)}" height="{h_b}" '
                 f'style="fill:var(--tint);stroke:var(--uni-mid);stroke-width:1.2"/>')
        s.append(T(x + w / 2, y_b + 30, rot, "eje-t", "middle", 'style="fill:var(--uni);font-weight:600"'))
        # La guía arranca en el rombo de la regla y no en la franja, para no
        # rozar los números de mes que quedan junto al cierre del hito.
        s.append(f'<path class="gm-l" d="M{r1(X(b))} {y_r}V{y_fin}"/>')
    # Regla de meses.
    s.append(f'<path class="rt-M" d="M{xa} {y_r}H{xb}"/>')
    for m in range(meses + 1):
        mayor = m % 3 == 0
        s.append(f'<path class="{"rt-M" if mayor else "rt-m"}" d="M{r1(X(m))} {y_r}V{y_r - (14 if mayor else 7)}"/>')
        if mayor and m:
            s.append(T(X(m) - kx / 2, y_r - 20, str(m), "regla-n", "middle", 'style="font-size:24px"'))
    s.append(T(xa - 16, y_r - 20, "MES", "regla-n", "end", 'style="font-size:22px"'))
    for (a, b, _r) in hitos:
        x = X(b)
        s.append(f'<polygon class="cruce" points="{pts([(x, y_r - 11), (x + 11, y_r), (x, y_r + 11), (x - 11, y_r)])}"/>')
    # Tareas.
    previo = None
    for i, (grupo, etq, a, b, critica) in enumerate(tareas):
        y = y0 + i * fila
        if grupo != previo:
            if previo is not None:
                s.append(f'<path class="guia" d="M112 {y - 1}H{xb}"/>')
            s.append(T(112, y + bh / 2 + 9, grupo, "anio"))
            previo = grupo
        cls = "b-clave es-clave" if critica else "b-pais"
        s.append(T(196, y + bh / 2 + 9, etq, "b-nom" + (" clave" if critica else ""), "start",
                   'style="font-size:24px"'))
        s.append(
            f'<g class="barra {cls}" style="--i:{i}"><rect class="b-fre" x="{r1(X(a - 1) + 2)}" y="{y}" '
            f'width="{r1((b - a + 1) * kx - 4)}" height="{bh}" rx="2"/></g>'
        )
    # Leyenda, sobre la columna de tareas.
    s.append(f'<g class="b-clave"><rect class="b-fre" x="112" y="{y_b + 10}" width="40" height="20" rx="2"/></g>')
    s.append(T(166, y_b + 29, leyenda[0], "eje-t"))
    xl = 380
    s.append(f'<polygon class="cruce" points="{pts([(xl, y_b + 9), (xl + 11, y_b + 20), (xl, y_b + 31), (xl - 11, y_b + 20)])}"/>')
    s.append(T(xl + 22, y_b + 29, leyenda[1], "eje-t"))
    return fig("".join(s), "".join(h))


def matriz_riesgo(columnas, filas, zonas, puntos, eje_x, eje_y, ley_x=1080):
    """Matriz de análisis de supuestos y riesgos: rejilla filas × columnas con
    zonas rotuladas y factores numerados, más una leyenda con el texto de
    cada factor. columnas y filas: rótulos (izquierda → derecha, arriba →
    abajo). zonas: (fila, col_ini, col_fin, rótulo, estilo) con estilo en
    {"clave", "fatal", "hecho", "tenue"}. puntos: (número, texto, fila, col)."""
    x0, x1 = 330, 1010
    y0, hf = 330, 176
    wc = (x1 - x0) / len(columnas)
    y1 = y0 + hf * len(filas)
    s, h = [], []
    fondo = {
        "clave": "var(--red-soft)",
        "fatal": "repeating-linear-gradient(45deg, var(--red-soft) 0 3px, transparent 3px 12px)",
        "hecho": "var(--tint)",
        "tenue": "transparent",
    }
    texto = {"clave": "var(--red)", "fatal": "var(--red)", "hecho": "var(--uni)", "tenue": "var(--ink-3)"}
    for (f, ca, cb, rot, est) in zonas:
        x, y, w = x0 + ca * wc, y0 + f * hf, (cb - ca + 1) * wc
        fichas = "".join(
            f'<span style="display:inline-grid;place-items:center;width:44px;height:44px;margin:0 6px;'
            f'border-radius:50%;background:var(--paper);border:2px solid {texto[est]};'
            f'font:700 24px/1 var(--f-mono);color:{texto[est]}">{n}</span>'
            for (n, _t, pf, pc) in puntos if pf == f and ca <= pc <= cb
        )
        h.append(
            f'<div style="position:absolute;left:{r1(x)}px;top:{r1(y)}px;width:{r1(w)}px;height:{hf}px;'
            f'box-sizing:border-box;padding:16px 16px;display:flex;flex-direction:column;'
            f'justify-content:space-between;align-items:center;text-align:center;background:{fondo[est]}">'
            f'<span style="font:600 24px/1.15 var(--f-sans);color:{texto[est]};text-wrap:balance">{e(rot)}</span>'
            f'<span>{fichas}</span></div>'
        )
    s.append(f'<rect class="rt-M" fill="none" x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/>')
    # Divisiones de columna, salvo dentro de una zona que abarca varias.
    for f in range(len(filas)):
        for k in range(1, len(columnas)):
            if any(zf == f and ca < k <= cb for (zf, ca, cb, _r, _e) in zonas):
                continue
            s.append(f'<path class="rt-m" d="M{r1(x0 + k * wc)} {y0 + f * hf}V{y0 + (f + 1) * hf}"/>')
    for k in range(1, len(filas)):
        s.append(f'<path class="rt-m" d="M{x0} {y0 + k * hf}H{x1}"/>')
    for k, c in enumerate(columnas):
        s.append(T(x0 + (k + 0.5) * wc, y1 + 34, c, "eje-t", "middle"))
    for k, f in enumerate(filas):
        s.append(T(x0 - 18, y0 + (k + 0.5) * hf + 8, f, "eje-t", "end"))
    s.append(T((x0 + x1) / 2, y1 + 74, eje_x, "eje-t", "middle", 'style="fill:var(--ink);font-weight:600"'))
    yc = (y0 + y1) / 2
    s.append(T(150, yc, eje_y, "eje-t", "middle",
               f'style="fill:var(--ink);font-weight:600" transform="rotate(-90 150 {r1(yc)})"'))
    # Leyenda de factores: una columna con separación fija entre factores,
    # sea cual sea el número de líneas de cada uno.
    items = "".join(
        f'<div style="display:flex;gap:16px;align-items:flex-start">'
        f'<b style="flex:none;font:700 24px/1.2 var(--f-mono);color:var(--uni)">{n:02d}</b>'
        f'<span>{e(t)}</span></div>'
        for (n, t, pf, pc) in puntos
    )
    h.append(
        f'<div style="position:absolute;left:{ley_x}px;top:{y0}px;width:{1488 - ley_x}px;display:flex;'
        f'flex-direction:column;gap:28px;font:400 24px/1.2 var(--f-sans);color:var(--ink)">{items}</div>'
    )
    return fig("".join(s), "".join(h))


def icono_nodo_acustico():
    """Nodo acústico de monitoreo forestal sujeto al tronco de un árbol, en
    alzado, con las mismas clases t-* y el mismo viewBox (0 0 420 420) que
    `icono()`: tronco con abrazaderas, caja del nodo con placa y micrófono,
    panel solar, antena con señal de alerta, ondas de sonido que llegan al
    micrófono y cota de altura de instalación."""
    corteza = "".join(
        f'<path class="t-cota" d="M{x} {y}v{h}"/>'
        for x, y, h in ((132, 60, 34), (164, 96, 30), (140, 300, 40), (172, 316, 30), (128, 196, 26))
    )
    suelo = "".join(f'<path class="t-cota" d="M{x} 380l-12 12"/>' for x in range(52, 400, 24))
    cuerpo = (
        '<path class="t-eje" d="M150 24V392"/>'
        + '<path class="t-pieza" d="M30 380H404"/>' + suelo
        + '<path class="t-pieza" d="M118 24C115 150 112 300 102 380M182 24C185 150 188 300 198 380"/>'
        + corteza
        + '<rect class="t-pieza" x="112" y="182" width="86" height="10" rx="2"/>'
        + '<rect class="t-pieza" x="112" y="248" width="88" height="10" rx="2"/>'
        + '<rect class="t-cuerpo" x="196" y="168" width="104" height="104" rx="8"/>'
        + '<rect class="t-panel" x="210" y="182" width="76" height="38"/>'
        + '<path class="t-pieza" d="M220 194H262M220 208H250"/>'
        + '<circle class="t-pieza" cx="248" cy="246" r="15"/>'
        + '<circle class="t-sensor" cx="248" cy="246" r="6"/>'
        + '<path class="t-pieza" d="M224 168V150"/>'
        + '<rect class="t-panel" x="196" y="132" width="76" height="18"/>'
        + '<path class="t-pieza" d="M286 168V94"/><circle class="t-pieza" cx="286" cy="88" r="6"/>'
        + '<path class="t-onda" d="M268 76a26 26 0 0 1 36 0M256 62a44 44 0 0 1 60 0"/>'
        + '<path class="t-onda" d="M318 230a24 24 0 0 0 0 32M338 216a46 46 0 0 0 0 60M358 202a68 68 0 0 0 0 88"/>'
        + '<path class="t-cota" d="M48 246H96M48 380H96M60 246V380"/>'
        + '<path class="t-cota" d="M56 254L60 246L64 254M56 372L60 380L64 372"/>'
        + T(52, 320, "h", "t-etq t-etq--cota", "end")
    )
    return f'<svg class="tecnico" viewBox="0 0 420 420" aria-hidden="true">{cuerpo}</svg>'


# ------------------------------------------- sesión 5: ejecución y resultados
#
# Gráficos nuevos de la sesión 5. Ninguna función anterior se modifica (el
# antiguo `linea_tiempo` era un marcador vacío sin uso). Mismas clases de
# ponencia.css y mismo criterio que la sesión 4: los textos son <div> de
# `.fig-html` de 24 px o más, con variables del modo de la lámina.


def _etq_html(x, y, w, h, texto, clave=False, peso=600, alinear="flex-end", color=None):
    """Rótulo de texto libre (sin caja) centrado en x, en px del lienzo."""
    col = color or ("var(--red)" if clave else "var(--ink)")
    return (
        f'<div style="position:absolute;left:{r1(x - w / 2)}px;top:{r1(y)}px;width:{r1(w)}px;'
        f'height:{r1(h)}px;box-sizing:border-box;display:flex;flex-direction:column;'
        f'justify-content:{alinear};text-align:center;font:{peso} 24px/1.15 var(--f-sans);'
        f'color:{col};text-wrap:balance">{e(texto)}</div>'
    )


def linea_tiempo(eventos, tramos=(), escala=None, unidad="", nota="", y_r=560, x0=180, x1=1420):
    """Línea de tiempo sobre una regla horizontal. eventos: (posición, título,
    detalle, clave): rombo sobre la regla, título arriba y detalle abajo; si
    los eventos están juntos, los rótulos alternan dos alturas. El evento
    clave va en rojo. tramos: (inicio, fin, rótulo, clave), dibujados como
    bandas en dos carriles sobre los títulos. escala: (mínimo, máximo, paso)
    traza una regla con marcas y números (unidad a la izquierda); sin escala,
    las posiciones solo ordenan y `nota` declara el esquema."""
    ps = [ev[0] for ev in eventos]
    vmin, vmax, paso = escala if escala else (min(ps), max(ps), None)

    def X(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)

    xs = [X(p) for p in ps]
    sp = min((b - a for a, b in zip(xs, xs[1:])), default=600)
    alterna = sp < 230
    w = min(2 * sp - 16 if alterna else sp - 12, 300)
    s, h = [], []
    s.append(f'<path class="gm-p" d="M{x0 - 40} {y_r}H{x1 + 34}"/>')
    s.append(f'<path class="gm-p" fill="none" d="M{x1 + 22} {y_r - 8}L{x1 + 34} {y_r}L{x1 + 22} {y_r + 8}"/>')
    abajo = 26
    if paso:
        v = vmin
        while v <= vmax + 1e-6:
            x = X(v)
            s.append(f'<path class="rt-M" d="M{r1(x)} {y_r}V{y_r + 12}"/>')
            s.append(T(x, y_r + 34, _num(v, 0).replace("-", "−"), "regla-n", "middle"))
            v += paso
        abajo = 50
        if unidad:
            s.append(T(x0 - 52, y_r + 7, unidad, "etq-mono", "end"))
    # Tramos en dos carriles, por encima de los títulos.
    carriles = [[], []]
    for (a, b, rot, clave) in tramos:
        k = 0 if all(a >= fb or b <= fa for fa, fb in carriles[0]) else 1
        carriles[k].append((a, b))
        y = 300 + k * 42
        xa, xb = X(a), X(b)
        borde = "var(--red)" if clave else "var(--uni-mid)"
        fondo = "var(--red-soft)" if clave else "var(--tint)"
        s.append(f'<rect x="{r1(xa)}" y="{y}" width="{r1(xb - xa)}" height="34" '
                 f'style="fill:{fondo};stroke:{borde};stroke-width:1.4"/>')
        s.append(f'<path class="guia" d="M{r1(xa)} {y + 34}V{y_r - 184}M{r1(xb)} {y + 34}V{y_r - 184}"/>')
        h.append(
            f'<div style="position:absolute;left:{r1(xa + 10)}px;top:{y}px;height:34px;display:flex;'
            f'align-items:center;white-space:nowrap;font:600 24px/1 var(--f-sans);'
            f'color:{"var(--red)" if clave else "var(--uni)"}">{e(rot)}</div>'
        )
    for i, ((pos, tit, det, clave), x) in enumerate(zip(eventos, xs)):
        k = i % 2 if alterna else 0
        yb = y_r - 26 - k * 86
        xc = min(max(x, x0 - 40 + w / 2), x1 + 40 - w / 2)
        s.append(f'<path class="guia" d="M{r1(x)} {y_r - 14}V{yb + 2}"/>')
        h.append(_etq_html(xc, yb - 64, w, 62, tit, clave))
        yd = y_r + abajo + k * 84
        if det:
            s.append(f'<path class="guia" d="M{r1(x)} {y_r + 14}V{yd - 2}"/>')
            h.append(_etq_html(xc, yd, w, 84, det, False, 400, "flex-start", "var(--ink-2)"))
        estilo = "" if clave else ' style="fill:var(--paper);stroke:var(--uni);stroke-width:2.4"'
        s.append(f'<polygon class="cruce"{estilo} points="{pts([(x, y_r - 13), (x + 13, y_r), (x, y_r + 13), (x - 13, y_r)])}"/>')
    if nota:
        s.append(T(x0 - 40, 790, nota, "etq-mono"))
    return fig("".join(s), "".join(h))


def barras_apiladas(datos, maximo, paso, unidad="", leyenda=(), menor=None, xb=520, decimales=2):
    """Barras horizontales con espesor en dos tramos (p. ej., tasa de
    presentación y tasa de examen), con la misma construcción que
    `barras_valor`. datos: (etiqueta, [valor1, valor2], rol, texto_final);
    el segundo tramo va rayado. leyenda: rótulos de los dos tramos."""
    menor = menor or paso / 5
    x_fin = 1330
    kx = (x_fin - xb) / maximo
    n = len(datos)
    fila = 54 if n > 4 else 72
    bh, dz = 30, 9
    y_r = 392
    y0 = y_r + 52
    s, regla = [], []
    v = 0.0
    while v <= maximo + 1e-6:
        x = xb + v * kx
        mayor = abs(v / paso - round(v / paso)) < 1e-6
        regla.append(f'<path class="{"rt-M" if mayor else "rt-m"}" d="M{r1(x)} {y_r}V{y_r - (22 if mayor else 11)}"/>')
        if mayor:
            regla.append(T(x, y_r - 32, _num(v, 0), "regla-n", "middle"))
            if v > 0:
                s.append(f'<path class="guia" d="M{r1(x)} {y_r + 8}V{y0 + fila * n - 16}"/>')
        v += menor
    regla.insert(0, f'<path class="rt-M" d="M{xb} {y_r}H{r1(xb + maximo * kx)}"/>')
    if unidad:
        regla.append(T(xb, y_r - 66, unidad, "etq-mono"))
    for i, (nom, vals, rol, texto) in enumerate(datos):
        y = y0 + i * fila
        cls1 = "b-clave es-clave" if rol == "clave" else "b-pais"
        s.append(T(xb - 28, y + bh / 2 + 9, nom, f"b-nom {rol}", "end"))
        xa = xb
        for k, val in enumerate(v_ for v_ in vals if v_):
            w = max(3, val * kx)
            cls = cls1 if k == 0 else "b-ref"
            s.append(
                f'<g class="barra {cls}" style="--i:{i}">'
                f'<polygon class="b-sup" points="{pts([(xa, y), (xa + dz, y - dz), (xa + w + dz, y - dz), (xa + w, y)])}"/>'
                f'<rect class="b-fre" x="{r1(xa)}" y="{y}" width="{r1(w)}" height="{bh}"/></g>'
            )
            xa += w
        s.append(
            f'<g class="barra {cls1 if len([v_ for v_ in vals if v_]) == 1 else "b-ref"}" style="--i:{i}">'
            f'<polygon class="b-fin" points="{pts([(xa, y), (xa + dz, y - dz), (xa + dz, y + bh - dz), (xa, y + bh)])}"/></g>'
        )
        s.append(T(xa + dz + 16, y + bh / 2 + 9, texto, f"b-val {rol}"))
    if leyenda:
        yl = y0 + fila * n + 14
        s.append(f'<g class="barra b-pais"><rect class="b-fre" x="{xb}" y="{yl}" width="36" height="20"/></g>')
        s.append(T(xb + 50, yl + 18, leyenda[0], "etq-mono"))
        xl = xb + 50 + len(leyenda[0]) * 12.5 + 40
        s.append(f'<g class="barra b-ref"><rect class="b-fre" x="{r1(xl)}" y="{yl}" width="36" height="20"/></g>')
        s.append(T(xl + 50, yl + 18, leyenda[1], "etq-mono"))
    cuerpo = (
        '<defs><pattern id="h-ref" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        '<path d="M0 0V10" class="hatch-ref"/></pattern></defs>' + "".join(regla) + "".join(s)
    )
    return fig(cuerpo)


def cronograma_portada():
    """Portada de la sesión 5: cronograma de ejecución en trazo de plano sobre
    la noche, con barras de actividades, hitos como rombos sobre una regla y
    el plazo de ejecución en rojo encendido; cota «FIRMA → CIERRE»."""
    x0, x1 = 1000, 1520
    y_r = 650
    g = [f'<path class="p-fre" fill="none" d="M{x0 - 20} {y_r}H{x1 + 10}"/>']
    for k in range(14):
        x = x0 + k * 40
        g.append(f'<path class="piso" d="M{x} {y_r}V{y_r - (16 if k % 3 == 0 else 8)}"/>')
    barras = [
        (x0, 120, 268, "p-top"), (x0 + 60, 160, 316, "p-fre"), (x0 + 130, 360, 364, "p-top9"),
        (x0 + 200, 180, 412, "p-top"), (x0 + 300, 200, 460, "p-fre"), (x0 + 420, 100, 508, "p-top"),
    ]
    cajas = ""
    for x, w, y, cls in barras:
        extra = ' filter="url(#glow-pc5)"' if cls == "p-top9" else ""
        cajas += f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="26" rx="3"{extra}/>'
        g.append(f'<path class="piso" d="M{x} {y + 26}V{y_r}"/>')
    rombos = "".join(
        f'<polygon class="{"p-top9" if i == 1 else "p-top"}" points="{pts([(x, y_r - 12), (x + 12, y_r), (x, y_r + 12), (x - 12, y_r)])}"/>'
        for i, x in enumerate((x0 + 40, x0 + 130, x0 + 280, x0 + 490))
    )
    xc = 1556
    cota = (
        '<g class="cota-luz">'
        f'<path class="ext" d="M{x0} {y_r + 40}V{y_r + 64}M{x1} {y_r + 40}V{y_r + 64}"/>'
        f'<path d="M{x0} {y_r + 56}H{x1}"/>'
        f'<path d="M{x1 - 14} {y_r + 49}L{x1} {y_r + 56}L{x1 - 14} {y_r + 63}"/></g>'
        + T((x0 + x1) / 2, y_r + 92, "FIRMA → CIERRE", "mono-luz", "middle")
    )
    nodos = "".join(f'<circle class="nodo-luz" cx="{x}" cy="{y_r}" r="4"/>' for x in (x0, x1))
    cuerpo = (
        '<defs><filter id="glow-pc5" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="12" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
        f'<g class="anim-fade">{"".join(g)}</g>' + cajas + rombos + cota + nodos
        + f'<path class="piso" d="M{xc} 260V{y_r}"/>'
    )
    return fig(cuerpo, cls="fig--portada")


def icono_s5(nombre: str) -> str:
    """Dibujos de línea técnica para los casos de la sesión 5, con las mismas
    clases t-* y el mismo viewBox (0 0 420 420) que `icono()`:
    «fotorreactor» (colector solar de tubos con tanque, alzado), «cdi» (celda
    de desionización capacitiva, corte), «electrodo» (electrodo serigrafiado
    de tres pistas, planta), «moneda» (celda de supercapacitor tipo moneda,
    vista explosionada), «acelerografo» (acelerógrafo triaxial sobre pedestal,
    alzado) y «magnetica» (nanopartículas con enzima inmovilizada separadas con un imán, alzado)."""
    if nombre == "fotorreactor":
        tubos = "".join(
            f'<path class="t-pieza" d="M{120 + k * 26} {300 - k * 15}L{214 + k * 26} {136 - k * 15}"/>'
            for k in range(6)
        )
        rayos = "".join(
            f'<path class="t-onda" d="M{70 + k * 14} {60 + k * 4}l{18 - k * 2} 22"/>' for k in range(1)
        )
        suelo = "".join(f'<path class="t-cota" d="M{x} 364l-12 12"/>' for x in range(52, 400, 24))
        cuerpo = (
            '<path class="t-pieza" d="M30 352H400"/>' + suelo
            + '<polygon class="t-panel" points="104,308 238,76 386,160 252,392"/>'
            + '<polygon class="t-cuerpo" points="112,304 230,98 360,172 244,376" style="fill:none"/>'
            + tubos
            + '<path class="t-pieza" d="M244 376V352M150 300V352"/>'
            + '<circle class="t-pieza" cx="74" cy="74" r="24"/>'
            + '<path class="t-onda" d="M108 92l34 18M96 116l30 26M118 64l38 6"/>' + rayos
            + '<rect class="t-cuerpo" x="300" y="260" width="78" height="92" rx="6"/>'
            + '<path class="t-pieza" d="M310 284H368M310 300H352"/>'
            + '<path class="t-pieza" d="M262 352H300"/><circle class="t-sensor" cx="339" cy="326" r="7"/>'
        )
    elif nombre == "cdi":
        iones = "".join(
            f'<circle class="t-sensor" cx="{x}" cy="{y}" r="6"/>' for x, y in
            ((150, 140), (150, 200), (150, 262), (270, 170), (270, 232), (270, 292))
        )
        flujo = "".join(
            f'<path class="t-onda" d="M{x} 60V350"/><path class="t-pieza" d="M{x - 8} 336L{x} 352L{x + 8} 336"/>'
            for x in (192, 228)
        )
        cuerpo = (
            '<path class="t-eje" d="M210 30V392"/>'
            + '<rect class="t-cuerpo" x="96" y="80" width="40" height="260" rx="3"/>'
            + '<rect class="t-cuerpo" x="284" y="80" width="40" height="260" rx="3"/>'
            + '<rect class="t-panel" x="136" y="80" width="18" height="260"/>'
            + '<rect class="t-panel" x="266" y="80" width="18" height="260"/>'
            + flujo + iones
            + '<path class="t-pieza" d="M116 80V40H170M304 80V40H250"/>'
            + T(186, 46, "−", "t-etq t-etq--cota", "middle") + T(234, 46, "+", "t-etq t-etq--cota", "middle")
            + '<path class="t-cota" d="M154 372H266M154 364V380M266 364V380"/>'
        )
    elif nombre == "electrodo":
        cuerpo = (
            '<path class="t-eje t-eje--m" d="M210 20V400"/>'
            + '<rect class="t-cuerpo" x="140" y="40" width="140" height="330" rx="8"/>'
            + '<path class="t-pieza" d="M176 290V352M210 270V352M244 290V352"/>'
            + '<rect class="t-panel" x="166" y="340" width="20" height="24"/><rect class="t-panel" x="200" y="340" width="20" height="24"/>'
            + '<rect class="t-panel" x="234" y="340" width="20" height="24"/>'
            + '<circle class="t-sensor" cx="210" cy="140" r="34"/>'
            + '<path class="t-pieza" d="M164 110a58 58 0 0 0 0 64M256 110a58 58 0 0 1 0 64"/>'
            + '<path class="t-pieza" d="M164 174L176 290M256 174L244 290M210 174V270"/>'
            + '<path class="t-barrido" d="M150 70H270V214H150Z"/>'
            + '<path class="t-onda" d="M210 20c-14 18-20 28-20 36a20 20 0 0 0 40 0c0-8-6-18-20-36z"/>'
            + '<path class="t-cota" d="M300 40H330M300 370H330M318 40V370"/>'
            + T(338, 212, "L", "t-etq t-etq--cota")
        )
    elif nombre == "moneda":
        capas = []
        for k, (y, cls) in enumerate(((70, "t-cuerpo"), (130, "t-panel"), (186, "t-cuerpo"), (242, "t-panel"),
                                      (298, "t-cuerpo"))):
            capas.append(f'<ellipse class="{cls}" cx="210" cy="{y}" rx="{120 if k in (0, 4) else 100}" ry="28"/>')
        cuerpo = (
            '<path class="t-eje" d="M210 24V372"/>' + "".join(capas)
            + '<path class="t-barrido" d="M90 70V298M330 70V298"/>'
            + '<path class="t-cota" d="M346 130H372M346 242H372M362 130V242"/>'
            + T(380, 192, "e", "t-etq t-etq--cota")
        )
    elif nombre == "acelerografo":
        traza = "M40 96" + "".join(
            f"l12 {(-1) ** k * a}" for k, a in enumerate((6, 12, 30, 54, 70, 46, 62, 30, 22, 12, 8, 4, 6, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2))
        )
        suelo = "".join(f'<path class="t-cota" d="M{x} 362l-12 12"/>' for x in range(52, 400, 24))
        cuerpo = (
            f'<path class="t-onda" d="{traza}"/>'
            + '<path class="t-pieza" d="M30 350H400"/>' + suelo
            + '<rect class="t-panel" x="120" y="300" width="180" height="50"/>'
            + '<rect class="t-cuerpo" x="146" y="200" width="128" height="100" rx="6"/>'
            + '<circle class="t-sensor" cx="210" cy="250" r="9"/>'
            + '<path class="t-pieza" d="M210 250H330M210 250V156M210 250L150 196"/>'
            + '<path class="t-pieza" d="M318 242L332 250L318 258M202 168L210 154L218 168M156 206L148 194L162 196"/>'
            + T(342, 258, "X", "t-etq t-etq--cota") + T(222, 158, "Z", "t-etq t-etq--cota")
            + T(132, 196, "Y", "t-etq t-etq--cota", "end")
            + '<path class="t-pieza" d="M274 220H300V176"/><circle class="t-pieza" cx="300" cy="170" r="6"/>'
        )
    elif nombre == "magnetica":
        parts = "".join(
            f'<circle class="t-panel" cx="{x}" cy="{y}" r="11"/><circle class="t-sensor" cx="{x}" cy="{y}" r="4"/>'
            for x, y in ((236, 214), (250, 246), (232, 278), (252, 306), (230, 334), (214, 246), (216, 304))
        )
        sueltas = "".join(
            f'<circle class="t-panel" cx="{x}" cy="{y}" r="7"/>' for x, y in ((118, 232), (150, 300), (126, 330))
        )
        cuerpo = (
            '<path class="t-pieza" d="M86 130V352a18 18 0 0 0 18 18H252a18 18 0 0 0 18-18V130"/>'
            + '<path class="t-pieza" d="M76 130H96M260 130H280"/>'
            + '<path class="t-barrido" d="M90 196H266"/>'
            + parts + sueltas
            + '<path class="t-cuerpo" d="M292 196H360a24 24 0 0 1 24 24V320a24 24 0 0 1-24 24H292V308H346V232H292Z"/>'
            + '<path class="t-pieza" d="M292 196V232M292 308V344"/>'
            + T(330, 188, "N", "t-etq t-etq--cota", "middle") + T(330, 368, "S", "t-etq t-etq--cota", "middle")
            + '<circle class="t-pieza" cx="150" cy="84" r="34"/><circle class="t-panel" cx="150" cy="84" r="20"/>'
            + '<circle class="t-sensor" cx="150" cy="84" r="9"/>'
            + '<path class="t-cota" d="M184 84H226M170 108L214 220"/>'
            + T(234, 80, "NÚCLEO Y SiO2", "t-etq") + T(234, 102, "CON ENZIMA", "t-etq")
        )
    else:
        return icono(nombre)
    return f'<svg class="tecnico" viewBox="0 0 420 420" aria-hidden="true">{cuerpo}</svg>'


# ------------------------------------------------------------ sesión 6


def deck_portada():
    """Portada de la sesión 6: juego de láminas de una presentación en vista
    isométrica, en trazo de plano sobre la noche, con una lámina en rojo
    encendido; debajo, una regla con el tramo de la exposición y el tramo,
    más largo, de las preguntas (esquema, sin escala)."""
    an, alto, dx, dy = 250, 168, 46, 27

    def P(x0, y0, u, v):
        return (x0 + u * an, y0 - u * an * S30 * 1.15 + v * alto)

    g, laminas = [], []
    for k in range(6):
        x0, y0 = 1010 + k * dx, 350 + k * dy
        cls = "p-top9" if k == 3 else ("p-top" if k == 5 else "p-fre")
        extra = ' filter="url(#glow-pd6)"' if k == 3 else ""
        laminas.append(
            f'<polygon class="{cls}"{extra} points="{pts([P(x0, y0, 0, 0), P(x0, y0, 1, 0), P(x0, y0, 1, 1), P(x0, y0, 0, 1)])}"/>'
        )
        g.append(f'<path class="piso" d="M{r1(x0)} {r1(y0 + alto)}V660"/>')
    # Contenido de la lámina del frente: línea de título y barras.
    x0, y0 = 1010 + 5 * dx, 350 + 5 * dy
    a, b = P(x0, y0, 0.1, 0.16), P(x0, y0, 0.62, 0.16)
    cont = f'<path class="p-fre" fill="none" d="M{r1(a[0])} {r1(a[1])}L{r1(b[0])} {r1(b[1])}"/>'
    for j, h in enumerate((0.22, 0.38, 0.3, 0.52)):
        u0, u1 = 0.14 + j * 0.19, 0.26 + j * 0.19
        cont += (
            f'<polygon class="p-top" points="{pts([P(x0, y0, u0, 0.86 - h), P(x0, y0, u1, 0.86 - h), P(x0, y0, u1, 0.86), P(x0, y0, u0, 0.86)])}"/>'
        )
    y_r, xa, xm, xb = 690, 1000, 1150, 1520
    regla = [f'<path class="p-fre" fill="none" d="M{xa - 20} {y_r}H{xb + 10}"/>']
    for k in range(14):
        x = xa + k * 40
        regla.append(f'<path class="piso" d="M{x} {y_r}V{y_r - (16 if k % 3 == 0 else 8)}"/>')
    cota = (
        '<g class="cota-luz">'
        f'<path class="ext" d="M{xa} {y_r + 22}V{y_r + 46}M{xm} {y_r + 22}V{y_r + 46}M{xb} {y_r + 22}V{y_r + 46}"/>'
        f'<path d="M{xa} {y_r + 38}H{xb}"/>'
        f'<path d="M{xb - 14} {y_r + 31}L{xb} {y_r + 38}L{xb - 14} {y_r + 45}"/></g>'
        + T((xa + xm) / 2, y_r + 74, "EXPOSICIÓN", "mono-luz", "middle")
        + T((xm + xb) / 2, y_r + 74, "PREGUNTAS DEL JURADO", "mono-luz", "middle")
    )
    nodos = "".join(f'<circle class="nodo-luz" cx="{x}" cy="{y_r}" r="4"/>' for x in (xa, xm, xb))
    cuerpo = (
        '<defs><filter id="glow-pd6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="12" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
        f'<g class="anim-fade">{"".join(g)}</g>' + "".join(laminas) + cont + "".join(regla) + cota + nodos
    )
    return fig(cuerpo, cls="fig--portada")


def matriz_guias(columnas, filas, nota="", x0=112, x1=1488, y0=300, cab=64, alto=None):
    """Matriz de correspondencia: filas = bloques de contenido, columnas =
    guías o bases que se comparan. columnas: rótulos de cabecera. filas:
    (rótulo, [celda por columna]); celda vacía = la guía no lo pide (raya).
    El texto va en HTML sobre el SVG para que corte en dos líneas."""
    n, m = len(filas), len(columnas)
    alto = alto or min(74, (770 - y0 - cab) / n)
    wl = 300
    wc = (x1 - x0 - wl) / m
    s, h = [], []
    yb = y0 + cab
    s.append(f'<path class="gm-p" d="M{x0} {yb}H{x1}"/>')
    for j, col in enumerate(columnas):
        xc = x0 + wl + j * wc
        s.append(f'<path class="guia" d="M{r1(xc)} {y0}V{r1(yb + n * alto)}"/>')
        h.append(
            f'<div style="position:absolute;left:{r1(xc + 16)}px;top:{y0}px;width:{r1(wc - 28)}px;'
            f'height:{cab - 10}px;display:flex;align-items:flex-end;font:600 23px/1.12 var(--f-sans);'
            f'color:var(--uni)">{e(col)}</div>'
        )
    for i, (rot, celdas) in enumerate(filas):
        y = yb + i * alto
        s.append(f'<path class="guia" d="M{x0} {r1(y + alto)}H{x1}"/>')
        h.append(
            f'<div style="position:absolute;left:{x0}px;top:{r1(y)}px;width:{wl - 20}px;height:{r1(alto)}px;'
            f'display:flex;align-items:center;font:600 27px/1.1 var(--f-sans);color:var(--ink)">{e(rot)}</div>'
        )
        for j, c in enumerate(celdas):
            xc = x0 + wl + j * wc
            vacio = not c
            h.append(
                f'<div style="position:absolute;left:{r1(xc + 16)}px;top:{r1(y)}px;width:{r1(wc - 28)}px;'
                f'height:{r1(alto)}px;display:flex;align-items:center;font:{"500 26px/1 var(--f-mono)" if vacio else "400 22px/1.15 var(--f-sans)"};'
                f'color:{"var(--ink-3)" if vacio else "var(--ink-2)"};text-wrap:balance">{e(c or "–")}</div>'
            )
            if not vacio:
                s.append(f'<circle class="cruce" style="fill:var(--uni)" cx="{r1(xc + 6)}" cy="{r1(y + alto / 2)}" r="3"/>')
    if nota:
        s.append(T(x0, yb + n * alto + 30, nota, "etq-mono"))
    return fig("".join(s), "".join(h))


def icono_s6(nombre: str) -> str:
    """Dibujos de línea técnica para los casos de la sesión 6, con las clases
    t-* y el viewBox (0 0 420 420) de `icono()`: «embarcacion» (bote con
    motor fuera de borda y satélite de observación, alzado), «biocuero»
    (bandeja de cultivo con la lámina de biocuero, alzado), «ronda» (mesa de
    reuniones con documentos, planta), «prenda» (prenda con código QR y
    teléfono que lo lee, alzado) y «escenario» (pantalla, atril y mesa del
    jurado, alzado)."""
    if nombre == "embarcacion":
        olas = "M24 300" + "q16 -10 32 0 " * 12
        cuerpo = (
            f'<path class="t-onda" d="{olas}"/>'
            + '<polygon class="t-cuerpo" points="96,258 296,258 274,300 120,300"/>'
            + '<rect class="t-panel" x="146" y="218" width="76" height="40"/>'
            + '<path class="t-pieza" d="M222 238H246M296 262H316V330M306 330H326"/>'
            + '<rect class="t-cuerpo" x="300" y="58" width="44" height="32" rx="3"/>'
            + '<rect class="t-panel" x="244" y="64" width="52" height="20"/><rect class="t-panel" x="348" y="64" width="52" height="20"/>'
            + '<path class="t-pieza" d="M296 74H300M344 74H348"/>'
            + '<path class="t-barrido" d="M322 90L228 344M322 90L380 344"/>'
            + "".join(f'<circle class="t-sensor" cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in
                      ((262, 340, 5), (296, 352, 7), (334, 338, 9), (360, 356, 6), (90, 346, 3), (140, 360, 3)))
            + '<path class="t-cota" d="M96 380H296M96 372V388M296 372V388"/>'
        )
    elif nombre == "biocuero":
        puntos = "".join(f'<circle class="t-sensor" cx="{x}" cy="{y}" r="3"/>' for x, y in
                         ((96, 300), (130, 310), (168, 298), (214, 312), (262, 300), (300, 314), (334, 302)))
        hojas = "".join(
            f'<path class="t-pieza" d="M{x} {y}c18-22 44-22 56 0c-18 18-40 18-56 0z"/><path class="t-pieza" d="M{x} {y}h56"/>'
            for x, y in ((80, 120), (170, 92), (262, 128))
        )
        cuerpo = (
            hojas
            + '<path class="t-onda" d="M210 152V214M196 200L210 216L224 200"/>'
            + '<path class="t-pieza" d="M60 252V332H360V252"/><path class="t-pieza" d="M48 252H72M348 252H372"/>'
            + '<path class="t-onda" d="M64 284q24-8 48 0t48 0t48 0t48 0t48 0t48 0"/>' + puntos
            + '<path class="t-cuerpo" d="M84 268H300c22 0 34-14 40-36l8 6c-8 26-24 42-48 42H84z"/>'
            + '<path class="t-cota" d="M84 360H300M84 352V368M300 352V368"/>'
            + T(192, 390, "LÁMINA", "t-etq t-etq--cota", "middle")
        )
    elif nombre == "ronda":
        sillas = []
        for k in range(8):
            a = math.radians(k * 45 + 22.5)
            cx, cy = 210 + math.cos(a) * 128, 200 + math.sin(a) * 128
            sillas.append(
                f'<rect class="t-panel" x="{r1(cx - 17)}" y="{r1(cy - 17)}" width="34" height="34" rx="6" '
                f'transform="rotate({k * 45 + 22.5} {r1(cx)} {r1(cy)})"/>'
            )
        cuerpo = (
            '<path class="t-eje t-eje--m" d="M30 200H390M210 30V370"/>'
            + "".join(sillas)
            + '<circle class="t-cuerpo" cx="210" cy="200" r="96"/>'
            + '<rect class="t-pieza" x="160" y="150" width="54" height="70" transform="rotate(-10 187 185)"/>'
            + '<path class="t-pieza" d="M168 170H200M168 184H204M168 198H192" transform="rotate(-10 187 185)"/>'
            + '<rect class="t-pieza" x="214" y="186" width="54" height="70" transform="rotate(8 241 221)"/>'
            + '<path class="t-onda" d="M224 240L238 224L250 232L262 210" transform="rotate(8 241 221)"/>'
            + '<path class="t-cota" d="M114 376H306M114 368V384M306 368V384"/>'
        )
    elif nombre == "prenda":
        qr = "".join(
            f'<rect class="t-sensor" x="{196 + c * 9}" y="{170 + f * 9}" width="8" height="8"/>'
            for f in range(5) for c in range(5) if (f * 7 + c * 3) % 4 != 1
        )
        cuerpo = (
            '<path class="t-cuerpo" d="M150 60L100 80L46 150L92 180L120 150V352H300V150L328 180L374 150L320 80L270 60'
            'c-8 22-32 36-60 36s-52-14-60-36z"/>'
            + '<path class="t-pieza" d="M210 96V352"/>'
            + '<rect class="t-panel" x="186" y="160" width="68" height="68"/>' + qr
            + '<rect class="t-cuerpo" x="300" y="236" width="70" height="124" rx="10"/>'
            + '<path class="t-pieza" d="M322 248H348"/>'
            + '<path class="t-barrido" d="M300 270L254 194M300 320L254 228"/>'
            + '<path class="t-cota" d="M186 140H254M186 132V148M254 132V148"/>'
        )
    elif nombre == "escenario":
        jurado = "".join(
            f'<circle class="t-pieza" cx="{x}" cy="256" r="13"/><path class="t-pieza" d="M{x - 18} 290c0-14 8-20 18-20s18 6 18 20"/>'
            for x in (242, 286, 330, 374)
        )
        cuerpo = (
            '<path class="t-pieza" d="M24 340H400"/>'
            + "".join(f'<path class="t-cota" d="M{x} 350l-12 12"/>' for x in range(48, 400, 24))
            + '<rect class="t-panel" x="40" y="56" width="220" height="132"/>'
            + '<path class="t-pieza" d="M60 80H160"/>'
            + "".join(f'<rect class="t-cuerpo" x="{70 + j * 44}" y="{176 - hh}" width="26" height="{hh}"/>'
                      for j, hh in enumerate((34, 56, 46, 76)))
            + '<polygon class="t-cuerpo" points="96,232 156,232 148,340 104,340"/>'
            + '<path class="t-pieza" d="M90 232H162"/>'
            + '<circle class="t-pieza" cx="126" cy="206" r="13"/>'
            + jurado
            + '<rect class="t-cuerpo" x="222" y="290" width="172" height="20"/>'
            + '<path class="t-pieza" d="M236 310V340M380 310V340"/>'
            + '<path class="t-barrido" d="M126 220L242 256"/>'
        )
    else:
        return icono(nombre)
    return f'<svg class="tecnico" viewBox="0 0 420 420" aria-hidden="true">{cuerpo}</svg>'
