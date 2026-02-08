# $pagesLoader->get($selector, $options = array()): Page|NullPage

Source: `wire/core/PagesLoader.php`

Returns the first page matching the given selector with no exclusions

## Arguments

- string|int|array|Selectors $selector
- array $options See Pages::find method for options

## Return value

Page|NullPage Always returns a Page object, but will return NullPage (with id=0) when no match found
