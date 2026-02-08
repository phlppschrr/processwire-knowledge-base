# Page::trash()

Source: `wire/core/Page.php`

Move this page to the trash

This is the same as calling `$pages->trash($page)`.

~~~~~
// Trash a page
$item = $pages->get('/some-page/');
$item->trash();
~~~~~


@return bool True on success, false on failure

@throws WireException
