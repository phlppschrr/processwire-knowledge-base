# $sanitizer->testAll($value): array

Source: `wire/core/Sanitizer.php`

Run value through all sanitizers, return array indexed by sanitizer name and resulting value

Used for debugging and testing purposes.

## Usage

~~~~~
// basic usage
$array = $sanitizer->testAll($value);
~~~~~

## Arguments

- `$value` `mixed`

## Return value

- `array`

## Hooking

- Hookable method name: `testAll`
- Implementation: `___testAll`
- Hook with: `Sanitizer::testAll`

### Hooking Before

~~~~~
$this->addHookBefore('Sanitizer::testAll', function(HookEvent $event) {
  $sanitizer = $event->object;

  // Get arguments
  $value = $event->arguments(0);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $value);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('Sanitizer::testAll', function(HookEvent $event) {
  $sanitizer = $event->object;

  // Get arguments
  $value = $event->arguments(0);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~
