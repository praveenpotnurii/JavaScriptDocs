
# 01-express-api-setup

# Express API Setup

Now we are going to get into some back-end web development. We are going to build a simple REST API using Express. This will be a random ideas API, so the data will be ideas that people post. We'll keep it simple and just have the idea text, a tag, the date and a username. We won't be adding authentication or anything, even what we're doing now is way beyond what I planned for this course. We'll just add the username to the request.

We will implement `CRUD` functionality, which is create, read, update and delete. Express handles a lot of the heavy lifting for us, so we can focus on the important stuff.

Create a folder called `randomideas-api` and `cd` into it.

First, we need to install Express. Let's initialize our project with a `package.json` file:

```bash
npm init -y
```

Then we can install Express:

```bash
npm install express
```

Now we can create a file called `server.js`. You can call it absolutely anything you want, but `server.js` is a common name for the main file in a Node.js API.

Let's start by

- Importing Express
- Creating an instance of the `express` function
- Creating a route that responds to a `GET` request to the `/` path
- Listening on port 5000

```js
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(5000, () => {
  console.log('Server is listening on port 5000');
});
```

As you can see, this is much simpler and cleaner than the vanilla Node.js server we built in the previous lesson. We have this `app` object that we can use to create routes. We can also use it to listen for requests on a specific port, etc.

Now, let's add an NPM script to our `package.json` file so we can start the server with `npm start`:

```json
"scripts": {
  "start": "node server.js"
},
```

Now you can run `npm start` to start the server. You should see the message `Server is listening on port 5000` in your terminal.

As far as data, I'm just going to keep the data in memory for now. Create an array with a few ideas right in the `server.js` file under where we initialized the `app` object:

```js
const ideas = [
  {
    id: 1,
    text: 'Positive NewsLetter, a newsletter that only shares positive, uplifting news',
    tag: 'Technology',
    username: 'TonyStark',
    date: '2022-01-02',
  },
  {
    id: 2,
    text: 'Milk cartons that turn a different color the older that your milk is getting',
    tag: 'Inventions',
    username: 'SteveRogers',
    date: '2022-01-02',
  },
  {
    id: 3,
    text: 'ATM location app which lets you know where the closest ATM is and if it is in service',
    tag: 'Software',
    username: 'BruceBanner',
    date: '2022-01-02',
  },
];
```

Let's create a route that responds to a `GET` request to the `/api/ideas` path. It will return an array of ideas. Add this to the bottom of your `server.js` file above the `app.listen()` call:

```js
// Get all ideas
app.get('/api/ideas', (req, res) => {
  res.json(ideas);
});
```

The reason that I used `/api/ideas` instead of just `/ideas` is because I want to keep the API separate from the front-end. I don't want to have to worry about the front-end routes conflicting with the API routes.

All of our routes take in a callback with a request and response object. The request object contains information about the request, such as the path, query string, headers, etc. The response object contains methods for responding to the request, such as `send()`, `json()`, `status()`, etc. We are sending back a JSON response with the `res.json()` method. This will automatically set the `Content-Type` header to `application/json`.

Now we can test it out in Postman. Create a new GET request to http://localhost:5000/api/ideas. You should see the array of ideas in the response body.

Let's also create a route for individual ideas. We can use a route parameter to get the ID of the idea we want to get. Add this to the bottom of your `server.js` file:

```js
// Get single idea
app.get('/api/ideas/:id', (req, res) => {
  const idea = ideas.find((idea) => idea.id === parseInt(req.params.id));

  if (!idea) {
    res.status(404).json({ success: false, error: 'Resource not found' });
  } else {
    res.json({ success: true, data: idea });
  }
});
```

We specified ':id' in the route. We can then access that route parameter using `req.params.id`.

Then we are using the `find()` method to find the idea with the ID that matches the route parameter. If we don't find a idea, we send a 404 status code and an error. If we do find an idea, we send it back as a successful JSON response.

You have to restart the server to see the changes. I will show you a tool to get around that soon.

Test it out in Postman. Create a new GET request to http://localhost:5000/api/ideas/1. You should see the idea with the ID of 1 in the response body.

Try going to http://localhost:5000/api/ideas/4. You should see the error message in the response body.

In the next lesson, I will show you how to use a package called `Nodemon` to automatically restart the server when you make changes. We will also clean up our code a bit and create a separate file for our routes.


---


# 02-nodemon-routes-folder

