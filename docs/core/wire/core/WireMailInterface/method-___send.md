# $wireMailInterface->send(): int

Source: `wire/core/WireMailInterface.php`

Send the email

## Usage

~~~~~
// basic usage
$int = $wireMailInterface->send();
~~~~~

## Hookable

- Hookable method name: `send`
- Implementation: `___send`
- Hook with: `$wireMailInterface->send()`

## Return value

- `int` Returns number of messages sent or 0 on failure
