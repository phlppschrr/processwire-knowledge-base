# $inputfieldWrapper->renderValue(): string

Source: `wire/core/InputfieldWrapper.php`

Render the output of this Inputfield and its children, showing values only (no inputs)

## Usage

~~~~~
// basic usage
$string = $inputfieldWrapper->renderValue();
~~~~~

## Hookable

- Hookable method name: `renderValue`
- Implementation: `___renderValue`
- Hook with: `$inputfieldWrapper->renderValue()`

## Hooking Before

~~~~~
$this->addHookBefore('InputfieldWrapper::renderValue', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('InputfieldWrapper::renderValue', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `string`
