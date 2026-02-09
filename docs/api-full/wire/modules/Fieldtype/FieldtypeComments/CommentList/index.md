# CommentList

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Inherits: `Wire`
Implements: `CommentListInterface`

## Summary

CommentList provides the default implementation of the CommentListInterface interface.

Common methods:
- [`options()`](method-options.md)
- [`getReplies()`](method-getreplies.md)
- [`getCommentListClasses()`](method-getcommentlistclasses.md)
- [`getCommentItemClasses()`](method-getcommentitemclasses.md)
- [`render()`](method-render.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`__construct(CommentArray $comments, array $options = array())`](method-__construct.md) Construct the CommentList
- [`options(string|null|array $key = null, string|int|bool|null $value = null): array|string|int|bool|null`](method-options.md) Get or set options
- [`getReplies(int|Comment $commentID): array`](method-getreplies.md) Get replies to the given comment ID, or 0 for root level comments
- [`getCommentListClasses(int $parent_id): array`](method-getcommentlistclasses.md) Get classes to use with comment list
- [`getCommentItemClasses(Comment $comment): array`](method-getcommentitemclasses.md) Get classes to use with comment item
- [`render(): string`](method-render.md) Rendering of comments for API demonstration and testing purposes (or feel free to use for production if suitable)
- [`renderList(int $parent_id = 0, int $depth = 0): string`](method-renderlist.md) Render comment list
- [`populatePlaceholders(Comment $comment, string $out, array $placeholders = array()): string`](method-populateplaceholders.md) Populate comment {variable} placeholders
- [`allowRenderItem(Comment $comment): bool`](method-allowrenderitem.md) Allow comment to be rendered in list?
- [`renderItem(Comment $comment, array $options = array()): string`](method-renderitem.md) Render the comment
- [`renderItem(Comment $comment, array|int $options = array()): string`](method-___renderitem.md) (hookable) Render the comment (hookable version)
- [`renderCheckActions(array $options = array()): string`](method-rendercheckactions.md) Check for URL-based comment approval actions
- [`placeholders(string|array|false $name = '', string|bool $value = null): string|array`](method-placeholders.md) Get or set placeholders that will be populated by populatePlaceholders() method
