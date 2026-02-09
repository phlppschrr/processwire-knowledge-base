# $fileCompilerModule->uninstall()

Source: `wire/core/FileCompilerModule.php`

Perform any uninstall procedures specific to this module, if needed.

## Usage

~~~~~
// basic usage
$result = $fileCompilerModule->uninstall();
~~~~~

## Hooking

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `FileCompilerModule::uninstall`

### Hooking Before

~~~~~
$this->addHookBefore('FileCompilerModule::uninstall', function(HookEvent $event) {
  $fileCompilerModule = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('FileCompilerModule::uninstall', function(HookEvent $event) {
  $fileCompilerModule = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
