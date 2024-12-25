
# 01-what-are-web-apis

# What Are Web/Browser APIs?

Web APIs, also known as browser APIs are a set of tools that allow developers to interact with the browser and its features. They are not part of the core JavaScript language, but they are built into the browser and can be accessed using JavaScript. We don't need to use any external libraries to use them, they are already built into the browser.

We have already used a few Web APIs in previous chapters, such as the DOM API, the Fetch API and the localStorage API. In this section, we are going to dive into some others and create some small projects using them.

The web APIs that we will be going over include:

- The Geolocation API
- The Canvas API
- The Web Audio API
- The Web Video API
- The WebRTC API
- The Web Workers API
- The WebSockets API
- The Web Animation API
- The Web Speech API
- The Web Bluetooth API


---


# 02-geolocation-api

# Geolocation API

The Geolocation API allows us to access the user's location. It is part of the HTML5 specification and is supported by all modern browsers. For privacy reasons, the user is asked for permission to report location information. If the user grants permission, the location information is made available to the web page. I'm sure most of you have seen this when the webpage asks you if it can access your location.

## Why use the Geolocation API?

The Geolocation API is useful for a variety of applications. For example, if you are building a weather app, you can use the Geolocation API to get the user's location and then use that information to display the weather for that location. You can also use the Geolocation API to build a map app that shows the user's location on a map.

There are 2 main methods that we can use to access the user's location:

- `navigator.geolocation.getCurrentPosition()` - This method is used to get the user's current position.
- `navigator.geolocation.watchPosition()` - This method is used to watch the user's position for changes.

## Getting the user's current position

The `navigator.geolocation.getCurrentPosition()` method is used to get the user's current position. It takes 2 callback functions as parameters as well as a third optional parameter that is an object containing options.

- `success` - This callback function is called if the user's location is successfully retrieved.
- `error` - This callback function is called if there is an error getting the user's location.
- `options` - Options about how to get the user's location. This is an optional parameter.

Let's call the method, with named functions as the callbacks:

```js
navigator.geolocation.getCurrentPosition(curSuccess, curError, curOptions);
```

Let's create the success function:

```js
function curSuccess(pos) {
  const coords = pos.coords;

  console.log('Current position is:');
  console.log(`Latitude : ${coords.latitude}`);
  console.log(`Longitude: ${coords.longitude}`);
  console.log(`More or less ${coords.accuracy} meters.`);
}
```

Let's create the error function:

```js
function curError(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}
```

Let's create the options object:

```js
const curOptions = {
  enableHighAccuracy: true, // use GPS if available
  timeout: 5000, // wait 5 seconds before giving up
  maximumAge: 0, // do not use a cached position
};
```

As you can see, it will show your latitude and longitude as well as the accuracy of the location. The accuracy is the radius of a 95% confidence interval. In other words, it is the radius of a circle centered at the given position, where the probability of the device's position being within the circle is 95%.

My location is based on my VPN so it is not accurate. If you are using a VPN, make sure to disable it before testing this.

## Watching the user's position

Let's call the `navigator.geolocation.watchPosition()` method, with named functions as the callbacks:

```js
navigator.geolocation.watchPosition(watchSuccess, watchError, watchOptions);
```

Let's create the success function. We can also create a target that when that target is reached, it can do something. In this case, we will just log a message to the console when the target is reached. We won't see the message, because obviously I am not moving, while I'm sitting here creating a tutorial. But if you were to move and reach the target, you would see the message in the console.

```js
let target = {
  latitude: 41.7568588,
  longitude: -71.6789246,
};
```

```js
function watchSuccess(pos) {
  const coords = pos.coords;

  if (
    target.latitude === coords.latitude &&
    target.longitude === coords.longitude
  ) {
    console.log('Congratulations, you reached the target');
    navigator.geolocation.clearWatch(id);
  }
}
```

Let's create the error function:

```js
function watchError(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}
```

And the options:

```js
const watchOptions = {
  enableHighAccuracy: false, // use GPS if available
  timeout: 5000, // wait 5 seconds before giving up
  maximumAge: 0, // do not use a cached position
};
```

This method returns an ID that we can use to stop watching the user's position. We used this in the success function with the `navigator.geolocation.clearWatch()` method to stop watching the user's position.

```js
const id = navigator.geolocation.watchPosition(
  watchSuccess,
  watchError,
  watchOptions
);
console.log(id);
```


---


# 03-location-map

# Plotting Your Location on a Map

In this lesson, you will learn how to use the Geolocation API along with a map library called `Leaflet` to plot your location on a map.

The Leaflet website is located at [https://leafletjs.com/](https://leafletjs.com/). If you go to `Tutorials->Get Started`, you will see the code to add Leaflet to your project. We can include the CDN in our HTML. Your HTML page should look like this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"
      integrity="sha256-kLaT2GOSpHechhsozzB+flnD+zUyjE2LlfWPgU04xyI="
      crossorigin=""
    />
    <title>My Location</title>

    <style>
      #map {
        height: 600px;
        width: 600px;
      }
    </style>
  </head>
  <body>
    <h1>My Location</h1>

    <div id="map"></div>
    <script
      src="https://unpkg.com/leaflet@1.9.3/dist/leaflet.js"
      integrity="sha256-WBkoXOwTeyKclOHuWtc+i2uENFpDZ9YPdf5Hf+D7ewM="
      crossorigin=""
    ></script>
    <script src="script.js"></script>
  </body>
</html>
```

We brought in the CSS and JS and added a div for the map to display. I also set the size to 600x600. Now we need to add the JavaScript to plot our location on the map.

Let's start by displaying the map:

```js
// Initialize the map
const map = L.map('map').setView([0, 0], 2);

// Add a tile layer to the map
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);
```

This is just the basic code from the docs to display a map. It will show the whole world. Now let's add a marker to the map:

```js
// Add a marker to the map
const marker = L.marker([0, 0]).addTo(map);
```

Right now, it will just display a marker in the mioddle of the map. We need to get the user's location and update the marker's position. We can do this using the Geolocation API:

```js
// Use the HTML5 geolocation API to get the current location
navigator.geolocation.getCurrentPosition(function (position) {
  // Get the coordinates of the current location
  const lat = position.coords.latitude;
  const lng = position.coords.longitude;

  // Set the marker to the current location and zoom the map
  marker.setLatLng([lat, lng]).update();
  map.setView([lat, lng], 13);

  // Add a popup to the marker
  marker.bindPopup('<b>Hello world!</b><br>This is my current location');
});
```

So we are just using the `getCurrentPosition` method to get the current location. We then get the latitude and longitude from the `position` object. We then set the marker's position to the current location and zoom the map to 13.

We can also add a popup:

```js
navigator.geolocation.getCurrentPosition(function (position) {
  // ...

  // Add a popup to the marker
  marker.bindPopup('<b>Hello world!</b><br>This is my current location');
});
```

That's it. We can now see our location on a map.


---


# 04-canvas-api

# Canvas API

The Canvas API is used to draw graphics, on the fly, via JavaScript. It is part of the HTML5 specification and is supported by all modern browsers.

## Why use the Canvas API?

The Canvas API is useful for a variety of applications. It's used a lot for gaming and animation, data visualization, photo manipulation and more.

## How does it work?

The Canvas API is based on a 2D rendering context. This context is created by the `<canvas>` element. The `<canvas>` element is a container for graphics, similar to an `<img>` element. The `<canvas>` element has a `width` and `height` attribute, just like an `<img>` element. The `width` and `height` attributes define the size of the canvas, in pixels.

Let's create a simple example. We need to add the `<canvas>` element to our HTML page. You can add a width and a height. Also, add an ID, so that we can access it from our JavaScript. I am also going to put a border on the canvas, so that we can see it.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="script.js" defer></script>
    <style>
      canvas {
        border: 1px solid black;
      }
    </style>
    <title>Canvas</title>
  </head>
  <body>
    <h1>Canvas</h1>

    <canvas id="my-canvas" width="600" height="600"></canvas>
  </body>
</html>
```

## Creating the rendering context

Now, we need to create the rendering context. We can do this in our JavaScript file. We need to get a reference to the `<canvas>` element, and then call the `getContext()` method. The `getContext()` method takes a string argument, which is the type of context we want. In this case, we want a 2D context, so we pass in the string `"2d"`. This will return a 2D rendering context object, which we can store in a variable.

```js
const canvas = document.getElementById('my-canvas');
// Create a 2D context
const ctx = canvas.getContext('2d');
```

## Drawing on the canvas

Let's start by drawing a rectangle on the canvas:

```js
ctx.fillStyle = 'green';
ctx.fillRect(10, 10, 150, 100);
```

