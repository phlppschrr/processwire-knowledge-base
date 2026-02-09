# $roles->delete(Page $page, $recursive = false): bool

Source: `wire/core/Roles.php`

Permanently delete a Role

## Usage

~~~~~
// basic usage
$bool = $roles->delete($page);

// usage with all arguments
$bool = $roles->delete(Page $page, $recursive = false);
~~~~~

## Arguments

- `$page` `Role|Page` Permission to delete
- `$recursive` (optional) `bool` If set to true, then this will attempt to delete any pages below the Permission too.

## Return value

- `bool` True on success, false on failure

## Hooking

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `Roles::delete`

### Hooking Before

~~~~~
$this->addHookBefore('Roles::delete', function(HookEvent $event) {
  $roles = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $recursive = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
  $event->arguments(1, $recursive);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Roles::delete', function(HookEvent $event) {
  $roles = $event->object;

  // Get arguments
  $page = $event->arguments(0);
  $recursive = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException`
