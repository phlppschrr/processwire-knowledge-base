# $session->getAll($ns = null): array

Source: `wire/core/Session.php`

Get all session variables in an associative array

## Usage

~~~~~
// basic usage
$array = $session->getAll();

// usage with all arguments
$array = $session->getAll($ns = null);
~~~~~

## Arguments

- `$ns` (optional) `object|string` Optional namespace

## Return value

- `array`
