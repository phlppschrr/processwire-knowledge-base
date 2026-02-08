# Pages::___emptyTrash()

Source: `wire/core/Pages.php`

Delete all pages in the trash

Note that once the trash is emptied, pages in the trash are permanently deleted.
This method populates error notices when there are errors deleting specific pages.

~~~~~
// Empty the trash
$pages->emptyTrash();
~~~~~


@param array $options See PagesTrash::emptyTrash() for advanced options

@return int|array Returns total number of pages deleted from trash, or array if verbose option specified.
	This number is negative or 0 if not all pages could be deleted and error notices may be present.

@see Pages::trash(), Pages::restore()
