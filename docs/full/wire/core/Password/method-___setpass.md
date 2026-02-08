# $password->setPass($value)

Source: `wire/core/Password.php`

Set the 'pass' to the given value

## Usage

~~~~~
// basic usage
$result = $password->setPass($value);
~~~~~

## Hookable

- Hookable method name: `setPass`
- Implementation: `___setPass`
- Hook with: `$password->setPass()`

## Arguments

- `$value` `string`

## Exceptions

- `WireException` if given invalid $value
