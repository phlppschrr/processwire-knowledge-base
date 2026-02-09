# CommentArray

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Inherits: `PaginatedArray`
Implements: `WirePaginatable`

ProcessWire FieldtypeComments > CommentArray

Maintains an array of multiple Comment instances.
Serves as the value referenced when a FieldtypeComment field is reference from a Page.

Methods:
- [`isValidItem(Wire|Comment $item): bool`](method-isvaliditem.md) Per the WireArray interface, is the item a Comment
- [`render(array $options = array()): string`](method-render.md) Provides the default rendering of a comment list, which may or may not be what you want
- [`makeNew(): CommentArray`](method-makenew.md) Make a new blank CommentArray setup for the same Page/Field as the one it is called on
- [`renderForm(array $options = array()): string`](method-renderform.md) Provides the default rendering of a comment form, which may or may not be what you want
- [`renderAll(array $options = array()): string`](method-renderall.md) Render all comments and a comments form below it
- [`getCommentList(array $options = array()): CommentList`](method-getcommentlist.md) Return instance of CommentList object
- [`getCommentForm(array $options = array()): CommentForm`](method-getcommentform.md) Return instance of CommentForm object
- [`setPage(Page $page)`](method-setpage.md) Set the page that these comments are on
- [`setField(Field $field)`](method-setfield.md) Set the Field that these comments are on
- [`getPage(): Page`](method-getpage.md) Get the page that these comments are on
- [`getField(): CommentField|Field`](method-getfield.md) Get the Field that these comments are on
- [`getTotal(): int`](method-gettotal.md) Get the total number of comments
- [`getLimit(): int`](method-getlimit.md) Get the imposed limit on number of comments.
- [`isIdentical(WireArray $items, bool|int $strict = true): bool`](method-isidentical.md) Is the given CommentArray identical to this one?
- [`stars(bool $allowPartial = true, bool $getCount = false): int|float|false|array`](method-stars.md) Get an average of all star ratings for all comments in this CommentsArray
- [`renderStars(bool $showCount = false, array $options = array()): string`](method-renderstars.md) Render combined star rating for all comments in this CommentsArray
- [`trackAdd(Comment $item, int|string $key)`](method-trackadd.md) Track an item added
- [`hasComment(Comment|int $comment): bool`](method-hascomment.md) Does this CommentArray have the given Comment (or comment ID)?
