# ProcessWire API variables

Source: https://processwire.com/docs/start/variables/

## Summary

ProcessWire provides various API variables to every template file. These variables provide full access to all site content. This page provides an introduction on how to use them.

## Key Points

- ProcessWire provides various API variables to every template file. These variables provide full access to all site content. This page provides an introduction on how to use them.
- API variables can be accessed in a few different ways. The most common way is as a variable. Here are a few different ways you might access the same $page API variable (as an example):
- `$page` the most common access as a variable.

## Sections


## Introduction to ProcessWire API variables

ProcessWire provides various API variables to every template file. These variables provide full access to all site content. This page provides an introduction on how to use them.

API variables can be accessed in a few different ways. The most common way is as a variable. Here are a few different ways you might access the same $page API variable (as an example):

`$page` the most common access as a variable.

`page()` accessing as a function can be very convenient, when available.

`wire('page')` This works anywhere, and with any version of ProcessWire.

`wire()->page` This works anywhere too, and is more IDE friendly.

`$this->page` This is how you might access it from within a Wire-derived class.

`$this->wire('page')` A slightly more efficient way you can access from within a Wire-derived class.

`$this->wire()->page` Like the above, but more IDE friendly.

`$pages->wire()->page` API variables can also access all other API variables, by way of their wire() method. In this example, we are accessing the $page API variable from the $pages API variable. So if you have any one API variable, then you actually have them all.

Accessing API variables as a function rather than a variable can be more convenient when the variable version may be out of scope, or if your IDE highlights API variables as undefined. So whenever we refer to an API variable, make note that access it however you'd like.

This is just an introduction to some of ProcessWire's API variables. Once you are familiar with these, you'll want to use ProcessWire's full [API reference](/api/ref/) instead.


### Some of ProcessWire’s most common API variables
