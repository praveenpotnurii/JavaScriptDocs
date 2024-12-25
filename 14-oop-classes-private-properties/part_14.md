
# 01-classes

# Classes

We have talked about OOP quite a bit and as I've said before, JavaScript does not have classes at its core. However, The ES6 spec does have classes and they are very similar to classes in other languages. I would say that most OOP languages use classes, including Java, C#, C++, PHP and Objective-C. If you have worked with a language that uses classes, then this should be pretty familiar to you.

What I mean when I say JavaScript does not have classes at it's core is that the code that is actually being run looks like what we have already learned. Constructor functions, prototypes, etc. However, ES6 gave us what is called a "syntactic sugar" for classes. This means that we can write code that looks like classes, but it is actually just constructor functions and prototypes under the hood.

It has become pretty popular to use classes in JavaScript. Many people think that it is a much easier and less confusing syntax. Also, a lot of people are coming from class-based languages. So, it is nice to have a syntax that is similar to what they are used to. What you use is completely up to you. We saw the basics of constructors/prototypes, now let's get into classes.

## Creating a Class

To create a class, we use the `class` keyword. We then give it a name. The name should be capitalized. This is just a convention. It is not required. We then use the `constructor` keyword to create a constructor function. This is the function that will be called when we create a new instance of the class. We can then add properties to `this` just like we would in a constructor function. We can also add methods to the prototype just like we would in a constructor function. Here is an example:

```js
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }

  area() {
    return this.height * this.width;
  }
}
```

We can then create a new instance of the class by using the `new` keyword. We then call the class like it was a function. We pass in the arguments that the constructor function expects. Here is an example:

```js
const square = new Rectangle(10, 10);
```

We can then access the properties and methods on the instance just like we would with any other object. Here is an example:

```js
console.log(square.area()); // 100
```

In the `area()` method, we used `this` to access the properties. We can also access methods with `this`. Let's add a few more methods, including a `logArea()` method and access `area()` within it.

```js
class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }

  area() {
    return this.height * this.width;
  }

  perimeter() {
    return 2 * (this.height + this.width);
  }

  isSquare() {
    return this.height === this.width;
  }

  logArea() {
    console.log('Rectangle Area: ' + this.area());
  }
}

console.log(square.perimeter()); // 40
console.log(square.isSquare()); // true
square.logArea(); // Rectangle Area: 100
```

## Under The Hood

Let's log the `square` variable that we created from the class to the console:

```js
console.log(square);
```

Notice we see the same thing that we have been seeing when we use constructors/prototypes.

<img src="images/rect-class-console.png" width="500">

It is a `Rectangle` object with a `height` property of `10` and a `width` property of `10`. It also has an `area` method on the prototype. This is exactly what we would expect.

As I mentioned before, classes are just syntactic sugar for constructor functions and prototypes. So, what is actually happening when we create a class? Let's take a look:

```js
function Rectangle(height, width) {
  this.height = height;
  this.width = width;
}

Rectangle.prototype.area = function () {
  return this.height * this.width;
};

Rectangle.prototype.perimeter = function () {
  return 2 * (this.height + this.width);
};

Rectangle.prototype.isSquare = function () {
  return this.height === this.width;
};

Rectangle.prototype.logArea = function () {
  console.log('Rectangle Area: ' + this.area());
};

const square = new Rectangle('Square', 20, 20);
console.log(square.perimeter()); 
console.log(square.isSquare()); 
square.logArea(); 
```

The same code that we have been writing throughout this section. The only difference is that we are using the `class` keyword and the `constructor` keyword and the code looks a bit nicer.

It's up to you on how you want to write your code. My job is just to show you the different ways that you can write it. Some people like the constructor/prototype method instead of using the abstraction of classes. Some people like neat structure of classes. I prefer classes most of the time, but I'll use either.


---


# 02-class-inheritance

# Class Inheritance

We looked at the ES6 class syntax in the previous lesson. In this lesson, we will look at inheritance in classes.

