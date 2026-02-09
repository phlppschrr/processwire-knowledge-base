# $inputfieldTinyMCE->getModuleConfigInputfields(InputfieldWrapper $inputfields)

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Module config

## Usage

~~~~~
// basic usage
$result = $inputfieldTinyMCE->getModuleConfigInputfields($inputfields);

// usage with all arguments
$result = $inputfieldTinyMCE->getModuleConfigInputfields(InputfieldWrapper $inputfields);
~~~~~

## Arguments

- `$inputfields` `InputfieldWrapper`

## Hooking

- Hookable method name: `getModuleConfigInputfields`
- Implementation: `___getModuleConfigInputfields`
- Hook with: `InputfieldTinyMCE::getModuleConfigInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldTinyMCE::getModuleConfigInputfields', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Get arguments
  $inputfields = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $inputfields);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldTinyMCE::getModuleConfigInputfields', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Get arguments
  $inputfields = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
