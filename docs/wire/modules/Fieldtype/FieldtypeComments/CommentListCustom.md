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

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

## getMarkup()

Get markup property or all markup

@param string $property Specify property or omit to get all

@return array|mixed|null

## setMarkup()

Set markup

Set any or all of the following markup properties via associative array:

list, sublist, item, subitem, gravtar, website, permalink, reply,
noticeMessage, noticeLink, noticeSuccessClass, noticeErrorClass

@param array $markup

## markup()

Get or set markup properties

@param string|array $key Property to get or set, or array of properties to set

@param null|mixed $value Specify only if setting individual property

@return mixed

## renderList()

Render comment list

@param int $parent_id

@param int $depth

@return string

## ___renderItem()

Render the comment

@param Comment $comment

@param array|int $options Options array

@return string

@see CommentArray::render()