Here we used the context object to set the fill style to green. We then used the `fillRect()` method to draw a rectangle. The `fillRect()` method takes four arguments: the x and y coordinates of the top-left corner, and the width and height of the rectangle.

## Drawing a circle

Let's draw a circle on the canvas. We can do this by using the `arc()` method. The `arc()` method takes five arguments: the x and y coordinates of the center of the circle, the radius, the start angle and the end angle. The start angle and end angle are measured in radians. We can use the `Math.PI` constant to convert degrees to radians. For example, `Math.PI / 2` is 90 degrees, and `Math.PI` is 180 degrees.

```js
ctx.beginPath();
ctx.arc(300, 300, 100, 0, Math.PI * 2);
ctx.fillStyle = 'red';
ctx.fill();
```

## Drawing text

We can draw text on the canvas using the `fillText()` method. The `fillText()` method takes three arguments: the text to draw, the x and y coordinates of the top-left corner of the text.

```js
ctx.font = '30px Arial';
ctx.fillStyle = 'blue';
ctx.fillText('Hello World', 10, 300);
ctx.strokeText('Hello World', 10, 300);
```

## Drawing lines

We can draw lines from one point to another using the `moveTo()` and `lineTo()` methods. The `moveTo()` method takes two arguments: the x and y coordinates of the starting point. The `lineTo()` method takes two arguments: the x and y coordinates of the ending point.

```js
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.lineTo(300, 300);
ctx.lineTo(10, 300);
ctx.lineTo(300, 10);
ctx.strokeStyle = 'orange';
ctx.stroke();
```

`stroke()` is used to draw the line.

## Drawing an image

We can draw an image on the canvas using the `drawImage()` method. The `drawImage()` method takes five arguments: the image to draw, the x and y coordinates of the top-left corner of the image, and the width and height of the image. The image can be an `<img>` element, a `<video>` element or a `<canvas>` element.

  Let's add an image on the page. I have a `ball.png` image in the sandbox files.

  ```html
<img src="ball.png" width="100" height="100" />
  ```

```js
const image = document.querySelector('img');
image.style.display = 'none';

image.addEventListener('load', () => {
  ctx.drawImage(image, 270, 270, 50, 50);
});
```

We brought in the image, and set the display to `none`, so that it is not visible on the page. We then added an event listener to the image, so that we can draw it on the canvas once it has loaded. We used the `drawImage()` method to draw the image on the canvas.

## Draw quadratic curves

We can draw quadratic curves using the `quadraticCurveTo()` method. This method takes four arguments: the x and y coordinates of the control point, and the x and y coordinates of the end point.

```js
ctx.beginPath();
ctx.moveTo(10, 10);
ctx.quadraticCurveTo(300, 300, 10, 300); // (cp1x, cp1y, x, y)
ctx.strokeStyle = 'purple';
ctx.stroke();
```

There are other types of curves that we can draw, such as bezier curves and arcs. You can find more information about these in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Drawing_shapes).

This is all very basic and may leave you saying, what is this actually good for? It's actually very powerful, especially when you introduce animation, which we will do in the next lesson.


---


# 05-requestAnimationFrame

# requestAnimationFrame

The `requestAnimationFrame()` method tells the browser that you wish to perform an animation and requests that the browser call a specified function to update an animation before the next repaint. The method takes as an argument a callback to be invoked before the repaint.

Let's go through this very slowly so that I can explain everything in an understandable way.

We are going to create a function called `step` to be called before the next repaint. For now, we will just log 'hello' to the console.

```js
function step() {
  console.log('Hello');
}
```

Now, I am going to call the `requestAnimationFrame()` method, passing in the `step` function as an argument. This will tell the browser to call the `step` function before the next repaint.

```js
requestAnimationFrame(step);
```

No big deal, we just see 'Hello' logged to the console once. That was just a single call to the `requestAnimationFrame()` method. Let's make it a little more interesting. Let's call the `requestAnimationFrame()` method inside the `step` function. This will tell the browser to call the `step` function before the next repaint, and then call the `step` function again before the next repaint, again and again, creating a loop.

```js
function step() {
  console.log('Hello');
  requestAnimationFrame(step);
}

requestAnimationFrame(step);
```

Now, you're seeing 'Hello' logged to the console over and over again, in a never-ending loop.

We can also pass in a timestamp to the `step` function. This is the number of milliseconds since the page was loaded. We can use this to calculate the time that has passed since the last repaint. Let's log this to the console.

```js
function step(timestamp) {
  console.log(timestamp);
  requestAnimationFrame(step);
}
```

Now, you're seeing a number logged to the console over and over again, in a never-ending loop. This number is the number of milliseconds since the page was loaded. We can use this to calculate the time that has passed since the last repaint.

```js
let start;
let done = false;

function step(timestamp) {
  if (start === undefined) {
    start = timestamp;
  }

  const elapsed = timestamp - start;
  console.log(elapsed);

  requestAnimationFrame(step);
}
```

Here, we created some variables and we are using the `start` variable to store the timestamp of the first repaint. We are then using the `elapsed` variable to store the number of milliseconds that have passed since the first repaint. We are then logging this to the console.

Let's make the animation stop after 2 seconds. We can do this by using the `done` variable. We are going to set the `done` variable to `true` after 2 seconds have passed. We are then going to check the `done` variable inside the `step` function. If the `done` variable is `true`, we are going to return from the function. This will stop the animation.

```js
function step(timestamp) {
  if (start === undefined) {
    start = timestamp;
  }

  const elapsed = timestamp - start;

  if (elapsed > 2000) {
    done = true;
  }
  if (done) {
    return;
  }
  requestAnimationFrame(step);
}
```

Now let's actually have something happen. Let's move the soccer ball image. Or, I'm sorry, the "football", image for my non-American friends. We will do this by changing the transform property of the image. I am also going to change the animation to 5 seconds.

```js
function step(timestamp) {
  if (start === undefined) {
    start = timestamp;
  }

  const elapsed = timestamp - start;

  if (elapsed > 5000) {
    done = true;
  }
  if (done) {
    return;
  }
  image.style.transform = `translateX(${elapsed / 20}px)`;
  requestAnimationFrame(step);
}
```

Let's rotate the ball as well. Just add `rotate` to the transform property.

```js
image.style.transform = `translateX(${elapsed / 20}px) rotate(${
  elapsed / 20
}deg)`;
```

Now that you know how the `canvas` API works as well as the `requestAnimationFrame()` method, in the next lesson, we will create an animated clock project.


---


# 06-animated-clock-1

# Animated Clock Project - Part 1

In this project, we will use the `canvas` api along with the `requestAnimationFrame` method to create an animated clock. This will be 2 parts. In this part, we will create the clock and animate it. In the next part, we will add a form to change the clocks colors and save the clock as an image.

## The HTML

The HTML is very simple. We just have a `canvas` element. In part 2, we will have a form to change the look of the clock, but for now, we just have the clock on the canvas.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="script.js" defer></script>

    <title>Animated Clock</title>
  </head>
  <body>
    <canvas id="canvas" width="500" height="500"></canvas>
  </body>
</html>

```

Let's start by creating our `clock()` function. This function will be called by the `requestAnimationFrame` method. For now, let's get the current time and create a new canvas context

```js
function clock() {
  const now = new Date();
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
}

clock();
```

For now, we are not using `requestAnimationFrame` because we just want to test our code without any animation. We will add the `requestAnimationFrame` method later.

## Setting Up the Canvas

Before we draw anything, we need to set some initial values for the canvas and where we will draw the clock. I want to draw in the center of the canvas. Let's add the following code:

```js
function clock() {
  const now = new Date();
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  // Setup canvas
  ctx.save(); // Save the default state
  ctx.clearRect(0, 0, 500, 500); // Clear the entire canvas
  ctx.translate(250, 250); // Move the origin to the center of the canvas
  ctx.rotate(-Math.PI / 2); // Rotate the canvas -90 degrees
  // Set some default styles
  ctx.strokeStyle = '#000000';
  ctx.fillStyle = '#f4f4f4';
  ctx.lineWidth = 5;
  ctx.lineCap = 'round';
}

