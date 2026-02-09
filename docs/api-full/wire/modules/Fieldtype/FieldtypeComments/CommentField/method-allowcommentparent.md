# $commentField->allowCommentParent(Comment $comment, $parent, $verbose = false): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Allow given Comment to have given parent comment?

## Usage

~~~~~
// basic usage
$bool = $commentField->allowCommentParent($comment, $parent);

// usage with all arguments
$bool = $commentField->allowCommentParent(Comment $comment, $parent, $verbose = false);
~~~~~

## Arguments

- `$comment` `Comment`
- `$parent` `Comment|int`
- `$verbose` (optional) `bool` Report reason why not to standard errors? (default=false)

## Return value

- `bool`

## Since

3.0.149
