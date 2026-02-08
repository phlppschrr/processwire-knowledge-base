# Various ways of accessing the ProcessWire API

Source: https://processwire.com/docs/start/api-access/

## Summary

In ProcessWire there are several ways that you can access the API and we take a look at the most common ones here. Regardless of what method you use, you are technically accessing what are called API variables.

## Key Points

- In ProcessWire there are several ways that you can access the API and we take a look at the most common ones here. Regardless of what method you use, you are technically accessing what are called API variables.
- Each API variable has a unique name to distinguish it from others. For instance, the “pages” (plural) API variable provides access to loading and saving pages, the “page” (singular) API variable provides access to the page being viewed, the “input” API variable provides access to user input, and so on. See the API reference for a full list of ProcessWire’s core API variables.
- There are several different ways to access these API variables. For instance, all of the following accesses to the $page API variable are synonyms of each other, though with different benefits depending on the context:

## Sections


### You are always accessing the same exact thing

Whichever way you access an API variable, there’s no need for confusion, simply remember that you are always accessing exactly the same thing. The return value from all of the above access methods would be identical.


## API variables in template files (the most common context)

Most users will be accessing API variables exclusively from the context of their site’s template files. The two most common ways to access API variables from template files are directly, like $pages or as a function, like pages(). Sometimes you might also see wire('pages'). They are all the same thing, but we’ll cover them all here and look at the benefits and drawbacks of each.


### The API as PHP $variables

The most common way to access the API is from PHP variables like $pages, $user, $input, etc. This has been available all the way since ProcessWire version 1.0. Every template file that ProcessWire renders is provided with all of the defined API variables, ready to access. If new API variables are added by some module, they likewise become available as $variables in your template files.


### The API as PHP functions()

In ProcessWire 3.x you also have the option of accessing the API as PHP functions, i.e. pages(), user(), input(), etc. They access exactly the same thing as their variable counterparts, but are just typed slightly differently in that they are accessed as var() rather than $var, which is a very minor difference. Accessing a property or method from them is identical, i.e. $var->method() and var()->method() are equivalent. However, the function version adds some additional convenience that we’ll take a closer look at here.


### Enabling the functions API

First things first, if you want to use the functions API, you might have to enable it, if it isn’t already. For most new installations, it will already be enabled by default. But for existing installations you may have to add the following to your /site/config.php file:


## Benefits of the functions API


### Functions are always in scope (variables are not)

When ProcessWire renders your template file, it provides all of the API variables to it. But a best practice when coding anything is: do not repeat yourself. Meaning, don’t write the same blocks of code more than once. Most commonly you do this by bundling that block of code into a function, and then calling that function whenever you need the logic that it provides. The problem is that such functions will not see any of the API $variables (unless you pass them in as arguments)—but they can see the API functions, because they are always in scope.


### Functions cannot be accidentally overwritten (variables can be)

When using API variables, it’s possible to accidentally overwrite any API variable, and thus break your site. Sometimes it’s not immediately obvious. Take the following as an examples:
