# $modules->install($class, $options = array()): null|Module

Source: `wire/core/Modules.php`

Install the given module name

## Usage

~~~~~
// basic usage
$modules->install($class);

// usage with all arguments
$modules->install($class, $options = array());
~~~~~

## Hookable

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `$modules->install()`

## Hooking Before

~~~~~
$this->addHookBefore('Modules::install', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $class);
  $event->arguments(1, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Modules::install', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $class = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$class` `string` Module name (class name)
- `$options` (optional) `array|bool` Optional associative array that can contain any of the following: - `dependencies` (boolean): When true, dependencies will also be installed where possible. Specify false to prevent installation of uninstalled modules. (default=true) - `resetCache` (boolean): When true, module caches will be reset after installation. (default=true) - `force` (boolean): Force installation, even if dependencies can't be met.

## Return value

- `null|Module` Returns null if unable to install, or ready-to-use Module object if successfully installed.

## Exceptions

- `WireException`
