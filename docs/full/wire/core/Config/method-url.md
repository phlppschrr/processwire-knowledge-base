# Config::url()

Source: `wire/core/Config.php`

Get URL for requested resource or module

`$config->url('something')` is a shorter alternative for `$config->urls->get('something')`.

~~~~~
// Get the admin URL
$url = $config->url('admin');

// Same thing, using alternate syntax
$url = $config->urls->admin;
~~~~~


@param string|Wire $for Predefined ProcessWire URLs property or module name

@return string|null
