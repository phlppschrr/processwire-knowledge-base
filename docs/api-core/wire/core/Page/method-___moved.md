# $page->moved($oldParent, $newParent)

Source: `wire/core/Page.php`

Called after this Page has been moved to another parent

## Example

~~~~~
$wire->addHook('Page::moved', function($e) {
  $page = $e->object;
  list($oldParent, $newParent) = $e->arguments;
  $e->log->message("Moved page $page from $oldParent->path into $newParent->path");
  if($newParent->isTrash()) $e->log->save("trash", "Trashed page $page");
});
~~~~~

## Usage

~~~~~
// basic usage
$result = $page->moved($oldParent, $newParent);
~~~~~

## Arguments

- `$oldParent` `Page`
- `$newParent` `Page`

## Hooking

- Hookable method name: `moved`
- Implementation: `___moved`
- Hook with: `Page::moved`

### Hooking Before

~~~~~
$this->addHookBefore('Page::moved', function(HookEvent $event) {
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
$this->addHookAfter('Page::moved', function(HookEvent $event) {
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
