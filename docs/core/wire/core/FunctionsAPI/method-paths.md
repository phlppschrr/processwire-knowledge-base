# FunctionsAPI::paths()

Source: `wire/core/FunctionsAPI.php`

Get one of any named server disk paths (shortcut to the $config API variable “paths” property)

Paths always have a trailing slash.

~~~~~
// you can use either syntax below, where “templates” can be the name for any system URL
$path = paths()->templates;
$path = paths('templates');
~~~~~


@param string $key

@return null|Paths|string

@see Config::paths()
