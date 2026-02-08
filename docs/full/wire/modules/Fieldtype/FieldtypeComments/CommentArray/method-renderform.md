# $commentArray->renderForm(array $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Provides the default rendering of a comment form, which may or may not be what you want

## Usage

~~~~~
// basic usage
$string = $commentArray->renderForm();

// usage with all arguments
$string = $commentArray->renderForm(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array`

## Return value

- `string`

## See Also

- CommentForm: class and override it to serve your needs
