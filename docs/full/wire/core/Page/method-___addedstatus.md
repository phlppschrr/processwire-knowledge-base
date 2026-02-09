# $page->addedStatus($name, $value)

Source: `wire/core/Page.php`

Called when a new status flag has been added (and saved)

## Example

~~~~~
$wire->addHook('Page::addedStatus', function($e) {
  $page = $e->object;
  $name = $e->arguments(0);
  $e->message("Added status $name to page $page");
  if($name === 'unpublished') $e->message("Unpublished page $page");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->addedStatus($name, $value);
~~~~~

## Hookable

- Hookable method name: `addedStatus`
- Implementation: `___addedStatus`
- Hook with: `$page->addedStatus()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::addedStatus', function(HookEvent $event) {
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

## Hooking After

~~~~~
$this->addHookAfter('Page::addedStatus', function(HookEvent $event) {
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

## Arguments

- `$name` `string` Name of the status flag that was added, i.e. unpublished, hidden, trash, locked
- `$value` `int` Value of the status flag that was added, a `Page::status*` constant

## Since

3.0.253
