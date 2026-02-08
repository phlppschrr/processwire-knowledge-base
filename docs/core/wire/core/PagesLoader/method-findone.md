# $pagesLoader->findOne($selector, $options = array()): Page|NullPage

Source: `wire/core/PagesLoader.php`

Like find() but returns only the first match as a Page object (not PageArray)

This is functionally similar to the get() method except that its default behavior is to
filter for access control and hidden/unpublished/etc. states, in the same way that the
find() method does. You can add an `include=` to your selector with value `hidden`,
`unpublished` or `all` to change this behavior, just like with find().

Unlike the find() method, this method performs a secondary runtime access check by calling
`$page->viewable()` with the found $page, and returns a `NullPage` if the page is not
viewable with that call. In 3.0.142+, an `include=` mode of `all` or `unpublished` will
override this, where appropriate.

This method also accepts an `$options` array, whereas `Pages::get()` does not.

## Usage

~~~~~
// basic usage
$page = $pagesLoader->findOne($selector);

// usage with all arguments
$page = $pagesLoader->findOne($selector, $options = array());
~~~~~

## Arguments

- `$selector` `string|int|array|Selectors`
- `$options` (optional) `array|string` See $options for `Pages::find`

## Return value

- `Page|NullPage`
