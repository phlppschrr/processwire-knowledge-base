# $permissions->saved(Page $page, array $changes = array(), $values = array())

Source: `wire/core/Permissions.php`

Hook called when a permission is saved

## Usage

~~~~~
// basic usage
$result = $permissions->saved($page);

// usage with all arguments
$result = $permissions->saved(Page $page, array $changes = array(), $values = array());
~~~~~

## Hookable

- Hookable method name: `saved`
- Implementation: `___saved`
- Hook with: `$permissions->saved()`

## Hooking Before

~~~~~
$this->addHookBefore('Permissions::saved', function(HookEvent $event) {
  $permissions = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $changes = $event->arguments(1);
  $values = $event->arguments(2);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $changes);
  $event->arguments(2, $values);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Permissions::saved', function(HookEvent $event) {
  $permissions = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $changes = $event->arguments(1);
  $values = $event->arguments(2);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page that was saved
- `$changes` (optional) `array` Array of changed field names
- `$values` (optional) `array` Array of changed field values indexed by name (when enabled)

## Exceptions

- `WireException`
