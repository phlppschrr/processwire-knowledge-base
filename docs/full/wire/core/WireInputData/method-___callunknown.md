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

## Arguments

- `$method` `string`
- `$arguments` `array`

## Return value

- `string|int|array|float|null` Returns null when input variable does not exist

## Exceptions

- `WireException`
