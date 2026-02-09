# $permissions->save(Page $page): bool

Source: `wire/core/Permissions.php`

Save a Permission

## Usage

~~~~~
// basic usage
$bool = $permissions->save($page);

// usage with all arguments
$bool = $permissions->save(Page $page);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$permissions->save()`

## Hooking Before

~~~~~
$this->addHookBefore('Permissions::save', function(HookEvent $event) {
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
$this->addHookAfter('Permissions::save', function(HookEvent $event) {
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

- `$page` `Permission|Page`

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
