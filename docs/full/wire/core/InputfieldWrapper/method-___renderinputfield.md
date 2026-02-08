# $inputfieldWrapper->___renderInputfield(Inputfield $inputfield, $renderValueMode = false): string

Source: `wire/core/InputfieldWrapper.php`

Render output for an individual Inputfield

This method takes care of all the pre-and-post requisites needed for rendering an Inputfield
among a group of Inputfields. It is used by the `InputfieldWrapper::render()` method for each
Inputfield present in the children.

## Usage

~~~~~
// basic usage
$string = $inputfieldWrapper->___renderInputfield($inputfield);

// usage with all arguments
$string = $inputfieldWrapper->___renderInputfield(Inputfield $inputfield, $renderValueMode = false);
~~~~~

## Arguments

- `$inputfield` `Inputfield` The Inputfield to render.
- `$renderValueMode` (optional) `bool` Specify true if we are only rendering values (default=false).

## Return value

- `string` Rendered output
