# $commentList->options($key = null, $value = null): array|string|int|bool|null

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Get or set options

## Usage

~~~~~
// basic usage
$array = $commentList->options();

// usage with all arguments
$array = $commentList->options($key = null, $value = null);
~~~~~

## Arguments

- `$key` (optional) `string|null|array` Use one of the following: - Omit to get array of all options - Specify option name to get (and omit $value argument) - Specify option name to set and provide a non-null $value argument - Specify array of one or more [ 'option' => 'value' ] to set and omit $value argument
- `$value` (optional) `string|int|bool|null` When setting an individual option, value should be specified here, otherwise omit

## Return value

- `array|string|int|bool|null` When getting singe option, value is returned, otherwise array of all options is returned.

## Since

3.0.138