Inheritance is the ability to create a new class from an existing class. The new class will inherit all the properties and methods of the existing class. This is called a `subclass` or `child class`. The existing class is called a `superclass` or `parent class`.

Let's create a parent class of `Shape`. This class will have a constructor that takes in a name. It will also have a `logName` method that will log the name to the console. Here is an example:

```js
class Shape {
  constructor(name) {
    this.name = name;
  }

  logName() {
    console.log(this.name);
  }
}
```

Now, let's create a subclass of `Shape` called `Rectangle`. This class will have a constructor that takes in a height and width. It will also have an `area` method that will return the area of the rectangle. Here is an example:

```js
class Rectangle extends Shape {
  constructor(name, height, width) {
    super(name);
    this.height = height;
    this.width = width;
  }

  area() {
    return this.height * this.width;
  }
}
```

We did a couple of new things here. First, we used the `extends` keyword to create a subclass of `Shape`. This is how we tell JavaScript that `Rectangle` is a subclass of `Shape`. Second, we used the `super()` method to call the constructor of the parent class. We need to do this so that the `name` property is set on the instance. If we did not call `super`, the `name` property would not be set on the instance. Third, we added the `height` and `width` properties to the instance. Finally, we added the `area` method to the instance.

We can create a `Circle` class and do the same thing.

```js
class Circle extends Shape {
  constructor(name, radius) {
    super(name);
    this.radius = radius;
  }

  area() {
    return Math.PI * this.radius * this.radius;
  }
}
```

We can now create a new instance of `Rectangle` and/or `Circle` and call the `logName` method. Here is an example:

```js
const square = new Rectangle('Square', 10, 10);
square.logName(); // Square
```

Let's log the square variable to the console.

```js
console.log(square);
```

<img src="images/rect-class-inherit.png" width="500">

You can see that in the prototype, the constructor is the `Rectangle` class. The `prototype` property is the `Shape` class. This is how inheritance works in JavaScript. The `Rectangle` class inherits all the properties and methods of the `Shape` class. You can see the `logName()` function in the `Shape` prototype. This is how the `logName()` method is available on the `Rectangle` instance.

We can use `instanceOf` to check if our `square` instance is an instance of the `Rectangle` AND the `Shape` class. Which it is.

```js
console.log(square instanceof Rectangle); // true
console.log(square instanceof Shape); // true
```

## Overriding Methods

We can override methods in a subclass. Let's override the `logName` method in the `Rectangle` class.

```js
 logName() {
    console.log('Rectangle name is: ' + this.name);
  }

 square.logName(); // Rectangle name is: Square
```


---


# 03-static-methods

# Static Methods

Static methods are methods that are available on the class itself. They are not available on the instances of the class. Static methods are often used to create utility functions or to hold data that is shared across all instances of the class. Let's create our `Shape` and `Rectangle` class from the previous example and add a static method called `getClassName`.

A static method is created the same way as a regular method. The only difference is that we use the `static` keyword.

```js
class Shape {
  constructor(name) {
    this.name = name;
  }

  logName() {
    console.log(this.name);
  }

  static getClassName() {
    return 'Shape';
  }
}
```

```js
class Rectangle extends Shape {
  constructor(name, height, width) {
    super(name);
    this.height = height;
    this.width = width;
  }

  area() {
    return this.height * this.width;
  }

  static getClassName() {
    return 'Rectangle';
  }
}
```

Let's try to crate an instance of a `Rectangle` and call the `getClassName` method.

```js
const rect = new Rectangle('Rectangle', 10, 20);

rect.getClassName(); // TypeError: rect.getClassName is not a function
```

This does not work, because the `getClassName` method is not available on the instance of the `Rectangle` class. It is only available on the class itself.

```js
console.log(Shape.getClassName());
console.log(Rectangle.getClassName());
```

So if you have a method where you don't need to access the instance of the class, you can make it a static method. This way you can call it directly on the class.


---


# 04-bind-this

# bind() & this

