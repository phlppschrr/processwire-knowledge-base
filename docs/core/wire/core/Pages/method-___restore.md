# Pages::___restore()

Source: `wire/core/Pages.php`

Restore a page in the trash back to its original location and state

If you want to restore the page to some location other than its original location, set the `$page->parent` property
of the page to contain the location you want it to restore to. Otherwise the page will restore to its original location,
when possible to do so.

~~~~~
// Grab a page from the trash and restore it
$trashedPage = $pages->get(1234);
$pages->restore($trashedPage);
~~~~~


@param Page $page Page that is in the trash that you want to restore

@param bool $save Set to false if you only want to prep the page for restore (i.e. you will save the page yourself later). Primarily for internal use.

@return bool True on success, false on failure.

@see Pages::trash()
