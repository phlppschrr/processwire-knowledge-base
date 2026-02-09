# $page->moveReady($oldParent, $newParent)

Source: `wire/core/Page.php`

Called when this Page is about to be moved to another parent

## Example

~~~~~
$wire->addHook('Page::moveReady', function($e) {
  $page = $e->object;
  list($oldParent, $newParent) = $e->arguments;
  $e->log->message("Moving page $page from $oldParent->path into $newParent->path");
  if($newParent->isTrash()) $e->log->save("trash", "Trashing page $page");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->moveReady($oldParent, $newParent);
~~~~~

## Arguments

- `$oldParent` `Page`
- `$newParent` `Page`

## Hooking

- Hookable method name: `moveReady`
- Implementation: `___moveReady`
- Hook with: `Page::moveReady`

### Hooking Before

~~~~~
$this->addHookBefore('Page::moveReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $oldParent = $event->arguments(0);
  $newParent = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $oldParent);
  $event->arguments(1, $newParent);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Page::moveReady', function(HookEvent $event) {
  $page = $event->object;

  // Get arguments
  $oldParent = $event->arguments(0);
  $newParent = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Since

3.0.253
