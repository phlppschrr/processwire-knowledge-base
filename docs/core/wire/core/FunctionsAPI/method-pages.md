# FunctionsAPI::pages()

Source: `wire/core/FunctionsAPI.php`

Retrieve or save pages ($pages API variable as a function)

Accessing `pages()` is exactly the same as accessing `$pages`. Though there are a couple of optional
shortcuts available by providing an argument to this function.

~~~~
// A call with no arguments returns the $pages API variable
$pages = pages();
$pageArray = pages()->find("selector");
$page = pages()->get(123);

// Providing selector as argument maps to $pages->find()
$pageArray = pages("template=basic-page");

// Providing argument of single page ID, path or name maps to $pages->get()
$page = pages(123);
$page = pages("/path/to/page/");
$page = pages("page-name");
~~~~


@param string|array|int $selector Specify one of the following:
 - Nothing, makes it return the $pages API variable.
 - Selector (string) to find matching pages, makes function return PageArray - equivalent to $pages->find("selector");
 - Page ID (int) to return a single matching Page - equivalent to $pages->get(123);
 - Page name (string) to return a single page having the given name - equivalent to $pages->get("name");

@return Pages|PageArray|Page|NullPage

@see Pages
