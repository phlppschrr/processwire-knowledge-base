# Pages::___trash()

Source: `wire/core/Pages.php`

Move a page to the trash

When a page is moved to the trash, it is in a "delete pending" state. Once trashed, the page can be either restored
to its original location, or permanently deleted (when the trash is emptied).

~~~~~
// Trash a product page
$product = $pages->get('/products/foo-bar-widget/');
$pages->trash($product);
~~~~~


@param Page $page Page to trash

@param bool $save Set to false if you will perform your own save() call afterwards to complete the operation. Omit otherwise. Primarily for internal use.

@return bool Returns true on success, false on failure.

@throws WireException

@see Pages::restore(), Pages::emptyTrash(), Pages::delete()
