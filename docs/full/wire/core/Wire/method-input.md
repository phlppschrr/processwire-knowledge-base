# $wire->input($type = '', $key = '', $sanitizer = ''): WireInput|WireInputData|WireInputDataCookie|array|string|int|null

Source: `wire/core/Wire.php`

Access the $input API variable as a function.

## Usage

~~~~~
// basic usage
$wireInput = $wire->input();

// usage with all arguments
$wireInput = $wire->input($type = '', $key = '', $sanitizer = '');
~~~~~
