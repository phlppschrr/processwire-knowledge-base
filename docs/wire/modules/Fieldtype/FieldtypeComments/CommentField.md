# CommentField

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

ProcessWire Comments Field

Custom “Field” class for Comments fields.

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com


@todo Some more methods from FieldtypeComments can be moved into this class

## other

@property int $moderate

@property int|bool $redirectAfterPost

@property int|bool $quietSave

@property string $notificationEmail

@property string $fromEmail

@property int $notifySpam

@property int $useNotify See Comment::flagNotify* constants

@property bool|int $useNotifyText Include comment text in notification emails?

@property int|bool $useAkismet

@property int $deleteSpamDays

@property int $depth

@property int|bool $sortNewest

@property int|bool $useWebsite

@property string $dateFormat

@property int $useVotes

@property int $useStars

@property string $useGravatar

@property int $schemaVersion

## find()

Find comments matching given selector

@param $selectorString

@param array $options

@return CommentArray

## count()

Return total quantity of comments matching the selector

@param string|null $selectorString Selector string with query

@return int

## getNumComments()

Get number of comments for Page, optionally limited by specific $options

Unlike the count() method this is focused on a specific Page and may be faster in
cases where it matches what you need to count.

@param Page $page

@param array $options
 - `status` (int): Specify Comment::status* constant to include only this status
 - `minStatus` (int): Specify Comment::status* constant to include only comments with at least this status
 - `maxStatus` (int): Specify Comment::status* constant or include only comments up to this status
 - `parent` (int|Comment): Specify parent comment ID, 0 for root-only, or omit for no parent limitation
 - `minCreated` (int): Minimum created unix timestamp
 - `maxCreated` (int): Maximum created unix timestamp
 - `stars` (int): Number of stars to match (1-5)
 - `minStars` (int): Minimum number of stars to match (1-5)
 - `maxStars` (int): Maximum number of stars to match (1-5)

@return int

@since 3.0.153

## getCommentByCode()

Given a comment code or subcode, return the associated comment ID or 0 if it doesn't exist

@param Page|int|string $page

@param string $code

@return Comment|null

## getCommentByID()

Get a comment by ID or NULL if not found

@param Page|int|string $page

@param int $id

@return Comment|null

## getCommentsByID()

Get multiple comments by ID

@param int[] $ids Comment IDs

@param Page|null $page Optionally limit comments to this page

@return CommentArray

@since 3.0.255

## getCommentParents()

Get parent comments for given Comment

@param Page $page

@param Comment $comment

@return CommentArray

@since 3.0.153

## addComment()

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

## updateComment()

Update specific properties for a comment

@param Page $page

@param Comment $comment

@param array $properties Associative array of properties to update

@return bool

## deleteComment()

Delete a given comment

@param Page $page

@param Comment $comment

@param string $notes

@return mixed

## voteComment()

Add a vote to the current comment from the current user/IP

@param Page $page

@param Comment $comment

@param bool $up Specify true for upvote, or false for downvote

@return bool Returns true on success, false on failure or duplicate

## allowCommentParent()

Allow given Comment to have given parent comment?

@param Comment $comment

@param Comment|int $parent

@param bool $verbose Report reason why not to standard errors? (default=false)

@return bool

@since 3.0.149

## allowCommentPage()

Allow given comment to live on given page?

@param Comment $comment

@param Page $page

@param bool $verbose Report reason why not to standard errors? (default=false)

@return bool

@since 3.0.149

## allowDeleteComment()

May the given comment be deleted?

@param Comment $comment

@return bool

## getFieldtype()

@return FieldtypeComments|Fieldtype
