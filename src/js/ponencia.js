// Cromo de las láminas de ponencia (11.ª edición · «Mezcla A + C»).
// Reutiliza deck.js entero —progreso, inicio, tema, pantalla completa,
// flechas— y añade los atajos propios del formato de ponencia:
//   N        muestra u oculta las notas del docente de la lámina
//   T        conmuta tema claro / oscuro (las láminas base pasan a plano nocturno)
//   Espacio  avanza, como en cualquier software de presentación
//   C        inicia, detiene o reinicia el cronómetro de una pausa
import "./deck.js";

/* El lienzo mide 1600 × 900 y se escala entero a la ventana. Cada lámina ya
   fija --s con un script en línea (para que el primer cuadro salga a
   escala); aquí solo se repite por si el documento se abre sin él. */
function escalar() {
	document.documentElement.style.setProperty(
		"--s",
		String(Math.min(innerWidth / 1600, innerHeight / 900)),
	);
}
escalar();
addEventListener("resize", escalar);

const notas = document.querySelector(".pz__notas");
const NOTAS_KEY = "idie-ver-notas";

try {
	if (notas && sessionStorage.getItem(NOTAS_KEY) === "1") {
		document.body.classList.add("ver-notas");
	}
} catch {
	// Sin almacenamiento de sesión las notas empiezan ocultas.
}

/* Cronómetro de las pausas: no arranca solo (el docente explica primero la
   consigna). Clic o tecla C: iniciar → detener → reiniciar. */
const crono = document.querySelector(".crono");
let restante = 0;
let reloj = null;

function pintarCrono() {
	if (!crono) return;
	const total = Number(crono.dataset.segundos) || 1;
	const m = Math.floor(restante / 60);
	const s = restante % 60;
	crono.querySelector(".crono__t").textContent =
		`${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
	crono.style.setProperty("--gastado", String(Math.round((1 - restante / total) * 1000)));
	crono.classList.toggle("is-fin", restante === 0);
}

function conmutarCrono() {
	if (!crono) return;
	const total = Number(crono.dataset.segundos) || 0;
	if (reloj) {
		clearInterval(reloj);
		reloj = null;
		crono.classList.remove("is-corriendo");
		return;
	}
	if (restante === 0 || crono.classList.contains("is-fin")) restante = total;
	crono.classList.add("is-corriendo");
	reloj = setInterval(() => {
		restante = Math.max(0, restante - 1);
		pintarCrono();
		if (restante === 0) {
			clearInterval(reloj);
			reloj = null;
			crono.classList.remove("is-corriendo");
		}
	}, 1000);
	pintarCrono();
}

if (crono) {
	restante = Number(crono.dataset.segundos) || 0;
	crono.addEventListener("click", conmutarCrono);
}

document.addEventListener("keydown", (e) => {
	if (e.metaKey || e.ctrlKey || e.altKey) return;
	const k = e.key.toLowerCase();

	if (k === "n" && notas) {
		const on = document.body.classList.toggle("ver-notas");
		try {
			sessionStorage.setItem(NOTAS_KEY, on ? "1" : "0");
		} catch {}
	} else if (k === "t") {
		document.querySelector(".deck-controls__btn:nth-child(2)")?.click();
	} else if (k === "c" && crono) {
		conmutarCrono();
	} else if (e.key === " ") {
		const next = document.querySelectorAll(".slide-nav__link")[1];
		if (next) {
			e.preventDefault();
			window.location.href = next.getAttribute("href");
		}
	}
});
