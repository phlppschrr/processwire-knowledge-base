# $pages->___emptyTrash(array $options = array()): int|array

Source: `wire/core/Pages.php`

Delete all pages in the trash

Note that once the trash is emptied, pages in the trash are permanently deleted.
This method populates error notices when there are errors deleting specific pages.

~~~~~
// Empty the trash
$pages->emptyTrash();
~~~~~

## Arguments

- `$options` (optional) `array` See PagesTrash::emptyTrash() for advanced options

## Return value

int|array Returns total number of pages deleted from trash, or array if verbose option specified. This number is negative or 0 if not all pages could be deleted and error notices may be present.

## See also

- [Pages::trash()](method-___trash.md)
- [Pages::restore()](method-___restore.md)