# Nodemon & Routes Folder

So right now, we have to keep restarting our app everytime we make a change. This is not ideal. We can use a package called `nodemon` to automatically restart our app when we make changes.

Let's install as a dev dependency:

```bash
npm install -D nodemon
```

Now, in your `package.json` file, you can add a script to run your app with `nodemon`:

```json
"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js"
}
```

From now on, in development, you can run `npm run dev` to start your app with `nodemon` and you will not have to restart your app everytime you make a change.

## Cleaning up the routes

Right now we have our idea routes in the main `server.js` file. This is not ideal. We should move them to a separate file. Let's create a new folder called `routes` and inside that folder, create a new file called `ideas.js`.

In order to use the Express router, we need to import it:

```js
const express = require('express');
const router = express.Router();
```

Now, we can move our ideas and idea routes to this file. We do have to make a couple changes to the routes. We are using the router now, so we need to change the `app.get()` to `router.get()`. We also need to change the paths from `/api/ideas` to `/` because we are already in the `/api/ideas` route. The single idea route will be `/:id` because we are already in the `/api/ideas` route.

Lastly, we need to export the router (I always forget this 🤨):

```js
module.exports = router;
```

## Hook up routes folder

Now we need to hook up the routes folder. In your `server.js`, you can remove the 2 idea routes and add the following:

```js
const ideasRouter = require('./routes/ideas');
app.use('/api/ideas', ideasRouter);
```

`app.use` is a way to add middleware to your app. In this case, we are adding the `ideasRouter` middleware to the `/api/ideas` route. This means that all the routes in the `ideasRouter` will be prefixed with `/api/ideas` automatically.

So now the api should work the same as before, but we have a cleaner `server.js` file. You can go ahead and test out the `/api/ideas` and `/api/ideas/:id` routes in postman.

In the next lesson, we will make it so that we can add ideas with a POST request.


---


# 03-handle-post-requests

# Handling POST Requests & Data

Now that we have a basic API set up, we can start adding more functionality. We will start by adding the ability to create ideas with a POST request. This means that we need to send some data with the request.

In the `routes/ideas.js` file, we will add a new route to handle the POST request:

```js
// Create idea
router.post('/', (req, res) => {
  const idea = {
    id: ideas.length + 1,
    text: req.body.text,
    tag: req.body.tag,
    username: req.body.username,
    date: new Date().toISOString().slice(0, 10),
  };

  ideas.push(idea);

  res.json({ success: true, data: idea });
});
```

We are not using a database, so we are just going to add the idea to an array. We will also send back the idea that was created. Usually, when you integrate a database, it will create the ID automatically, but we are just going to increment the ID by 1.

The data that we send with our HTTP request will have the data of the idea. We can access this data with `req.body`. In order to do this, we do have to add a piece of middleware to our app. In the `server.js` file, add the following:

```js
// Body parser middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
```

This will allow us to access the data that we send with the request. Now, we can test out the POST request in Postman. In the body, we can add the text, tag and username of the idea. The endpoint stays the same - http://localhost:5000/api/ideas. However, we will also need to change the request type to POST.

## Sending data to the server

We need to send our idea data in the request body. In Postman, we can do this by clicking on the body tab and selecting `x-www-form-urlencoded`. We can then add the text, tag and username of the idea.

When you send your request, you should get a response with the idea that was created.

Remember, your data is just being saved in memory. If you restart the server, the data will be lost.

If you make a GET request right after, you will see that the idea was added to the array.

If we were using a database, most of this would be the same. We make the requests the same way, etc. It would actually be easier once the database is all configured, because we dont have to worry about the IDs. Also, there are methods we could use like `findByIdAndUpdate` to update the idea. Here, we are doing it manually.

In the next lesson, we will add the update and delete functionality


---


# 04-handle-put-delete-requests

# Handling PUT & DELETE Requests

We can read and create ideas via our API, now let's add the functionality to update and delete ideas.

## Updating Ideas

In the `routes/ideas.js` file, we will add a new route to handle the PUT request:

```js
// Update idea
router.put('/:id', (req, res) => {
  const idea = ideas.find((idea) => idea.id === parseInt(req.params.id));

  if (!idea) {
    res.status(404).json({ success: false, error: 'Resource not found' });
  } else {
    idea.text = req.body.text || idea.text;
    idea.tag = req.body.tag || idea.tag;

    res.json({ success: true, data: idea });
  }
});
```

