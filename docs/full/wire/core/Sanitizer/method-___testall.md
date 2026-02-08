# $sanitizer->testAll($value): array

Source: `wire/core/Sanitizer.php`

Run value through all sanitizers, return array indexed by sanitizer name and resulting value

Used for debugging and testing purposes.

## Usage

~~~~~
// basic usage
$array = $sanitizer->testAll($value);
~~~~~

## Hookable

- Hookable method name: `testAll`
- Implementation: `___testAll`
- Hook with: `$sanitizer->testAll()`

## Arguments

- `$value` `mixed`

## Return value

- `array`
