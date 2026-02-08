# $functionsAPI->urls($key = ''): null|Paths|string

Source: `wire/core/FunctionsAPI.php`

Get one of any named system URLs (shortcut to the $config API variable “urls” property)

URLs always have a trailing slash.

~~~~~
// you can use either syntax below, where “templates” can be the name for any system URL
$url = urls()->templates;
$url = urls('templates');
~~~~~

## Arguments

- string $key

## Return value

null|Paths|string

## See also

- [Config::urls()](../Config/method-urls.md)
