# $pages->___trash(Page $page, $save = true): bool

Source: `wire/core/Pages.php`

Move a page to the trash

When a page is moved to the trash, it is in a "delete pending" state. Once trashed, the page can be either restored
to its original location, or permanently deleted (when the trash is emptied).

~~~~~
// Trash a product page
$product = $pages->get('/products/foo-bar-widget/');
$pages->trash($product);
~~~~~

## Arguments

- `$page` `Page` Page to trash
- `$save` (optional) `bool` Set to false if you will perform your own save() call afterwards to complete the operation. Omit otherwise. Primarily for internal use.

## Return value

bool Returns true on success, false on failure.

## Throws

- WireException

## See also

- [Pages::restore()](method-___restore.md)
- [Pages::emptyTrash()](method-___emptytrash.md)
- [Pages::delete()](method-___delete.md)
