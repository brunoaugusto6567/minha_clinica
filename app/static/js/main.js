// Sistema Clínica Médica

console.log("Sistema carregado com sucesso!");


// Confirmação de retorno

document.addEventListener("DOMContentLoaded", () => {

    const linksRetorno = document.querySelectorAll(
        'a[href*="/retorno/"]'
    );

    linksRetorno.forEach(link => {

        link.addEventListener("click", function(event){

            const confirmar = confirm(
                "Deseja solicitar uma consulta de retorno?"
            );

            if(!confirmar){
                event.preventDefault();
            }

        });

    });

});


// Mensagem ao marcar consulta

document.addEventListener("DOMContentLoaded", () => {

    const formulario = document.querySelector("form");

    if(formulario){

        formulario.addEventListener("submit", () => {

            alert(
                "Consulta enviada com sucesso!"
            );

        });

    }

});


// Destacar item atual do menu

document.addEventListener("DOMContentLoaded", () => {

    const links = document.querySelectorAll("nav a");

    links.forEach(link => {

        if(link.href === window.location.href){

            link.style.fontWeight = "bold";

            link.style.textDecoration = "underline";

        }

    });

});


// Saudação automática

document.addEventListener("DOMContentLoaded", () => {

    const hora = new Date().getHours();

    let saudacao = "";

    if(hora < 12){
        saudacao = "Bom dia!";
    }
    else if(hora < 18){
        saudacao = "Boa tarde!";
    }
    else{
        saudacao = "Boa noite!";
    }

    console.log(saudacao);

});


// Botão voltar ao topo

const botaoTopo = document.createElement("button");

botaoTopo.innerText = "↑";

botaoTopo.style.position = "fixed";
botaoTopo.style.bottom = "20px";
botaoTopo.style.right = "20px";
botaoTopo.style.padding = "10px 15px";
botaoTopo.style.display = "none";
botaoTopo.style.cursor = "pointer";

document.body.appendChild(botaoTopo);

window.addEventListener("scroll", () => {

    if(window.scrollY > 200){
        botaoTopo.style.display = "block";
    }else{
        botaoTopo.style.display = "none";
    }

});

botaoTopo.addEventListener("click", () => {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

});