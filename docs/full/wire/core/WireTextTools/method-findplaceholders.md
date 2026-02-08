# $wireTextTools->findPlaceholders($str, array $options = array()): array|bool

Source: `wire/core/WireTextTools.php`

Find and return all {placeholder} tags found in given string

## Usage

~~~~~
// basic usage
$array = $wireTextTools->findPlaceholders($str);

// usage with all arguments
$array = $wireTextTools->findPlaceholders($str, array $options = array());
~~~~~

## Arguments

- `$str` `string` String that might contain field {tags}
- `$options` (optional) `array` - `has` (bool): Specify true to only return true or false if it has tags (default=false). - `tagOpen` (string): The required opening tag character(s), default is '{' - `tagClose` (string): The required closing tag character(s), default is '}'

## Return value

- `array|bool` Always returns array unless you specify the `has` option as true.

## Since

3.0.126
