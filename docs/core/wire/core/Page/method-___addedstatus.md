# $page->___addedStatus($name, $value)

Source: `wire/core/Page.php`

Called when a new status flag has been added (and saved)

~~~~~
$wire->addHook('Page::addedStatus', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  $e->message("Added status $name to page $page");
  if($name === 'unpublished') $e->message("Unpublished page $page");
});
~~~~~

## Arguments

- string $name Name of the status flag that was added, i.e. unpublished, hidden, trash, locked
- int $value Value of the status flag that was added, a `Page::status*` constant

## Meta

- @since 3.0.253
