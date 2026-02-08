# $inputfield->getRootParent(): InputfieldForm|InputfieldWrapper|null

Source: `wire/core/Inputfield.php`

Get the root parent InputfieldWrapper element (farthest parent, commonly InputfieldForm)

This returns null only if Inputfield it is called from has not yet been added to an InputfieldWrapper.

## Usage

~~~~~
// basic usage
$inputfieldForm = $inputfield->getRootParent();
~~~~~

## Return value

- `InputfieldForm|InputfieldWrapper|null`

## Since

3.0.106
