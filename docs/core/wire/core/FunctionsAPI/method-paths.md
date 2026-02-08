# $functionsAPI->paths($key = ''): null|Paths|string

Source: `wire/core/FunctionsAPI.php`

Get one of any named server disk paths (shortcut to the $config API variable “paths” property)

Paths always have a trailing slash.

## Example

~~~~~
// you can use either syntax below, where “templates” can be the name for any system URL
$path = paths()->templates;
$path = paths('templates');
~~~~~

## Usage

~~~~~
// basic usage
$functionsAPI->paths();

// usage with all arguments
$functionsAPI->paths($key = '');
~~~~~

## Arguments

- `$key` (optional) `string`

## Return value

- `null|Paths|string`

## See Also

- [Config::paths()](../Config/method-paths.md)