clock();
```

Remember, this will run before every frame, so we need to save the default state of the canvas and restore it after we are done drawing. We do this with the `save()` and `restore()` methods. We will also use use these methods before and after we draw certain parts of the clock.

We also need to clear the canvas before we draw anything. We also need to move the origin to the center of the canvas and rotate the canvas -90 degrees. This will make it easier to draw the clock. We then set some default styles for the canvas.

## Draw clock face

Now, let's add the code to draw the clock face and border:

```js
function clock() {
  const now = new Date();
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  // Setup canvas
  ctx.save(); // Save the default state
  ctx.clearRect(0, 0, 500, 500); // Clear the entire canvas
  ctx.translate(250, 250); // Move the origin to the center of the canvas
  ctx.rotate(-Math.PI / 2); // Rotate the canvas -90 degrees

  // Set some default styles
  ctx.strokeStyle = '#000000';
  ctx.fillStyle = '#f4f4f4';
  ctx.lineWidth = 5;
  ctx.lineCap = 'round';

  // Draw clock face
  ctx.save();
  ctx.beginPath();
  ctx.lineWidth = 14;
  ctx.strokeStyle = '#800000';
  ctx.arc(0, 0, 142, 0, Math.PI * 2, true);
  ctx.stroke();
  ctx.fill();
  ctx.restore();

  ctx.restore(); // Restore the default state
}

clock();
```

We used the `save()` and `restore()` methods to save the default state of the canvas before we draw the clock border and restore it after we are done drawing the clock border. We also set the `lineWidth` to 14 and the `strokeStyle` to `#800000` before we draw the clock border. We created the circle using the `arc()` method. The `arc()` method takes 6 parameters: the x and y coordinates of the center of the circle, the radius of the circle, the starting angle, the ending angle, and a boolean value that determines if the circle is drawn clockwise or counter-clockwise. We set the starting angle to 0 and the ending angle to `Math.PI * 2` to draw a full circle.

## Draw hour lines

Now, we will draw the hour lines on the clock. I am just going to add this code rather than repeating all of the code again. Just be sure to add it right below the clock border `restore()` and above the last default state `restore()`:

```js
// Draw hour lines
ctx.save();
for (let i = 0; i < 12; i++) {
  ctx.beginPath();
  ctx.rotate(Math.PI / 6);
  ctx.moveTo(100, 0);
  ctx.lineTo(120, 0);
  ctx.stroke();
}
ctx.restore();
```

Here, we used a for loop to draw 12 lines. We used the `rotate()` method to rotate the canvas 30 degrees before drawing each line. We then used the `moveTo()` and `lineTo()` methods to draw the lines.

## Draw minute lines

```js
// Draw minute lines
ctx.save();
ctx.lineWidth = 4;
for (let i = 0; i < 60; i++) {
  // Do not draw on hour lines
  if (i % 5 !== 0) {
    ctx.beginPath();
    ctx.moveTo(117, 0);
    ctx.lineTo(120, 0);
    ctx.stroke();
  }
  ctx.rotate(Math.PI / 30);
}
ctx.restore();
```

We did the same thing here except we used a for loop to draw 60 lines. We used the `rotate()` method to rotate the canvas 6 degrees before drawing each line. We then used the `moveTo()` and `lineTo()` methods to draw the lines. We used the `stroke()` method to draw the lines. We also used an if statement to only draw the lines that are not on the hour marks. We used the `lineWidth` to 4 to make the minute marks thinner than the hour marks.

## Creating the hands

Now we have to create the clock hands. The placement on these are based on the current time. Let's first, get the hours, minutes, and seconds from the current time and log it.

```js
const hr = now.getHours() % 12;
const min = now.getMinutes();
const sec = now.getSeconds();
console.log(`${hr}:${min}:${sec}`);
```

## Set hand colors

Right now, the `strokeStyle` is set to `#000`. I want the hands to be `#800000` like the border. So we need to set that here before we draw the hands:

```js
// Color for hands
ctx.strokeStyle = '#800000';
```

## Draw hour hand

Now, let's draw the hour hand:

```js
// Write Hours
ctx.save();
ctx.rotate(
  (Math.PI / 6) * hr + (Math.PI / 360) * min + (Math.PI / 21600) * sec
);
ctx.lineWidth = 14;
ctx.beginPath();
ctx.moveTo(-20, 0);
ctx.lineTo(80, 0);
ctx.stroke();
ctx.restore();
```

The hour hand will not move yet, because we aren't using `requestAnimationFrame`, but it should be in the correct place based on the time.

We used the `rotate()` method to rotate the canvas based on the current time. We used the `lineWidth` to 14 to make the hour hand thicker than the minute and second hands. We then used the `moveTo()` and `lineTo()` methods to draw the hour hand.

## Draw minute hand

```js
// Draw minute hand
ctx.save();
ctx.rotate((Math.PI / 30) * min + (Math.PI / 1800) * sec);
ctx.lineWidth = 10;
ctx.beginPath();
ctx.moveTo(-28, 0);
ctx.lineTo(112, 0);
ctx.stroke();
ctx.restore();
```

## Draw second hand

```js
// Draw second hand
ctx.save();
ctx.rotate((sec * Math.PI) / 30);
ctx.strokeStyle = '#FF7F50';
ctx.fillStyle = '#FF7F50';
ctx.lineWidth = 6;
ctx.beginPath();
ctx.moveTo(-30, 0);
ctx.lineTo(100, 0);
ctx.stroke();
ctx.beginPath();
ctx.arc(0, 0, 10, 0, Math.PI * 2, true);
ctx.fill();
ctx.restore();
```

We also created the center circle of the clock here with the `arc()` method. We made it the same color as the second hand.

## Animating the clock

Now, we just need to add the `requestAnimationFrame` to animate the clock:

```js
function clock() {
  // ...
  requestAnimationFrame(clock);
}

requestAnimationFrame(clock);
```

We now have a working clock!


---


# 07-animated-clock-2

# Animated Clock Project - Part 2

In the last lesson, we used `canvas` to draw an animated clock. In this video, we will add a form with some CSS to change the clock colors and save the clock as an image. This is a good opportunity for you to try the color changing on your own. It is all stuff that we have worked with. You can get the value of the color inputs in the JS and simply add them as the `strokeStyle` and `fillStyle` where needed.

## Creating the form

Here is the HTML for the form. This is actually where we want to sent the default colors. The clock will directly correspond to the colors in the form.

```html
<div class="card">
  <h3>Clock Style</h3>
  <form>
    <div class="form-input">
      <label for="face-color">Face Color</label>
      <input type="color" value="#f4f4f4" id="face-color" />
    </div>
    <div class="form-input">
      <label for="border-color">Border Color</label>
      <input type="color" value="#800000" id="border-color" />
    </div>
    <div class="form-input">
      <label for="line-color">Number Lines Color</label>
      <input type="color" value="#000000" id="line-color" />
    </div>
    <div class="form-input">
      <label for="large-hand-color">Large Hands Color</label>
      <input type="color" value="#800000" id="large-hand-color" />
    </div>
    <div class="form-input">
      <label for="second-hand-color">second-hand Hand Color</label>
      <input type="color" value="#FF7F50" id="second-hand-color" />
    </div>
    <div class="form-input">
      <button id="save-btn" type="submit">Save As Image</button>
    </div>
  </form>
</div>
<canvas id="canvas" width="500" height="500"></canvas>
```

We have a little but of CSS as well...

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

body {
  font-family: 'Roboto', sans-serif;
  font-size: 18px;
}

