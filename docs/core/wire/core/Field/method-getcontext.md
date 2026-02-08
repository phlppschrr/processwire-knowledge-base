# $field->getContext($for, $namespace = '', $has = false): Field|bool

Source: `wire/core/Field.php`

Get this field in context of a Page/Template

## Arguments

- Page|Template|Fieldgroup|string $for Specify Page, Template, or template name string
- string $namespace Optional namespace (internal use)
- bool $has Return boolean rather than Field to check if context exists? (default=false)

## Return value

Field|bool

## See also

- [Fieldgroup::getFieldContext()](../Fieldgroup/method-getfieldcontext.md)
- [Field::hasContext()](method-hascontext.md)

## Meta

- @since 3.0.162
