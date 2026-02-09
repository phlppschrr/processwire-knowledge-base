# $roles->add($name): Role|NullPage

Source: `wire/core/Roles.php`

Add a new Role with the given name and return it

## Usage

~~~~~
// basic usage
$role = $roles->add($name);
~~~~~

## Hookable

- Hookable method name: `add`
- Implementation: `___add`
- Hook with: `$roles->add()`

## Hooking Before

~~~~~
$this->addHookBefore('Roles::add', function(HookEvent $event) {
  $roles = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Roles::add', function(HookEvent $event) {
  $roles = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$name` `string` Name of role you want to add, i.e. "hello-world"

## Return value

- `Role|NullPage` Returns a Role page on success, or a NullPage on error