button {
  background: #333;
  color: #fff;
  border: 0;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.card {
  background: #f4f4f4;
  border-left: 1px solid #ccc;
  border-bottom: 1px solid #ccc;
  padding: 7px 20px;
  width: 300px;
  position: absolute;
  bottom: 0;
  left: 0;
}

.form-input {
  margin-bottom: 20px;
}

label {
  margin-right: 10px;
  font-weight: bold;
}
```

Now, in the JS, we need to get the values of the inputs. We can set variables to either the elements themselves or the values of the elements. I like to set them to the element and then just add `.value()` to get the value.

```js
const faceColor = document.getElementById('face-color');
const borderColor = document.getElementById('border-color');
const lineColor = document.getElementById('line-color');
const largeHandColor = document.getElementById('large-hand-color');
const secondHandColor = document.getElementById('second-hand-color');
```

## Face & Border Color

For the face color, we are using the default `fillStyle`, So we need to add a `fillStyle` to the face code between the `save()` and `restore()`. We will set the `fillStyle` to `faceColor.value`. The `strokeStyle` is the border, so we will set that to `borderColor.value`.

```js
// Draw clock face/border
ctx.save();
ctx.beginPath();
ctx.lineWidth = 14;
ctx.fillStyle = faceColor.value; // Add this
ctx.strokeStyle = borderColor.value; // Add this
ctx.arc(0, 0, 142, 0, Math.PI * 2, true);
ctx.stroke();
ctx.fill();
ctx.restore();
```

Now if you change those color inputs, it should reflect on the clock.

## Number Lines Color

For the number lines, we need to add a `strokeStyle` right before the loop for the hour and minute lines. You could also put it inside the loop, but I like to keep it outside. We will set the `strokeStyle` to `lineColor.value`.

```js
// Draw hour lines
ctx.save();
ctx.strokeStyle = lineColor.value; // Add this
for (let i = 0; i < 12; i++) {
  ctx.beginPath();
  ctx.rotate(Math.PI / 6);
  ctx.moveTo(100, 0);
  ctx.lineTo(120, 0);
  ctx.stroke();
}
ctx.restore();

// Draw minute lines
ctx.save();
ctx.lineWidth = 4;
ctx.strokeStyle = lineColor.value; // Add this
for (let i = 0; i < 60; i++) {
  if (i % 5 !== 0) {
    ctx.beginPath();
    ctx.moveTo(117, 0);
    ctx.lineTo(120, 0);
    ctx.stroke();
  }
  ctx.rotate(Math.PI / 30);
}
ctx.restore();
```

## Large Hand Color

```js
// Draw hour hand
ctx.save();
ctx.rotate(
  (Math.PI / 6) * hr + (Math.PI / 360) * min + (Math.PI / 21600) * sec
);
ctx.strokeStyle = largeHandColor.value; // Add this
ctx.lineWidth = 14;
ctx.beginPath();
ctx.moveTo(-20, 0);
ctx.lineTo(80, 0);
ctx.stroke();
ctx.restore();

// Draw minute hand
ctx.save();
ctx.rotate((Math.PI / 30) * min + (Math.PI / 1800) * sec);
ctx.strokeStyle = largeHandColor.value; // Add this
ctx.lineWidth = 10;
ctx.beginPath();
ctx.moveTo(-28, 0);
ctx.lineTo(112, 0);
ctx.stroke();
ctx.restore();
```

## Second Hand Color

We will add the value to the `strokeStyle` and `fillStyle` for the second hand. The `fillStyle` pertains to the clock center dot.

```js
// Draw second hand
ctx.save();
ctx.rotate((sec * Math.PI) / 30);
ctx.strokeStyle = secondHandColor.value; // Add this
ctx.fillStyle = secondHandColor.value; // Add this
ctx.lineWidth = 6;
ctx.beginPath();
ctx.moveTo(-30, 0);
ctx.lineTo(100, 0);
ctx.stroke();
ctx.beginPath();
ctx.arc(0, 0, 10, 0, Math.PI * 2, true);
ctx.fill();
ctx.restore();
```

## Save As Image

To save a canvas as an image, we can use the `toDataURL()` method. This will return a base64 encoded string. We can then essentially create a link and click it programmatically. We will do this in an event listener for the save button.

```js
document.getElementById('save-btn').addEventListener('click', () => {
  const canvas = document.getElementById('canvas');
  const dataURL = canvas.toDataURL('image/png');
  const link = document.createElement('a');
  link.download = 'clock.png';
  link.href = dataURL;
  link.click();
});
```

Now, you can change the clock to any style that you want and download it as an image.


---


# 08-web-audio-api

# Web Audio API

The Audio API is a powerful tool for creating audio in the browser. It is a low-level API that allows you to create audio nodes and connect them together to create a sound. The nodes can be used to create effects, filters, and more. The API is also used to play audio files.

## `<audio>` Element

The `<audio>` element is used to play audio files. It is a simple element, but you can interact with it using the JavaScript API. The element has a `src` attribute that is used to set the source of the audio file. Of course, you can change this within the JavaScript to play different audio files. I will show you how to do this in the next lesson where we build an audio player. The `<audio>` element also has a `controls` attribute that will show the default browser controls. Let's embed a simple audio file in our HTML.

`summer.mp3` is included in the resources for this lesson. You can also use a remote link to an audio file.

```html
<audio src="summer.mp3" id="audio" controls></audio>
```

Since, I used the `controls` attribute, I can control the audio, however, usually we will create our own interface and control everything using the JavaScript API. Let's look at the JavaScript API.

## JavaScript API

Here are some of the common methods and properties of the audio element.

- `play()`
- `pause()`
- `currentTime`
- `duration`
- `volume`

Let's remove the `controls` attribute and create our own buttons as well as a `current-time` div and a volume slider. This will be really ugly for now, but in another lesson, we will create a really cool looking audio player.

```html
<audio src="summer.mp3" id="audio"></audio>

<button id="play">Play</button>
<button id="pause">Pause</button>
<button id="stop">Stop</button>
<div id="current-time"></div>
<input id="volume" type="range" min="0" max="1" step="0.01" value="1" />
```

In the JavaScript, let's bring all of the elements in

```js
const audio = document.getElementById('audio');
const play = document.getElementById('play');
const pause = document.getElementById('pause');
const stop = document.getElementById('stop');
const currentTime = document.getElementById('current-time');
const volume = document.getElementById('volume');
```

## play() & pause()

Then we can create events for the play and pause buttons and call the `play()` and `pause()` methods.

```js
play.addEventListener('click', () => {
  audio.play();
});

pause.addEventListener('click', () => {
  audio.pause();
});
```

## Stopping Audio

We use `pause()` because there is no `stop()` method. We can use `pause()` and set the `currentTime` to `0` to stop the audio.

```js
const stop = document.getElementById('stop');

stop.addEventListener('click', () => {
  audio.pause();
  audio.currentTime = 0;
});
```

Now, the track is reset to the beginning.

## timeUpdate Event

The `timeupdate` event is fired when the `currentTime` is updated. In our project we will create a progress bar, but for now, let's just view the `currentTime`

```js
audio.addEventListener('timeupdate', () => {
  // console.log(audio.currentTime);
  currentTime.innerHTML = audio.currentTime;
});
```

## Volume

We can change the volume, by adding a listener on to the slider

```js
volume.addEventListener('change', () => {
  audio.volume = volume.value;
});
```

## Adding filters & effects

We can create audio interfaces, etc just by bringing in the audio element like we did and then using the API methods, however if you wanted to add filters, effects, etc, you would need to create an audio context and audio nodes. We will cover this in the next lesson.


---


# 09-audio-context-filters

# Audio Context & Nodes For Filtering & Effects

In the last lesson, we saw how to control audio using the web audio API. However, the API is more powerful than just being used to control. We can also add all kinds of effects and filters. I am not going to pretend I know about this stuff, as far as adding "biquad filters" and all that. I'm far from an audio engineer. But I will show you how you can use them.

So we are going to use the same audio file as before. We will create an audio context and then create a source node. We will then create a `biquad filter` and connect the source node to the filter. Then we will connect the filter to the destination. The destination is the speakers. We will also create an oscillator node and connect it to the destination. This will allow us to hear the audio file and the oscillator at the same time.

In our HTML, we have a new `filter` select and filter frequency slider as well as an `oscillator` select and an oscillator frequency slider as well as a stop button for the oscillator.

```html
<audio src="summer.mp3" id="audio"></audio>
<button id="play">Play</button>
<button id="pause">Pause</button>
<button id="stop">Stop</button>
<div id="current-time"></div>

<input id="volume" type="range" min="0" max="1" step="0.01" value="1" />

<h4>Filter</h4>
<!-- Filter Select -->
<select id="filter">
  <option value="none">None</option>
  <option value="lowpass">Lowpass</option>
  <option value="highpass">Highpass</option>
  <option value="bandpass">Bandpass</option>
  <option value="lowshelf">Lowshelf</option>
  <option value="highshelf">Highshelf</option>
  <option value="peaking">Peaking</option>
  <option value="notch">Notch</option>
  <option value="allpass">Allpass</option>
</select>

<label for="filter-frequency">Filter Frequency</label>
<input
  id="filter-frequency"
  type="range"
  min="0"
  max="1000"
  step="1"
  value="440"
/>

<h4>Oscillator</h4>
<select id="oscillator">
  <option value="none">None</option>

  <option value="sine">Sine</option>
  <option value="square">Square</option>
  <option value="sawtooth">Sawtooth</option>
  <option value="triangle">Triangle</option>
</select>

<label for="oscillator-frequency">Oscillator Frequency</label>
<input
  id="oscillator-frequency"
  type="range"
  min="0"
  max="1000"
  step="1"
  value="440"
/>

<button id="oscillator-stop">Stop Oscillator</button>
```

Let's bring in some additional elements:

```js
const filterEl = document.getElementById('filter');
const filterFrequency = document.getElementById('filter-frequency');
const oscillatorEl = document.getElementById('oscillator');
const oscillatorFrequency = document.getElementById('oscillator-frequency');
const oscillatorStop = document.getElementById('oscillator-stop');
```

## Add Context & nodes

In order to do stuff like this, we need to create an `audio context` and then create a `source node`. We don't want to do this in the global scope because Chrome will complain about auto play policies. So we will just create the context variable and then initialize it in the `play` function. We will do the same for the source node.

```js
let audioCtx, gainNode;

play.addEventListener('click', () => {
  // Create an AudioContext & connect the source to the gain node
  audioCtx = new AudioContext();
  const source = audioCtx.createMediaElementSource(audio);
  gainNode = audioCtx.createGain();
  source.connect(gainNode);
  gainNode.connect(audioCtx.destination);
  audio.play();
});
```

Our player still works the same. We can play, pause, etc. We just created the audio context, then the source and we connected the source to the gain node. Then we connected the gain node to the destination. The destination, which are the speakers.

## Filter

Now we are going to make it so that we can select a filter. This is called a `biquad filter`. We will create the filter variable in the global scope so that the frequency event handler can access it.

```js
let filter;
filterEl.addEventListener('change', () => {
  filter = audioCtx.createBiquadFilter();
  filter.type = filterEl.value;
  gainNode.disconnect();
  gainNode.connect(filter);
  filter.connect(audioCtx.destination);
});
```

Let's also add the frequency event handler.

```js
filterFrequency.addEventListener('change', () => {
  filter.frequency.value = filterFrequency.value;
  gainNode.disconnect();
  gainNode.connect(filter);
  filter.connect(audioCtx.destination);
});
```

We created a `biquad filter` and then set the type to the value of the select. We then disconnect the gain node from the destination and connect it to the filter. Then we connect the filter to the destination. This will allow us to hear the audio file with the filter applied. We also created the frequency handler.

Let's try it out and play the audio file. We can select a filter and hear the difference. We can also change the frequency of the filter. We can do this by adding an event listener to the filter frequency slider.

## Oscillator

We can also add an oscillator. We will create the oscillator variable in the global scope so that the frequency event handler can access it. We also need to create a stop button handler.

```js
let oscillator;
oscillatorEl.addEventListener('change', () => {
  oscillator = audioCtx.createOscillator();
  oscillator.type = oscillatorEl.value;
  oscillator.frequency.value = 440; // 440Hz
  oscillator.connect(audioCtx.destination);
  oscillator.start();
});

oscillatorFrequency.addEventListener('change', () => {
  oscillator.frequency.value = oscillatorFrequency.value;
});

oscillatorStop.addEventListener('click', () => {
  oscillator.stop();
});
```

Now if we choose a type of oscillator, we can hear it. It's VERY annoying. We can also change the frequency of the oscillator. We can also stop the oscillator.

Again, I can't really tell you the point of an oscillator. Maybe some of you are really good with audio and can tell me. But this is how you can use it with the audio API.


---


# 10-music-player-project

# Music Player Project

Now, we are going to create a really nice looking music player. This is the same player that we used in my 20 vanilla projects course. I figured, why create a new project that will show you the same exact thing? This player also has some CSS transitions and animations.

There is a folder called `music` with 3 songs in it. There is also a folder called `images` with 3 cover images. We will be using these songs and images for the player. In this project, the music file and image file should be the same.

## The HTML

Let's go ahead and take a look at the HTML. It is really simple and minimal.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.2/css/all.min.css"
    />
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
    <title>Music Player</title>
  </head>
  <body>
    <h1>Music Player</h1>

    <div class="music-container" id="music-container">
      <div class="music-info">
        <h4 id="title"></h4>
        <div class="progress-container" id="progress-container">
          <div class="progress" id="progress"></div>
        </div>
      </div>

      <audio src="music/ukulele.mp3" id="audio"></audio>

      <div class="img-container">
        <img src="images/ukulele.jpg" alt="music-cover" id="cover" />
      </div>
      <div class="navigation">
        <button id="prev" class="action-btn">
          <i class="fas fa-backward"></i>
        </button>
        <button id="play" class="action-btn action-btn-big">
          <i class="fas fa-play"></i>
        </button>
        <button id="next" class="action-btn">
          <i class="fas fa-forward"></i>
        </button>
      </div>
    </div>
  </body>
</html>
```

Notice, we did include the Font Awesome 5 CDN. We will be using some icons for the play, prev, next button, etc. We also have an area for the progress bar, an `h4` for the title, and an image for the cover. We have the default audio file and image as the ukulele song, but this player will have 3 songs and cover images.

## The CSS

Here is the CSS. I am not going to go over it all. It is pretty simple and self explanatory. The one thing I want to point out is the `.play` class. This class is applied to the music container via javascript. This is what makes the image rotate as well as the title slide up.

```css
@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');

* {
  box-sizing: border-box;
}

body {
  background-image: linear-gradient(
    0deg,
    rgba(247, 247, 247, 1) 23.8%,
    rgba(252, 221, 221, 1) 92%
  );
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: 'Lato', sans-serif;
  margin: 0;
}

.music-container {
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 20px 20px 0 rgba(252, 169, 169, 0.6);
  display: flex;
  padding: 20px 30px;
  position: relative;
  margin: 100px 0;
  z-index: 10;
}

.img-container {
  position: relative;
  width: 110px;
}

.img-container::after {
  content: '';
  background-color: #fff;
  border-radius: 50%;
  position: absolute;
  bottom: 100%;
  left: 50%;
  width: 20px;
  height: 20px;
  transform: translate(-50%, 50%);
}

.img-container img {
  border-radius: 50%;
  object-fit: cover;
  height: 110px;
  width: inherit;
  position: absolute;
  bottom: 0;
  left: 0;
  animation: rotate 3s linear infinite;

  animation-play-state: paused;
}

.music-container.play .img-container img {
  animation-play-state: running;
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

.navigation {
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.action-btn {
  background-color: #fff;
  border: 0;
  color: #dfdbdf;
  font-size: 20px;
  cursor: pointer;
  padding: 10px;
  margin: 0 20px;
}

.action-btn.action-btn-big {
  color: #cdc2d0;
  font-size: 30px;
}

.action-btn:focus {
  outline: 0;
}

.music-info {
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 15px 15px 0 0;
  position: absolute;
  top: 0;
  left: 20px;
  width: calc(100% - 40px);
  padding: 10px 10px 10px 150px;
  opacity: 0;
  transform: translateY(0%);
  transition: transform 0.3s ease-in, opacity 0.3s ease-in;
  z-index: 0;
}

.music-container.play .music-info {
  opacity: 1;
  transform: translateY(-100%);
}

.music-info h4 {
  margin: 0;
}

.progress-container {
  background: #fff;
  border-radius: 5px;
  cursor: pointer;
  margin: 10px 0;
  height: 4px;
  width: 100%;
}

.progress {
  background-color: #fe8daa;
  border-radius: 5px;
  height: 100%;
  width: 0%;
  transition: width 0.1s linear;
}
```

## The JavaScript

Now for the fun part. First we will bring in all of the elements that we need.

```js
const musicContainer = document.getElementById('music-container');
const playBtn = document.getElementById('play');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

const audio = document.getElementById('audio');
const progress = document.getElementById('progress');
const progressContainer = document.getElementById('progress-container');
const title = document.getElementById('title');
const cover = document.getElementById('cover');
```

## Setup & Load Song

Next, we will create an array of songs and their cover images. Remember, they are named the same, so we just have an array with 3 titles/image names

```js
const songs = ['hey', 'summer', 'ukulele'];
```

We need a way to keep track of the songs. So we will create a song index. We will start with the song with the index of 2.

```js
let songIndex = 2;
```

Now we will load the song into the DOM. We will set the title, audio source, and cover image source.

```js
loadSong(songs[songIndex]);

function loadSong(song) {
  title.innerText = song;
  audio.src = `music/${song}.mp3`;
  cover.src = `images/${song}.jpg`;
}
```

## Play & Pause Song

The play and pause button are the same, so we will have an event listener and then choose to run either the `playSong` or `pauseSong` function based on if the song is playing or not.

This is also where we will either add or remove the `play` class from the music container. This will make the image spin and display the song info.

```js
playBtn.addEventListener('click', () => {
  const isPlaying = musicContainer.classList.contains('play');

  if (isPlaying) {
    pauseSong();
  } else {
    playSong();
  }
});
```

Let's create both methods

```js
function playSong() {
  musicContainer.classList.add('play'); // Makes image spin and display info
  playBtn.querySelector('i.fas').classList.remove('fa-play');
  playBtn.querySelector('i.fas').classList.add('fa-pause');

  audio.play();
}

function pauseSong() {
  musicContainer.classList.remove('play');
  playBtn.querySelector('i.fas').classList.add('fa-play');
  playBtn.querySelector('i.fas').classList.remove('fa-pause');

  audio.pause();
}
```

## Prev & Next Buttons

Now, let's add the prev and next functionality. We need to change the song index and then load the song.

```js
prevBtn.addEventListener('click', prevSong);
nextBtn.addEventListener('click', nextSong);

function prevSong() {
  songIndex--;

  if (songIndex < 0) {
    songIndex = songs.length - 1;
  }

  loadSong(songs[songIndex]);

  playSong();
}

function nextSong() {
  songIndex++;

  if (songIndex > songs.length - 1) {
    songIndex = 0;
  }

  loadSong(songs[songIndex]);

  playSong();
}
```

## Show Progress Bar

We need to show the progress bar. It should be relative to where in the song is being played. We listen for the `timeupdate` event on the audio element. This event is fired when the time indicated by the `currentTime` attribute has been updated. We will then calculate the percentage of the song that has been played and set the width of the progress bar.

```js
audio.addEventListener('timeupdate', updateProgress);

function setProgress(e) {
  const width = this.clientWidth;
  const clickX = e.offsetX;
  const duration = audio.duration;

  audio.currentTime = (clickX / width) * duration;
}
```

## Set Progress Bar

We also want to be able to click on the progress bar and have the song go to that point

```js
progressContainer.addEventListener('click', setProgress);

function setProgress(e) {
  const width = this.clientWidth;
  const clickX = e.offsetX;
  const duration = audio.duration;

  audio.currentTime = (clickX / width) * duration;
}
```

That's it! We now have a cool little music player.


---


# 11-drum-machine-project

# Drum Machine Project

In this project, we will create a drum machine that plays sounds when the user presses specific keys. We will use the `Audio` object to play the sounds.

## The HTML

Let's start with the HTML.

```html
<header>
  <h1>Drum Machine</h1>
</header>
<div class="keys">
  <div data-key="65" class="key">
    <kbd>A</kbd>
    <span class="sound">clap</span>
  </div>
  <div data-key="83" class="key">
    <kbd>S</kbd>
    <span class="sound">hihat</span>
  </div>
  <div data-key="68" class="key">
    <kbd>D</kbd>
    <span class="sound">kick</span>
  </div>
  <div data-key="70" class="key">
    <kbd>F</kbd>
    <span class="sound">openhat</span>
  </div>
  <div data-key="71" class="key">
    <kbd>G</kbd>
    <span class="sound">boom</span>
  </div>
  <div data-key="72" class="key">
    <kbd>H</kbd>
    <span class="sound">ride</span>
  </div>
  <div data-key="74" class="key">
    <kbd>J</kbd>
    <span class="sound">snare</span>
  </div>
  <div data-key="75" class="key">
    <kbd>K</kbd>
    <span class="sound">tom</span>
  </div>
</div>

<audio data-key="65" src="sounds/clap.wav"></audio>
<audio data-key="83" src="sounds/hihat.wav"></audio>
<audio data-key="68" src="sounds/kick.wav"></audio>
<audio data-key="70" src="sounds/openhat.wav"></audio>
<audio data-key="71" src="sounds/boom.wav"></audio>
<audio data-key="72" src="sounds/ride.wav"></audio>
<audio data-key="74" src="sounds/snare.wav"></audio>
<audio data-key="75" src="sounds/tom.wav"></audio>
```

We are creating a `div` for each key. We are using the `data-key` attribute to store the key code for each key. We went over key codes in past lessons. We are also adding a `span` element to display the name of the sound. At the bottom, we are adding an `audio` element for each sound. We are using the `data-key` attribute to store the key code for each sound.

## The CSS

Just some simple CSS to style the page.

```css
@import url('https://fonts.googleapis.com/css?family=Poppins:300,400,700');

html,
body {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background: #f4f4f4;
}

h1 {
  margin: 0;
  padding: 0;
  text-align: center;
}

.keys {
  font-size: 40px;
  width: 500px;
  margin: 100px auto;
}

.keys kbd {
  display: inline-block;
  padding: 10px 20px;
  margin: 0 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: #eee;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  font-size: 20px;
  font-weight: 300;
}

.keys .playing kbd {
  transform: scale(1.2);
  transition: all 0.07s;
}
```

## The JavaScript

Surprisingly, this will only take about 13 or 14 lines of code.

```js
window.addEventListener('keydown', playSound);

function playSound(e) {
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`.key[data-key="${e.keyCode}"]`);
  if (!audio) return; // stop the function from running all together
  audio.currentTime = 0; // rewind to the start
  audio.play();
  key.classList.add('playing');

  setTimeout(() => {
    key.classList.remove('playing');
  }, 100);
}
```

We are adding an event listener to the `window` object. We are listening for the `keydown` event. When the event fires, we are calling the `playSound` function. The `playSound` function takes an event object as a parameter. We are using the `keyCode` property of the event object to get the key code of the key that was pressed. We are using the `querySelector` method to get the `audio` element and the `key` element that have the same `data-key` attribute as the key code of the key that was pressed. We are using the `play` method to play the sound. We are using the `currentTime` property to rewind the sound to the start. We are using the `classList` property to add the `playing` class to the `key` element. We are using the `setTimeout` method to remove the `playing` class from the `key` element after 100 milliseconds.

Now, when you press a key, the sound will play and the key will animate. Have fun!


---


# 12-video-api

# Video API

Just like the audio API, the video API is a set of methods and properties that allow you to control the video element. In fact, you'll see that they both use many of the same methods.

First, let's use the HTML5 video element to play a video. I have included a `clouds.mov` video in the sandbox files, but you can use any video that you want.

```html
<vide controls width="700">
  <source src="media/clouds.mov" />
</vide
```

There are some attributes that you can use for the `video` element:

- `controls` - This will show the default controls for the video
- `autoplay` - This will automatically play the video when the page loads
- `muted` - This will mute the video (In Chrome, the video must be muted for autoplay to work)
- `loop` - This will loop the video
- `poster` - This will show an image before the video starts playing
- `width` - This will set the width of the video
- `height` - This will set the height of the video

Let's give the video a poster. We will use the `poster.png` image in the sandbox files.

```html
<video controls width="700" poster="media/poster.png">
  <source src="media/clouds.mov" />
</video>
```

Let's also make it loop and autoplay. It must also be muted for autoplay.

```html
<video controls autoplay loop width="700" poster="media/poster.png" muted>
  <source src="media/clouds.mov" />
</video>
```

## JavaScript API

The JavaScript API for the video element is very similar to the audio element. Let's add a play, pause, stop button and a current-time div to display the time. In the next video, we will create a nice looking video player, but for now, I just want you to learn the basic methods.

Let's add the buttons and also remove all of the attributes except for `width` and `poster`. We will use JavaScript to control the video.

```html
<video width="700">
  <source src="media/clouds.mov" width="700" poster="media/poster.png" />
</video>

<div>
  <button id="play">Play</button>
  <button id="pause">Pause</button>
  <button id="stop">Stop</button>
  <div id="current-time"></div>
</div>
```

In the JavaScript, let's bring in what we need.

```js
const video = document.querySelector('video');
const play = document.getElementById('play');
const pause = document.getElementById('pause');
const stop = document.getElementById('stop');
const currentTime = document.getElementById('current-time');
```

We will add an event listener on the play and pause button and then call the `play()` and `pause()` methods.

```js
play.addEventListener('click', () => {
  video.play();
});

pause.addEventListener('click', () => {
  video.pause();
});
```

Just like with the audio API, there is no `stop()` method, so we will pause and reset the time.

```js
stop.addEventListener('click', () => {
  video.pause();
  video.currentTime = 0;
});
```

To show the current time, we will listen for the `timeupdate` event and then display the current time.

```js
video.addEventListener('timeupdate', () => {
  currentTime.textContent = video.currentTime;
});
```

In the next video, we will get a little more into this and create a custom video player.


---


# 13-video-player-project

# Video Player Project

Now, we are going to create a custom video player using the video API.

## The HTML

The HTML is pretty simple. We have our `video` element and then some custom controls and a time display. We are also including font awesome because we are using it for the icons.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Custom Video Player</title>
    <link
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      rel="stylesheet"
      integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <video
      src="media/clouds.mov"
      poster="media/poster.png"
      id="video"
      class="screen"
    ></video>
    <div class="controls">
      <button class="btn" id="play">
        <i class="fa fa-play fa-2x"></i>
      </button>
      <button class="btn" id="stop">
        <i class="fa fa-stop fa-2x"></i>
      </button>
      <input
        type="range"
        id="progress"
        class="progress"
        min="0"
        max="100"
        step="0.1"
        value="0"
      />
      <span class="timestamp" id="timestamp">00:00</span>
    </div>

    <script src="script.js"></script>
  </body>
</html>
```

## The CSS

The CSS is quite long, mostly because we used a custom slider. You don't really need to pay much attention to this part as this is not a CSS course.

```css
@import url('https://fonts.googleapis.com/css?family=Questrial&display=swap');

* {
  box-sizing: border-box;
}

body {
  font-family: 'Questrial', sans-serif;
  background-color: steelblue;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  max-height: 100vh;
  margin: 30px 0;
}

h1 {
  color: #fff;
}

.screen {
  cursor: pointer;
  width: 60%;
  background-color: #000 !important;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.controls {
  background: #333;
  color: #fff;
  width: 60%;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
}

.controls .btn {
  border: 0;
  background: transparent;
  cursor: pointer;
}

.controls .fa-play {
  color: #28a745;
}

.controls .fa-stop {
  color: #dc3545;
}

.controls .fa-pause {
  color: #fff;
}

.controls .timestamp {
  color: #fff;
  font-weight: bold;
  margin-left: 10px;
}

.btn:focus {
  outline: 0;
}

input[type='range'] {
  -webkit-appearance: none; /* Hides the slider so that custom slider can be made */
  width: 100%; /* Specific width is required for Firefox. */
  background: transparent; /* Otherwise white in Chrome */
}

input[type='range']::-webkit-slider-thumb {
  -webkit-appearance: none;
}

input[type='range']:focus {
  outline: none; /* Removes the blue border. You should probably do some kind of focus styling for accessibility reasons though. */
}

input[type='range']::-ms-track {
  width: 100%;
  cursor: pointer;

  /* Hides the slider so custom styles can be added */
  background: transparent;
  border-color: transparent;
  color: transparent;
}

/* Special styling for WebKit/Blink */
input[type='range']::-webkit-slider-thumb {
  -webkit-appearance: none;
  border: 1px solid #000000;
  height: 36px;
  width: 16px;
  border-radius: 3px;
  background: #ffffff;
  cursor: pointer;
  margin-top: -14px; /* You need to specify a margin in Chrome, but in Firefox and IE it is automatic */
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d; /* Add cool effects to your sliders! */
}

/* All the same stuff for Firefox */
input[type='range']::-moz-range-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 36px;
  width: 16px;
  border-radius: 3px;
  background: #ffffff;
  cursor: pointer;
}

