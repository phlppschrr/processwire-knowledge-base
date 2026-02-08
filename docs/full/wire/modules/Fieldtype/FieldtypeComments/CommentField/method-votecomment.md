# CommentField::voteComment()

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Add a vote to the current comment from the current user/IP

@param Page $page

@param Comment $comment

@param bool $up Specify true for upvote, or false for downvote

@return bool Returns true on success, false on failure or duplicate
