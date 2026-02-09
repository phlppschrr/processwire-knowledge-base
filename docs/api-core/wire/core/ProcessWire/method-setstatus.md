# $processWire->setStatus($status, array $data = array())

Source: `wire/core/ProcessWire.php`

Set the system status to one of the ProcessWire::status* constants

This also triggers init/ready functions for modules, when applicable.

## Usage

~~~~~
// basic usage
$result = $processWire->setStatus($status);

// usage with all arguments
$result = $processWire->setStatus($status, array $data = array());
~~~~~

## Arguments

- `$status` `int`
- `$data` (optional) `array` Associative array of any extra data to pass along to include files as locally scoped vars (3.0.142+)
