# $functionsAPI->page($key = '', $value = null): Page|mixed

Source: `wire/core/FunctionsAPI.php`

Returns the current Page being viewed ($page API variable as a function)

This function behaves the same as the `$page` API variable, though does support optional
arguments as shortcuts for getting from the page or setting values to it.

~~~~
$page = page(); // Simply get $page API var

// Get the “body” field
$body = page()->body; // direct syntax
$body = page()->get('body'); // regular syntax
$body = page('body'); // shortcut syntax

// Get the “headline” field or fallback to “title’
$headline = page()->get('headline|title'); // regular syntax
$headline = page('headline|title'); // shortcut syntax

// Set the “headline” field
page()->headline = 'My headline'; // direct syntax
page()->set('headline', 'My headline'); // regular syntax
page('headline', 'My headline'); // shortcut syntax
~~~~

## Usage

~~~~~
// basic usage
$page = $functionsAPI->page();

// usage with all arguments
$page = $functionsAPI->page($key = '', $value = null);
~~~~~

## Arguments

- `$key` (optional) `string` Optional property to get or set
- `$value` (optional) `null` Optional value to set

## Return value

- `Page|mixed`

## See Also

- Page
