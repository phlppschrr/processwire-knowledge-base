# $page->removedStatus($name, $value)

Source: `wire/core/Page.php`

Called when a status flag has been removed from this page (and saved)

## Example

~~~~~
$wire->addHook('Page::removedStatus', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  $e->message("Removed status $name from page $page");
  if($name === 'unpublished') $e->message("Published page $page");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->removedStatus($name, $value);
~~~~~

## Arguments

- `$name` `string` Name of the status flag that was removed, i.e. unpublished, hidden, trash, locked
- `$value` `int` Value of the status flag that was removed, a `Page::status*` constant

## Hooking

- Hookable method name: `removedStatus`
- Implementation: `___removedStatus`
- Hook with: `Page::removedStatus`

### Hooking Before

~~~~~
$this->addHookBefore('Page::removedStatus', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $value = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
  $event->arguments(1, $value);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::removedStatus', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $name = $event->arguments(0);
  $value = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
