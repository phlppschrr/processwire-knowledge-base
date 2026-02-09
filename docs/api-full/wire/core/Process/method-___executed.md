# $process->executed($method)

Source: `wire/core/Process.php`

Hookable method automatically called after execute() method has finished.

## Usage

~~~~~
// basic usage
$result = $process->executed($method);
~~~~~

## Arguments

- `$method` `string` Name of method that was executed

## Hooking

- Hookable method name: `executed`
- Implementation: `___executed`
- Hook with: `Process::executed`

### Hooking Before

~~~~~
$this->addHookBefore('Process::executed', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $method = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $method);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Process::executed', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $method = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
