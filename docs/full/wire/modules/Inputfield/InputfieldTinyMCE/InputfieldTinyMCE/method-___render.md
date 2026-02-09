# $inputfieldTinyMCE->render(): string

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Render Inputfield

## Usage

~~~~~
// basic usage
$string = $inputfieldTinyMCE->render();
~~~~~

## Return value

- `string`

## Hooking

- Hookable method name: `render`
- Implementation: `___render`
- Hook with: `InputfieldTinyMCE::render`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldTinyMCE::render', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldTinyMCE::render', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
