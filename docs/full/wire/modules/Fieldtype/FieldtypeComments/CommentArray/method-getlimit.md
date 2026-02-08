# $commentArray->getLimit(): int

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Get the imposed limit on number of comments.

If no limit set, then return number of comments currently here.

Used for pagination.

## Usage

~~~~~
// basic usage
$int = $commentArray->getLimit();
~~~~~

## Return value

- `int`
