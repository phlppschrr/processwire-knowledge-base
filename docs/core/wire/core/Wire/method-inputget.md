# $wire->inputGet($key = '', $sanitizer = ''): WireInputData|string|int|array|null

Source: `wire/core/Wire.php`

Access the $input->get() API variable as a function.

## Usage

~~~~~
// basic usage
$wireInputData = $wire->inputGet();

// usage with all arguments
$wireInputData = $wire->inputGet($key = '', $sanitizer = '');
~~~~~
