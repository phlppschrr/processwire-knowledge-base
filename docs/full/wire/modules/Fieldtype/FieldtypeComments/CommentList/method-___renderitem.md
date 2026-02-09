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

## Hooking Before

~~~~~
$this->addHookBefore('CommentList::renderItem', function(HookEvent $event) {
  $commentList = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally change arguments
  $event->arguments(0, $comment);
  $event->arguments(1, $options);
});
~~~~~

## Hooking After

~~~~~
$this->addHookAfter('CommentList::renderItem', function(HookEvent $event) {
  $commentList = $event->object;

  // Get arguments
  $comment = $event->arguments(0);
  $options = $event->arguments(1);

  // Your code here

  // Optionally modify return value
  $return = $event->return;
  $event->return = $return;
});
~~~~~

## Arguments

- `$comment` `Comment`
- `$options` (optional) `array|int` Options array

## Return value

- `string`

## See Also

- [CommentArray::render()](../CommentArray/method-render.md)
