# $commentList->renderItem(Comment $comment, $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Render the comment

This is the default rendering for development/testing/demonstration purposes

It may be used for production, but only if it meets your needs already. Typically you'll want to render the comments
using your own code in your templates.

## Usage

~~~~~
// basic usage
$string = $commentList->renderItem($comment);

// usage with all arguments
$string = $commentList->renderItem(Comment $comment, $options = array());
~~~~~

## Arguments

- `$comment` `Comment`
- `$options` (optional) `array`

## Return value

- `string`

## See Also

- [CommentArray::render()](../CommentArray/method-render.md)