We are going to find the idea that we want to update by the ID. If the idea is not found, we will send back an error. If the idea is found, we will update the text and/or tag of the idea. We are not going to allow username updates. We will then send back the updated idea.

Try it out in Postman. Make a `PUT` request to `http://localhost:5000/api/ideas/1`. Remember to choose PUT as the request type and to send the `text` and `tag` in the request body.

## Deleting Ideas

In the `routes/ideas.js` file, we will add a new route to handle the DELETE request:

```js
// Delete idea
router.delete('/:id', (req, res) => {
  const idea = ideas.find((idea) => idea.id === parseInt(req.params.id));

  if (!idea) {
    res.status(404).json({ success: false, error: 'Resource not found' });
  } else {
    const index = ideas.indexOf(idea);
    ideas.splice(index, 1);

    res.json({ success: true, data: {} });
  }
});
```

We are going to find the idea that we want to delete by the ID. If the idea is not found, we will send back an error. If the idea is found, we will find the index of the idea in the array and remove it. We will then send back an empty object.

Now, make a `DELETE` request to `http://localhost:5000/api/ideas/1`. Remember to choose DELETE as the request type.

<img src="images/delete-success.png" width="600">

We now have a complete `CRUD` REST API. We can create, read, update and delete ideas.


---


# 05-what-is-mongodb

# What Is MongoDB?

Alright, so we have really reached a point in the course where this is totally optional and well beyond JavaScript fundamentals. However, if you're interested in becoming a full-stack developer, you'll need to know about databases. A database is technically and organized collection of data, but alot of times, we use the term "database", when talking about `database management systems`. An example of a database management system is `MongoDB` or `MySQL` or `PostgreSQL`. These work in different ways, but the goal is the same and that is to store and manage data. In our case, we need a place to store the ideas for our application/api. We're going to use `MongoDB`. 

Database systems can run and operate on a single file system or accross multiple nodes or clusters. There are also different types of databases that store and retrieve data in different ways. For instance a MySQL database uses tables and columns while MongoDB uses collections and documents.

MongoDB is a document database. It stores data in JSON-like documents. A Document Database is a type of NoSQL database, which means it does not use SQL to query data, so it's different than a relational database such as MySQL. There are pros and cons to every database including MongoDB, MySQL, Postgres and so on. NoSQL databases are typically faster and easier to scale than SQL databases. However, they are not as mature and do not have as many features as SQL databases. So it's really up to you as well as the project that you're working on to decide which database to use.

MongoDB is very popular in the JavaScript world. I think one of the reasons for that is because it is structured similarly to JavaScript objects. It's also very easy to get started with. You have probably heard of the `MERN` stack, which is a popular stack for building full-stack applications. `MERN` stands for MongoDB, Express, React, and Node. There is also the `MEAN` and `MEVN` stacks, where they use Angular or Vue instead of React.

## Collections & Documents

MongoDB stores data in collections and documents. A collection is a group of documents. A document is a set of key-value pairs. It's essentially JSON. It's actually something called BSON, which is a superset of JSON.  If you're familiar with relational databases like MySQL, you can think of a collection as a table and a document as a row or record. This could be an example of a document in a users collection.

```json
{
  "name": "John Doe",
  "email": "john@gmail.com",
  "password": "SOME_HASHED_PASSWORD"
}
```

## MongoDB Atlas

Another reason I like to use MongoDB is because they have an incredible cloud-hosted version called `Atlas`. So you don't even have to install MongoDB on your own server. It's simple to get started with. We are going to go through this process in the next video. It is absolutely free to get started. you get a small amount of storage and a small amount of bandwidth. However, if you want to scale up, you can do that as well.

## MongoDB Compass

Another tool that I like to use is called `MongoDB Compass`. It's a GUI for MongoDB. It's a free tool that you can use to view your data. It's very easy to use. You can also use it to import and export data. So, it's a very powerful tool. I'll show you how to get that setup as well.

## Mongoose

When it comes to integrating Mongo into your app or API that uses Node.js, there is a tool called `Mongoose` that is extremely powerful and very popular. It's a library that makes it easy to work with MongoDB. You create a `model` of your data and then you can use that model to create, read, update, and delete data from your database. You can also do things like validation and data sanitization. So, it's a very powerful tool. We'll be using Mongoose, but we'll just be scratching the surface of what it can do. Mongoose is installed using NPM.


---


# 06-atlas-setup

