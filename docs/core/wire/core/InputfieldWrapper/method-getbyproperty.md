# $inputfieldWrapper->getByProperty($property, $value, $getAll = false): Inputfield|InputfieldWrapper|null|array

Source: `wire/core/InputfieldWrapper.php`

Get Inputfield by some other non-attribute property or setting

## Usage

~~~~~
// basic usage
$inputfield = $inputfieldWrapper->getByProperty($property, $value);

// usage with all arguments
$inputfield = $inputfieldWrapper->getByProperty($property, $value, $getAll = false);
~~~~~

## Arguments

- `$property` `string`
- `$value` `mixed`
- `$getAll` (optional) `bool` Get array of all matching Inputfields rather than just first? (default=false)

## Return value

- `Inputfield|InputfieldWrapper|null|array`

## Since

3.0.239
