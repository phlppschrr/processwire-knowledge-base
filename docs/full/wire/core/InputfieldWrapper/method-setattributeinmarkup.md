# $inputfieldWrapper->setAttributeInMarkup($name, $value, $markup, $removeEmpty = false): string

Source: `wire/core/InputfieldWrapper.php`

Set attribute value in markup, optionally replacing a {placeholder} tag

When a placeholder is present in the given $markup, it should be the
attribute name wrapped in `{}`, i.e. `{class}`

Note that class attributes are appended while other attributes are replaced.

## Arguments

- string $name Attribute name (i.e. "class", "for", etc.)
- string $value Value to set for the attribute
- string $markup Markup where the attribute or placeholder exists
- bool $removeEmpty Remove attribute if it resolves to empty value?

## Return value

string Updated markup

## Meta

- @since 3.0.242
