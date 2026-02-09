# $processWire->init()

Source: `wire/core/ProcessWire.php`

Hookable init for anyone that wants to hook immediately before any autoload modules initialized or after all modules initialized

## Usage

~~~~~
// basic usage
$result = $processWire->init();
~~~~~

## Hookable

- Hookable method name: `init`
- Implementation: `___init`
- Hook with: `$processWire->init()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessWire::init', function(HookEvent $event) {
  $processWire = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessWire::init', function(HookEvent $event) {
  $processWire = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
