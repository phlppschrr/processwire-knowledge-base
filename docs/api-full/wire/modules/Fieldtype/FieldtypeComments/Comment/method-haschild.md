# $comment->hasChild($comment, $recursive = true): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Does this comment have the given child comment?

## Usage

~~~~~
// basic usage
$bool = $comment->hasChild($comment);

// usage with all arguments
$bool = $comment->hasChild($comment, $recursive = true);
~~~~~

## Arguments

- `$comment` `int|Comment` Comment or Comment ID
- `$recursive` (optional) `bool` Check all descending children recursively? Use false to check only direct children. (default=true)

## Return value

- `bool`

## Since

3.0.149
