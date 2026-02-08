# $page->trash(): bool

Source: `wire/core/Page.php`

Move this page to the trash

This is the same as calling `$pages->trash($page)`.

~~~~~
// Trash a page
$item = $pages->get('/some-page/');
$item->trash();
~~~~~

## Return value

bool True on success, false on failure

## Throws

- WireException
