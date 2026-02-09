# Comment

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

ProcessWire Fieldtype Comments > Comment

Class that contains an individual comment.

Methods:
- [`__construct()`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`get(string $key): mixed`](method-get.md)
- [`getFormatted(string $key, array $options = array()): string`](method-getformatted.md)
- [`getFormattedCommentText(array $options = array()): string`](method-getformattedcommenttext.md)
- [`set(string $key, mixed $value): self|WireData`](method-set.md)
- [`cleanCommentString(string $str): string`](method-cleancommentstring.md)
- [`__toString()`](method-__tostring.md)
- [`isApproved()`](method-isapproved.md)
- [`getGravatar(string $email, string $rating = 'g', string $imageset = 'mm', int $size = 80): string`](method-getgravatar.md)
- [`gravatar(string $rating = 'g', string $imageset = 'mm', int $size = 80): string`](method-gravatar.md)
- [`setPage(Page $page)`](method-setpage.md)
- [`setField(Field $field)`](method-setfield.md)
- [`getPage(): null|Page`](method-getpage.md)
- [`getField(): null|Field|CommentField`](method-getfield.md)
- [`depth(): int`](method-depth.md)
- [`parent(): Comment|null`](method-parent.md)
- [`parents(): CommentArray`](method-parents.md)
- [`children(): CommentArray`](method-children.md)
- [`numChildren(array $options = array()): int`](method-numchildren.md)
- [`allowChildren(): bool`](method-allowchildren.md)
- [`hasChild(int|Comment $comment, bool $recursive = true): bool`](method-haschild.md)
- [`renderStars(array $options = array()): string`](method-renderstars.md)
- [`quiet(bool $quiet = null): bool`](method-quiet.md)
- [`url(bool $http = false): string`](method-url.md)
- [`httpUrl(): string`](method-httpurl.md)
- [`editUrl(): string`](method-editurl.md)
- [`setMeta(string|array $key, null|string|array|int|float|mixed $value = null): self`](method-setmeta.md)
- [`getMeta(null|string $key = null): string|array|int|float|mixed|null`](method-getmeta.md)
- [`removeMeta(string $key): self`](method-removemeta.md)
- [`meta(string|array $key = null, mixed|null $value = null): array|string|int|mixed`](method-meta.md)

Constants:
- [`statusSpam`](const-statusspam.md)
- [`statusPending`](const-statuspending.md)
- [`statusApproved`](const-statusapproved.md)
- [`statusFeatured`](const-statusfeatured.md)
- [`statusDelete`](const-statusdelete.md)
- [`flagNotifyReply`](const-flagnotifyreply.md)
- [`flagNotifyAll`](const-flagnotifyall.md)
- [`flagNotifyConfirmed`](const-flagnotifyconfirmed.md)
- [`flagNotifyQueue`](const-flagnotifyqueue.md)
- [`maxCommentBytes`](const-maxcommentbytes.md)