# MongoDB Atlas Setup

Like I said in the last lesson, Atlas is the cloud version of MongoDB and it is incredibly popular and I would say much more popular than the on-premise version of MongoDB. So, we're going to go through the process of setting up an account and creating a cluster.

## Create an Account

Go to [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas) and click the `Try Free` button.

Fill out the form and click `Create Account`. You can also sign up with Google.

## Create an Organization

Once you log in, create an organization. You can name it whatever you want. I'm going to name mine `Traversy Media`.

## Create a Project

Now, create a project. I'm going to name mine `Node API`.

## Create a Database

Click on 'Build a Database' and select the "Shared" plan, which is 100% free. Keep the default selections, which includes AWS for the provider. You can name your cluster whatever you want. I'm going to name mine `node-api-cluster`. Click `Create Cluster`.

## Create a Database User

Add a username and password and click "create user"

## Whitelist Your IP Address

Choose "My Local Environment" and then click `Add IP Address`. This will add your current IP address to the whitelist. Click `Confirm`.

It may take a few minutes for your cluster to be created. Once it's created, you can click on 'Browse Collections' and then 'Add My Own Data'. Enter a database name. I just used 'ideas_db'. Also, and a collection name of 'ideas'.

Just a note, when you create new collections, you do not have to do it here, you can do it in your application.

You will be able to see all of your data from here. You can also edit data, however if you want to manage data directly from your application, I would suggest a tool called `MongoDB Compass`. We'll go over that a little later.

For now, let's go back to the Atlas dashboard/overview and click on `Connect`. Click on `Connect Your Application` and select `Node.js` from the dropdown. Copy the connection string and paste it anywhere for now. Mine looks like this

mongodb+srv://brad:<password>@node-api-cluster.4nsqdlb.mongodb.net/ideas_db?retryWrites=true&w=majority

Change `<password>` to your password and add whatever you named your database after the last slash. I called mine 'ideas_db'.

In the next lesson, we will connect to the database via our application.


---


# 07-connecting-to-mongodb

# Connecting To MongoDB

Now that we have our cloud database hooked up to our application, we need to connect to it. We'll use the [Mongoose](https://mongoosejs.com/) library to do this.

## Installing Mongoose & dotenv

