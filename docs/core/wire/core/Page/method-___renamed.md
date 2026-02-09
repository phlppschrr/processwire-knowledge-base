# $page->renamed($oldName, $newName)

Source: `wire/core/Page.php`

Called right after this page has been renamed (i.e. had its name property changed)

## Example

~~~~~
$wire->addHook('Page::renamed', function($e) {
  $page = $e->object;
  list($oldName, $newName) = $e->arguments;
  $e->message("Page $page renamed: $oldName => $newName");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->renamed($oldName, $newName);
~~~~~

## Arguments

- `$oldName` `string` The old name
- `$newName` `string` The new name

## Hooking

- Hookable method name: `renamed`
- Implementation: `___renamed`
- Hook with: `Page::renamed`

### Hooking Before

~~~~~
$this->addHookBefore('Page::renamed', function(HookEvent $event) {
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

### Hooking After

~~~~~
$this->addHookAfter('Page::renamed', function(HookEvent $event) {
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

## Since

3.0.253
