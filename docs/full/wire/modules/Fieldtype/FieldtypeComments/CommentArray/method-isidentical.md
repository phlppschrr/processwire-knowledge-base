# $commentArray->isIdentical(WireArray $items, $strict = true): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Is the given CommentArray identical to this one?

## Usage

~~~~~
// basic usage
$bool = $commentArray->isIdentical($items);

// usage with all arguments
$bool = $commentArray->isIdentical(WireArray $items, $strict = true);
~~~~~

## Arguments

- `$items` `WireArray`
- `$strict` (optional) `bool|int`

## Return value

- `bool`