/* All the same stuff for IE */
input[type='range']::-ms-thumb {
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  border: 1px solid #000000;
  height: 36px;
  width: 16px;
  border-radius: 3px;
  background: #ffffff;
  cursor: pointer;
}

input[type='range']::-webkit-slider-runnable-track {
  width: 100%;
  height: 8.4px;
  cursor: pointer;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: #3071a9;
  border-radius: 1.3px;
  border: 0.2px solid #010101;
}

input[type='range']:focus::-webkit-slider-runnable-track {
  background: #367ebd;
}

input[type='range']::-moz-range-track {
  width: 100%;
  height: 8.4px;
  cursor: pointer;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: #3071a9;
  border-radius: 1.3px;
  border: 0.2px solid #010101;
}

input[type='range']::-ms-track {
  width: 100%;
  height: 8.4px;
  cursor: pointer;
  background: transparent;
  border-color: transparent;
  border-width: 16px 0;
  color: transparent;
}
input[type='range']::-ms-fill-lower {
  background: #2a6495;
  border: 0.2px solid #010101;
  border-radius: 2.6px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type='range']:focus::-ms-fill-lower {
  background: #3071a9;
}
input[type='range']::-ms-fill-upper {
  background: #3071a9;
  border: 0.2px solid #010101;
  border-radius: 2.6px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type='range']:focus::-ms-fill-upper {
  background: #367ebd;
}

