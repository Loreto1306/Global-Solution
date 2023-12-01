const chk = document.getElementById('chk')

chk.addEventListener('change', ()=> {
    document.body.classList.toggle('dark')
})

let nome = document.getElementById("nome");
let email = document.getElementById("email");
let form = document.querySelector("form");

form.addEventListener("submit", (e)=>{
    console.log(nome.value);
    console.log(email.value)
    e.preventDefault()
    alert("Obrigado pelo Contato")
    
})

function limpar(){
    document.getElementById("nome").value='';
    document.getElementById("email").value='';
}