So we've talked about the `this` keyword quite a bit. You know that when we create either a constructor function or a class, `this` refers to the current instance. However, if we use it in a regular function or the global scope, it refers to the `window` object. If we use it on an event handler, it refers to the element that the event was triggered on. So the `this` keyword is very dynamic and it changes depending on how we use it. That's why we have certain methods that allow us to set the `this` value manually. Those methods are `call()`, `apply()`, and `bind()`. We already looked at `call()` back in the prototypical inheritance lesson. We'll look at `apply()` later. Right now I'm going to show you how to use `bind()`. We'll need to know this for our project that's coming up as well.

So `bind()` is used to set the `this` value manually. It returns a new function where the `this` value is bound to the value we pass in. One very common use case for `bind()` is when we want to use a callback function.

Let's create a class called `App` and add a property of `serverName` and add an event listener in the constructor to listen for a button click and when that happens, we want to call a class method and use the `this` value from the `App` class.

```js
class App {
  constructor() {
    this.serverName = 'http://localhost:3000';

    document
      .querySelector('button')
      .addEventListener('click', this.handleClick);
  }

  handleClick() {
    console.log(this.serverName);
  }
}

const app = new App();
```

If we run this code, we get **undefined**. This is because the `this` value is the `window` object due to the fact that we are using a callback function, which is a regular function.

If we just log `this` inside the `handleClick()` method, we get the `window` object.

```JavaScript
 handleClick() {
    console.log(this); // Window {window: Window, self: Window, document: document, name: "", location: Location, …}
  }
```

So we need to use `bind()` to set the `this` value to the `App` class.

```js
class App {
  constructor() {
    this.serverName = 'localhost';

    document
      .querySelector('button')
      .addEventListener('click', this.handleClick.bind(this));
  }
  handleClick() {
    console.log(this.serverName);
  }
}

const app = new App();
```

Now, we get the `serverName` property value. If you log `this` inside the `handleClick()` method, you get the `App` class instance.

```js
handleClick() {
    console.log(this); // App {serverName: "localhost"}
  }
```

Methods like `call` and `bind` are very overwhelming to a lot of people, but I gave you two real life examples, which I think helps people understand them better.


---


# 05-getters-setters-classes

# Getters & Setters With Classes

Getters and setters are methods that are used to get or set property values for objects. We can use them with classes, constructors, and object literals. I'm going to show you all three, but I'm going to start with classes, because it's the most common way to use them and the easier syntax.

There are a few reasons to use getters and setters. They allow you to control how a property is accessed. This is useful when you want to perform an action before returning the value of a property. For example, you may want to ensure that a property is always capitalized before getting or setting it.

They also allow you to keep the same syntax whether it's a regular property or a method.

They are also used with private properties. For example, you may have properties that you don't want to be accessed directly. Instead you'll have getters and setters for them. I'll get more into that soon.

I'm going to start off with a different example than our shapes classes. We're going to create a person class.

```js
class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
}
```

With this class, I can access the first name and last name of a person like this:

```js
const person = new Person('John', 'Doe');
console.log(person.firstName); // John
console.log(person.lastName); // Doe
```

But what if I want to make sure that the first name and last name are always capitalized? I check that before I get it and/or set it.

```js
class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  get firstName() {
    return this._firstName.charAt(0).toUpperCase() + this._firstName.slice(1);
  }

  set firstName(value) {
    this._firstName = value.charAt(0).toUpperCase() + value.slice(1);
  }
}
```

Now, when I get or set the first name, it will always be capitalized.

```js
const person = new Person('john', 'doe');
console.log(person.firstName); // John
```

I would probably do the same for the last name and create a utility function for capitalizing a string.

```js
class Person {
  // ...
  get firstName() {
    return this.capitalizeFirst(this._firstName);
  }

  set firstName(value) {
    this._firstName = this.capitalizeFirst(value);
  }

  get lastName() {
    return this.capitalizeFirst(this._lastName);
  }

  set lastName(value) {
    this._lastName = this.capitalizeFirst(value);
  }

  capitalizeFirst(value) {
    return value.charAt(0).toUpperCase() + value.slice(1);
  }
}
```

