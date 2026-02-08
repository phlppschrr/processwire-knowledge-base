# $functionsWireAPI->wirePages($selector = ''): Pages|PageArray|Page|NullPage

Source: `wire/core/FunctionsWireAPI.php`

Access the $pages API variable as a function

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

## Usage

~~~~~
// basic usage
$pages = $functionsWireAPI->wirePages();

// usage with all arguments
$pages = $functionsWireAPI->wirePages($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string|array` Specify one of the following: - Nothing, makes it return the $pages API variable. - Selector (string) to find matching pages, makes function return PageArray - equivalent to $pages->find("selector"); - Page ID (int) to return a single matching Page - equivalent to $pages->get(123); - Page name (string) to return a single page having the given name - equivalent to $pages->get("name");

## Return value

- `Pages|PageArray|Page|NullPage`
