# Page::___renameReady()

Source: `wire/core/Page.php`

Called right before this page is renamed (i.e. has its name property changed)

~~~~~
$wire->addHook('Page::renameReady', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page to be renamed: $oldName => $newName");
});
~~~~~


@param string $oldName The old name

@param string $newName The new name (read-only)

@since 3.0.253