Let's say that we want to have a full name property that is the first name and last name combined. We could create a method called `getFullName` that returns the full name. But we can also create a getter for it, which would make it look like a property.

```js
get fullName() {
  return `${this.firstName} ${this.lastName}`;
}

set fullName(name) {
  const names = name.split(' ');
  this.firstName = names[0];
  this.lastName = names[1];
}
```

Now we can just access the full name like a property.

```js
const person = new Person('brad', 'traversy');
console.log(person.fullName); // John Doe
```


---


# 06-getters-setters-defineproperty

# Getters & Setters Using defineProperty

In the last lesson, I showed you how to create getters and setters with the `get` and `set` keywords inside of a class. But there's another way that we can do this that is common with `constructor functions` and that is using the `Object.defineProperty()` method.

It takes three arguments. The first is the object that we want to add the property to (this). The second is the name of the property that we want to add. And the third is an object that contains the getter and setter functions. Let's add a getter and setter for the `firstName` and `lastName` property

```js
function Person(firstName, lastName) {
  this._firstName = firstName;
  this._lastName = lastName;

  Object.defineProperty(this, 'firstName', {
    get: function () {
      return this._firstName;
    },
    set: function (value) {
      this._firstName = value;
    },
  });

  Object.defineProperty(this, 'lastName', {
    get: function () {
      return this._lastName;
    },
    set: function (value) {
      this._lastName = value;
    },
  });
}
```

As you can see, the original properties are prefixed with an underscore. Because we want the non-underscore version to be the getter and setter.

Now, we can use it in the same way we used the class version. I'm going to use lowercase letters because I want to make it part of the getter that it returns uppercase

```js
const person1 = new Person('john', 'doe');
console.log(person1.firstName); //john
console.log(person1.lastName); // doe
```

Let's create a method to capitalize the first letter. I am actually going to put this on to the `prototype`. We don't have to, but why not?

```js
Person.prototype.capitalizeFirst = function (value) {
  return value.charAt(0).toUpperCase() + value.slice(1);
};

```

Now, let's add to the getters. Let's also create a getter for the `fullName`. In that getter, we can actually use the `firstName` and `lastName` getters. It will automatically be capitalized.

```js
function Person(firstName, lastName) {
  this._firstName = firstName;
  this._lastName = lastName;

  Object.defineProperty(this, 'firstName', {
    get: function () {
      return this.capitalizeFirst(this._firstName);
    },
    set: function (value) {
      this._firstName = value;
    },
  });

  Object.defineProperty(this, 'lastName', {
    get: function () {
      return this.capitalizeFirst(this._lastName);
    },
    set: function (value) {
      this._lastName = value;
    },
  });

  Object.defineProperty(this, 'fullName', {
    get: function () {
      // Using the getters
      return this.firstName + ' ' + this.lastName;
    },
    set: function (value) {
      this._firstName = value;
    },
  });
}
```

Let's try it out:

```js
console.log(person1.firstName); // John
console.log(person1.lastName); // Doe
console.log(person1.fullName); // John Doe
```

## Object Literal Syntax

Let's do the same thing using object literal syntax. We could create a new `capitalizeFirst()` function or we can use the `Person` prototype method.

```js
const PersonObj = {
  _firstName: 'jane',
  _lastName: 'doe',

  get firstName() {
    return Person.prototype.capitalizeFirst(this._firstName);
  },

  set firstName(value) {
    this._firstName = value;
  },

  get lastName() {
    return Person.prototype.capitalizeFirst(this._lastName);
  },

  set lastName(value) {
    this._lastName = value;
  },

  get fullName() {
    // Using the getters
    return this.firstName + ' ' + this.lastName;
  },
};
```

Now, we can set the `width` and `height` properties and get and set the `area` property. I'm going to use the `Object.create()` method to create a new object that inherits from the `RectangleObj` object, but you could just as well set it directly on the `RectangleObj` object.

