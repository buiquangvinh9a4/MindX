async function getListPokemon(limit) {
    let listPokemon = []
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon?limit=${limit}&offset=0`);
    const data = await response.json();
    const results = data.results;
    
    results.forEach(item => {
        listPokemon.push(item.name);
    });
    console.log(listPokemon);
    return listPokemon;
}

async function getPokemonInfo(pokemonName) {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
    const data = await response.json();
    
    return data;
}

async function getInformationHome() {
    let listPokemon = await getListPokemon(20);
    const lst = document.getElementById("list");
    
    
    listPokemon.forEach(async pokemonName => {
        const pokemon = await getPokemonInfo(pokemonName);
        console.log(pokemon);
        const itemElement = document.createElement("div");
        itemElement.classList.add("item")

        itemElement.innerHTML = `
            <a href="#"> 
                <img src="${pokemon.sprites.back_default}">
            </a>  
            <h3> ${pokemon.name} </h3>
        `
        lst.appendChild(itemElement);

    });

}

getInformationHome() 
