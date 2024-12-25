
# 00-project-intro

# Flixx App Project Intro

In this project, we are going to build a movie info application that will fetch data from the [TMDB](https://www.themoviedb.org/) API and display it in a nice way. The app will have the following features:

- Display the most popular movies
- Display the most popular TV shows
- Show specific movie details
- Show specific TV show details
- Display the 'Now Playing' movies in a slider
- Allow users to search for movies and TV shows
- Have pagination for search results

We will be working with the fetch api, async/await, the DOM and pretty much everything that we have talked about up until this point.

<img src="./images/screen.jpg" width="500">


---


# 01-theme-overview-prep

# Theme Overview & Prep

I am going to include an initial theme (flix-app-theme) that includes the HTML, CSS and any assets that the website uses. This will allow you to get started quickly and focus on the JavaScript.

The theme includes the following:

- HTML: All of the html pages including index.html, shows.html, movie-details.html, show-details.html and search.html.
- CSS: The main stylesheet (style.css) and the spinner.css stylesheet
- Images: There is a no-image.jpg that we will use for when there is no image available for a movie or TV show. There is also a showcase/slider background image
- Libraries: There is a `lib` folder which includes the CSS/JS files for the Swiper Slider that we will use. There is also a font-awesome CSS file as well as a `webfonts` folder that contains the font files for font-awesome.

## Getting Started

Simply rename the `flix-app-theme` folder to `flix-app` and open it in your code editor. Then open the `index.html` file in VS Code and run it with `Live Server`. Don't just open the index.html on your filesystem because the CSS and JS files may not load. You should have some kind of server running that will serve the files.

You may want to initialize your git repo at this point and commit the files. You can then create a new repo on GitHub and push the files to it.


---


# 02-api-overview-and-key

# API Overview & API Key

We will be using the [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api) to get the data for our app. You will need to create an account and get an API key. The API key is free and you can get one by following these steps:

1. Go to the [TMDb website](https://www.themoviedb.org/)
2. Click on the `Sign Up` button in the top right corner
3. Fill out the form and click `Sign Up`
4. Once you are logged in, click on your avatar in the top right corner and select `Settings`
5. Click on the `API` tab
6. Click on the `Create` button
7. Enter a name for your API key and click `Save`
8. Copy the API key and paste it into a text file. You will need it later

All of the API documentation at the https://developers.themoviedb.org/3. We are using version 3 of the API. The API documentation is very good and you should read through it to get a better understanding of how the API works.

Here are the endpoints that we will need to hit to get the data for the app. You will need to send your API key with every request.

- [Get Popular Movies](https://api.themoviedb.org/3/movie/popular)
- [Get Popular TV Shows](https://api.themoviedb.org/3/tv/popular)
- [Get Movie Details](https://api.themoviedb.org/3/movie/MOVIE_ID)
- [Get TV Show Details](https://api.themoviedb.org/3/tv/SHOW_ID)
- [Get Now Playing Movies](https://api.themoviedb.org/3/movie/now_playing)
- [Search Movies](https://api.themoviedb.org/3/search/movie?query=QUERY)
- [Search TV Shows](https://api.themoviedb.org/3/search/tv?query=QUERY)


---


# 03-page-router-active-link

# Page Router & Active Link

Since we will have multiple HTML pages in the project and we need to run different JavaScript code on each page, we will be creating a very simple page router using a `switch` statement. We will also be creating a function to add an `active` class to the active link in the navigation.

## App State

At the very top of the JS file, we will have a `global` object for our global state. This will include any values that we will need in multiple places. We will create a `currentPage` property and set it to `window.location.pathname`. This will give us the current page path.

```js
const global = {
  currentPage: window.location.pathname,
};
```

## Init() and Router

We will have an `init()` function that will run when the DOM loads and this is where we will add the router code. Right now, we will just add a `console.log()` statement for each page. We will add the code to the `init()` function later.

```js
// Init App
function init() {
  switch (global.currentPage) {
    case '/':
    case '/index.html':
      console.log('Home');
      break;
    case '/shows.html':
      console.log('Shows');
      break;
    case '/movie-details.html':
      console.log('Movie Details');
      break;
    case '/tv-details.html':
      console.log('TV Details');
      break;
    case '/search.html':
      console.log('Search');
      break;
  }
}

document.addEventListener('DOMContentLoaded', init);
```

## Highlight Active Link

Let's create a function to highlight the nav link for the current page. We will add a `active` class to the link. We will also remove the `active` class from any other links. We will call the `highlightActiveLink()` function in the `init()` function.

```js
// Highlight active link
function highlightActiveLink() {
  const links = document.querySelectorAll('.nav-link');
  links.forEach((link) => {
    if (link.getAttribute('href') === global.currentPage) {
      link.classList.add('active');
    }
  });
}
```

```js
// Init App
function init() {
  // ...
  highlightActiveLink();
}
```

Now you should see the link highlight and the `console.log()` for each page.


---


# 04-display-popular-movies

# Display Popular Movies

In this section, we will be displaying the popular movies on the home screen of the app. We will be using the [Get Popular Movies](https://api.themoviedb.org/3/movie/popular) endpoint to get the data. The endpoint returns a list of movies sorted by popularity.

## `fetchAPIData()` function

We are going to create a function called `fetchAPIData()` that will be used to fetch data from the API. We will pass in the URL for the endpoint as a parameter.

```js
async function fetchAPIData(endpoint) {
  const API_KEY = ''; // Put your api key here
  const API_URL = 'https://api.themoviedb.org/3/';

  const response = await fetch(
    `${API_URL}${endpoint}?api_key=${API_KEY}&language=en-US`
  );

  const data = await response.json();

  return data;
}
```

This function will reach out to the server and get the data that we need using the endpoint that is passed in. It will then return the data as a JavaScript object.

It is important to understand that the API Key is public in this case. This is only for development and small projects. For real production projects, you should not store your API Key in your code. You should store it in a server and make requests from there. That is beyond what we have covered so far. I may do that later on in the course.

## `displayPopularMovies()` function

Now we can create a function to display the popular movies. We will call the `fetchAPIData()` function and pass in the endpoint. We will then loop through the results and display the data. We will add a link to the movie details page as well. This will include the id of the movie.

```js
async function displayPopularMovies() {
  const { results } = await fetchAPIData('movie/popular');

  results.forEach((movie) => {
    const div = document.createElement('div');
    div.classList.add('card');
    div.innerHTML = `
          <a href="movie-details.html?id=${movie.id}">
            ${
              movie.poster_path
                ? `<img
              src="https://image.tmdb.org/t/p/w500${movie.poster_path}"
              class="card-img-top"
              alt="${movie.title}"
            />`
                : `<img
            src="../images/no-image.jpg"
            class="card-img-top"
            alt="${movie.title}"
          />`
            }
          </a>
          <div class="card-body">
            <h5 class="card-title">${movie.title}</h5>
            <p class="card-text">
              <small class="text-muted">Release: ${movie.release_date}</small>
            </p>
          </div>
        `;

    document.querySelector('#popular-movies').appendChild(div);
  });
}
```

## Remove Hardcoded Movies

In the `index.html` file, we have some hardcoded movies. We can remove those now. Every div that has the class of `card` can be removed. So the div with the id of `popular-movies` should be empty.

We will call the `displayPopularMovies()` function in the `switch` statement.

```js
switch (global.currentPage) {
  case '/':
  case '/index.html':
    displayPopularMovies();
    break;
  // ...
}
```

Now you should see 20 popular movies on the page


---


# 05-spinner-display-popular-shows

# Spinner and Display Popular Shows

One thing I want to do before we fetch the TV shows, is add a spinner to display while data is being fetched. This will give the user some feedback that the app is working.

In the HTML, there is

```HTML
<div class="spinner"></div>
```

If you add a class of `show` to that div, it will display the spinner. We will add this class when we are fetching the data. Let's create a function to show and hide the spinner.

```js
function showSpinner() {
  document.querySelector('.spinner').classList.add('show');
}

function hideSpinner() {
  document.querySelector('.spinner').classList.remove('show');
}
```

Now in the `fetchAPIData()` function, we can call the `showSpinner()` function before we fetch the data. We can also call the `hideSpinner()` function after the data is fetched.

```js
async function fetchAPIData(endpoint) {
  const API_KEY = '';
  const API_URL = 'https://api.themoviedb.org/3/';

  showSpinner();

  const response = await fetch(
    `${API_URL}${endpoint}?api_key=${API_KEY}&language=en-US`
  );

  const data = await response.json();

  hideSpinner();

  return data;
}
```

## `displayPopularShows()` function

Now we can create a function to display the popular shows. We will call the `fetchAPIData()` function and pass in the endpoint. We will then loop through the results and display the data. We will add a link to the show details page as well. This will include the id of the show.

```js
async function displayPopularShows() {
  const { results } = await fetchAPIData('tv/popular');

  results.forEach((show) => {
    const div = document.createElement('div');
    div.classList.add('card');
    div.innerHTML = `
          <a href="tv-details.html?id=${show.id}">
            ${
              show.poster_path
                ? `<img
              src="https://image.tmdb.org/t/p/w500${show.poster_path}"
              class="card-img-top"
              alt="${show.name}"
            />`
                : `<img
            src="../images/no-image.jpg"
            class="card-img-top"
            alt="${show.name}"
          />`
            }
          </a>
          <div class="card-body">
            <h5 class="card-title">${show.name}</h5>
            <p class="card-text">
              <small class="text-muted">Air Date: ${show.first_air_date}</small>
            </p>
          </div>
        `;

    document.querySelector('#popular-shows').appendChild(div);
  });
}
```

Remove all of the hardcoded show divs with the class of `card` in the `shows.html` file. You should now see a list of popular TV shows.

Now add the `displayPopularShows()` function to `switch` statement

```js
// Init App
function init() {
  switch (global.currentPage) {
    // ...
    case '/shows.html':
      displayPopularShows();
      break;
    // ...
  }
}
```


---


# 06-movie-details-page

# Movie Details Page

Right now, when we click a movie on the homepage, it brings us to a url like this:

`/movie-details.html?id=550988`

We need to create a function to get the movie id from the url and then fetch the movie data from the API. We will call it `displayMovieDetails()`.

We will use the `window.location.search` property to get the query string from the url. The query string will look like this: `?id=550988`. We will use the `split()` method to split the string at the `=` sign and then get the second item in the array, which will be the movie id.

We then use the `fetchAPIData()` function to fetch the movie data from the API. We pass in the `movie/${movieId}` as the endpoint. Then we add the movie data to the DOM.

```js
async function displayMovieDetails() {
  const movieId = window.location.search.split('=')[1];

  const movie = await fetchAPIData(`movie/${movieId}`);

  const div = document.createElement('div');

  div.innerHTML = `
  <div class="details-top">
  <div>
  ${
    movie.poster_path
      ? `<img
    src="https://image.tmdb.org/t/p/w500${movie.poster_path}"
    class="card-img-top"
    alt="${movie.title}"
  />`
      : `<img
  src="../images/no-image.jpg"
  class="card-img-top"
  alt="${movie.title}"
/>`
  }
  </div>
  <div>
    <h2>${movie.title}</h2>
    <p>
      <i class="fas fa-star text-primary"></i>
      ${movie.vote_average.toFixed(1)} / 10
    </p>
    <p class="text-muted">Release Date: ${movie.release_date}</p>
    <p>
      ${movie.overview}
    </p>
    <h5>Genres</h5>
    <ul class="list-group">
      ${movie.genres.map((genre) => `<li>${genre.name}</li>`).join('')}
    </ul>
    <a href="${
      movie.homepage
    }" target="_blank" class="btn">Visit Movie Homepage</a>
  </div>
</div>
<div class="details-bottom">
  <h2>Movie Info</h2>
  <ul>
    <li><span class="text-secondary">Budget:</span> $${addCommasToNumber(
      movie.budget
    )}</li>
    <li><span class="text-secondary">Revenue:</span> $${addCommasToNumber(
      movie.revenue
    )}</li>
    <li><span class="text-secondary">Runtime:</span> ${
      movie.runtime
    } minutes</li>
    <li><span class="text-secondary">Status:</span> ${movie.status}</li>
  </ul>
  <h4>Production Companies</h4>
  <div class="list-group">
    ${movie.production_companies
      .map((company) => `<span>${company.name}</span>`)
      .join(', ')}
  </div>
</div>
  `;

  document.querySelector('#movie-details').appendChild(div);
}
```

Notice that we used a function called `addCommasToNumber()` to add commas to the budget and revenue numbers. Let's create that now.

```js
function addCommasToNumber(number) {
  return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}
```

This function uses the `replace()` method to replace every three digits with a comma. It takes in a regular expression. We have not gone over regular expressions yet, but it is something that we will get to soon. For now, just know that it is a way to match patterns in strings.

Call the `displayMovieDetails()` function in the `switch` statement:

```js
// Init App
function init() {
  switch (global.currentPage) {
    // ...
    case '/movie-details.html':
      displayMovieDetails();
      break;
    // ...
  }
}
```


---


# 07-details-page-backdrop

# Details Page Backdrop

The API that we are working with gives us a link to a really cool backdrop image of the movie or show that we are fetching. We can use this image to create a nice background for our details page.

Let's create a function called `displayBackgroundImage` that will take in a type and a path. The type will be either `movie` or `tv` and the path will be the backdrop path that we get from the API.

```js
// Display Backdrop On Details Pages
function displayBackgroundImage(type, backgroundPath) {
  const overlayDiv = document.createElement('div');
  overlayDiv.style.backgroundImage = `url(https://image.tmdb.org/t/p/original/${backgroundPath})`;
  overlayDiv.style.backgroundSize = 'cover';
  overlayDiv.style.backgroundPosition = 'center';
  overlayDiv.style.backgroundRepeat = 'no-repeat';
  overlayDiv.style.height = '100vh';
  overlayDiv.style.width = '100vw';
  overlayDiv.style.position = 'absolute';
  overlayDiv.style.top = '0';
  overlayDiv.style.left = '0';
  overlayDiv.style.zIndex = '-1';
  overlayDiv.style.opacity = '0.1';

  if (type === 'movie') {
    document.querySelector('#movie-details').appendChild(overlayDiv);
  } else {
    document.querySelector('#show-details').appendChild(overlayDiv);
  }
}
```

So what we are doing here is taking in the type, which will be tv or movie and then the path, which will come from the api. Then we are just setting the image and a bunch of background styles to the overlay div. We are also appending it to the movie details or show details div depending on the type.

We can then call this function in our `displayMovieDetails` and `displayShowDetails` functions.

```js
async function displayMovieDetails() {
  const movieId = window.location.search.split('=')[1];

  const movie = await fetchAPIData(`movie/${movieId}`);

  // Overlay for background image
  displayBackgroundImage('movie', movie.backdrop_path);

  // ...
}

async function displayShowDetails() {
  const showId = window.location.search.split('=')[1];

  const show = await fetchAPIData(`tv/${showId}`);

  // Overlay for background image
  displayBackgroundImage('tv', show.backdrop_path);

  // ...
}
```


---


# 08-show-details-page

# Show Details Page

Just like we did with movies, we need to create a page to show the details of a TV show. This will be on the `tv-details.html` page. We will create a function called `displayShowDetails()` to get the show id from the url and then fetch the show data from the API.

```js
// Display Show Details
async function displayShowDetails() {
  const showId = window.location.search.split('=')[1];

  const show = await fetchAPIData(`tv/${showId}`);

  // Overlay for background image
  displayBackgroundImage('tv', show.backdrop_path);

  const div = document.createElement('div');

  div.innerHTML = `
  <div class="details-top">
  <div>
  ${
    show.poster_path
      ? `<img
    src="https://image.tmdb.org/t/p/w500${show.poster_path}"
    class="card-img-top"
    alt="${show.name}"
  />`
      : `<img
  src="../images/no-image.jpg"
  class="card-img-top"
  alt="${show.name}"
/>`
  }
  </div>
  <div>
    <h2>${show.name}</h2>
    <p>
      <i class="fas fa-star text-primary"></i>
      ${show.vote_average.toFixed(1)} / 10
    </p>
    <p class="text-muted">Last Air Date: ${show.last_air_date}</p>
    <p>
      ${show.overview}
    </p>
    <h5>Genres</h5>
    <ul class="list-group">
      ${show.genres.map((genre) => `<li>${genre.name}</li>`).join('')}
    </ul>
    <a href="${
      show.homepage
    }" target="_blank" class="btn">Visit show Homepage</a>
  </div>
</div>
<div class="details-bottom">
  <h2>Show Info</h2>
  <ul>
    <li><span class="text-secondary">Number of Episodes:</span> ${
      show.number_of_episodes
    }</li>
    <li><span class="text-secondary">Last Episode To Air:</span> ${
      show.last_episode_to_air.name
    }</li>
    <li><span class="text-secondary">Status:</span> ${show.status}</li>
  </ul>
  <h4>Production Companies</h4>
  <div class="list-group">
    ${show.production_companies
      .map((company) => `<span>${company.name}</span>`)
      .join(', ')}
  </div>
</div>
  `;

  document.querySelector('#show-details').appendChild(div);
}
```

Call the function in the `switch` statement:

```js
// Init App
function init() {
  switch (global.currentPage) {
    // ...
    case '/tv-details.html':
      displayShowDetails();
      break;
    // ...
  }
}
```


---


# 09-swiper-slider

# Swiper Slider

The Swiper Slider is a popular slider library. We will use it to display the 'now playing' movies on the home/movies page.

I already included the `swiper.js` and `swiper.css` in the `lib` folder and it is already included in the `index.html` file.

Let's create a function called `displaySwiperSlider` that will take in the movies array and display the slider.

```js
// Display Slider Movies
async function displaySlider() {
  const { results } = await fetchAPIData('movie/now_playing');

  results.forEach((movie) => {
    const div = document.createElement('div');
    div.classList.add('swiper-slide');

    div.innerHTML = `
      <a href="movie-details.html?id=${movie.id}">
        <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}" />
      </a>
      <h4 class="swiper-rating">
        <i class="fas fa-star text-secondary"></i> ${movie.vote_average} / 10
      </h4>
    `;

    document.querySelector('.swiper-wrapper').appendChild(div);

    initSwiper();
  });
}
```

Here we fetched the `now_playing` movies and looped through them. For each movie, we created a `div` element and added the `swiper-slide` class to it. Then we added the movie poster image and the rating. We also are calling a function called `initSwiper` that will initialize the slider.

```js
function initSwiper() {
  const swiper = new Swiper('.swiper', {
    slidesPerView: 1,
    spaceBetween: 30,
    freeMode: true,
    loop: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
    },
    breakpoints: {
      500: {
        slidesPerView: 2,
      },
      700: {
        slidesPerView: 3,
      },
      1200: {
        slidesPerView: 4,
      },
    },
  });
}
```

We need to call the `displaySlider()` function in the `switch` statement on the home/index page

```js
switch (global.currentPage) {
  case '/':
  case '/index.html':
    displaySlider();
    displayPopularMovies();
    break;
  // ...
}
```


---


# 10-search-function-and-alert

# Search Function & Custom Alert

In this lesson, we will start to add our search functionality. We will also create a custom alert function that will display a message to the user.

## Search Info In Global State

We are going to need to access certain search info in multiple places in our app, so I am going to add a search object to the `global` object. I am also going to move the api key and api url into the global object because we will have a separate function for the search requests and we need those pieces of info in that function.

```js
const global = {
  currentPage: window.location.pathname,
  search: {
    term: '',
    type: '',
    page: 1,
    totalPages: 1,
  },
  api: {
    apiKey: '',
    apiUrl: 'https://api.themoviedb.org/3/',
  },
};
```

The page stuff is for pagination. We will add that later. We are concerned with the search term and the search type right now.

## `search()` Function

Let's create the `search()` function that will fetch the search results from the API and display them. We run a function called `searchAPIData()` to fetch the data from the API. We will create that function next. For now, we are just logging the data.

We also call a function called `showAlert()` to display a message to the user if something went wrong. We will create that function as well.

```js
async function search() {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  // Add the type and term to the global object
  global.search.type = urlParams.get('type');
  global.search.term = urlParams.get('search-term');

  if (global.search.term !== '' && global.search.term !== null) {
    const results = await searchAPIData();
    console.log(results);
  } else {
    showAlert('Please enter a search term');
  }
}
```

## `searchAPIData()` Function

Notice we used a different function for getting data. We are going to create a function called `searchAPIData()` because the request is a bit different than the other requests we have made.

```js
// Make Request To Search
async function searchAPIData() {
  const API_KEY = global.api.apiKey;
  const API_URL = global.api.apiUrl;

  showSpinner();

  const response = await fetch(
    `${API_URL}search/${global.search.type}?api_key=${API_KEY}&language=en-US&query=${global.search.term}`
  );

  const data = await response.json();

  hideSpinner();

  return data;
}
```

Also, change the api key and url lines in the `fetchAPIData()` function to use the global object.

```js
async function fetchAPIData() {
  const API_KEY = global.api.apiKey;
  const API_URL = global.api.apiUrl;

  // ...
}
```

Our form in the html has an `action` attribute that submits to the `search.html` page. We will call the `search()` function within the `switch` statement on the search page.

```js
switch (global.currentPage) {
  case '/search.html':
    search();
    break;
  // ...
}
```

## `showAlert()` Function

We are going to create a function that will display a message to the user. It will take in a message and a class name. The class name will be used to style the alert. It will use the `alert` class and the class name that is passed in. The class name will be `error` by default.

```js
// Show Alert
function showAlert(message, className = 'error') {
  const alertEl = document.createElement('div');
  alertEl.classList.add('alert', className);
  alertEl.appendChild(document.createTextNode(message));
  document.querySelector('#alert').appendChild(alertEl);

  setTimeout(() => alertEl.remove(), 3000);
}
```


---


# 11-display-search-results

# Display Search Results

In the last lesson, we made it so that we could search for a term and get the data and log it. Now we will display the results on the page. Let's add to the `search()` function.

```js
async function search() {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);

  // Add the type and term to the global object
  global.search.type = urlParams.get('type');
  global.search.term = urlParams.get('search-term');

  if (global.search.term !== '' && global.search.term !== null) {
    const { results, total_pages, page } = await searchAPIData();

    if (results.length === 0) {
      showAlert('No results found');
      return;
    }

    displaySearchResults(results);

    document.querySelector('#search-term').value = '';
  } else {
    showAlert('Please enter a search term');
  }
}
```

Now we are destructuring the results from the `searchAPIData()` function. We are also getting the `total_pages` and `page` from the API. We will use these to display the pagination. For now, we only need the `results` array. We will pass that into the `displaySearchResults()` function. Let's create that function now.

```js
function displaySearchResults(results) {
  results.forEach((result) => {
    const div = document.createElement('div');
    div.classList.add('card');
    div.innerHTML = `
          <a href="${global.search.type}-details.html?id=${result.id}">
            ${
              result.poster_path
                ? `<img
              src="https://image.tmdb.org/t/p/w500/${result.poster_path}"
              class="card-img-top"
              alt="${
                global.search.type === 'movie' ? result.title : result.name
              }"
            />`
                : `<img
            src="../images/no-image.jpg"
            class="card-img-top"
             alt="${
               global.search.type === 'movie' ? result.title : result.name
             }"
          />`
            }
          </a>
          <div class="card-body">
            <h5 class="card-title">${
              global.search.type === 'movie' ? result.title : result.name
            }</h5>
            <p class="card-text">
              <small class="text-muted">Release: ${
                global.search.type === 'movie'
                  ? result.release_date
                  : result.first_air_date
              }</small>
            </p>
          </div>
        `;

    document.querySelector('#search-results').appendChild(div);
  });
}
```

Now we are showing the results on the page in cards. You can remove any hardcoded data from the HTML and CSS. In the next lesson, we will implement the pagination.


---


# 12-search-pagination

# Search Pagination

We are now able to search for movies and TV shows, but we only display 20 at a time. We need to add pagination to the search results.

## Add Dynamic Heading

One thing I want to do before that is show a heading that says "X of Y results found for MOVIE NAME". Let's start by adding `totalResults` to the `global` object:

```js
const global = {
  // ...
  search: {
    term: '',
    type: '',
    page: 1,
    totalPages: 1,
    totalResults: 0, // Add this
  },
  // ...
};
```

In the `search()` function, we will add `totalResults` to the global object:

```js
// ...
const { results, total_pages, page, total_results } = await searchAPIData();
global.search.totalResults = total_results;
// ...
```

Now at the bottom of `displaySearchResults()`, right above where we add the results to the DOM, add the following code:

```js
document.querySelector('#search-results-heading').innerHTML = `
              <h2>${results.length} of ${global.search.totalResults} Results for ${global.search.term}</h2>
    `;
```

## Add Pagination

The pagination HTML is in the `search.html` file. We need to cut the following code:

```html
<div class="pagination">
  <button class="btn btn-primary" id="prev">Prev</button>
  <button class="btn btn-primary" id="next">Next</button>
  <div class="page-counter">Page 1 of 5</div>
</div>
```

Keep the div with the `id` of pagination. The class and everything within it can be cut because we will insert it with JavaScript and make it dynamic.

## `displayPagination()` Function

This function will display the HTML and include a `prev` and `next` event listener. When the user clicks on the `prev` or `next` button, it will change the page number and call the `searchAPIData()` function again with the page number needed. Then we will call displaySearchResults() with the new results.

```js
// Create & Display Pagination For Search
function displayPagination() {
  const div = document.createElement('div');
  div.classList.add('pagination');
  div.innerHTML = `
  <button class="btn btn-primary" id="prev">Prev</button>
  <button class="btn btn-primary" id="next">Next</button>
  <div class="page-counter">Page ${global.search.page} of ${global.search.totalPages}</div>
  `;

  document.querySelector('#pagination').appendChild(div);

  // Disable prev button if on first page
  if (global.search.page === 1) {
    document.querySelector('#prev').disabled = true;
  }

  // Disable next button if on last page
  if (global.search.page === global.search.totalPages) {
    document.querySelector('#next').disabled = true;
  }

  // Next page
  document.querySelector('#next').addEventListener('click', async () => {
    global.search.page++;
    const { results, total_pages } = await searchAPIData();
    displaySearchResults(results);
  });

  // Prev page
  document.querySelector('#prev').addEventListener('click', async () => {
    global.search.page--;
    const { results, total_pages } = await searchAPIData();
    displaySearchResults(results);
  });
}
```

We do need to update the `searchAPIData()` function to include the page number:

```js
const response = await fetch(
  `${API_URL}search/${global.search.type}?api_key=${API_KEY}&language=en-US&query=${global.search.term}&page=${global.search.page}`
);
```

That's it! Our application is complete! We can now search for movies and TV shows, and we can paginate through the results.
