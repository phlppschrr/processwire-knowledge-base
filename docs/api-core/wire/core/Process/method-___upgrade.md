# $process->upgrade($fromVersion, $toVersion)

Source: `wire/core/Process.php`

Called when module version changes

See the `Module` interface and the `upgrade` method there for more details.

## Usage

~~~~~
// basic usage
$result = $process->upgrade($fromVersion, $toVersion);
~~~~~

## Arguments

- `$fromVersion` `int|string` Previous version
- `$toVersion` `int|string` New version

## Hooking

- Hookable method name: `upgrade`
- Implementation: `___upgrade`
- Hook with: `Process::upgrade`

### Hooking Before

~~~~~
$this->addHookBefore('Process::upgrade', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $fromVersion = $event->arguments(0);
  $toVersion = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $fromVersion);
  $event->arguments(1, $toVersion);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Process::upgrade', function(HookEvent $event) {
  $process = $event->object;

  // Get arguments
  $fromVersion = $event->arguments(0);
  $toVersion = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Exceptions

- `WireException` if upgrade fails
