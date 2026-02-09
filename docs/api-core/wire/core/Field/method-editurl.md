# $field->editUrl($options = array()): string

Source: `wire/core/Field.php`

Get URL to edit field in the admin

## Usage

~~~~~
// basic usage
$string = $field->editUrl();

// usage with all arguments
$string = $field->editUrl($options = array());
~~~~~

## Arguments

- `$options` (optional) `array|bool|string` Specify array of options, string for find option, or bool for http option. - `find` (string): Name of field to find in editor form - `http` (bool): True to force inclusion of scheme and hostname

## Return value

- `string`

## Since

3.0.151
