# $config->path($for): null|string

Source: `wire/core/Config.php`

Get disk path for requested resource or module

`$config->path('something')` is a shorter alternative for `$config->paths->get('something')`.

## Example

~~~~~
// Get the PW installation root disk path
$path = $config->path('root');

// Same thing, using alternate syntax
$path = $config->paths->root;
~~~~~

## Usage

~~~~~
// basic usage
$config->path($for);
~~~~~

## Arguments

- `$for` `string` Predefined ProcessWire paths property or module class name

## Return value

- `null|string`
