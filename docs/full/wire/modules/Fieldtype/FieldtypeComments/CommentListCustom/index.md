# CommentListCustom

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentListCustom.php`

ProcessWire CommentListCustom

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

Methods:
Method: [getMarkup()](method-getmarkup.md)
Method: [setMarkup()](method-setmarkup.md)
Method: [markup()](method-markup.md)
Method: [renderList()](method-renderlist.md)
Method: [renderItem()](method-___renderitem.md) (hookable)
