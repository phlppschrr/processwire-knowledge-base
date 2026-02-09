# $process->install()

Source: `wire/core/Process.php`

Per the Module interface, Install the module

By default a permission equal to the name of the class is installed, unless overridden with
the 'permission' property in your module information array.

See the `Module` interface and the `install` method there for more details.

## Usage

~~~~~
// basic usage
$result = $process->install();
~~~~~

## Hooking

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `Process::install`

### Hooking Before

~~~~~
$this->addHookBefore('Process::install', function(HookEvent $event) {
  $process = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Process::install', function(HookEvent $event) {
  $process = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
