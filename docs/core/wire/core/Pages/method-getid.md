# $pages->getID($selector, $options = array()): int|array

Source: `wire/core/Pages.php`

Get one ID of page matching given selector with no exclusions, like get() but returns ID rather than a Page

This method is an alias of the has() method, and depending on what you are after, may make more
or less sense with your code readability. Use whichever better suits your case.

## Arguments

- string|array|Selectors $selector Specify selector to find first matching page ID
- bool|array $options Specify boolean true to return all pages columns rather than just IDs. Or specify array of options (see find method for details), `verbose` option can optionally be in array.

## Return value

int|array

## See also

- [Pages::get()](method-get.md)
- [Pages::has()](method-has.md)
- [Pages::findIDs()](method-findids.md)

## Meta

- @since 3.0.156
