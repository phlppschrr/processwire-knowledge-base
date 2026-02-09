# $modules->uninstall($class): bool

Source: `wire/core/Modules.php`

Uninstall the given module name

## Usage

~~~~~
// basic usage
$bool = $modules->uninstall($class);
~~~~~

## Hookable

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `$modules->uninstall()`

## Hooking Before

~~~~~
$this->addHookBefore('Modules::uninstall', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $class);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Modules::uninstall', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$class` `string` Module name (class name)

## Return value

- `bool`

## Exceptions

- `WireException`
