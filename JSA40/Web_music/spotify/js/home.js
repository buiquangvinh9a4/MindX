const CLIENT_ID = "3e9f98a5d5194c2ab4ef3ec273f8dcdc";
const CLIENT_SECRET = "3190c7f495fa4e658136edb359a6cb55";
const artistId = "0TnOYISbd1XYRBk9myaseg"; //

async function getAccessToken() {
    const response = await fetch("https://accounts.spotify.com/api/token", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + btoa(`${CLIENT_ID}:${CLIENT_SECRET}`)
        },
        body: "grant_type=client_credentials"
    });

    const data = await response.json();
    return data.access_token;
}

async function getTopAlbum () {
    const token = await getAccessToken();
    
    const response = await fetch(`https://api.spotify.com/v1/artists/${artistId}/top-tracks?market=VN`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });
    const data = await response.json();
    const albums = data.tracks;
    const albumList = document.getElementById('album-list');



    albums.forEach(album => {
        let itemElement = document.createElement("div");
        itemElement.innerHTML = 
        `
        <div class = "album" data-id="${album.id}">
             <a href="song.html?id=${album.id}"> <img class="al" src="${album.album.images[0].url}"  alt=""></a>
             <h5>${album.name}</h5>
            </div>
        `
        albumList.appendChild(itemElement);
        console.log(album.id)

    });
    // albums.forEach(album => {
    //     const itemElement = document.createElement('div');
    //     itemElement.classList.add("album");
    //     itemElement.innerHTML = 
    //     `
    //          <a href="#"> <img class="al" src="${album.album.images[0].url}"  alt=""></a>
    //          <h5>${album.album.name}</h5>
    //     `
    //     albumList.appendChild(itemElement);
    //     console.log(album.album.id)

    // });

}


getTopAlbum ()

