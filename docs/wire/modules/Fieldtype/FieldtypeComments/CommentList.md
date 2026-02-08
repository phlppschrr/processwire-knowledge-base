# CommentList

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

CommentList provides the default implementation of the CommentListInterface interface.

## other

@method void renderItemReady(Comment $comment, $depth)

## __construct()

Construct the CommentList

@param CommentArray $comments

@param array $options Options that may override those provided with the class (see CommentList::$options)

## options()

Get or set options

@param string|null|array $key Use one of the following:
 - Omit to get array of all options
 - Specify option name to get (and omit $value argument)
 - Specify option name to set and provide a non-null $value argument
 - Specify array of one or more [ 'option' => 'value' ] to set and omit $value argument

@param string|int|bool|null $value When setting an individual option, value should be specified here, otherwise omit

@return array|string|int|bool|null When getting singe option, value is returned, otherwise array of all options is returned.

@since 3.0.138

## getReplies()

Get replies to the given comment ID, or 0 for root level comments

@param int|Comment $commentID

@return array

## getCommentListClasses()

Get classes to use with comment list

@param int $parent_id

@return array

## getCommentItemClasses()

Get classes to use with comment item

@param Comment $comment

@return array

## render()

Rendering of comments for API demonstration and testing purposes (or feel free to use for production if suitable)

@see Comment::render()

@return string or blank if no comments

## renderList()

Render comment list

@param int $parent_id

@param int $depth

@return string

## populatePlaceholders()

Populate comment {variable} placeholders

@param Comment $comment

@param string $out

@param array $placeholders Additional placeholders to populate as name => value (exclude the brackets)

@return string

## allowRenderItem()

Allow comment to be rendered in list?

@param Comment $comment

@return bool

## renderItem()

Render the comment

This is the default rendering for development/testing/demonstration purposes

It may be used for production, but only if it meets your needs already. Typically you'll want to render the comments
using your own code in your templates.

@param Comment $comment

@param array $options

@return string

@see CommentArray::render()

## ___renderItem()

Render the comment (hookable version)

Hookable since 3.0.138

@param Comment $comment

@param array|int $options Options array

@return string

@see CommentArray::render()

## renderCheckActions()

Check for URL-based comment approval actions

Note that when it finds an actionable approval code, it performs a
redirect back to the same page after completing the action, with
?comment_success=2 on successful action, or ?comment_success=3 on
error.

It also populates a session variable 'CommentApprovalMessage' with
a text message of what occurred.

@param array $options

@return string

## placeholders()

Get or set placeholders that will be populated by populatePlaceholders() method

@param string|array|false $name Specify placeholder name to get or set, array of placeholders to set, false to unset all, omit to get all

@param string|bool $value Specify placeholder value to set or boolean false to unset, or omit when getting

@return string|array

@since 3.0.153
