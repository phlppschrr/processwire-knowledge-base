# $inputfieldPageTableAjax->checkAjax()

Source: `wire/modules/Inputfield/InputfieldPageTable/InputfieldPageTableAjax.php`

Check if current request is a valid ajax request and call renderAjax() if it is.

## Usage

~~~~~
// basic usage
$result = $inputfieldPageTableAjax->checkAjax();
~~~~~

## Hooking

- Hookable method name: `checkAjax`
- Implementation: `___checkAjax`
- Hook with: `InputfieldPageTableAjax::checkAjax`

### Hooking Before

~~~~~
$this->addHookBefore('InputfieldPageTableAjax::checkAjax', function(HookEvent $event) {
  $inputfieldPageTableAjax = $event->object;

  // Your code here
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('InputfieldPageTableAjax::checkAjax', function(HookEvent $event) {
  $inputfieldPageTableAjax = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
