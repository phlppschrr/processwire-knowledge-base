# $wireHttp->getTimeout(): float

Source: `wire/core/WireHttp.php`

Get the number of seconds till connection times out

Used by send(), get(), post(), getJSON(), but not by download() methods.

## Usage

~~~~~
// basic usage
$float = $wireHttp->getTimeout();
~~~~~

## Return value

- `float`
