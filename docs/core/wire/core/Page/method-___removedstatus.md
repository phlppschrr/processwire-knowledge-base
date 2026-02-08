# $page->___removedStatus($name, $value)

Source: `wire/core/Page.php`

Called when a status flag has been removed from this page (and saved)

~~~~~
$wire->addHook('Page::removedStatus', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  $e->message("Removed status $name from page $page");
  if($name === 'unpublished') $e->message("Published page $page");
});
~~~~~

## Arguments

- string $name Name of the status flag that was removed, i.e. unpublished, hidden, trash, locked
- int $value Value of the status flag that was removed, a `Page::status*` constant

## Meta

- @since 3.0.253
