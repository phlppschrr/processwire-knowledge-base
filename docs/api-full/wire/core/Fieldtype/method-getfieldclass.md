# $fieldtype->getFieldClass(array $a = array()): string

Source: `wire/core/Fieldtype.php`

Get class name to use Field objects of this type (must be class that extends Field class)

Return blank if default class (Field) should be used.

## Usage

~~~~~
// basic usage
$string = $fieldtype->getFieldClass();

// usage with all arguments
$string = $fieldtype->getFieldClass(array $a = array());
~~~~~

## Arguments

- `$a` (optional) `array` Field data from DB (if needed)

## Return value

- `string` Return class name or blank to use default Field class

## Since

3.0.146
