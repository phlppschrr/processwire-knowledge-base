# CommentArray

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Inherits: `PaginatedArray`
Implements: `WirePaginatable`

ProcessWire FieldtypeComments > CommentArray

Maintains an array of multiple Comment instances.
Serves as the value referenced when a FieldtypeComment field is reference from a Page.

Methods:
- [`isValidItem(Wire|Comment $item): bool`](method-isvaliditem.md)
- [`render(array $options = array()): string`](method-render.md)
- [`makeNew(): CommentArray`](method-makenew.md)
- [`renderForm(array $options = array()): string`](method-renderform.md)
- [`renderAll(array $options = array()): string`](method-renderall.md)
- [`getCommentList(array $options = array()): CommentList`](method-getcommentlist.md)
- [`getCommentForm(array $options = array()): CommentForm`](method-getcommentform.md)
- [`setPage(Page $page)`](method-setpage.md)
- [`setField(Field $field)`](method-setfield.md)
- [`getPage(): Page`](method-getpage.md)
- [`getField(): CommentField|Field`](method-getfield.md)
- [`getTotal(): int`](method-gettotal.md)
- [`getLimit(): int`](method-getlimit.md)
- [`isIdentical(WireArray $items, bool|int $strict = true): bool`](method-isidentical.md)
- [`stars(bool $allowPartial = true, bool $getCount = false): int|float|false|array`](method-stars.md)
- [`renderStars(bool $showCount = false, array $options = array()): string`](method-renderstars.md)
- [`trackAdd(Comment $item, int|string $key)`](method-trackadd.md)
- [`hasComment(Comment|int $comment): bool`](method-hascomment.md)
