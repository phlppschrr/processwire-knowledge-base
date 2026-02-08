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

- string $oldName The old name
- string $newName The new name (read-only)

## Meta

- @since 3.0.253
