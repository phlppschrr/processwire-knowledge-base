# Config::path()

Source: `wire/core/Config.php`

Get disk path for requested resource or module

`$config->path('something')` is a shorter alternative for `$config->paths->get('something')`.

~~~~~
// Get the PW installation root disk path
$path = $config->path('root');

// Same thing, using alternate syntax
$path = $config->paths->root;
~~~~~


@param string $for Predefined ProcessWire paths property or module class name

@return null|string
