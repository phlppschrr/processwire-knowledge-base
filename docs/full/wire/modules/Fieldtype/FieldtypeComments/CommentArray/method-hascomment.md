# CommentArray::hasComment()

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Does this CommentArray have the given Comment (or comment ID)?

Note: this method is very specific in purpose, accepting only a Comment object or ID.
You can use the has() method for more flexibility.

@param Comment|int $comment

@return bool

@since 3.0.149

@see WireArray::has()
