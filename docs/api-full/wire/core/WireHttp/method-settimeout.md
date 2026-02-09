# $wireHttp->setTimeout($seconds): $this

Source: `wire/core/WireHttp.php`

Set the number of seconds till connection times out

Note that the default timeout for http requests is 4.5 seconds

## Usage

~~~~~
// basic usage
$result = $wireHttp->setTimeout($seconds);
~~~~~

## Arguments

- `$seconds` `int|float`

## Return value

- `$this`
