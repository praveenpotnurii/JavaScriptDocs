
# 01-section-intro

# Section Intro

This is not a Node.js course, however, I do want you to be familiar with it. We already talked about what Node.js is, we installed it and we have used NPM along with CommonJS modules. So you already know the absolute basics.

In this section, I want to introduce you to some of the built-in Node.js modules. We won't be covering all of them. I haven't even used all of them, but we'll cover the ones that are really common that you'll probably run into at some point. We will look at the following modules:

- fs: Allows us to work with the file system, meaning we can do things like read files, create files and folders, move files around and delete files.
- path: Gives us a bunch of helpers to deal with file paths. This is especially helpful because file paths can look different depending on which operating system is being used.
- os: Methods and properties that have to do with the platform or operating system
- url: Helpers for parsing and formatting urls
- querystring - Helpers for  working with querystrings from URLs. We'll actually look at the url and querystring modules together
- http - Handles http requests and responses. We can create a very simpme webserver with this module

I know we're starting to move pretty quickly, but I wanted this course to basically be a JavaScript bootcamp and I want to give you as much information as possible. If you feel like you're not ready for Node.js, that's absolutely fine. You can take this course any way that you'd like. Alright, so in the nect lesson, we'll jump into the Node.js `fs` module.


---


# 02-file-system-module

# `fs` Module

The `fs` module is a core module that allows us to interact with the file system. It is used to create, read, update, and delete files and folders. Obviously, from the browser environment, we cannot access the file system. However, we can use the `fs` module in Node.js.

There are methods for doing just about anything with files and folders. There are also asynchronous and synchronous versions of each method. The asynchronous versions are preferred because they do not block the execution of the program. The synchronous versions are useful when we need to wait for the operation to complete before continuing.

There is also a callback and promise version. For the callback, it is just require('fs') and for the promise version, it is require('fs/promises').

Let's look at some of the most common methods.

First, we need to bring the module in.

```js
const fs = require('fs');
```

## Creating a file

We use the `writeFile` method to create a file. The first argument is the path to the file. The second argument is the content of the file. The third argument is a callback function that will be called when the operation is complete.

```js
// Callback version
fs.writeFile('file.txt', 'Hello World', (err) => {
  if (err) throw err;
  console.log('File created!');
});
```

`writeFile` is asynchronous as it takes in a callback function to run when the operation is complete. If we want to use a promise instead, we can use the `writeFile` method from the `fs/promises` module.

```js
// Promise version
const fs = require('fs/promises');

fs.writeFile('file.txt', 'Hello World')
  .then(() => console.log('File created!'))
  .catch((err) => console.log(err));
```

We can also use async/await. Of course, it has to be wrapped in a function that is marked as `async`. Let's do that and let's pass in the name of the file and the content as arguments.

```js
// Async/Await version
async function createFile(filename, content) {
  try {
    await fs.writeFile(filename, content);
    console.log('File created!');
  } catch (err) {
    console.error(err);
  }
}

createFile('file.txt', 'Hello World');
```

Like I said, there is also a synchronous version of `writeFile`. It is called `writeFileSync`. It does not take in a callback function. Instead, it returns `undefined` if the operation is successful. If there is an error, it will throw an exception. Let's put this in a function as well

```js
function createFileSync(filename, content) {
  try {
    fs.writeFileSync('file.txt', 'Hello World');
    console.log('File created!');
  } catch (err) {
    console.error(err);
  }
}
```

For the rest of these examples, we will use the async/await version, because that is what I would use in a real application. it's completely up to you which version you use.

## Reading a file

To read from a file, we can use the `readFile` method. The first argument is the path to the file. The second argument is the encoding of the file. If you are using the standard callback version, the third argument is a callback function that will be called when the operation is complete. I will be using promises with Async/Await in the examples below.

```js
async function readFile(filename) {
  try {
    const data = await fs.readFile(filename, 'utf8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}

readFile('file.txt');
```

## Delete a file

We can use the `unlink` method to delete a file.

```js
async function deleteFile(filename) {
  try {
    await fs.unlink(filename);
    console.log(`File ${filename} deleted!`);
  } catch (err) {
    console.error(err);
  }
}

deleteFile('file.txt');
```

