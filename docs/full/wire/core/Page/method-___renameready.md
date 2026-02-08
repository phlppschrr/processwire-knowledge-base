# $page->___renameReady($oldName, $newName)

Source: `wire/core/Page.php`

Called right before this page is renamed (i.e. has its name property changed)

~~~~~
$wire->addHook('Page::renameReady', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page to be renamed: $oldName => $newName");
});
~~~~~

## Arguments

- `$oldName` `string` The old name
- `$newName` `string` The new name (read-only)

## Since

3.0.253
