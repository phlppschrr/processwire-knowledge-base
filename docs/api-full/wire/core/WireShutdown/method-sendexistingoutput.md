# $wireShutdown->sendExistingOutput(): bool

Source: `wire/core/WireShutdown.php`

Send any existing output while removing PHP’s error message from it (to avoid duplication)

## Usage

~~~~~
// basic usage
$bool = $wireShutdown->sendExistingOutput();
~~~~~

## Return value

- `bool` Returns true if there was existing output, false if not
