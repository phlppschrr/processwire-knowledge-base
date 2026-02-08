# Using template files in ProcessWire

Source: https://processwire.com/docs/start/templates/

## Summary

Every time a page is loaded on your site, ProcessWire looks at what template is assigned to the page, loads it, gives it several API variables, and then runs it as a PHP script.

## Key Points

- Every time a page is loaded on your site, ProcessWire looks at what template is assigned to the page, loads it, gives it several API variables, and then runs it as a PHP script.
- This section covers the use of template files and serves as an introduction to using ProcessWire’s API with examples.
- Every time a page is loaded on your site, ProcessWire looks at what template is assigned to the page, loads it, gives it several API variables, and then runs it as a PHP script. These template files are located in this directory: /site/templates/.

## Sections


## How do template files work?

Every time a page is loaded on your site, ProcessWire looks at what template is assigned to the page, loads it, gives it several API variables, and then runs it as a PHP script. These template files are located in this directory: /site/templates/.


## Basic Usage

Lets assume we are editing a template file that is just an HTML document. Taking a value from your page in ProcessWire and outputting it from your template file is very simple. Here is an example of a line in a template file that outputs the current page's title:


## Using other types of fields

Most fields contain simple values like text or numbers, but some fields can contain other types that you should output in a different way. For instance, lets say that you created a field with the 'Page' field type (FieldtypePage). That type of field is designed to hold one or more other pages. This is different from the title and bodycopy fields mentioned above, which just contained text.


## Creating markup is your job (most of the time)

ProcessWire is designed to be completely document type agnostic, meaning it makes no assumptions about whether you are using it to output HTML, XHTML, HTML5, XML, JSON, any kind of web service, etc. As a result, ProcessWire's core framework never outputs markup, and that's why we generate the HTML markup in the manner shown in the examples above. However, plugin modules are provided with ProcessWire that do output Markup, should you want to use them (or create your own).


## Finding and loading other pages from your template file

The API is not limited to just the $page variable and the variables reference will cover all of them for you. But lets look at another common one, which is the $pages variable. The $pages variable is your connection to all the other pages in your site. It provides get() and find() functions that enable you to find and load other pages with ease.


### Example: finding all featured pages

As an example, lets say that we wanted to display a list of all pages in the site that have a field called 'featured' with a value of 1 (in ProcessWire, a checkbox field has a value of 1 when checked). We want to display this list of featured pages in the sidebar of our homepage. Here is how we could do that in our homepage template file:


### Beyond the basics

So now we've got a list of featured pages that we're displaying in the sidebar of our homepage. But what if we wanted it to do all of these too:


### Taking it further

Lets say that down the road the press releases section grows and now contains multiple categories of press releases, where the press releases are subpages of categories like:
