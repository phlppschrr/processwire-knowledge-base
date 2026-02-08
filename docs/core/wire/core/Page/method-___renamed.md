# $page->___renamed($oldName, $newName)

Source: `wire/core/Page.php`

Called right after this page has been renamed (i.e. had its name property changed)

~~~~~
$wire->addHook('Page::renamed', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page renamed: $oldName => $newName");
});
~~~~~

## Arguments

- string $oldName The old name
- string $newName The new name

## Meta

- @since 3.0.253
