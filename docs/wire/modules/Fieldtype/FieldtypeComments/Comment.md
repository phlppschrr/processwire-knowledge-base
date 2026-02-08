# Comment

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

ProcessWire Fieldtype Comments > Comment

Class that contains an individual comment.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property int $id

@property int $parent_id

@property string $text

@property string|null $textFormatted Text value formatted for output (runtime use only, must be set manually)

@property int $sort

@property int $status

@property int|null $prevStatus

@property int $flags

@property int $created

@property string $email

@property string $cite

@property string $website

@property string $ip

@property string $user_agent

@property int $created_users_id

@property string $code

@property string $subcode

@property int $upvotes

@property int $downvotes

@property int $stars

@property null|bool $isNew Was this comment added in this request? (since 3.0.169)

@property null|string $approvalNote Runtime approval note for newly added comment, internal use (since 3.0.169)

@property-read Comment|null $parent Parent comment when depth is enabled or null if no parent (since 3.0.149)

@property-read CommentArray $parents All parent comments (since 3.0.149)

@property-read CommentArray $children Immediate child comments (since 3.0.149)

@property-read int $depth Current comment depth (since 3.0.149)

@property-read bool $loaded True when comment is fully loaded from DB (since 3.0.149)

@property-read int $numChildren Number of children with no exclusions. See and use numChildren() method for more options. (since 3.0.154)

@property-read User $createdUser User that created the comment

## statusSpam

Status for Comment identified as spam

## statusPending

Status for Comment pending review

## statusApproved

Status for Comment that's been approved

## statusFeatured

Status for comment that's been approved and featured

## statusDelete

Status for Comment to indicate pending deletion

## flagNotifyReply

Flag to indicate author of this comment wants to be notified of replies to their comment

## flagNotifyAll

Flag to indicate author of this comment wants to be notified of all comments on page

## flagNotifyConfirmed

Flag to indicate author of this comment wants notifications and request confirmed by double opt in

## flagNotifyQueue

Flag to indicate comment is queued for notifications to be sent later by 3rd party implementation

## maxCommentBytes

Max bytes that a Comment may use

## __construct()

Construct a Comment and set defaults

## wired()

Wired to API

## get()

Get property

@param string $key

@return mixed

## getFormatted()

Same as get() but with output formatting applied

Note that we won't apply this to get() when $page->outputFormatting is active
in order for backwards compatibility with older installations.

@param string $key One of: text, cite, email, user_agent, website

@param array $options

@return string

## getFormattedCommentText()

Get comment text as formatted string

Note that the default options behavior is to return comment text with paragraphs split by `</p><p>`
but without the first `<p>` and last `</p>` since it is assumed these will be the markup you wrap
the comment in. If you want it to include the wrapping `<p>…</p>` tags then specify true for the
`wrapParagraph` option in the `$options` argument.

@param array $options
 - `useParagraphs` (bool): Convert newlines to paragraphs? (default=true)
 - `wrapParagraph` (bool): Use wrapping <p>…</p> tags around return value? (default=false)
 - `useLinebreaks` (bool): Convert single newlines to <br> tags? (default=true)

@return string

@since 3.0.169

## set()

Set property

@param string $key

@param mixed $value

@return self|WireData

## cleanCommentString()

Clean a comment string by issuing several filters

@param string $str

@return string

## __toString()

String value of a Comment is it's database ID

## isApproved()

Returns true if the comment is approved and thus appearing on the site

## getGravatar()

Returns a URL to this user's gravatar image (static version, use non-static gravatar() function unless you specifically need static)

@param string $email

@param string $rating Gravatar rating, one of [ g | pg | r | x ], default is g.

@param string $imageset Gravatar default imageset, one of [ 404 | mm | identicon | monsterid | wavatar | retro | blank ], default is mm.

@param int $size Gravatar image size, default is 80.

@return string

## gravatar()

Returns a URL to this user's gravatar image

@param string $rating Gravatar rating, one of [ g | pg | r | x ], default is g.

@param string $imageset Gravatar default imageset, one of [ 404 | mm | identicon | monsterid | wavatar | retro | blank ], default is mm.

@param int $size Gravatar image size, default is 80.

@return string

## setPage()

Set Page that this Comment belongs to

@param Page $page

## setField()

Set Field that this Comment belongs to

@param Field $field

## getPage()

Get Page that this Comment belongs to

@return null|Page

## getField()

Get Field that this Comment belongs to

@return null|Field|CommentField

## depth()

Get current comment depth

@return int

@since 3.0.149

## parent()

Return the parent comment, if applicable

@return Comment|null

## parents()

Get CommentArray of all parent comments for this one

Order is closest parent to furthest parent

@return CommentArray

@since 3.0.149

## children()

Return children comments, if applicable

@return CommentArray

## numChildren()

Return number of children (replies) for this comment

~~~~~
$qty = $comment->numChildren([ 'minStatus' => Comment::statusApproved ]);
~~~~~

@param array $options Limit return value by specific properties (below):
 - `status` (int): Specify Comment::status* constant to include only this status
 - `minStatus` (int): Specify Comment::status* constant to include only comments with at least this status
 - `maxStatus` (int): Specify Comment::status* constant or include only comments up to this status
 - `minCreated` (int): Minimum created unix timestamp
 - `maxCreated` (int): Maximum created unix timestamp
 - `stars` (int): Number of stars to match (1-5)
 - `minStars` (int): Minimum number of stars to match (1-5)
 - `maxStars` (int): Maximum number of stars to match (1-5)

@return int

@since 3.0.153

## allowChildren()

Are child comments (replies) allowed?

@return bool

@since 3.0.204

## hasChild()

Does this comment have the given child comment?

@param int|Comment $comment Comment or Comment ID

@param bool $recursive Check all descending children recursively? Use false to check only direct children. (default=true)

@return bool

@since 3.0.149

## renderStars()

Render stars markup

@param array $options See CommentArray::renderStars for $options

@return string

## quiet()

Get or set quiet mode

When quiet mode is active, comment additions/changes don't trigger notifications and such.

@param bool $quiet Specify only if setting

@return bool The current quiet mode

## url()

Return URL to view comment

@param bool $http

@return string

## httpUrl()

Return full http URL to view comment

@return string

## editUrl()

Return URL to edit comment

@return string

## setMeta()

Set meta data (custom fields for comments)

To set multiple properties at once specify an associative array for $key and omit $value.

@param string|array $key Property name to set or assoc array of them

@param null|string|array|int|float|mixed $value Value to set for $key or omit of you used an array.

@return self

@since 3.0.203

## getMeta()

Get meta data property value (custom fields for comments)

Note: values returned are exactly as they were set and do not go through any runtime
formatting for HTML entities or anything like that. Be sure to provide your own formatting
where necessary.

@param null|string $key Name of property to get

@return string|array|int|float|mixed|null Returns value or null if not found

@since 3.0.203

## removeMeta()

Remove given meta data property or '*' to remove all

@param string $key

@return self

@since 3.0.203

## meta()

Get or set meta data property

@param string|array $key Property to get/set or omit to get all.

@param mixed|null $value Value to set for given property ($key) or omit if getting.

@return array|string|int|mixed Returns value for $key or null if it does not exist. Returns array when getting all.

@since 3.0.203
