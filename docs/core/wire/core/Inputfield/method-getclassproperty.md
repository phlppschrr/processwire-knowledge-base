# $inputfield->getClassProperty($property): string

Source: `wire/core/Inputfield.php`

Get the internal property name for given class property

This converts things like 'wrap' to 'wrapClass', 'header' to 'headerClass', etc.

## Usage

~~~~~
// basic usage
$string = $inputfield->getClassProperty($property);
~~~~~

## Arguments

- `$property` `string`

## Return value

- `string`

## Since

3.0.204
