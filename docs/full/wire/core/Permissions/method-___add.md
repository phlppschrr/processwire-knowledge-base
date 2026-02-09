# $permissions->add($name): Permission|NullPage

Source: `wire/core/Permissions.php`

Add a new Permission with the given name and return it

## Usage

~~~~~
// basic usage
$permission = $permissions->add($name);
~~~~~

## Arguments

- `$name` `string` Name of permission you want to add, i.e. "hello-world"

## Return value

- `Permission|NullPage` Returns a Permission page on success, or a NullPage on error

## Hooking

- Hookable method name: `add`
- Implementation: `___add`
- Hook with: `Permissions::add`

### Hooking Before

~~~~~
$this->addHookBefore('Permissions::add', function(HookEvent $event) {
  $permissions = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Permissions::add', function(HookEvent $event) {
  $permissions = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
