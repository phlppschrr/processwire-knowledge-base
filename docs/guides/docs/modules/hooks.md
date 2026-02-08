# Using hooks in ProcessWire

Source: https://processwire.com/docs/modules/hooks/

## Summary

ProcessWire contains many methods that you may easily hook in order to modify the behavior of the method. Hooks can also be used to add new methods to existing classes.

## Key Points

- ProcessWire contains many methods that you may easily hook in order to modify the behavior of the method. Hooks can also be used to add new methods to existing classes.
- Before hooks: A hook that runs before the hooked method. These hooks typically analyze and/or modify the arguments passed to the hooked method.
- After hooks: A hook that runs after the hooked method. These hooks typically analyze and/or modify the return value of the method.

## Sections


## About hooks


### What are the different types of hooks in ProcessWire?

Before hooks: A hook that runs before the hooked method. These hooks typically analyze and/or modify the arguments passed to the hooked method.


### What methods in ProcessWire are hookable?

Any method that begins with 3 underscores, i.e. ___method(), is hookable in ProcessWire.* There are hundreds of them. The ProcessWire API reference outlines the hookable methods for every class and API variable in ProcessWire. Note the icon in the right column of each method list table which identifies hookable methods (example). If you click on the details of any hookable method (example), it also provides introduction of how to hook both before and after that method (example).


## Defining Hooks


### Do I want my hook to run before or after the method I am hooking? (Or, does it matter?)

Before hooks You would want your hook to run before the hooked method if you want to analyze or modify the arguments supplied to the hooked method. Another use case for a before hook is if you wanted to entirely replace the implementation of the hooked method. Before hooks are defined with $this->addHookBefore(…); within a class, or wire()->addHookBefore(…); outside of a class.


### Do I want my hook to apply to all instances of a class, or just one?

Most of the time you want a hook to apply to all instances of a class. For instance, when you hook Page::viewable, you likely want your hook to be called regardless of what Page it is. Such hooks are defined by specifying the class and method (i.e. Class::method) in the addHook() call. For example:


### Where should I define my hook?

Hooks are most often defined in ProcessWire plugin modules or initialization template files. However, this is not a requirement, and you may technically define hooks anywhere you want. But you need to make sure that your hook really does get called when you want it to, so your hook must be defined and attached sometime before the method you are hooking gets called.


### Attaching hooks from a plugin module

Attach hooks with a plugin module set to "autoload" on every request. Such modules are called "autoload modules." These autoload modules have an init() method that gets called before ProcessWire handles a web request. This is the best place to attach hooks. However, this init() method is called before ProcessWire even knows what $page it will be rendering. So if your module needs to determine whether it should hook or not based on what $page is being viewed, you should attach your hook in a ready() method rather than an init() method. The ready() method is always called for all autoload modules right after ProcessWire determines what $page is going to be viewed.
