# $processWire->ready()

Source: `wire/core/ProcessWire.php`

Hookable ready for anyone that wants to hook immediately before any autoload modules ready or after all modules ready

## Usage

~~~~~
// basic usage
$result = $processWire->ready();
~~~~~

## Hookable

- Hookable method name: `ready`
- Implementation: `___ready`
- Hook with: `$processWire->ready()`

## Hooking Before

~~~~~
$this->addHookBefore('ProcessWire::ready', function(HookEvent $event) {
  $processWire = $event->object;

  // Your code here
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('ProcessWire::ready', function(HookEvent $event) {
  $processWire = $event->object;

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
