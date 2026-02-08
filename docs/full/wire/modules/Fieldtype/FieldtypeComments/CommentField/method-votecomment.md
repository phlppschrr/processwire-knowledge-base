# $commentField->voteComment(Page $page, Comment $comment, $up = true): bool

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Add a vote to the current comment from the current user/IP

## Arguments

- `$page` `Page`
- `$comment` `Comment`
- `$up` (optional) `bool` Specify true for upvote, or false for downvote

## Return value

bool Returns true on success, false on failure or duplicate
