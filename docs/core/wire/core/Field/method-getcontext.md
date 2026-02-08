# $field->getContext($for, $namespace = '', $has = false): Field|bool

Source: `wire/core/Field.php`

Get this field in context of a Page/Template

## Arguments

- `$for` `Page|Template|Fieldgroup|string` Specify Page, Template, or template name string
- `$namespace` (optional) `string` Optional namespace (internal use)
- `$has` (optional) `bool` Return boolean rather than Field to check if context exists? (default=false)

## Return value

Field|bool

## See also

- [Fieldgroup::getFieldContext()](../Fieldgroup/method-getfieldcontext.md)
- [Field::hasContext()](method-hascontext.md)

## Since

3.0.162
