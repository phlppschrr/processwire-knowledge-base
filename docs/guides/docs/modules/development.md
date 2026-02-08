# Developing modules in ProcessWire

Source: https://processwire.com/docs/modules/development/

## Summary

It is easy to develop a module in ProcessWire, though some PHP experience is helpful. This section introduces module development and guides you through a simple example to get you started.

## Key Points

- It is easy to develop a module in ProcessWire, though some PHP experience is helpful. This section introduces module development and guides you through a simple example to get you started.
- To create a module, you simply create PHP class that extends one of ProcessWire’s core classes, and also implements the Module interface. This Module interface doesn't actually have any required methods, but it serves as a way for ProcessWire to recognize PHP classes that are intended to be modules, and it provides guidance on how to implement various optional methods. If creating a module that isn't of a predefined type, it should extend the ProcessWire WireData class, and this is a good place to start (we'll get into predefined types later). Here's an example to summarize the above:
- Save the class that you create in a file with the same name as the class, but with the extension “.module” or “.module.php” (either works). For example, a module with class Foo (like above) would be in a file named Foo.module or Foo.module.php. The file should be placed in /site/modules/. Though we recommend placing it in a directory within that, having the same name as the module class, like /site/modules/Foo/Foo.module.

## Sections


### Creating a simple module

To create a module, you simply create PHP class that extends one of ProcessWire’s core classes, and also implements the Module interface. This Module interface doesn't actually have any required methods, but it serves as a way for ProcessWire to recognize PHP classes that are intended to be modules, and it provides guidance on how to implement various optional methods. If creating a module that isn't of a predefined type, it should extend the ProcessWire WireData class, and this is a good place to start (we'll get into predefined types later). Here's an example to summarize the above:


### Telling ProcessWire about your module

One of the first things that a module should provide is information about itself, so that it can be identified in ProcessWire. This information can be provided via static getModuleInfo() method in the class, or a separate ModuleName.info.php or ModuleName.info.json file. We'll use a static method for now, so that we can keep everything in one file. The method returns an array of information about the module. The minimum information that ProcessWire needs is to know the module’s title, a short text summary, and the version number:


### Making the module do something

Continuing our examle above, lets make the module do something. In this case, lets add a hi() method to the module that returns the string "Hello name", where "name" would be the current user's name:


### Automatically loading modules

ProcessWire supports something called autoload modules. These are modules that are loaded automatically when ProcessWire boots. Autoload modules are especially useful when you want to hook into anything within ProcessWire. We'll get into hooks in a bit, but first we'll tell you how to define an autoload module. It's as simple as just adding 'autoload' => true to the information returned by your getModuleInfo() method or file:


### Adding hooks to autoload modules

Modules may add hooks to methods in ProcessWire's core or to other modules. Nearly every key component and action in ProcessWire is hookable. A hookable method is identified by the presence of three underscores before its definition, i.e. public function ___someMethod() { ... }. You can hook any such methods from your autoload modules.


### Using an autoload module to add new methods to existing classes

Before we wrap things up, lets show you how to add a new method to an existing class in ProcessWire. In this case we'll add a new summarize() method to the Page class. This method will auto-generate a summary of the “body” text, of a specified length. This is something that might actually be useful, unlike the previous examples.


### Another example

Before we finish, lets take a look at one more module example. In this case, the module displays a message to the user every time they save a page. If most of this example makes sense to you, then you are ready to move forward with module development. There is one thing a little different here though, lets see if you can spot it. I'll tell you more after the example.


### Module name requirements

When deciding on a name for a module (the class name), please use a format where the first character is an uppercase letter (A-Z), the second character is a lowercase letter (a-z), and the remaining characters are upper-or-lowercase letters. If needed, you may also use numbers at the end of a module name, though it is rare.
