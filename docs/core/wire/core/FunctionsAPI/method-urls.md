# FunctionsAPI::urls()

Source: `wire/core/FunctionsAPI.php`

Get one of any named system URLs (shortcut to the $config API variable “urls” property)

URLs always have a trailing slash.

~~~~~
// you can use either syntax below, where “templates” can be the name for any system URL
$url = urls()->templates;
$url = urls('templates');
~~~~~


@param string $key

@return null|Paths|string

@see Config::urls()
