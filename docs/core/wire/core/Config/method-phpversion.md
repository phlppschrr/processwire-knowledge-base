# Config::phpVersion()

Source: `wire/core/Config.php`

Return true if current PHP version is equal to or newer than the given version

~~~~~
if($config->phpVersion('7.0.0')) {
  // PHP version is 7.x
}
~~~~~


@param string|null $minVersion

@return bool

@since 3.0.101
