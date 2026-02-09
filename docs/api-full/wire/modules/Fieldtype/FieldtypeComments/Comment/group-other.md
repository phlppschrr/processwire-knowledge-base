# Comment: other

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

- `$id: int`
- `$parent_id: int`
- `$text: string`
- `$textFormatted: string|null` Text value formatted for output (runtime use only, must be set manually)
- `$sort: int`
- `$status: int`
- `$prevStatus: int|null`
- `$flags: int`
- `$created: int`
- `$email: string`
- `$cite: string`
- `$website: string`
- `$ip: string`
- `$user_agent: string`
- `$created_users_id: int`
- `$code: string`
- `$subcode: string`
- `$upvotes: int`
- `$downvotes: int`
- `$stars: int`
- `$isNew: null|bool` Was this comment added in this request? (since 3.0.169)
- `$approvalNote: null|string` Runtime approval note for newly added comment, internal use (since 3.0.169)
- [`$parent: Comment|null`](method-parent.md) Parent comment when depth is enabled or null if no parent (since 3.0.149)
- [`$parents: CommentArray`](method-parents.md) All parent comments (since 3.0.149)
- [`$children: CommentArray`](method-children.md) Immediate child comments (since 3.0.149)
- [`$depth: int`](method-depth.md) Current comment depth (since 3.0.149)
- `$loaded: bool` True when comment is fully loaded from DB (since 3.0.149)
- [`$numChildren: int`](method-numchildren.md) Number of children with no exclusions. See and use `numChildren()` method for more options. (since 3.0.154)
- `$createdUser: User` User that created the comment
