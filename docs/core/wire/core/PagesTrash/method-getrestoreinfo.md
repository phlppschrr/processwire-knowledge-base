# $pagesTrash->getRestoreInfo(Page $page, $populateToPage = false): array

Source: `wire/core/PagesTrash.php`

Get info needed to restore a Page that is in the trash

Returns array with the following info:
 - `restorable` (bool): Is the page restorable to a previous known/existing parent?
 - `notes` (array): Any additional notes to explain restore info (like reason why not restorable, or why name changed, etc.)
 - `parent` (Page|NullPage): Parent page that it should restore to
 - `parent_id` (int): ID of parent page that it should restore to
 - `sort` (int): Sort order that should be restored to page
 - `name` (string): Name that should be restored to page’s “name” property.
 - `namePrevious` (string): Previous name, if we had to modify the original name to make it restorable.
 - `name{id}` (string): Name that should be restored  to language where {id} is language ID (if appliable).

## Arguments

- Page $page Page to restore
- bool $populateToPage Populate this information to given page? (default=false)

## Return value

array
