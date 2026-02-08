# Comment: other

Source: `wire/modules/Fieldtype/FieldtypeComments/Comment.php`

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
