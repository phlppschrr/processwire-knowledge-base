# $permissions->deleted(Page $page)

Source: `wire/core/Permissions.php`

Hook called when a permission is deleted

## Usage

~~~~~
// basic usage
$result = $permissions->deleted($page);

// usage with all arguments
$result = $permissions->deleted(Page $page);
~~~~~

## Hookable

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `$permissions->deleted()`

## Hooking Before

~~~~~
$this->addHookBefore('Permissions::deleted', function(HookEvent $event) {
  $permissions = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Permissions::deleted', function(HookEvent $event) {
  $permissions = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Page` Page that was deleted

## Exceptions

- `WireException`