```js
const person2 = Object.create(PersonObj);
console.log(person2.firstName); // Jane
console.log(person2.lastName); // Doe
console.log(person2.fullName); // Jane Doe
```


---


# 07-private-properties-convention

# Convention For Private Properties

Now we are going to get a bit deeper into encapsulation, which often includes the process of hiding data or hiding specific properties and methods of a class.

In many OOP languages that use classes, you can use specific keywords to indicate which properties and methods are accessible from outside the class. For example, in Java, you can use the `private` keyword to indicate that a property or method is only accessible from within the class. In JavaScript, we don't have those keywords, but there is a convention that is commonly used to indicate that a property or method is private. We use an underscore `_` before the property or method name.

There is also a new feature in ES2022 that allows us to use the `#` symbol to create private fields. This is a new feature that isn't yet supported in all browsers. We'll look at that in the next video. Right now, in the beginning of 2023, you'll probably run into the underscore convention more often than the `#` symbol. There are a few other ways to implement this as well including using `Symbols` and the `WeakMap` object. The underscore convention is definitely the most common at this point in time.

Let's create a new class called `Wallet` and add a constructor that has a `balance` and a `transactions` property. The `balance` will be 0 and `transactions` will be an empty array.

```js
class Wallet {
  constructor() {
    this.balance = 0;
    this.transactions = [];
  }
}
```

Now let's add a `deposit` method that takes an amount and adds it to the `balance` and adds a new transaction to the `transactions` array. We'll also add a `withdraw` method that takes an amount and subtracts it from the `balance` and adds a new transaction to the `transactions` array.

```js
class Wallet {
  constructor() {
    this.balance = 0;
    this.transactions = [];
  }

  deposit(amount) {
    this.balance += amount;
  }

  withdraw(amount) {
    this.balance -= amount;
  }
}
```

Now let's create a new instance of the `Wallet` class and call the `deposit` method with an amount of 300. Then withdraw an amount of 50. Then we'll log the `balance` property to the console.

```js
const wallet = new Wallet();
wallet.deposit(300);
wallet.withdraw(50);
console.log(wallet.balance); // 250
```

It works as expected. However, we don't want to expose the `balance` property to the outside world. We want to make it private. We want to make it so that the only way to access the `balance` property is through the `deposit` and `withdraw` methods. This is part of encapsulation.

Now, like I said, JavaScript does not have a `private` keyword, but we can use the underscore convention to indicate that a property or method is private. So let's add an underscore to the `balance` property.

```js
class Wallet {
  constructor() {
    this._balance = 0;
    this.transactions = [];
  }

  deposit(amount) {
    this._balance += amount;
  }

  withdraw(amount) {
    if (amount > this._balance) {
      console.log(`No enough funds`);
      return;
    }
    this._balance -= amount;
  }
}
```

This convention tells the developer that the `balance` property is private and should not be accessed directly. We do want to be able to get the balance. We just don't want to be able to set it directly. So let's add a `getBalance` method that returns the `balance` property.

```js
class Wallet {
  constructor() {
    this._balance = 0;
    this.transactions = [];
  }

  deposit(amount) {
    this._balance += amount;
  }

  withdraw(amount) {
    if (amount > this._balance) {
      console.log(`No enough funds`);
      return;
    }
    this._balance -= amount;
  }

  getBalance() {
    return this._balance;
  }
}
```

Now we can call the `getBalance` method to get the balance. We can't access the `balance` property directly.

```js
const wallet = new Wallet();
wallet.deposit(300);
wallet.withdraw(50);
console.log(wallet.getBalance()); // 250
```

## Using a Getter

We could use a function, but I would prefer to use a getter to get the balance. Let's remove the function and add a getter.

```js
class Wallet {
  constructor() {
    this._balance = 0;
    this.transactions = [];
  }

  deposit(amount) {
    this._balance += amount;
  }

  withdraw(amount) {
    if (amount > this._balance) {
      console.log(`No enough funds`);
      return;
    }
    this._balance -= amount;
  }

  get balance() {
    return this._balance;
  }
}
```

