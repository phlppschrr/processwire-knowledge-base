# Comment

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

ProcessWire Fieldtype Comments > Comment

Class that contains an individual comment.

Methods:
- [`__construct()`](method-__construct.md) Construct a Comment and set defaults
- [`wired()`](method-wired.md) Wired to API
- [`get(string $key): mixed`](method-get.md) Get property
- [`getFormatted(string $key, array $options = array()): string`](method-getformatted.md) Same as get() but with output formatting applied
- [`getFormattedCommentText(array $options = array()): string`](method-getformattedcommenttext.md) Get comment text as formatted string
- [`set(string $key, mixed $value): self|WireData`](method-set.md) Set property
- [`cleanCommentString(string $str): string`](method-cleancommentstring.md) Clean a comment string by issuing several filters
- [`__toString()`](method-__tostring.md) String value of a Comment is it's database ID
- [`isApproved()`](method-isapproved.md) Returns true if the comment is approved and thus appearing on the site
- [`getGravatar(string $email, string $rating = 'g', string $imageset = 'mm', int $size = 80): string`](method-getgravatar.md) Returns a URL to this user's gravatar image (static version, use non-static gravatar() function unless you specifically need static)
- [`gravatar(string $rating = 'g', string $imageset = 'mm', int $size = 80): string`](method-gravatar.md) Returns a URL to this user's gravatar image
- [`setPage(Page $page)`](method-setpage.md) Set Page that this Comment belongs to
- [`setField(Field $field)`](method-setfield.md) Set Field that this Comment belongs to
- [`getPage(): null|Page`](method-getpage.md) Get Page that this Comment belongs to
- [`getField(): null|Field|CommentField`](method-getfield.md) Get Field that this Comment belongs to
- [`depth(): int`](method-depth.md) Get current comment depth
- [`parent(): Comment|null`](method-parent.md) Return the parent comment, if applicable
- [`parents(): CommentArray`](method-parents.md) Get CommentArray of all parent comments for this one
- [`children(): CommentArray`](method-children.md) Return children comments, if applicable
- [`numChildren(array $options = array()): int`](method-numchildren.md) Return number of children (replies) for this comment
- [`allowChildren(): bool`](method-allowchildren.md) Are child comments (replies) allowed?
- [`hasChild(int|Comment $comment, bool $recursive = true): bool`](method-haschild.md) Does this comment have the given child comment?
- [`renderStars(array $options = array()): string`](method-renderstars.md) Render stars markup
- [`quiet(bool $quiet = null): bool`](method-quiet.md) Get or set quiet mode
- [`url(bool $http = false): string`](method-url.md) Return URL to view comment
- [`httpUrl(): string`](method-httpurl.md) Return full http URL to view comment
- [`editUrl(): string`](method-editurl.md) Return URL to edit comment
- [`setMeta(string|array $key, null|string|array|int|float|mixed $value = null): self`](method-setmeta.md) Set meta data (custom fields for comments)
- [`getMeta(null|string $key = null): string|array|int|float|mixed|null`](method-getmeta.md) Get meta data property value (custom fields for comments)
- [`removeMeta(string $key): self`](method-removemeta.md) Remove given meta data property or '*' to remove all
- [`meta(string|array $key = null, mixed|null $value = null): array|string|int|mixed`](method-meta.md) Get or set meta data property

Constants:
- [`statusSpam = -2`](const-statusspam.md)
- [`statusPending = 0`](const-statuspending.md)
- [`statusApproved = 1`](const-statusapproved.md)
- [`statusFeatured = 2`](const-statusfeatured.md)
- [`statusDelete = 999`](const-statusdelete.md)
- [`flagNotifyReply = 2`](const-flagnotifyreply.md)
- [`flagNotifyAll = 4`](const-flagnotifyall.md)
- [`flagNotifyConfirmed = 8`](const-flagnotifyconfirmed.md)
- [`flagNotifyQueue = 16`](const-flagnotifyqueue.md)
- [`maxCommentBytes = 81920`](const-maxcommentbytes.md)
