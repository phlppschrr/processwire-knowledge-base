# $config->setPath($for, $path): self

Source: `wire/core/Config.php`

Change or set just the server disk path for the named location (leaving URL as-is)

- If you want to update both disk path and URL at the same time, or if URL and path are going to be the same relative to
  installation root, use the `setLocation()` method instead.

- Paths relative to PW installation root should omit the leading slash, i.e. use `site/templates/` and NOT `/site/templates/`.

- The `$for` argument can be: `cache`, `logs`, `files`, `tmp`, `templates`, or one of your own. Other named locations may
  also work, but since they can potentially be used before PW’s “ready” state, they may not be reliable.

## Usage

~~~~~
// basic usage
$result = $config->setPath($for, $path);
~~~~~

## Arguments

- `$for` `string` Named location from `$config->paths`, one of: `cache`, `logs`, `files`, `tmp`, `templates`, or your own.
- `$path` `string` Path relative to PW installation root (no leading slash), or absolute path if not.

## Return value

- `self`

## Exceptions

- `WireException`

## Since

3.0.141
