# $functionsWireAPI->wireFields($name = ''): Fields|Field|null

Source: `wire/core/FunctionsWireAPI.php`

Access the $fields API variable as a function

## Usage

~~~~~
// basic usage
$fields = $functionsWireAPI->wireFields();

// usage with all arguments
$fields = $functionsWireAPI->wireFields($name = '');
~~~~~

## Arguments

- `$name` (optional) `string` Optional field name to retrieve

## Return value

- `Fields|Field|null`