Now, we can access the `balance` through the getter

```js
const wallet = new Wallet();
wallet.deposit(300);
wallet.withdraw(50);
console.log(wallet.balance); // 250
```

The `transactions` property should also be private, so let's add an underscore to that property and create another getter for that. Let's also create 2 new private methods called `_processDeposit` and `_processWithdrawal`. These methods will add a new transaction to the `transactions` array.

```js
class Wallet {
  constructor() {
    this._balance = 0;
    this._transactions = [];
  }

  get balance() {
    return this._balance;
  }

  get transactions() {
    return this._transactions;
  }

  deposit(amount) {
    this._processDeposit(amount);
    this._balance += amount;
  }

  withdraw(amount) {
    this._processWithdraw(amount);
    if (amount > this._balance) {
      console.log(`No enough funds`);
      return;
    }
    this._balance -= amount;
  }

  _processDeposit(amount) {
    console.log(`Depositing ${amount}`);

    this._transactions.push({
      type: 'deposit',
      amount,
    });
  }

  _processWithdraw(amount) {
    console.log(`Withdrawing ${amount}`);

    this._transactions.push({
      type: 'withdraw',
      amount,
    });
  }
}
```

We made the 2 new methods private because there is absolutely no reason for the outside world to call these methods. They are only used internally by the `deposit` and `withdraw` methods. When we create documentation for this interface, we would not include these methods. there is no reason to. Hopefully, encapsulation makes sense to you now.

Now, we can call the `deposit` and `withdraw` methods and we can access the `balance` and `transactions` properties through the getters.

```js
const wallet = new Wallet();
wallet.deposit(300);
wallet.withdraw(50);
console.log(wallet.balance); // 250
console.log(wallet.transactions); // [{type: 'deposit', amount: 300}, {type: 'withdraw', amount: 50}]
```


---


# 08-private-fields-es2022

# Private Fields In ES2022

Up until recently, JavaScript did not have a way to create private entities in classes. We used the underscore convention for a long time. However, in ES2022, we now have a way to create private class fields by using the `#` symbol. This is a new feature that isn't yet supported in all browsers. Right now, in the beginning of 2023, you'll probably run into the underscore convention more often than the `#` symbol. But this seems to be the future of private fields in JavaScript.

Let's use our `Wallet` example from the last video and go through and see what we need to change.

First, there is now a concept of `fields` and `properties`. A `field` is a variable that is declared inside of a class. A `property` is a variable that is declared inside of an object. So, in the last video, we had a `balance` property and a `transactions` property. Now, we're going to have a `#balance` field and a `#transactions` field defined directly in the class as opposed to in the constructor.

```js
class Wallet {
  #balance = 0;
  #transactions = [];
}
```

The getters will remain the same. We'll just need to change the `balance` property to `#balance` and the `transactions` property to `#transactions`.

```js
class Wallet {
  #balance = 0;
  #transactions = [];

  get balance() {
    return this.#balance;
  }

  get transactions() {
    return this.#transactions;
  }
}
```

The `deposit` and `withdraw` methods will also remain the same. We'll just need to change the `balance` property to `#balance` and the `transactions` property to `#transactions`. We will also make the process methods private by adding the `#` symbol to the beginning of the method name.

```js
class Wallet {
  #balance = 0;
  #transactions = [];

  get balance() {
    return this.#balance;
  }

  get transactions() {
    return this.#transactions;
  }

  deposit(amount) {
    this.#processDeposit(amount);
    this.#balance += amount;
  }

  withdraw(amount) {
    this.#processWithdraw(amount);
    if (amount > this.#balance) {
      console.log(`No enough funds`);
      return;
    }
    this.#balance -= amount;
  }

  #processDeposit(amount) {
    console.log(`Depositing ${amount}`);

    this.#transactions.push({
      type: 'deposit',
      amount,
    });
  }

  #processWithdraw(amount) {
    console.log(`Withdrawing ${amount}`);

    this.#transactions.push({
      type: 'withdraw',
      amount,
    });
  }
}
```

