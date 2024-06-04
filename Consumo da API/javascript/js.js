//Utilizando o Axios
//Enviando uma requisição GET para API, para listar todos os hogos


//Capturar botão de Criar Jogo
const createBtn = document.getElementById("createBtn")

createBtn.addEventListener("click", createGame)

//Capturar botão de Edição
const updateBtn = document.getElementById("updateBtn")

updateBtn.addEventListener("click", updateGame)

axios.get("http://localhost:5000/games").
then(response => {
    const games = response.data
    const listGames = document.getElementById("games")
    games.forEach(game => {
        let item = document.createElement("li")

        //setando o Atributo ID para cada game
        item.setAttribute("data-id", game._id)
        item.setAttribute("data-titulo", game.titulo)
        item.setAttribute("data-descricao", game.descricao)
        item.setAttribute("data-ano", game.ano)

        //const id = listItem.getAttibute("data-id")

        item.innerHTML = `<h4> ${game.titulo}</h4>
        <p>Descrição: ${game.descricao}</p>
        <p>ano: ${game.ano}</p>
        <p>id: ${game._id}</p>`

        
        
        var deleteBTN = document.createElement("button")
        deleteBTN.innerHTML = "Deletar"
        deleteBTN.classList.add("btn", "btn-danger", "mb-3", "mx-2")
        //quando clickar no botão
        deleteBTN.addEventListener("click", function(){
            deleteGame(item)
        })

        var editBTN = document.createElement("button")
        editBTN.innerHTML = "Editar"
        editBTN.classList.add("btn", "btn-warning", "mb-3")
        editBTN.addEventListener("click", function(){
            loadForm(item)
        })

        listGames.appendChild(item)
        item.appendChild(deleteBTN)
        item.appendChild(editBTN)

    })
})


//Função para deletar um game
function deleteGame(listItem){

    const id = listItem.getAttribute("data-id")
    axios.delete(`http://localhost:5000/games/${id}`).
    then(response => {
        window.alert("Game deletado com sucesso:", response.data)
        listItem.remove()
    })
    .catch(error =>{
        window.alert("Erro ao deletar o Game", error)
    })

}

    function createGame(){

        const form = document.getElementById("createForm")
        form.addEventListener("submit" , function(event){
            event.preventDefault() //Evita o envio padrão do formulário
        })

        const tituloInput = document.getElementById("titulo")
        const descricaoInput = document.getElementById("descricao")
        const anoInput = document.getElementById("ano")

        const game = {
            titulo : tituloInput.value,
            descricao : descricaoInput.value,
            ano: anoInput.value
        }

        console.log(game)

        //Enviando as informações do game para API
axios.post("http://localhost:5000/games", game).then(response =>{

if (response.status ==201){
    alert("Game Cadastrado com sucesso!")
    location.reload()
}
}).catch(error => {
    console.log(error)
})

    }


    //Função para carregar o formiulário de edição

    function loadForm(listItem){
        const id = listItem.getAttribute("data-id")
        const titulo = listItem.getAttribute("data-titulo")
        const ano = listItem.getAttribute("data-ano")
        const descricao = listItem.getAttribute("data-descricao")
        document.getElementById("idEdit").value = id
        document.getElementById("tituloEdit").value = titulo
        document.getElementById("anoEdit").value = ano
        document.getElementById("descricaoEdit").value = descricao

    }

    //Função para alterar o game

    function updateGame(){

        
        const form = document.getElementById("editForm")
        form.addEventListener("submit", function(event){
            event.preventDefault() // Evita o envio padrão do formulário
        })


        const idInput = document.getElementById("idEdit")
        const tituloInput = document.getElementById("tituloEdit")
        const anoInput = document.getElementById("anoEdit")
        const descricaoInput = document.getElementById("descricaoEdit")
        
        const game = {
        titulo: tituloInput.value,
        descricao: descricaoInput.value,
        ano: anoInput.value
        }

        var id = idInput.value

        axios.put(`http://localhost:5000/games/${id}`, game).then(response => {
            if(response.status == 200){
                alert("Game Atualizado com sucesso")
                location.reload()
            }
        }).catch(error => {
            console.log(error)
        })

    }

