# CommentListCustom

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentListCustom.php`

Inherits: `CommentList`

## Summary

ProcessWire CommentListCustom

Common methods:
- [`getMarkup()`](method-getmarkup.md)
- [`setMarkup()`](method-setmarkup.md)
- [`markup()`](method-markup.md)
- [`renderList()`](method-renderlist.md)
- [`renderItem()`](method-___renderitem.md)

Manages custom CommentList implementations where you specify your own markup

~~~~~~
$list = $page->comments->getCommentList([
  'className' => 'CommentListCustom',
]);

$list->setMarkup([
  'noticeMessage' => "<div id='{id}' class='uk-alert {class}'>{message}</div>",
  'noticeSuccessClass' => 'uk-alert-success',
  'noticeErrorClass' => 'uk-alert-danger',
  'list' => "<ul id='my-comments-list' class='{class}'>{comments}</ul>",
  // and so on for any other $markup properties
]);

echo $list->render();
~~~~~~

## Methods
- [`getMarkup(string $property = ''): array|mixed|null`](method-getmarkup.md) Get markup property or all markup
- [`setMarkup(array $markup)`](method-setmarkup.md) Set markup
- [`markup(string|array $key = '', null|mixed $value = null): mixed`](method-markup.md) Get or set markup properties
- [`renderList(int $parent_id = 0, int $depth = 0): string`](method-renderlist.md) Render comment list
- [`renderItem(Comment $comment, array|int $options = array()): string`](method-___renderitem.md) (hookable) Render the comment
