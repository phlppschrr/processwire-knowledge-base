# $functionsAPI->paths($key = ''): null|Paths|string

Source: `wire/core/FunctionsAPI.php`

Get one of any named server disk paths (shortcut to the $config API variable “paths” property)

Paths always have a trailing slash.

~~~~~
// you can use either syntax below, where “templates” can be the name for any system URL
$path = paths()->templates;
$path = paths('templates');
~~~~~

## Arguments

- string $key

## Return value

null|Paths|string

## See also

- [Config::paths()](../Config/method-paths.md)
