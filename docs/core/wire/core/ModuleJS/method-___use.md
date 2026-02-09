# $moduleJS->use($name): $this

Source: `wire/core/ModuleJS.php`

Use an extra named component

## Usage

~~~~~
// basic usage
$result = $moduleJS->use($name);
~~~~~

## Hookable

- Hookable method name: `use`
- Implementation: `___use`
- Hook with: `$moduleJS->use()`

## Hooking Before

~~~~~
$this->addHookBefore('ModuleJS::use', function(HookEvent $event) {
  $moduleJS = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $name);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ModuleJS::use', function(HookEvent $event) {
  $moduleJS = $event->object;

  // Get arguments
  $name = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- $name

## Return value

- `$this`
