# CommentList

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Inherits: `Wire`
Implements: `CommentListInterface`


Groups:
Group: [other](group-other.md)

CommentList provides the default implementation of the CommentListInterface interface.

Methods:
- [`__construct(CommentArray $comments, array $options = array())`](method-__construct.md)
- [`options(string|null|array $key = null, string|int|bool|null $value = null): array|string|int|bool|null`](method-options.md)
- [`getReplies(int|Comment $commentID): array`](method-getreplies.md)
- [`getCommentListClasses(int $parent_id): array`](method-getcommentlistclasses.md)
- [`getCommentItemClasses(Comment $comment): array`](method-getcommentitemclasses.md)
- [`render(): string`](method-render.md)
- [`renderList(int $parent_id = 0, int $depth = 0): string`](method-renderlist.md)
- [`populatePlaceholders(Comment $comment, string $out, array $placeholders = array()): string`](method-populateplaceholders.md)
- [`allowRenderItem(Comment $comment): bool`](method-allowrenderitem.md)
- [`renderItem(Comment $comment, array $options = array()): string`](method-renderitem.md)
- [`renderItem(Comment $comment, array|int $options = array()): string`](method-___renderitem.md) (hookable)
- [`renderCheckActions(array $options = array()): string`](method-rendercheckactions.md)
- [`placeholders(string|array|false $name = '', string|bool $value = null): string|array`](method-placeholders.md)
