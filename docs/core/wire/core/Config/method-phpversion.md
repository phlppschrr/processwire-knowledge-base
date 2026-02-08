# $config->phpVersion($minVersion): bool

Source: `wire/core/Config.php`

Return true if current PHP version is equal to or newer than the given version

~~~~~
if($config->phpVersion('7.0.0')) {
  // PHP version is 7.x
}
~~~~~

## Arguments

- `$minVersion` `string|null`

## Return value

bool

## Since

3.0.101