@media (max-width: 800px) {
  .screen,
  .controls {
    width: 90%;
  }
}
```

## The JavaScript

Let's start by bringing in what we need from the DOM:

```js
const video = document.getElementById('video');
const play = document.getElementById('play');
const stop = document.getElementById('stop');
const progress = document.getElementById('progress');
const timestamp = document.getElementById('timestamp');
```

## Play/pause video

Let's create a function to toggle the video between playing and pausing and add the event listeners. I want it on the play button as well as the video itself.

```js
function playPause() {
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
}

video.addEventListener('click', playPause);
play.addEventListener('click', playPause);
```

## Update icon

Now let's update the icon. If it is playing, the icon should show a play icon, if it is paused, it should show a pause icon.

```js
function updateIcon() {
  if (video.paused) {
    play.innerHTML = '<i class="fa fa-play fa-2x"></i>';
  } else {
    play.innerHTML = '<i class="fa fa-pause fa-2x"></i>';
  }
}

video.addEventListener('pause', updateIcon);
video.addEventListener('play', updateIcon);
```

## Stop video

Let's create the stop function and event.

```js
function stopVideo() {
  video.currentTime = 0;
  video.pause();
}

stop.addEventListener('click', stopVideo);
```

## Progress bar

Let's make the progress bar function. We can use the `timeupdate` event to do so.

```js
function updateProgress() {
  progress.value = (video.currentTime / video.duration) * 100;

  // Get minutes
  let mins = Math.floor(video.currentTime / 60);
  if (mins < 10) {
    mins = '0' + String(mins);
  }

  // Get seconds
  let secs = Math.floor(video.currentTime % 60);
  if (secs < 10) {
    secs = '0' + String(secs);
  }

  timestamp.innerHTML = `${mins}:${secs}`;
}

