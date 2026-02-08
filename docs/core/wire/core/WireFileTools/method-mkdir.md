# WireFileTools::mkdir()

Source: `wire/core/WireFileTools.php`

Create a directory that is writable to ProcessWire and uses the defined $config chmod settings

Unlike PHP's `mkdir()` function, this function manages the read/write mode consistent with ProcessWire's
setting `$config->chmodDir`, and it can create directories recursively. Meaning, if you want to create directory /a/b/c/
and directory /a/ doesn't yet exist, this method will take care of creating /a/, /a/b/, and /a/b/c/.

The `$recursive` and `$chmod` arguments may optionally be swapped (since 3.0.34).

~~~~~
// Create a new directory in ProcessWire's cache dir
if($files->mkdir($config->paths->cache . 'foo-bar/')) {
  // directory created: /site/assets/cache/foo-bar/
}
~~~~~


@param string $path Directory you want to create

@param bool|string $recursive If set to true, all directories will be created as needed to reach the end.

@param string|null|bool $chmod Optional mode to set directory to (default: $config->chmodDir), format must be a string i.e. "0755"
  If omitted, then ProcessWire's `$config->chmodDir` setting is used instead.

@return bool True on success, false on failure
