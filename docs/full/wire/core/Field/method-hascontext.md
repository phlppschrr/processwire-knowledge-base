# $field->hasContext($for, $namespace = ''): Field|bool

Source: `wire/core/Field.php`

Does this field have context settings for given Page/Template?

## Usage

~~~~~
// basic usage
$field = $field->hasContext($for);

// usage with all arguments
$field = $field->hasContext($for, $namespace = '');
~~~~~

## Arguments

- `$for` `Page|Template|Fieldgroup|string` Specify Page, Template, or template name string
- `$namespace` (optional) `string` Optional namespace (internal use)

## Return value

- `Field|bool`

## See Also

- [Field::getContext()](method-getcontext.md)

## Since

3.0.163
