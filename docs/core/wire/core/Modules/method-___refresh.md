# $modules->refresh($showMessages = false)

Source: `wire/core/Modules.php`

Refresh the modules cache

This forces the modules file and information cache to be re-created.

## Usage

~~~~~
// basic usage
$result = $modules->refresh();

// usage with all arguments
$result = $modules->refresh($showMessages = false);
~~~~~

## Arguments

- `$showMessages` (optional) `bool` Show notification messages about what was found? (default=false) 3.0.172+

## Hooking

- Hookable method name: `refresh`
- Implementation: `___refresh`
- Hook with: `Modules::refresh`

### Hooking Before

~~~~~
$this->addHookBefore('Modules::refresh', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $showMessages = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $showMessages);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Modules::refresh', function(HookEvent $event) {
  $modules = $event->object;

  // Get arguments
  $showMessages = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
