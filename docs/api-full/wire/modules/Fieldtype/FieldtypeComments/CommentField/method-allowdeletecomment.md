# $commentField->allowDeleteComment(Comment $comment): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

May the given comment be deleted?

## Usage

~~~~~
// basic usage
$bool = $commentField->allowDeleteComment($comment);

// usage with all arguments
$bool = $commentField->allowDeleteComment(Comment $comment);
~~~~~

## Arguments

- `$comment` `Comment`

## Return value

- `bool`
