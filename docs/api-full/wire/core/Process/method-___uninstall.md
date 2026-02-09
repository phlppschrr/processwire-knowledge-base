# $process->uninstall()

Source: `wire/core/Process.php`

Uninstall this Process

Note that the Modules class handles removal of any Permissions that the Process may have installed.

See the `Module` interface and the `uninstall` method there for more details.

## Usage

~~~~~
// basic usage
$result = $process->uninstall();
~~~~~

## Hooking

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `Process::uninstall`

### Hooking Before

~~~~~
$this->addHookBefore('Process::uninstall', function(HookEvent $event) {
  $process = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Process::uninstall', function(HookEvent $event) {
  $process = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
