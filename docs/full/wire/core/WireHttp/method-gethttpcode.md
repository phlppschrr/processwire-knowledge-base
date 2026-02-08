# $wireHttp->getHttpCode($withText = false): int|string

Source: `wire/core/WireHttp.php`

Get last HTTP code

## Usage

~~~~~
// basic usage
$int = $wireHttp->getHttpCode();

// usage with all arguments
$int = $wireHttp->getHttpCode($withText = false);
~~~~~

## Arguments

- `$withText` (optional) `bool` Specify true to include the HTTP code text label with the code

## Return value

- `int|string`
