# $commentListCustom->renderItem(Comment $comment, $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentListCustom.php`

Render the comment

## Usage

~~~~~
// basic usage
$string = $commentListCustom->renderItem($comment);

// usage with all arguments
$string = $commentListCustom->renderItem(Comment $comment, $options = array());
~~~~~

## Hookable

- Hookable method name: `renderItem`
- Implementation: `___renderItem`
- Hook with: `$commentListCustom->renderItem()`

## Arguments

- `$comment` `Comment`
- `$options` (optional) `array|int` Options array

## Return value

- `string`

## See Also

- [CommentArray::render()](../CommentArray/method-render.md)
