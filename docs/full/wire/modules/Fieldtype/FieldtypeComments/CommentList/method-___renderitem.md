# $commentList->renderItem(Comment $comment, $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Render the comment (hookable version)

Hookable since 3.0.138

## Usage

~~~~~
// basic usage
$string = $commentList->renderItem($comment);

// usage with all arguments
$string = $commentList->renderItem(Comment $comment, $options = array());
~~~~~

## Hookable

- Hookable method name: `renderItem`
- Implementation: `___renderItem`
- Hook with: `$commentList->renderItem()`

## Arguments

- `$comment` `Comment`
- `$options` (optional) `array|int` Options array

## Return value

- `string`

## See Also

- [CommentArray::render()](../CommentArray/method-render.md)