Now, we can create a new instance of the `Wallet` class and call the `deposit` and `withdraw` methods and then show the balance and transactions using the getters.

```js
const myWallet = new Wallet();
myWallet.deposit(300);
myWallet.withdraw(50);
console.log(myWallet.balance); // 250
console.log(myWallet.transactions); // [ { type: 'deposit', amount: 300 }, { type: 'withdraw', amount: 50 } ]
```

Now, lets try and access the `#balance` and `#transactions` fields directly. We'll get an error because they are private fields.

```js
console.log(myWallet.#balance); // Uncaught SyntaxError: Private field '#balance' must be declared in an enclosing class
console.log(myWallet.#transactions); // Uncaught SyntaxError: Private field '#transactions' must be declared in an enclosing class
```

Let's try to be criminals and directly change our balance to $1,000,0000.

```js
myWallet.#balance = 1000000;
console.log(myWallet.balance); // Uncaught SyntaxError: Private field '#balance' must be declared in an enclosing class
```

What if we try and just do `myWallet.balance = 1000000`? This will work because we're not directly changing the `#balance` field.

```js
myWallet.balance = 1000000;
console.log(myWallet.balance); // 250
```

Let's try and call the `#processDeposit` method directly. We'll get an error because it is a private method. Same with `#processWithdraw`

```js
myWallet.#processDeposit(100); // Uncaught SyntaxError: Private field '#processDeposit' must be declared in an enclosing class
```

So, you see, we now have full encapsulation and real private fields and methods in JavaScript. This is a huge step forward for JavaScript.


---


# 09-property-flags-descriptors

# Property Flags & Descriptors

Property flags are internal attributes of a property. They are not accessible directly, but we can use `Object.getOwnPropertyDescriptor`. The following is a list of available property flags:

- `[[Configurable]]` - if `true`, the property can be deleted and these attributes can be modified, otherwise not
- `[[Enumerable]]` - if `true`, the property will be returned in a `for...in` loop, otherwise not
- `[[Writable]]` - if `true`, the value of the property can be changed, otherwise not
- `[[Value]]` - the value of the property

## `getOwnPropertyDescriptor` Method

When we create a new object, wether it is an object literal or an instance from a constructor or a class, the flags for all properties are set to `true` by default. The `getOwnPropertyDescriptor()` method returns an object with property flags. This object is called a property descriptor.

Before, we create our own object and experiment, let's check the flags for the `Math.PI` property.

```js
let descriptor = Object.getOwnPropertyDescriptor(Math, 'PI');
console.log(descriptor); // {value: 3.141592653589793, writable: false, enumerable: false, configurable: false}
```

As you can see, the property flags of the `Math.PI` property are `false`. If we try and change the value of the `Math.PI` property, it will not work.

```js
Math.PI = 3;
console.log(Math.PI); // 3.141592653589793
```

Let's create an object literal called `rectObj` object to work with. It will have a `name`, `height` and `width` property. You could also use a constructor or a class to create the object, but an object literal is easier to work with.

```js
const rectObj = {
  name: 'Rectangle 1',
  width: 10,
  height: 10,
};

console.log(rectObj); // {name: "Rectangle 1", width: 10, height: 10}
```

## Get Property Flags

Let's get the property flags of the `name` property of the `rectObj` object.

```js
console.log(Object.getOwnPropertyDescriptor(rectObj, 'name'));
// {value: "Rectangle 1", writable: true, enumerable: true, configurable: true}
```

They are all set to `true` by default.

## Change Property Flags

We can use the `Object.defineProperty` method to change the property flags of an existing property. Let's change the property flags of the `name` property of the `rectObj` object.

```js
Object.defineProperty(rectObj, 'name', {
  writable: false,
  enumerable: false,
  configurable: false,
});
```

if we check again the property flags of the `name` property, we can see that they have changed.

```js
console.log(Object.getOwnPropertyDescriptor(rectObj, 'name'));
// {value: "Rectangle 1", writable: false, enumerable: false, configurable: false}
```

