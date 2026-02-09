# $roles->save(Page $page): bool

Source: `wire/core/Roles.php`

Save a Role

## Usage

~~~~~
// basic usage
$bool = $roles->save($page);

// usage with all arguments
$bool = $roles->save(Page $page);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$roles->save()`

## Hooking Before

~~~~~
$this->addHookBefore('Roles::save', function(HookEvent $event) {
  $roles = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $page);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Roles::save', function(HookEvent $event) {
  $roles = $event->object;

  // Get arguments
  $page = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$page` `Role|Page`

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
