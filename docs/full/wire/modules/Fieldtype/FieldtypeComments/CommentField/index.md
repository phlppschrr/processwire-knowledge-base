# CommentField

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Inherits: `Field`


Groups:
Group: [other](group-other.md)

ProcessWire Comments Field

Custom “Field” class for Comments fields.



@todo Some more methods from FieldtypeComments can be moved into this class

Methods:
- [`find($selectorString, array $options = array()): CommentArray`](method-find.md)
- [`count(string|null $selectorString): int`](method-count.md)
- [`getNumComments(Page $page, array $options = array()): int`](method-getnumcomments.md)
- [`getCommentByCode(Page|int|string $page, string $code): Comment|null`](method-getcommentbycode.md)
- [`getCommentByID(Page|int|string $page, int $id): Comment|null`](method-getcommentbyid.md)
- [`getCommentsByID(array $ids, Page|null $page = null): CommentArray`](method-getcommentsbyid.md)
- [`getCommentParents(Page $page, Comment $comment): CommentArray`](method-getcommentparents.md)
- [`addComment(Page $page, Comment $comment, bool $send): bool`](method-addcomment.md)
- [`updateComment(Page $page, Comment $comment, array $properties): bool`](method-updatecomment.md)
- [`deleteComment(Page $page, Comment $comment, string $notes = ''): mixed`](method-deletecomment.md)
- [`voteComment(Page $page, Comment $comment, bool $up = true): bool`](method-votecomment.md)
- [`allowCommentParent(Comment $comment, Comment|int $parent, bool $verbose = false): bool`](method-allowcommentparent.md)
- [`allowCommentPage(Comment $comment, Page $page, bool $verbose = false): bool`](method-allowcommentpage.md)
- [`allowDeleteComment(Comment $comment): bool`](method-allowdeletecomment.md)
- [`getFieldtype(): FieldtypeComments|Fieldtype`](method-getfieldtype.md)
