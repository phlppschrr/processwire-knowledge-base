# $pages->getID($selector, $options = array()): int|array

Source: `wire/core/Pages.php`

Get one ID of page matching given selector with no exclusions, like get() but returns ID rather than a Page

This method is an alias of the has() method, and depending on what you are after, may make more
or less sense with your code readability. Use whichever better suits your case.

## Usage

~~~~~
// basic usage
$int = $pages->getID($selector);

// usage with all arguments
$int = $pages->getID($selector, $options = array());
~~~~~

## Arguments

- `$selector` `string|array|Selectors` Specify selector to find first matching page ID
- `$options` (optional) `bool|array` Specify boolean true to return all pages columns rather than just IDs. Or specify array of options (see find method for details), `verbose` option can optionally be in array.

## Return value

- `int|array`

## See Also

- [Pages::get()](method-get.md)
- [Pages::has()](method-has.md)
- [Pages::findIDs()](method-findids.md)

## Since

3.0.156