## Rename a file

We can use the `rename` method to rename a file.

```js
async function renameFile(oldName, newName) {
  try {
    await fs.rename(oldName, newName);
    console.log(`File ${oldName} renamed to ${newName}!`);
  } catch (err) {
    console.error(err);
  }
}

renameFile('file.txt', 'new-file.txt');
```

## Create a folder

We can use the `mkdir` method to create a folder.

```js
async function createFolder(folderName) {
  try {
    await fs.mkdir(folderName);
    console.log(`Folder ${folderName} created!`);
  } catch (err) {
    console.error(err);
  }
}
```

## Move a file to a folder

We can use the `rename` method to move a file to a folder. I am using a couple methods from the `path` module to get the file name and to join the folder path and the file name. We will look at the path module in the next lesson.

```js
async function moveFileToFolder(filePath, folderPath) {
  try {
    const newFilePath = path.join(folderPath, path.basename(filePath));
    await fs.rename(filePath, newFilePath);
    console.log(`File ${filePath} moved to ${newFilePath}`);
  } catch (err) {
    console.error(err);
  }
}

moveFileToFolder('file.txt', 'folder');
```

There are many more methods to work with files and folders. To see the full list, check out the [Node.js documentation](https://nodejs.org/api/fs.html).


---


# 03-path-module

# `path` Module

The `path` module is a core module that allows us to work with file and directory paths. It is used to get the base name of a file, get the extension of a file, create absolute paths, and much more. One big reason that this is useful is because the path separator, among other things can vary between operating systems. For example, on Windows, the path separator is `\` and on Linux and macOS, it is `/`. The `path` module will take care of this for us.

Let's look at some of the most common methods.

First, we need to bring the module in.

```js
const path = require('path');
```

Let's create a variable that holds the path to a file.

```js
const myFilePath = 'subfolder/anotherfolder/index.js';
```

## basename() - Getting the base name of a file

We use the `basename` method to get the base name of a file. The first argument is the path to the file. The second argument is the extension of the file. If we do not pass in the second argument, it will return the base name with the extension. If we pass in the second argument, it will remove the extension from the base name.

```js
const base1 = path.basename(myFilePath);
const base2 = path.basename(myFilePath, '.js');
console.log(base1, base2); // index.js index
```

## extname() - Getting the extension of a file

We use the `extname` method to get the extension of a file.

```js
const ext = path.extname(myFilePath);
console.log(ext); // .js
```

## dirname() - Getting the directory name of a file

We use the `dirname` method to get the directory name of a file.

```js
const dir = path.dirname(myFilePath);
console.log(dir);
```

## join() - Creating a path

We use the `join` method to create a path. It takes in any number of arguments and joins them together to create a path. It will also normalize the path. For example, if we pass in `subfolder`, `anotherfolder`, and `index.js`, it will join them together with the correct path separator and it will remove any extra path separators.

```js
const myPath = path.join('subfolder', 'anotherfolder', 'index.js');
console.log(myPath); // subfolder/anotherfolder/index.js
```

If you are on Windows, you will see that the path separator is `\`. If you are on Linux or macOS, you will see that the path separator is `/`.

## resolve() - Creating an absolute path

We use the `resolve` method to create an absolute path. It takes in any number of arguments and joins them together to create a path. It will also normalize the path, just like the `join` method. The difference is that the `resolve` method will return an absolute path.

```js
const resolved = path.resolve('subfolder', 'anotherfolder', 'index.js');
console.log(resolved);
```

You may see `resolve` and `join` used interchangeably. The difference is that `resolve` will always return an absolute path, while `join` will return a relative path if the first argument is a relative path.

The next two things we are going to look at are `__filename` and `__dirname`. These are environment variables that Node provides for us. They are not part of the `path` module, but they are often used with `path` module methods.

## \_\_dirname - Getting the directory name of the current file

The `__dirname` is an environment variable that tells you the absolute path of the directory containing the currently executing file. Whenever you are pointing to the file that you are in, you should use `__dirname` instead of `./`. This will ensure that your code will work on any operating system.

```js
console.log(__dirname);
```

## \_\_filename - Getting the file name of the current file

The `__filename` is an environment variable that is similar to the `__dirname` environment variable. It tells you the absolute path of the currently executing file as well as the file name.

```js
console.log(__filename);
```


---


# 04-os-module

# `os` Module

The `os` module is a core module that allows us to work with the operating system. It is used to get information about the operating system, get information about the user, and much more. One big reason that this is useful is because the operating system can vary between operating systems. For example, on Windows, the path separator is `\` and on Linux and macOS, it is `/`. The `os` module will take care of this for us. You also may want to have different functionality or content based on the operating system.

## `os.arch()`

This method returns a string identifying the operating system CPU architecture for which the Node.js binary was compiled. Possible values are `'arm'`, `'arm64'`, `'ia32'`, `'mips'`, `'mipsel'`, `'ppc'`, `'ppc64'`, `'s390'`, `'s390x'`, `'x32'`, and `'x64'`.

```js
const os = require('os');
```

```js
console.log(os.arch()); // x64
```

## `os.platform()`

This method returns a string identifying the operating system platform on which Node.js is running. Possible values are `'aix'`, `'darwin'`, `'freebsd'`, `'linux'`, `'openbsd'`, `'sunos'`, and `'win32'`.

```js
console.log(os.platform()); // darwin
```

## `os.cpus()`

This method returns an array of objects containing information about each logical CPU core.

```js
console.log(os.cpus()); // [ { model: 'Intel(R) Core(TM) i7-1068NG7 CPU @ 2.30GHz',
```

## `os.freemem()`

This method returns the amount of free system memory in bytes as an integer.

```js
console.log(os.freemem()); // 17179869184
```

To display in gigabytes, we can use the following code:

```js
console.log(`Free memory: ${os.freemem() / 1024 / 1024 / 1024} GB`);
```

## `os.totalmem()`

This method returns the total amount of system memory in bytes as an integer.

```js
console.log(os.totalmem()); // 17179869184
```

To display in gigabytes, we can use the following code:

```js
console.log(`Total memory: ${os.totalmem() / 1024 / 1024 / 1024} GB`);
```

## `os.homedir()`

This method returns the home directory of the current user as a string.

```js
console.log(os.homedir()); // /Users/username
```

## os.uptime()

This method returns the system uptime in seconds as an integer.

```js
console.log(os.uptime()); // 123456
```

Convert to days, hours, minutes, and seconds:

```js
const uptime = os.uptime();
const days = Math.floor(uptime / 60 / 60 / 24);
const hours = Math.floor(uptime / 60 / 60) % 24;
const minutes = Math.floor(uptime / 60) % 60;
const seconds = Math.floor(uptime) % 60;

console.log(
  'Uptime: ',
  `${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds`
);
```

## `os.hostname()`

This method returns the hostname of the operating system as a string.

```js
console.log(os.hostname()); // hostname
```

## `os.networkInterfaces()`

This method returns an object containing network interfaces that have been assigned a network address.

```js
console.log(os.networkInterfaces());
```


---


# 05-url-querystring

# `url` and `querystring` Modules

These are two different modules, but they are related. The `url` module is used to parse and manipulate URLs. The `querystring` module is used to parse and manipulate query strings.

## url Module

Let's start with the `url` module.

### `url.parse()`

This method takes a URL string and returns an object. The object has properties for each part of the URL. The following code shows how to use this method:

```js
const url = require('url');
```

```js
const myURL = url.parse(
  'https://www.example.com/listing?id=1000&premium=true'
);
console.log(myUrl);
```

```js
{
  host: 'example.com',
  port: null,
  hostname: 'example.com',
  hash: null,
  search: '?id=1000&premium=true',
  query: 'id=1000&premium=true',
  pathname: '/listing',
  path: '/listing?id=1000&premium=true',
  href: 'https://example.com/listing?id=1000&premium=true'
}
```

As you can see, we get a lot of information here. We can use this information to manipulate the URL.

### `url.format()`

This method takes an object and returns a URL string. It is basically the opposite of `url.parse()`. The following code shows how to use this method:

```js
const myURL2 = url.format({
  protocol: 'https',
  host: 'www.example.com',
  pathname: 'listing',
  query: {
    id: 1000,
    premium: true,
  },
});
console.log(myURL2); 
```

## querystring Module

The `querystring` module is used to parse and manipulate query strings. Query strings are the options that you see in a URL after the `?` character.

Let's create a variable with a query string with the year, month and day:

```js
const myQueryString = 'year=2023&month=january&day=20';
```

### `querystring.parse()`

Now, we can use the `querystring.parse()` method to parse the query string into an object:

```js
const q = querystring.parse(myQueryString);
console.log(q.month, q.day, q.year); // january 20 2017
```

We can get the query string from the google url in the previous example:

```js
const googleQuery = querystring.parse(myURL.search.slice(1));
console.log(googleQuery.q); // how to parse url nodejs
```

### `querystring.stringify()`

We can use the `querystring.stringify()` method to convert an object into a query string:

```js
const myQueryString2 = querystring.stringify({
  year: 2023,
  month: 'january',
  day: 20,
});

console.log(myQueryString2); // year=2023&month=january&day=20
```

So, both of these modules can be useful for certain tasks in certain applications.


---


# 06-http-module

# `http` module - Creating a Server

The `http` module is a core module that allows us to create a server and listen for requests. You can create a complete web server with just this module, however, it is not recommended. The `http` module is low-level and does not provide many features that are needed in a production environment. For example, it does not handle routing, sessions, or any static files. To create a production-ready web server, you would use a framework, such as Express. Express as well as other frameworks are built on top of the `http` module. We will be using Express in the next lesson.

## Creating a Server

To create a server, we use the `createServer` method. This method takes a callback function that is called every time a request is made to the server. The callback function takes two parameters, `request` and `response`. The `request` object contains information about the request, such as the URL, headers, and body. The `response` object is used to send a response back to the client. The `response` object has a method called `end` that takes a string as a parameter. This string is what is sent back to the client.

```js
const http = require('http');

const server = http.createServer((request, response) => {
  response.end('Hello World');
});

server.listen(5000, () => {
  console.log('Server is listening on port 5000. Ready to accept requests!');
});
```

We now actually have a server running on our localhost on port 5000. So you can make requests to that server. You can use the browser, since it is a `GET` request by default. Or you can use a tool like Postman. Or you can use the `curl` command in the terminal.

```bash
curl localhost:5000
```

I would suggest using `Postman`. That's what I'll be using. You can get it from [https://www.postman.com/](https://www.postman.com/) for free.

If you are using your browser, open up the `network` tab in the developer tools. Then refresh the page. You should see a request to `localhost:5000`. If you click on it, you can see the response. You can also see the request and response headers.

Congratulations! You have created your first server! It doesn't do anything except say hello, but it is a server.

## Routing

The `http` module does not have any built-in routing. So we have to implement it ourselves. We can do this by checking the `request.url` property. If the URL matches a certain pattern, we can send a response back to the client. If the URL does not match, we can send a 404 response.

```js
const server = http.createServer((request, response) => {
  const url = request.url;

  if (url === '/') {
    response.writeHead(200, { 'content-type': 'text/html' });
    response.end('<h1>Welcome</h1>');
  } else if (url === '/about') {
    response.writeHead(200, { 'content-type': 'text/html' });
    response.end('<h1>About Us</h1>');
  } else {
    response.writeHead(404, { 'content-type': 'text/html' });
    response.end('<h1>Page not found</h1>');
  }
});
```

It is important to note that when you change anything, you have to restart your server. you can do this by pressing `ctrl + c` in the terminal. Then run `node index.js` again.

Creating routes and doing other things without a framework can get very tedious. We would have to write a lot of `if` statements to handle all the different routes. What I have done is created a route for the index page, about and then a 404 page. If you go to `localhost:5000/about`, you should see the about page. If you go to `localhost:5000/anythingelse`, you should see the 404 page.

Remember we talked about status codes? The `200` response means `ok` so I used that on the index and about pages. The `404` response means `not found` so I used that on the 404 page.

## Returning an HTML File

We can also return an HTML file instead of a string. We can do this by using the `fs` module. The `fs` module allows us to read and write files. We can use the `readFile` method to read an HTML file and send it back to the client.

```js
const fs = require('fs');

const server = http.createServer((request, response) => {
  const url = request.url;

  if (url === '/') {
    fs.readFile('index.html', (error, file) => {
      if (error) {
        console.log(error);
        response.writeHead(500, { 'content-type': 'text/html' });
        response.end('<h1>Sorry, we have a problem on our end</h1>');
      } else {
        response.writeHead(200, { 'content-type': 'text/html' });
        response.end(file);
      }
    });
  } else if (url === '/about') {
    response.writeHead(200, { 'content-type': 'text/html' });
    response.end('<h1>About Us</h1>');
  } else {
    response.writeHead(404, { 'content-type': 'text/html' });
    response.end('<h1>Page not found</h1>');
  }
});
```

You can go ahead and create an about and a 404 page if you want.

## Returning a JSON File

Node.js can of course server HTML files, but usually we want to create a backend API with Node.js. So we want to return JSON data. You saw earlier that we used public APIs like the GitHub API, the movie database, the chuck norris joke API and many others. They all served JSON data. We can put some JSON data in a file and return it to the client.

let's change the `about` route to `posts`. We will also get rid of the `fs` module. We will put some JSON with some blog posts at the top of the file. Then when we hit the endpoint of `http://localhost:5000/posts`, we will return the JSON data.

```js
const posts = [
  { id: 1, title: 'Post One', body: 'This is post one' },
  { id: 2, title: 'Post Two', body: 'This is post two' },
];

const server = http.createServer((request, response) => {
  const url = request.url;

  if (url === '/') {
    response.writeHead(200, { 'content-type': 'application/json' });
    response.end(JSON.stringify({ success: true, message: 'Welcome' }));
  } else if (url === '/posts') {
    response.writeHead(200, { 'content-type': 'application/json' });
    response.end(JSON.stringify({ success: true, data: posts }));
  } else {
    response.writeHead(404, { 'content-type': 'application/json' });
    response.end(JSON.stringify({ success: false, error: 'Not found' }));
  }
});
```

When creating a response with JSON data, you have to set the `content-type` header to `application/json`. When formatting your JSON, it's common to have a `success` property that is a boolean. If the request was successful, it will be `true`. If it was not successful, it will be `false`. You can also have an `error` property if the request was not successful. You can also have a `data` property if the request was successful. You can put whatever data you want in there. This is the convention that I like to use.

Now if you visit `http://localhost:5000/posts`, you should see the JSON data.

## Getting a single post

We can also get a single post. We can do this by using the `request.url` property. We can use the `split` method to split the URL into an array. Then we can get the last item in the array. That will be the id of the post. We can then use that id to get the post from the array.

```js
const posts = [
  { id: 1, title: 'Post One', body: 'This is post one' },
  { id: 2, title: 'Post Two', body: 'This is post two' },
];

const server = http.createServer((request, response) => {
  const url = request.url;
  const id = url.split('/')[2];

  if (url === '/') {
    response.writeHead(200, { 'content-type': 'application/json' });
    response.end(JSON.stringify({ success: true, message: 'Welcome' }));
  } else if (url === '/posts') {
    response.writeHead(200, { 'content-type': 'application/json' });
    response.end(JSON.stringify({ success: true, data: posts }));
  } else if (url === `/posts/${id}`) {
    const post = posts.find((post) => post.id === Number(id));
    response.writeHead(200, { 'content-type': 'application/json' });
    response.end(JSON.stringify({ success: true, data: post }));
  } else {
    response.writeHead(404, { 'content-type': 'application/json' });
    response.end(JSON.stringify({ success: false, error: 'Not found' }));
  }
});
```

Now, if you go to `http://localhost:5000/posts/1`, you should see the first post. If you go to `http://localhost:5000/posts/2`, you should see the second post.

So this is the VERY beginning of creating an API. Like I said, usually you are not going to do it this way with 'vanilla Node.js'. It would be too tedious, you would need to write a ton of code and it wouldn't be as secure as if you used a framework. But this is just to give you an idea of how it works.
