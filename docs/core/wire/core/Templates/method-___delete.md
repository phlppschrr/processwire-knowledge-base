# $templates->delete(Saveable $item): bool

Source: `wire/core/Templates.php`

Delete a Template

## Usage

~~~~~
// basic usage
$bool = $templates->delete($item);

// usage with all arguments
$bool = $templates->delete(Saveable $item);
~~~~~

## Arguments

- `$item` `Template|Saveable` Template to delete

## Return value

- `bool` True on success, false on failure

## Hooking

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `Templates::delete`

### Hooking Before

~~~~~
$this->addHookBefore('Templates::delete', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $item);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Templates::delete', function(HookEvent $event) {
  $templates = $event->object;

  // Get arguments
  $item = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` Thrown when you attempt to delete a template in use, or a system template.
