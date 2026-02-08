# $commentList->___renderItem(Comment $comment, $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Render the comment (hookable version)

Hookable since 3.0.138

## Usage

~~~~~
// basic usage
$string = $commentList->___renderItem($comment);

// usage with all arguments
$string = $commentList->___renderItem(Comment $comment, $options = array());
~~~~~

## Arguments

- `$comment` `Comment`
- `$options` (optional) `array|int` Options array

## Return value

- `string`

## See Also

- [CommentArray::render()](../CommentArray/method-render.md)
