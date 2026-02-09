# $inputfield->uninstall()

Source: `wire/core/Inputfield.php`

Per the Module interface, uninstall() is called when this Inputfield is uninstalled

## Usage

~~~~~
// basic usage
$result = $inputfield->uninstall();
~~~~~

## Hookable

- Hookable method name: `uninstall`
- Implementation: `___uninstall`
- Hook with: `$inputfield->uninstall()`

## Hooking Before

~~~~~
$this->addHookBefore('Inputfield::uninstall', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Inputfield::uninstall', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
