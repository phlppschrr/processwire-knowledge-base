# Page::___moveReady()

Source: `wire/core/Page.php`

Called when this Page is about to be moved to another parent

~~~~~
$wire->addHook('Page::moveReady', function($e) {
  $page = $e->object;
  list($oldParent, $newParent) = $e->arguments;
  $e->log->message("Moving page $page from $oldParent->path into $newParent->path");
  if($newParent->isTrash()) $e->log->save("trash", "Trashing page $page");
});
~~~~~


@param Page $oldParent

@param Page $newParent

@since 3.0.253
