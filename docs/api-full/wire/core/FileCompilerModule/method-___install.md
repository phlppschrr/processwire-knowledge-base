# $fileCompilerModule->install()

Source: `wire/core/FileCompilerModule.php`

Perform any installation procedures specific to this module, if needed.

## Usage

~~~~~
// basic usage
$result = $fileCompilerModule->install();
~~~~~

## Hooking

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `FileCompilerModule::install`

### Hooking Before

~~~~~
$this->addHookBefore('FileCompilerModule::install', function(HookEvent $event) {
  $fileCompilerModule = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('FileCompilerModule::install', function(HookEvent $event) {
  $fileCompilerModule = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
