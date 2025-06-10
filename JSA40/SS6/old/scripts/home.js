import { API_OPTIONS } from "./config.js"; // Import từ config.js
import {TMDB_API_KEY} from "./config.js";
const API_URL = 'https://api.themoviedb.org/3/trending/movie/day??api_key=${API_KEY}';
const API_URL2 = 'https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}'
const API_URL_BACKDROP = "https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}"
async function fetchMovies() {
    try {
        const response = await fetch(API_URL, API_OPTIONS);
        const response2 = await fetch(API_URL2, API_OPTIONS); 

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        if (!response2.ok) {
            throw new Error(`HTTP error! Status: ${response2.status}`);
        }

        const data = await response.json();
        const data2 = await response2.json();
        displayMovies(data.results, "movie-list");
        displayMovies(data2.results, "rank-list");
    } catch (error) {
        console.error("Lỗi khi lấy dữ liệu:", error);
    }
}

async function fetchBackdrop() {
    const response = await fetch(API_URL_BACKDROP, API_OPTIONS);
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`)
    }

    const data = await response.json();
    const resultsData = data["results"]
    console.log(resultsData);
    displayBackdrop(resultsData)
}

function displayBackdrop(back) {
    const backElement = document.getElementById("hero-image");
    const backTitle = document.getElementById("hero-title");
    console.log(backTitle)
    let index = 0;
    function changeBackdrop() {
        if (index >= back.length) {
            index = 0; // Quay lại ảnh đầu tiên nếu hết danh sách
        }

        let path = back[index].backdrop_path;
        let title = back[index].title;

        // Làm ảnh cũ mờ dần
        backElement.classList.remove("active");

        setTimeout(() => {
            backTitle.innerText = title;
            backElement.src = "https://image.tmdb.org/t/p/original" + path;
            // Khi ảnh mới load xong, làm nó sáng dần
            backElement.onload = () => {
                backElement.classList.add("active");
            };

            index++; // Tăng index cho lần tiếp theo
        }, 500); // Chờ 1 giây trước khi đổi ảnh

        setTimeout(changeBackdrop, 4000); // Gọi lại sau 4 giây
    }

    changeBackdrop(); // Bắt đầu vòng lặp
}   

function displayMovies(movies, _id) {
    const movieList = document.getElementById(_id);
    movieList.innerHTML = ""; // Xóa nội dung cũ

    movies.forEach(movie => {
        const movieElement = document.createElement("div");
        movieElement.classList.add("movie");

        movieElement.innerHTML = `
            <a href=""> <img src="https://image.tmdb.org/t/p/w200${movie.poster_path}" alt="${movie.title}"></a>
            
            <div class="movie-title">${movie.title}</div>
        `;

        movieList.appendChild(movieElement);
    });
}



    fetchMovies();
    fetchBackdrop();