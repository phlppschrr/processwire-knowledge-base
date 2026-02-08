# $page->___moved($oldParent, $newParent)

Source: `wire/core/Page.php`

Called after this Page has been moved to another parent

~~~~~
$wire->addHook('Page::moved', function($e) {
  $page = $e->object;
  list($oldParent, $newParent) = $e->arguments;
  $e->log->message("Moved page $page from $oldParent->path into $newParent->path");
  if($newParent->isTrash()) $e->log->save("trash", "Trashed page $page");
});
~~~~~

## Arguments

- `$oldParent` `Page`
- `$newParent` `Page`

## Since

3.0.253
