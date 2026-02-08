# $commentArray->render(array $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Provides the default rendering of a comment list, which may or may not be what you want

## Usage

~~~~~
// basic usage
$string = $commentArray->render();

// usage with all arguments
$string = $commentArray->render(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array`

## Return value

- `string`

## See Also

- CommentList: class and override it to serve your needs
