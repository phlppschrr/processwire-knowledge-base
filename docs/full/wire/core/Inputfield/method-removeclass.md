# $inputfield->removeClass($class, $property = 'class'): $this

Source: `wire/core/Inputfield.php`

Remove the given class (or classes) from this Inputfield

~~~~~
// Remove the "foo" class
$inputfield->removeClass('foo');

// Remove both the "foo" and "bar" classes (since 3.0.16)
$inputfield->removeClass('foo bar');

// Remove the "bar" class from the wrapping .Inputfield element
$inputfield->removeClass('bar', 'wrapClass');
~~~~~

## Arguments

- string|array $class Class name you want to remove or specify one of the following: - Single class name to remove. - Space-separated class names you want to remove (Since 3.0.16). - Array of class names you want to remove (Since 3.0.16).
- string $property Optionally specify the property you want to remove class from: - `class` (string): Default setting. Class for the input element (or whatever the Inputfield default is). - `wrapClass` (string): Class for the ".Inputfield" wrapping element, the most outer level element used for this Inputfield. - `headerClass` (string): Class for the ".InputfieldHeader" label element. - `contentClass` (string): Class for the ".InputfieldContent" wrapping element. - Or some other class property defined by a descending Inputfield class.

## Return value

$this

## See also

- [Inputfield::addClass()](method-addclass.md)
- [Inputfield::hasClass()](method-hasclass.md)
