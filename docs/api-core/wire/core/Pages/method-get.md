# $pages->get($selector, $options = array()): Page|NullPage

Source: `wire/core/Pages.php`

Returns the first page matching the given selector with no exclusions

Use this method when you need to retrieve a specific page without exclusions for access control or page status.

## Example

~~~~~~
// Get a page by ID
$p = $pages->get(1234);

// Get a page by path
$p = $pages->get('/about/contact/');

// Get a random 'skyscraper' page by selector string
$p = $pages->get('template=skyscraper, sort=random');
~~~~~~

## Usage

~~~~~
// basic usage
$page = $pages->get($selector);

// usage with all arguments
$page = $pages->get($selector, $options = array());
~~~~~

## Arguments

- `$selector` `string|array|Selectors|int` Selector string, array or Selectors object. May also be page path or ID.
- `$options` (optional) `array` See `Pages::find()` for extra options that may be specified.

## Return value

- `Page|NullPage` Always returns a Page object, but will return NullPage (with id=0) when no match found.

## See Also

- [Pages::findOne()](method-findone.md)
- [Pages::find()](method-___find.md)
