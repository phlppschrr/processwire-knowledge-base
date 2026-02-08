# $commentField->allowCommentPage(Comment $comment, Page $page, $verbose = false): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Allow given comment to live on given page?

## Usage

~~~~~
// basic usage
$bool = $commentField->allowCommentPage($comment, $page);

// usage with all arguments
$bool = $commentField->allowCommentPage(Comment $comment, Page $page, $verbose = false);
~~~~~

## Arguments

- `$comment` `Comment`
- `$page` `Page`
- `$verbose` (optional) `bool` Report reason why not to standard errors? (default=false)

## Return value

- `bool`

## Since

3.0.149
