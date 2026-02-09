# $inputfield->renderValue(): string

Source: `wire/core/Inputfield.php`

Render just the value (not input) in text/markup for presentation purposes.

## Usage

~~~~~
// basic usage
$string = $inputfield->renderValue();
~~~~~

## Return value

- `string` Text or markup where applicable

## Hooking

- Hookable method name: `renderValue`
- Implementation: `___renderValue`
- Hook with: `Inputfield::renderValue`

### Hooking Before

~~~~~
$this->addHookBefore('Inputfield::renderValue', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Inputfield::renderValue', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
