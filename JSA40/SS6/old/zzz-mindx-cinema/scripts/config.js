export const TMDB_API_KEY="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZDJiZWNkNTM0YmFiYjUxOTM4NTU1MTBlODY2NzBiYiIsIm5iZiI6MTczOTk4Mzk0OC41MjYsInN1YiI6IjY3YjYwYzRjZDI4ZTg3ZTBlNWUzZTE3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eFzofQcXDS15kmhqdUl1U2fpkBp9HHbQmP6nuRJn9uw"

const options = {
    method: 'GET',
    headers: {
      accept: 'application/json',
      Authorization: `Bearer ${TMDB_API_KEY}`
    }
  };