We are actually going to install two packages right now. One is Mongoose, which is called an "ODM" or "Object Document Mapper". This is a library that allows us to connect to our MongoDB database and interact with it. The other is called [dotenv](https://www.npmjs.com/package/dotenv), which is a library that allows us to store environment variables in a file called `.env`. We'll use this to store our MongoDB connection string.

```bash
npm install mongoose dotenv
```

## .env Setup

Let's add our MongoDB connection string as an environment variable. Create a file called `.env` in your root folder. Add the connection string that you copied from MongoDB Atlas in the last lesson. It should look something like this:

```bash
MONGODB_URI=mongodb+srv://<username>:<password>@cluster0-0z0z0.mongodb.net/ideas_db?retryWrites=true
```

I also add my port here. I'm going to use port 5000. You can use whatever port you want.

```bash
PORT=5000
```

Now, in the `server.js` file, we need to require the dotenv package and call the config method. This will load the environment variables from the `.env` file.

```js
require('dotenv').config();
```

Now, I will create a variable called `PORT` and set it to the value of the `PORT` environment variable. If it doesn't exist, I will set it to 5000. Then, just use that in the `app.listen` method.

```js
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
```

## Connecting To MongoDB

Now, let's connect to MongoDB. We'll use the Mongoose library to do this. Instead of putting this code directly in the `server.js` file, I'm going to create a folder called `config` and in it, create a new file called `db.js`. This will be a separate file that will handle all of our database connection logic.

```js
const mongoose = require('mongoose');

const connectDB = async () => {
  const conn = await mongoose.connect(process.env.MONGODB_URI);
  console.log(`MongoDB Connected: ${conn.connection.host}`);
};

mongoose.set('strictQuery', true);

module.exports = connectDB;
```

Now, in the `server.js` file, we need to require the `connectDB` function and call it.

```js
const connectDB = require('./config/db');

connectDB();
```

Now when you start your server, you should see a message that says "MongoDB Connected".

Congrats, you've connected to your MongoDB database!


---


# 08-mongoose-data-model

# Mongoose Data Model

With Mongoose, we can create a data model that will define the structure of our documents. This is similar to how we defined the structure of our tables in SQL. We can also define the data types of each field, as well as add validation to each field.

Create a folder called `models` and a new file called `Idea.js` inside of it. In this file, we will define our data model and schema.

```js
const mongoose = require('mongoose');

const IdeaSchema = new mongoose.Schema({
  text: {
    type: String,
    required: [true, 'Please add a text field'],
  },
  tag: {
    type: String,
  },
  username: {
    type: String,
  },
  date: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model('Idea', IdeaSchema);
```

In this file, we are importing the `mongoose` module and creating a new schema. We are then exporting the model using the `mongoose.model()` method. The first argument is the name of the model, and the second argument is the schema. The schema is just a collection of fields that we want to have in our documents.

We can now use this model to query our database, which we will do in the next lesson.


---


# 09-database-queries

# Database Queries

Now that we have Mongoose setup and a data model for our ideas, we can use really easy methods to query our database. We will be using the `Idea` model that we created in the last lesson.

Let's go into our `routes/ideas.js`

We will start by importing the `Idea` model:

```js
const Idea = require('../models/Idea');
```

## Async/await

Mongoose methods return promises, so we can use async/await to handle the promises. We will be using async/await in all of our routes. So before the callback function, we will add `async` and then we can use `await` before the Mongoose method.

## Get All Ideas

Now in the GET / route, let's get the ideas from the database and send them instead of the hardcoded ones. Yes, I know there are not any in there yet, but that's ok, we will still just get an empty array.

We can do this easily by using the `find()` method.

```js
// Get all posts
router.get('/', async (req, res) => {
  try {
    const ideas = await Idea.find();
    res.json({ success: true, data: ideas });
  } catch (err) {
    res.json({ success: false, message: err });
  }
});
```

Now, go to Postman and go to the route `http://localhost:5000/api/ideas`. You should see an empty array.

## Create an Idea

Now let's add a new idea to the database.We can use the `save()` method to save the idea to the database.

```js
// Create idea
router.post('/', async (req, res) => {
  const idea = new Idea({
    text: req.body.text,
    tag: req.body.tag,
    username: req.body.username,
  });

  try {
    const savedIdea = await idea.save();
    res.json({ success: true, data: savedIdea });
  } catch (err) {
    res.json({ success: false, message: err });
  }
});
```

Now, go to Postman and create a new POST request to `http://localhost:5000/api/ideas`. Be sure to add the text, tag and username in the body of the request. You should get a response with the idea that was created.

Now, make a get request to `http://localhost:5000/api/ideas` and you should see the idea that you just created.

It has the text, tag, username, date and an `_id` field. This is the unique identifier for the idea. We will use this to get a single idea and to delete an idea. You will also see `__v`, this is the version number of the document. This is used by Mongoose to keep track of changes to the document.

## Single Idea

Let's update the route that gets a single idea by it's ID. We can use the `findById()` method to get a single idea by it's ID.

```js
// Get single idea
router.get('/:id', async (req, res) => {
  try {
    const idea = await Idea.findById(req.params.id);
    res.json({ success: true, data: idea });
  } catch (err) {
    res.json({ success: false, message: err });
  }
});
```

Go to Postman and make a GET request to `http://localhost:5000/api/ideas/ID_OF_IDEA`. You should get the idea that you created.

## Update Idea

Now for the update route, we will is `findByIdAndUpdate()` to update the text and tag

```js
// Update idea
router.put('/:id', async (req, res) => {
  try {
    const updatedIdea = await Idea.findByIdAndUpdate(
      req.params.id,
      {
        $set: {
          text: req.body.text,
          tag: req.body.tag,
          username: req.body.username,
        },
      },
      { new: true }
    );
    res.json({ success: true, data: updatedIdea });
  } catch (err) {
    res.json({ success: false, message: err });
  }
});
```

Now, make a PUT request to `http://localhost:5000/api/ideas/ID_OF_IDEA` and update the title and body. You should get the updated idea back.

## Delete Idea

Finally, we will add the code to delete the idea. We will use the `findByIdAndDelete()` method to delete the idea.

```js
// Delete idea
router.delete('/:id', async (req, res) => {
  try {
    await Idea.findByIdAndDelete(req.params.id);
    res.json({ success: true, data: {} });
  } catch (err) {
    res.json({ success: false, message: err });
  }
});
```

We now have a fully functional API that can create, read, update and delete ideas from the database.

In the next section, we will create a simple front-end to interact with our API.