Now let's try and change the name value to something else:

```js
rectObj.name = 'Rectangle 1 Updated';
console.log(rectObj.name); // Rectangle 1
```

The name was not updated because we set the `writable` flag to `false`. Let's try and delete the `name` property:

```js
delete rectObj.name;
console.log(rectObj.name); // Rectangle 1
```

The `name` property was not deleted because we set the `configurable` flag to `false`.

Let's try and enumerate through the properties of the `rectObj` object. I'm going to use a `for...of` loop on the Object.entries method to get the key and value of each property.

```js
for (let [key, value] of Object.entries(rectObj)) {
  if (typeof value !== 'function') {
    console.log(`${key}: ${value}`);
  }
}
```

Notice the `name` property was not returned because we set the `enumerable` flag to `false`.

So we have really limited the access to the `name` property of the `rectObj` object. We can't change the value, delete the property, or enumerate through it. We can't even change the property flags of the `name` property because we set the `configurable` flag to `false`.

## `Object.getOwnPropertyDescriptors` Method

The `Object.getOwnPropertyDescriptors` method returns an object with all the property flags of the object.

```js
console.log(Object.getOwnPropertyDescriptors(rectObj));
// {name: {…}, width: {…}, height: {…}, area: {…}}
```

They are all true except for the `name` property, because we changed them.


---


# 10-sealing-freezing-properties

# Sealing & Freezing Objects

Let's use our `rectObj` object from the previous lesson to demonstrate `sealing` and `freezing`.

```js
const rectObj = {
  name: 'Rectangle 1',
  width: 10,
  height: 10,
};
```

## Sealing

Sealing an object prevents new properties from being added to it. Existing properties can still be modified or deleted. It sets the `configurable` flag to `false` for all existing properties. `writeable` and `enumerable` flags are not affected.

```js
Object.seal(rectObj);

// Check flags
let descriptor = Object.getOwnPropertyDescriptors(rectObj);
console.log(descriptor); // {name: {…}, width: {…}, height: {…}, area: {…}}
```

Let's try and add a new property to the `rectObj` object.

```js
rectObj.color = 'red';
console.log(rectObj); // NOT added
```

Try removing an existing property from the `rectObj` object.

```js
delete rectObj.width;
console.log(rectObj); // NOT removed
```

I can not add a new property, however I can still modify existing properties.

```js
rectObj.height = 20;
console.log(rectObj); // Rectangle {name: "Rectangle 1", width: 10, height: 20}
```

## Freezing

Freezing an object prevents new properties from being added to it and prevents existing properties from being modified or deleted. It sets the `configurable` and `writable` flags to `false` for all existing properties.

Let's create a new object called `circleObj` and freeze it.

```js
const circleObj = {
  name: 'Circle 1',
  radius: 10,
};
```

```js
Object.freeze(circleObj);

// Check flags
let descriptor = Object.getOwnPropertyDescriptors(circleObj);
console.log(descriptor); // {name: {…}, width: {…}, height: {…}}
```

Let's try adding, removing and changing a frozen object:

```js
// Try adding a new property
circleObj.color = 'red';
console.log(circleObj); // Not added

// Try deleting a property
delete circleObj.width;
console.log(circleObj); // Not deleted

// Try changing a property
circleObj.name = 'Rectangle 2 Updated';
console.log(circleObj); // Not changed
```

## Checking if an Object is Sealed or Frozen

We can use the `Object.isSealed` and `Object.isFrozen` methods to check if an object is sealed or frozen.

```js
console.log('rectObj sealed? ', Object.isSealed(rectObj)); // true
console.log('rectObj frozen? ', Object.isFrozen(rectObj)); // false
console.log('circleObj frozen? ', Object.isFrozen(circleObj)); // true
console.log('circleObj sealed? ', Object.isSealed(circleObj)); // true
```

Notice that `rectObj` is only frozen and not sealed. `circleObj` is both sealed and frozen. This is because if we freeze an object, it is automatically sealed.
