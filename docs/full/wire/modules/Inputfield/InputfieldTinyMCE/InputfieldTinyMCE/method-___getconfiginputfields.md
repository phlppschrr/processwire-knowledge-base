# $inputfieldTinyMCE->getConfigInputfields(): InputfieldWrapper

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Get Inputfield configuration settings

## Usage

~~~~~
// basic usage
$inputfieldWrapper = $inputfieldTinyMCE->getConfigInputfields();
~~~~~

## Hookable

- Hookable method name: `getConfigInputfields`
- Implementation: `___getConfigInputfields`
- Hook with: `$inputfieldTinyMCE->getConfigInputfields()`

## Hooking Before

~~~~~
$this->addHookBefore('InputfieldTinyMCE::getConfigInputfields', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('InputfieldTinyMCE::getConfigInputfields', function(HookEvent $event) {
  $inputfieldTinyMCE = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Return value

- `InputfieldWrapper`