video.addEventListener('timeupdate', updateProgress);
```

## Set progress bar

We also want to be able to click anywhere on the bar and have it take us to that point in the video.

```js
function setVideoProgress() {
  video.currentTime = (+progress.value * video.duration) / 100;
}

progress.addEventListener('change', setVideoProgress);
```

That's it! We now have a custom video player using the video API.


---


# 14-web-animations-api

# Web Animations API

The Web Animations API lets us construct animations and control their playback with JavaScript. A lot of times we use a combination of CSS and JavaScript, but this API allows us to do all of the animation work in JavaScript.

We are going to build a little project for this section.

## The HTML

```HTML
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Web Animations API</title>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"
      integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <link rel="stylesheet" href="style.css" />
    <script src="script.js" defer></script>
  </head>
  <body>
    <div class="wrapper">
      <div class="controls">
        <button id="play"><i class="fa-solid fa-play"></i></button>
        <button id="pause"><i class="fa-solid fa-pause"></i></button>
        <button id="reverse">
          <i class="fa-solid fa-clock-rotate-left"></i>
        </button>
        <button id="speed-up"><i class="fa-solid fa-plus"></i></button>
        <button id="slow-down">Slow Down</button>
      </div>
      <div id="ball">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="194"
          height="194"
          version="1.1"
        >
          <circle fill="#000000" cx="97" cy="97" r="97" />
          <path
            fill="#ffffff"
            d="m 94,9.2 a 88,88 0 0 0 -55,21.8 l 27,0 28,-14.4 0,-7.4 z m 6,0 0,7.4 28,14.4 27,0 a 88,88 0 0 0 -55,-21.8 z m -67.2,27.8 a 88,88 0 0 0 -20,34.2 l 16,27.6 23,-3.6 21,-36.2 -8.4,-22 -31.6,0 z m 96.8,0 -8.4,22 21,36.2 23,3.6 15.8,-27.4 a 88,88 0 0 0 -19.8,-34.4 l -31.6,0 z m -50,26 -20.2,35.2 17.8,30.8 39.6,0 17.8,-30.8 -20.2,-35.2 -34.8,0 z m -68.8,16.6 a 88,88 0 0 0 -1.8,17.4 88,88 0 0 0 10.4,41.4 l 7.4,-4.4 -1.4,-29 -14.6,-25.4 z m 172.4,0.2 -14.6,25.2 -1.4,29 7.4,4.4 a 88,88 0 0 0 10.4,-41.4 88,88 0 0 0 -1.8,-17.2 z m -106,57.2 -15.4,19 L 77.2,182.6 a 88,88 0 0 0 19.8,2.4 88,88 0 0 0 19.8,-2.4 l 15.4,-26.6 -15.4,-19 -39.6,0 z m -47.8,2.6 -7,4 A 88,88 0 0 0 68.8,180.4 l -14,-24.6 -25.4,-16.2 z m 135.2,0 -25.4,16.2 -14,24.4 a 88,88 0 0 0 46.4,-36.6 l -7,-4 z"
          />
        </svg>
      </div>
    </div>
  </body>
</html>

```

Here we have some buttons for controlling the animation. I will get to those later. First, we want to focus on making the ball roll. We are using an `svg`, but you could use anything.

## The CSS

Before we do anything with JavaScript, I want to show you how we can do the same animation using just CSS.

```CSS
body {
  background: #000;
  color: #fff;
}

html,
body {
  height: 100%;
}

.wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

#ball {
  /* animation: roll infinite 3s linear; */
  color: white;
  width: 25%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform-origin: 0 0;
  transform: rotate(0) translate3D(-50%, -50%, 0);
  backface-visibility: hidden;
  will-change: transform, color;
}

path {
  fill: currentColor;
}

