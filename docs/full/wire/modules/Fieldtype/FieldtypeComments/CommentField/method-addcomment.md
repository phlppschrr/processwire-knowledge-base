# CommentField::addComment()

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Add new comment

Requires a new Comment object with no id, that has all its required field populated and validated
and is ready to add. Note that the `sort` property is assigned automatically if not specified in Comment.

The primary reason to use this method is if you want to add a comment without loading all the other
comments on a given Page.

@param Page $page Page where comments field exists

@param Comment $comment New comment to add

@param bool $send Send comment for automatic approval filtering and email notifications?
 - `true` if comment was just submitted now from user input and filtering should apply, notifications sent, etc.
 - `false` if you are importing comments and NO filtering should be applied, NO notifications sent, etc.

@return bool Returns true on success, false on fail

@since 3.0.153
