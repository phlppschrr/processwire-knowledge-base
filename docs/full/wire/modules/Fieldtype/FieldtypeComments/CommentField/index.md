# CommentField

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentField.php`

Inherits: `Field`


Groups:
Group: [other](group-other.md)

ProcessWire Comments Field

Custom “Field” class for Comments fields.



@todo Some more methods from FieldtypeComments can be moved into this class

Methods:
- [`find($selectorString, array $options = array()): CommentArray`](method-find.md) Find comments matching given selector
- [`count(string|null $selectorString): int`](method-count.md) Return total quantity of comments matching the selector
- [`getNumComments(Page $page, array $options = array()): int`](method-getnumcomments.md) Get number of comments for Page, optionally limited by specific $options
- [`getCommentByCode(Page|int|string $page, string $code): Comment|null`](method-getcommentbycode.md) Given a comment code or subcode, return the associated comment ID or 0 if it doesn't exist
- [`getCommentByID(Page|int|string $page, int $id): Comment|null`](method-getcommentbyid.md) Get a comment by ID or NULL if not found
- [`getCommentsByID(array $ids, Page|null $page = null): CommentArray`](method-getcommentsbyid.md) Get multiple comments by ID
- [`getCommentParents(Page $page, Comment $comment): CommentArray`](method-getcommentparents.md) Get parent comments for given Comment
- [`addComment(Page $page, Comment $comment, bool $send): bool`](method-addcomment.md) Add new comment
- [`updateComment(Page $page, Comment $comment, array $properties): bool`](method-updatecomment.md) Update specific properties for a comment
- [`deleteComment(Page $page, Comment $comment, string $notes = ''): mixed`](method-deletecomment.md) Delete a given comment
- [`voteComment(Page $page, Comment $comment, bool $up = true): bool`](method-votecomment.md) Add a vote to the current comment from the current user/IP
- [`allowCommentParent(Comment $comment, Comment|int $parent, bool $verbose = false): bool`](method-allowcommentparent.md) Allow given Comment to have given parent comment?
- [`allowCommentPage(Comment $comment, Page $page, bool $verbose = false): bool`](method-allowcommentpage.md) Allow given comment to live on given page?
- [`allowDeleteComment(Comment $comment): bool`](method-allowdeletecomment.md) May the given comment be deleted?
- [`getFieldtype(): FieldtypeComments|Fieldtype`](method-getfieldtype.md)
