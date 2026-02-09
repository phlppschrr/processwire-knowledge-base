# $commentField->getCommentParents(Page $page, Comment $comment): CommentArray

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Get parent comments for given Comment

## Usage

~~~~~
// basic usage
$commentArray = $commentField->getCommentParents($page, $comment);

// usage with all arguments
$commentArray = $commentField->getCommentParents(Page $page, Comment $comment);
~~~~~

## Arguments

- `$page` `Page`
- `$comment` `Comment`

## Return value

- `CommentArray`

## Since

3.0.153
