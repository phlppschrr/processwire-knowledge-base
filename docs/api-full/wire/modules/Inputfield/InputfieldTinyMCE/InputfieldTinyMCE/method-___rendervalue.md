# $inputfieldTinyMCE->renderValue(): string

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Render non-editable value

## Usage

~~~~~
// basic usage
$string = $inputfieldTinyMCE->renderValue();
~~~~~

## Return value

- `string`

## Hooking

- Hookable method name: `renderValue`
- Implementation: `___renderValue`
- Hook with: `InputfieldTinyMCE::renderValue`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldTinyMCE::renderValue', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldTinyMCE::renderValue', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
