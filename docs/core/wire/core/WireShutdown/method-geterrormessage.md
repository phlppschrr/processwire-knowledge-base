# $wireShutdown->getErrorMessage(array $error): string

Source: `wire/core/WireShutdown.php`

Create more informative error message from $error array

## Usage

~~~~~
// basic usage
$string = $wireShutdown->getErrorMessage($error);

// usage with all arguments
$string = $wireShutdown->getErrorMessage(array $error);
~~~~~

## Arguments

- `$error` `array` Error array from PHP’s error_get_last()

## Return value

- `string`
