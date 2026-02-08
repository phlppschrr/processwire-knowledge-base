# CommentArray

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

ProcessWire FieldtypeComments > CommentArray

Maintains an array of multiple Comment instances.
Serves as the value referenced when a FieldtypeComment field is reference from a Page.

ProcessWire 3.x, Copyright 2016 by Ryan Cramer
https://processwire.com

## isValidItem()

Per the WireArray interface, is the item a Comment

@param Wire|Comment $item

@return bool

## render()

Provides the default rendering of a comment list, which may or may not be what you want

@param array $options

@return string

@see CommentList class and override it to serve your needs

## makeNew()

Make a new blank CommentArray setup for the same Page/Field as the one it is called on

@return CommentArray

## renderForm()

Provides the default rendering of a comment form, which may or may not be what you want

@param array $options

@return string

@see CommentForm class and override it to serve your needs

## renderAll()

Render all comments and a comments form below it

@param array $options

@return string

## getCommentList()

Return instance of CommentList object

@param array $options See CommentList::$options for details, plus:
 - `className` (string): PHP class name to use for CommentList (default='CommentList')

@return CommentList

## getCommentForm()

Return instance of CommentForm object

@param array $options

@return CommentForm

@throws WireException

## setPage()

Set the page that these comments are on

@param Page $page

## setField()

Set the Field that these comments are on

@param CommentField|Field $field

## getPage()

Get the page that these comments are on

@return Page

## getField()

Get the Field that these comments are on

@return CommentField|Field

## getTotal()

Get the total number of comments

Used for pagination.

@return int

## getLimit()

Get the imposed limit on number of comments.

If no limit set, then return number of comments currently here.

Used for pagination.

@return int

## isIdentical()

Is the given CommentArray identical to this one?

@param WireArray $items

@param bool|int $strict

@return bool

## stars()

Get an average of all star ratings for all comments in this CommentsArray

@param bool $allowPartial Allow partial stars? If true, returns a float. If false, returns int.

@param bool $getCount If true, this method returns an array(stars, count) where count is number of ratings.

@return int|float|false|array Returns false for stars value if no ratings yet.

## renderStars()

Render combined star rating for all comments in this CommentsArray

@param bool $showCount Specify true to include how many ratings the average is based on

@param array $options Overrides of stars and/or count, see $defaults in method

@return string

## trackAdd()

Track an item added

@param Comment $item

@param int|string $key

## hasComment()

Does this CommentArray have the given Comment (or comment ID)?

Note: this method is very specific in purpose, accepting only a Comment object or ID.
You can use the has() method for more flexibility.

@param Comment|int $comment

@return bool

@since 3.0.149

@see WireArray::has()
