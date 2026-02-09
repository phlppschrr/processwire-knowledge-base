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

## Arguments

- `$comment` `Comment`
- `$options` (optional) `array|int` Options array

## Return value

- `string`

## Hooking

- Hookable method name: `renderItem`
- Implementation: `___renderItem`
- Hook with: `CommentListCustom::renderItem`

### Hooking Before

~~~~~
$this->addHookBefore('CommentListCustom::renderItem', function(HookEvent $event) {
  $commentListCustom = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $comment);
  $event->arguments(1, $options);
});
~~~~~

### Hooking After

~~~~~
$this->addHookAfter('CommentListCustom::renderItem', function(HookEvent $event) {
  $commentListCustom = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## See Also

- [CommentArray::render()](../CommentArray/method-render.md)
