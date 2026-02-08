# Page::findOne()

Source: `wire/core/Page.php`

Find one descendant page matching given selector

This is the same as `Pages::findOne()` except that the match is always a descendant of page it is called on.

~~~~~
// Find the most recently modified descendant page
$item = $page->findOne("sort=-modified");
~~~~~


@param string|array $selector Selector string or array

@param array $options Optional options to modify default bheavior, see options for `Pages::find()`.

@return Page|NullPage Returns Page when found, or NullPage when nothing found.

@see Pages::findOne(), Page::child()

@since 3.0.116
