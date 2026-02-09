# $inputfieldWrapper->setAttributeInMarkup($name, $value, $markup, $removeEmpty = false): string

Source: `wire/core/InputfieldWrapper.php`

Set attribute value in markup, optionally replacing a {placeholder} tag

When a placeholder is present in the given $markup, it should be the
attribute name wrapped in `{}`, i.e. `{class}`

Note that class attributes are appended while other attributes are replaced.

## Usage

~~~~~
// basic usage
$string = $inputfieldWrapper->setAttributeInMarkup($name, $value, $markup);

// usage with all arguments
$string = $inputfieldWrapper->setAttributeInMarkup($name, $value, $markup, $removeEmpty = false);
~~~~~

## Arguments

- `$name` `string` Attribute name (i.e. "class", "for", etc.)
- `$value` `string` Value to set for the attribute
- `$markup` `string` Markup where the attribute or placeholder exists
- `$removeEmpty` (optional) `bool` Remove attribute if it resolves to empty value?

## Return value

- `string` Updated markup

## Since

3.0.242