.controls {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}

button {
  padding: 10px 20px;
  margin: 5px;
  background: #333;
  color: #fff;
  font-size: 18px;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background: blue;
}

/* The Animation */
@keyframes roll {
  0% {
    transform: rotate(0) translate3D(-50%, -50%, 0);
    color: white;
  }
  30% {
    color: blue;
  }
  100% {
    transform: rotate(360deg) translate3D(-50%, -50%, 0);
    color: white;
  }
}

```

In the CSS keyframe we are moving the ball by starting at one position and then rotating it 360 degrees. We are also changing the color of the ball at 30% of the animation.

Now, comment out the CSS, because we are going to do the same thing using JavaScript.

## The JavaScript

Let's start out by bringing in everything that we need.

```JavaScript
  const ball = document.getElementById('ball');
  const play = document.getElementById('play');
  const pause = document.getElementById('pause');
  const reverse = document.getElementById('reverse');
  const speedUp = document.getElementById('speed-up');
  const slowDown = document.getElementById('slow-down');
```

Now, we will create a keyframe object. We do this by creating an array of multiple objects. Each object represents a key from the original CSS.

```js
const rollAnimation = [
  { transform: 'rotate(0) translate3D(-50%, -50%, 0)', color: 'white' },
  { color: 'blue', offset: 0.3 },
  { transform: 'rotate(360deg) translate3D(-50%, -50%, 0)', color: 'white' },
];
```

We can also set the timing in an options object.

```js
const rollOptions = {
  duration: 3000,
  iterations: Infinity,
};
```

Now, let's make the element animate.

```js
const roll = ball.animate(rollAnimation, rollOptions);
```

Now, we get the same animation as we did with CSS. We can also control the animation with JavaScript. Let's add the play and pause button functionality.

```js
play.addEventListener('click', () => roll.play());
pause.addEventListener('click', () => roll.pause());
```

We can also have it go in reverse.

```js
reverse.addEventListener('click', () => roll.reverse());
```

If we want to go from reverse to clicking play again and having it move forward, then we have to add the `playbackRate` to `play`.

```js
play.addEventListener('click', () => {
  roll.playbackRate = 1;
  roll.play();
});
```

Now, it should work.

We can also speed up and slow down the animation using the `playbackRate`.

```js
speedUp.addEventListener(
  'click',
  () => (roll.playbackRate = roll.playbackRate * 2)
);

slowDown.addEventListener(
  'click',
  () => (roll.playbackRate = roll.playbackRate * 0.5)
);
```

This is a very simple animation, but you can imagine how powerful it can be when you get into some really complex animations.


---


# 15-speech-recognition

# Web Speech API - Speech Recognition

The Web Speech API is a set of JavaScript APIs that allow you to add speech recognition and speech synthesis to your web applications. In this lesson, we will look at speech recognition.

Speech recognition is the ability to convert spoken words into text. The Web Speech API provides a SpeechRecognition interface that lets you add speech recognition to your web applications.

## Creating a SpeechRecognition Object

To use the SpeechRecognition interface, you need to create a SpeechRecognition object. You can do this by calling the constructor of the SpeechRecognition interface. I am also going to set the language to English. Feel free to use something else.

```js
const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

const rec = new SpeechRecognition();

rec.lang = 'en-US';
```

## Setting the Speech Recognition Mode

The SpeechRecognition interface has a `continuous` property that lets you set the speech recognition mode. The value of the `continuous` property is a boolean. If the value is `true`, the speech recognition will continue until you stop it. If the value is `false`, the speech recognition will stop after a short pause. Let's set it to `true`.

```js
rec.continuous = true;
```

To start the speech recognition, we use the `start()` method.

```js
rec.start();
```

This will cause the browser to start to listen for speech. We can respond by using the `onresult` event.

```js
rec.onresult = function (e) {
  console.log(e.results);
};
```

The event passed in will include a `results` array, which will contain an object with a `transcript` property. The `transcript` property will contain the text that was recognized.

I want to say a color and have the background of the page change to that color.

```js
const script = e.results[i][0].transcript;
document.body.style.backgroundColor = transcript;
```

This will let us do it once, however, if we want this to be continuous, we have to loop through the array and set the background color for each result.

```js
for (let i = e.resultIndex; i < e.results.length; i++) {
  const script = e.results[i][0].transcript;
  document.body.style.backgroundColor = script;
}
```

Now, we can keep saying colors and it should respond.

Let's make it so if we don't say a color, we get an alert message. We'll create an array of accepted colors.

```js
const acceptedColors = [
  'red',
  'blue',
  'green',
  'yellow',
  'pink',
  'brown',
  'purple',
  'orange',
  'black',
  'white',
];
```

In the loop, let's make the transcript lowercase and trim any whitespace. Then we will check to see if the color is in the array. Here is the final code.

```js
const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

const rec = new SpeechRecognition();

rec.lang = 'en-US';
rec.continuous = true;

rec.onresult = function (e) {
  console.log(e.results);

  const acceptedColors = [
    'red',
    'blue',
    'green',
    'yellow',
    'pink',
    'brown',
    'purple',
    'orange',
    'black',
    'white',
  ];

  for (let i = e.resultIndex; i < e.results.length; i++) {
    const script = e.results[i][0].transcript.toLowerCase().trim();

    if (acceptedColors.includes(script)) {
      document.body.style.backgroundColor = script;
    } else {
      alert('Say a color');
    }
  }
};

rec.start();
```


---


# 16-speech-synthesis

# Speech Synthesis

`SpeechSynthesis` is a Web API that allows you to have your browser speak text. It is part of the [Web Speech API](https://dvcs.w3.org/hg/speech-api/raw-file/tip/speechapi.html).

We are going to learn this by creating a small project that lets us type in a textbox and reads what we type out loud. We will also be able to change the voice. You can get the simple HTML and CSS from the sandbox files.

Let's start by creating a `synth` variable that will hold the `SpeechSynthesis` object.

```js
const synth = window.speechSynthesis;
```

We will add an event listener for the form submit and get the textarea value.

```js
function onSubmit(e) {
  e.preventDefault();

  const textInput = document.getElementById('text-input');
}

document.getElementById('form').addEventListener('submit', onSubmit);
```

We need to create a `SpeechSynthesisUtterance` object that will hold the text we want to speak. Then we can use the `synth.speak()` method to speak the text.

```js
function onSubmit(e) {
  e.preventDefault();

  const textInput = document.getElementById('text-input');

  const utterThis = new SpeechSynthesisUtterance(textInput.value);

  synth.speak(utterThis);
}
```

## Getting the voices

Now, let's create a function that will get the voices and populate the select element with them.

```js
const voiceSelect = document.getElementById('voice-select');
let voices;

function addVoicesToSelect() {
  voices = synth.getVoices();

  for (let i = 0; i < voices.length; i++) {
    const option = document.createElement('option');
    option.textContent = `${voices[i].name} - ${voices[i].lang}`;

    if (voices[i].default) {
      option.textContent += ' - DEFAULT';
    }

    option.setAttribute('data-lang', voices[i].lang);
    option.setAttribute('data-name', voices[i].name);
    voiceSelect.appendChild(option);
  }
}
```

We got the select element outside of the function because we will need it in the submit function as well. We also create a `voices` variable to hold the array of voices that we get from the `synth.getVoices()` method.

Then we loop through the voices and create an option element for each one. We set the `textContent` to the name and language of the voice. If the voice is the default one, we add `- DEFAULT` to the text. We also set the `data-lang` and `data-name` attributes to the language and name of the voice. Finally, we append the option to the select element.

We need to call the `addVoicesToSelect()` function once to populate the select element with the voices. We also need to call it again when the voices change. We can do this by adding an event listener for the `voiceschanged` event. We will put this at the bottom above the form event listener.

```js
addVoicesToSelect();
if (speechSynthesis.onvoiceschanged !== undefined) {
  speechSynthesis.onvoiceschanged = addVoicesToSelect;
}
```

## Changing the voice

Edit the `onSubmit()` function to change the voice.

```js
function onSubmit(e) {
  e.preventDefault();

  const textInput = document.getElementById('text-input');

  const utterThis = new SpeechSynthesisUtterance(textInput.value);

  const selectedOption =
    voiceSelect.selectedOptions[0].getAttribute('data-name');
  for (let i = 0; i < voices.length; i++) {
    if (voices[i].name === selectedOption) {
      utterThis.voice = voices[i];
    }
  }

  synth.speak(utterThis);
}
```

Here, we get the selected option from the select element. Then we loop through the voices and check if the name of the voice is the same as the selected option. If it is, we set the `utterThis.voice` to the voice.

Now, you should be able to type in the text box, select a voice and have it read out loud.
