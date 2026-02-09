# $wire->inputPost($key = '', $sanitizer = ''): WireInputData|string|int|array|null

Source: `wire/core/Wire.php`

Access the $input->post() API variable as a function.

## Usage

~~~~~
// basic usage
$wireInputData = $wire->inputPost();

// usage with all arguments
$wireInputData = $wire->inputPost($key = '', $sanitizer = '');
~~~~~
