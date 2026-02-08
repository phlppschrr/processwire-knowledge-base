# Code Internationalization (i18n)

Source: https://processwire.com/docs/multi-language-support/code-i18n/

## Summary

This page provides detailed documentation on everything you need to know to make your template files or modules translatable using ProcessWire's translation tools.

## Key Points

- This page provides detailed documentation on everything you need to know to make your template files or modules translatable using ProcessWire's translation tools.
- This will primarily be of interest to those that are wanting to make static text in their own template files or modules translatable using ProcessWire's translation tools. ProcessWire uses a GNU gettext-like system for managing language translation of strings in your code (without actually using gettext).
- Below is a brief video demonstrating how simple it is to use ProcessWire's language translation tools in your own templates (switch to 720p and the full screen version to see it better):

## Sections


### Demonstration Video

Below is a brief video demonstrating how simple it is to use ProcessWire's language translation tools in your own templates (switch to 720p and the full screen version to see it better):


## Translatable strings

In order to make a string translatable in your template or module code, you just have to wrap the original string in a $this->_() or __() function call:


## Marking strings for translation

The strings for translation are wrapped in a call to one of a set of special functions. The most commonly used ones are $this->_() and __(). These functions just returns the translation of their argument:


### Syntax inside a class vs. syntax outside of a class

In ProcessWire, the functions __() and $this->_() are equivalent, but __() will work in all contexts while $this->_() will only work within the context of a class. So why have $this->_() at all? Because it has a speed advantage that can only be realized within the context of a class. As a result, the following rules apply:


### Placeholders

Lets say that you needed to output a string like this:


### Plurals

Let's get back to the 'created pages' example: sprintf(__("Created %d pages."), $count);. What if we create only 1 page? The output will be: “Created 1 pages.”, which is definitely not correct English, and would certainly be incorrect for many other languages as well.


### Context

Sometimes one term is used in several contexts and although it is one and the same word in English it has to be translated differently in other languages. For example the word Post can be used both as a verb (Click here to post your comment) and as a noun (Edit this post). In such cases the _x() or $this->_x() function should be used. It is similar to __(), but it has an additional second argument–the context:


## Comment descriptions

Do you think translators will know how to translate a string like: __('g:i:s a')? In this case you can add a clarifying comment in the source code. The comment must begin with // and be on the same line as the translation function call. Here is an example:
