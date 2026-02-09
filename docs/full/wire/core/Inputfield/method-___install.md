# $inputfield->install()

Source: `wire/core/Inputfield.php`

Per the Module interface, this method is called when this Inputfield is installed

## Usage

~~~~~
// basic usage
$result = $inputfield->install();
~~~~~

## Hookable

- Hookable method name: `install`
- Implementation: `___install`
- Hook with: `$inputfield->install()`

## Hooking Before

~~~~~
$this->addHookBefore('Inputfield::install', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('Inputfield::install', function(HookEvent $event) {
  $inputfield = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
