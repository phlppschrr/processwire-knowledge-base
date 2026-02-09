# $page->renameReady($oldName, $newName)

Source: `wire/core/Page.php`

Called right before this page is renamed (i.e. has its name property changed)

## Example

~~~~~
$wire->addHook('Page::renameReady', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page to be renamed: $oldName => $newName");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->renameReady($oldName, $newName);
~~~~~

## Hookable

- Hookable method name: `renameReady`
- Implementation: `___renameReady`
- Hook with: `$page->renameReady()`

## Hooking Before

~~~~~
$this->addHookBefore('Page::renameReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $oldName = $event->arguments(0);
  $newName = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $oldName);
  $event->arguments(1, $newName);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Page::renameReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $oldName = $event->arguments(0);
  $newName = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$oldName` `string` The old name
- `$newName` `string` The new name (read-only)

## Since

3.0.253
