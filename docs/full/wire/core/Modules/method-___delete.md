# $modules->delete($class): bool

Source: `wire/core/Modules.php`

Delete the given module, physically removing its files

## Usage

~~~~~
// basic usage
$bool = $modules->delete($class);
~~~~~

## Arguments

- `$class` `string` Module name (class name)

## Return value

- `bool`

## Hooking

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `Modules::delete`

### Hooking Before

~~~~~
$this->addHookBefore('Modules::delete', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $class);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Modules::delete', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` If module can't be deleted, exception will be thrown containing reason.
