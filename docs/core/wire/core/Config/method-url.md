# $config->url($for): string|null

Source: `wire/core/Config.php`

Get URL for requested resource or module

`$config->url('something')` is a shorter alternative for `$config->urls->get('something')`.

## Example

~~~~~
// Get the admin URL
$url = $config->url('admin');

// Same thing, using alternate syntax
$url = $config->urls->admin;
~~~~~

## Usage

~~~~~
// basic usage
$string = $config->url($for);
~~~~~

## Arguments

- `$for` `string|Wire` Predefined ProcessWire URLs property or module name

## Return value

- `string|null`
