# $wire->inputCookie($key = '', $sanitizer = ''): WireInputDataCookie|string|int|array|null

Source: `wire/core/Wire.php`

Access the $input->cookie() API variable as a function.

## Usage

~~~~~
// basic usage
$wireInputDataCookie = $wire->inputCookie();

// usage with all arguments
$wireInputDataCookie = $wire->inputCookie($key = '', $sanitizer = '');
~~~~~
