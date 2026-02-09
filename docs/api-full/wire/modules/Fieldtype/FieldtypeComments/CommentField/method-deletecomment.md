# $commentField->deleteComment(Page $page, Comment $comment, $notes = ''): mixed

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Delete a given comment

## Usage

~~~~~
// basic usage
$result = $commentField->deleteComment($page, $comment);

// usage with all arguments
$result = $commentField->deleteComment(Page $page, Comment $comment, $notes = '');
~~~~~

## Arguments

- `$page` `Page`
- `$comment` `Comment`
- `$notes` (optional) `string`

## Return value

- `mixed`
