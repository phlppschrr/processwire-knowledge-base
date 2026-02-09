# $pagefiles->delete($item): $this

Source: `wire/core/Pagefiles.php`

Delete a pagefile item

Deletes the filename associated with the Pagefile and removes it from this Pagefiles array.
The actual deletion of the file does not take effect until `$page->save()`.

## Usage

~~~~~
// basic usage
$result = $pagefiles->delete($item);
~~~~~

## Arguments

- `$item` `Pagefile|string` Pagefile or basename

## Return value

- `$this`

## Hooking

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `Pagefiles::delete`

### Hooking Before

~~~~~
$this->addHookBefore('Pagefiles::delete', function(HookEvent $event) {
  $pagefiles = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Pagefiles::delete', function(HookEvent $event) {
  $pagefiles = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
