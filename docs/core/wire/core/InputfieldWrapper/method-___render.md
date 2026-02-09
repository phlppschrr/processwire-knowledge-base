# $inputfieldWrapper->render(): string

Source: `wire/core/InputfieldWrapper.php`

Render this Inputfield and the output of its children.

## Usage

~~~~~
// basic usage
$string = $inputfieldWrapper->render();
~~~~~

## Hookable

- Hookable method name: `render`
- Implementation: `___render`
- Hook with: `$inputfieldWrapper->render()`

## Hooking Before

~~~~~
$this->addHookBefore('InputfieldWrapper::render', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('InputfieldWrapper::render', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `string`

## Details

- @todo this method has become too long/complex, move to its own pluggable class and split it up a lot
