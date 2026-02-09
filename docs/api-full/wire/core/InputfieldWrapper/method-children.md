# $inputfieldWrapper->children($selector = ''): InputfieldsArray

Source: `wire/core/InputfieldWrapper.php`

Return all children Inputfield objects

## Usage

~~~~~
// basic usage
$inputfieldsArray = $inputfieldWrapper->children();

// usage with all arguments
$inputfieldsArray = $inputfieldWrapper->children($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string` Optional selector string to filter the children by

## Return value

- `InputfieldsArray`
