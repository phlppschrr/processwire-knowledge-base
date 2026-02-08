# $wireTextTools->hasPlaceholders($str, array $options = array()): bool

Source: `wire/core/WireTextTools.php`

Does the string have any {placeholder} tags in it?

## Usage

~~~~~
// basic usage
$bool = $wireTextTools->hasPlaceholders($str);

// usage with all arguments
$bool = $wireTextTools->hasPlaceholders($str, array $options = array());
~~~~~

## Arguments

- `$str` `string`
- `$options` (optional) `array` - `tagOpen` (string): The required opening tag character(s), default is '{' - `tagClose` (string): The required closing tag character(s), default is '}'

## Return value

- `bool`

## Since

3.0.126
