# $commentForm->__construct(Page $page, CommentArray $comments, $options = array())

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentForm.php`

Construct a CommentForm

## Usage

~~~~~
// basic usage
$result = $commentForm->__construct($page, $comments);

// usage with all arguments
$result = $commentForm->__construct(Page $page, CommentArray $comments, $options = array());
~~~~~

## Arguments

- `$page` `Page` The page with the comments
- `$comments` `CommentArray` The field value from $page
- `$options` (optional) `array` Optional modifications to default behavior (see CommentForm::$options)
