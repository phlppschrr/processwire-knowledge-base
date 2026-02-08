# $config->requestPath($match = ''): string

Source: `wire/core/Config.php`

Current unsanitized request path (URL sans ProcessWire installation subdirectory, if present)

This excludes any subdirectories leading to ProcessWire installation root, if present.
Useful if you need to know request path from /site/config.php or other boot file.

~~~~~
if(strpos($config->requestPath(), '/processwire/') === 0) {
  // current request path starts with “/processwire/”
}
if($config->requestPath('/processwire/')) {
  // the text “/processwire/” appears somewhere in current request path
}
if($config->requestPath([ 'foo', 'bar', 'baz' ])) {
  // current request has one or more of 'foo', 'bar', 'baz' in the path
}
~~~~~

## Arguments

- `$match` (optional) `string|array` Optionally return path only if some part matches given string(s) (default='')

## Return value

string Returns path string or blank string if $match argument used and doesn’t match.

## Since

3.0.175
