# $wireInputData->callUnknown($method, $arguments): string|int|array|float|null

Source: `wire/core/WireInputData.php`

Maps to Sanitizer functions

## Usage

~~~~~
// basic usage
$string = $wireInputData->callUnknown($method, $arguments);
~~~~~

## Hookable

- Hookable method name: `callUnknown`
- Implementation: `___callUnknown`
- Hook with: `$wireInputData->callUnknown()`

## Hooking Before

~~~~~
$this->addHookBefore('WireInputData::callUnknown', function(HookEvent $event) {
  $wireInputData = $event->object;

  // Get arguments
  $method = $event->arguments(0);
  $arguments = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $method);
  $event->arguments(1, $arguments);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('WireInputData::callUnknown', function(HookEvent $event) {
  $wireInputData = $event->object;

  // Get arguments
  $method = $event->arguments(0);
  $arguments = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$method` `string`
- `$arguments` `array`

## Return value

- `string|int|array|float|null` Returns null when input variable does not exist

## Exceptions

- `WireException`
