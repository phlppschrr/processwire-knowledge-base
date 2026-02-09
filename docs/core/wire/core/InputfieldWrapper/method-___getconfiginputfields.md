# $inputfieldWrapper->getConfigInputfields(): InputfieldWrapper

Source: `wire/core/InputfieldWrapper.php`

Get configuration Inputfields for this InputfieldWrapper

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $inputfieldWrapper->getConfigInputfields();
~~~~~

## Return value

- `InputfieldWrapper`

## Hooking

- Hookable method name: `getConfigInputfields`
- Implementation: `___getConfigInputfields`
- Hook with: `InputfieldWrapper::getConfigInputfields`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldWrapper::getConfigInputfields', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldWrapper::getConfigInputfields', function(HookEvent $event) {
  $inputfieldWrapper = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
