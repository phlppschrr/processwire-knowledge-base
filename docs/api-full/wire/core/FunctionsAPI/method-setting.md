# $functionsAPI->setting($name = '', $value = null): array|string|int|bool|mixed|null

Source: `wire/core/FunctionsAPI.php`

Get or set a runtime site setting

This is a simple helper function for maintaining runtime settings in a site profile.
It simply sets and gets settings that you define. It is preferable to using ProcessWire’s
`$config` or `config()` API var/function because it is not used to store anything else for
ProcessWire. It is also preferable to using a variable (or variables) because it is always
in scope and accessible anywhere in your template files, even within existing functions.

*Note: unlike other functions in the Functions API, this function is not related to API variables.*

## Example

~~~~~
// set a setting named “foo” to value “bar”
setting('foo', 'bar');

// get a setting named “foo”
$value = setting('foo');

// set or replace multiple settings
setting([
  'foo' => 'value',
  'bar' => 123,
  'baz' => [ 'foo', 'bar', 'baz' ]
]);

// get all settings in associative array
$a = setting();

// to unset a setting
setting(false, 'foo');
~~~~~

## Usage

~~~~~
// basic usage
$array = $functionsAPI->setting();

// usage with all arguments
$array = $functionsAPI->setting($name = '', $value = null);
~~~~~

## Arguments

- `$name` (optional) `string|array` Setting name, or array to set multiple
- `$value` (optional) `string|int|array|float|mixed` Value to set, or omit if getting value of $name (default=null)

## Return value

- `array|string|int|bool|mixed|null`
