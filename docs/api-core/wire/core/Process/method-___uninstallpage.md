# $process->uninstallPage(): int

Source: `wire/core/Process.php`

Uninstall (trash) dedicated pages for this Process module

If there is more than one page using this Process, it will trash them all.

To be called by the Process module's ___uninstall() method.

## Usage

~~~~~
// basic usage
$int = $process->uninstallPage();
~~~~~

## Return value

- `int` Number of pages trashed

## Hooking

- Hookable method name: `uninstallPage`
- Implementation: `___uninstallPage`
- Hook with: `Process::uninstallPage`

### Hooking Before

~~~~~
$this->addHookBefore('Process::uninstallPage', function(HookEvent $event) {
  $process = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Process::uninstallPage', function(HookEvent $event) {
  $process = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
