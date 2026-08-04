/*====================================
        EL CORAZÓN DEL VALLENATO
        Creado por Ivan Lastre
====================================*/

//=============================
// Navbar cambia al hacer scroll
//=============================

const header = document.getElementById("header");

window.addEventListener("scroll", () => {

    if(window.scrollY > 80){

        header.classList.add("active");

    }else{

        header.classList.remove("active");

    }

});

//=============================
// Botón volver arriba
//=============================

const btnTop = document.getElementById("btnTop");

window.addEventListener("scroll",()=>{

    if(window.scrollY > 500){

        btnTop.style.display="block";

    }else{

        btnTop.style.display="none";

    }

});

btnTop.onclick=()=>{

    window.scrollTo({

        top:0,

        behavior:"smooth"

    });

};

//=============================
// Animación de aparición
//=============================

const sections = document.querySelectorAll("section");

const observer = new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.style.opacity="1";

            entry.target.style.transform="translateY(0)";

        }

    });

},{threshold:0.2});

sections.forEach(sec=>{

    sec.style.opacity="0";

    sec.style.transform="translateY(60px)";

    sec.style.transition="1s";

    observer.observe(sec);

});

//=============================
// Contadores animados
//=============================

const counters=document.querySelectorAll(".counter");

counters.forEach(counter=>{

    counter.innerText="0";

    const update=()=>{

        const target=+counter.getAttribute("data-target");

        const c=+counter.innerText;

        const increment=target/120;

        if(c<target){

            counter.innerText=Math.ceil(c+increment);

            setTimeout(update,20);

        }else{

            counter.innerText=target;

        }

    };

    update();

});

//=============================
// Efecto en las tarjetas
//=============================

const cards=document.querySelectorAll(".card, .song, .artista-card");

cards.forEach(card=>{

    card.addEventListener("mouseenter",()=>{

        card.style.transform="translateY(-12px) scale(1.03)";

    });

    card.addEventListener("mouseleave",()=>{

        card.style.transform="translateY(0px) scale(1)";

    });

});

//=============================
// Hero efecto Parallax
//=============================

window.addEventListener("scroll",()=>{

    const hero=document.querySelector(".hero");

    let value=window.scrollY;

    hero.style.backgroundPositionY=value*0.4+"px";

});

//=============================
// Destello del botón
//=============================

const boton=document.querySelector(".btn");

setInterval(()=>{

    boton.classList.toggle("glow");

},1200);

//=============================
// Título cambia de color
//=============================

const titulo=document.querySelector(".hero h1");

const colores=[

"#FFD54F",

"#D4AF37",

"#ffffff"

];

let indice=0;

setInterval(()=>{

    titulo.style.color=colores[indice];

    indice++;

    if(indice>=colores.length){

        indice=0;

    }

},1800);

//=============================
// Efecto de escritura
//=============================

const texto="El legado del folclor colombiano";

const subtitulo=document.querySelector(".hero h3");

subtitulo.innerHTML="";

let i=0;

function escribir(){

    if(i<texto.length){

        subtitulo.innerHTML+=texto.charAt(i);

        i++;

        setTimeout(escribir,80);

    }

}

escribir();

//=============================
// Mensaje en consola
//=============================

console.log("Proyecto creado por Ivan Lastre");