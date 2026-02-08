# $inputfield->getClassArray($property = 'class', $assoc = false): array

Source: `wire/core/Inputfield.php`

Get classes in array for given class property

## Usage

~~~~~
// basic usage
$array = $inputfield->getClassArray();

// usage with all arguments
$array = $inputfield->getClassArray($property = 'class', $assoc = false);
~~~~~

## Arguments

- `$property` (optional) `string` One of 'wrap', 'header', 'content' or 'input' (or alias 'class')
- `$assoc` (optional) `bool` Return as associative array where both keys and values are class names? (default=false)

## Return value

- `array`

## Since

3.0.204
