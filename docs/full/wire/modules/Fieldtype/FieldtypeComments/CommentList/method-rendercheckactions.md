# $commentList->renderCheckActions(array $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Check for URL-based comment approval actions

Note that when it finds an actionable approval code, it performs a
redirect back to the same page after completing the action, with
?comment_success=2 on successful action, or ?comment_success=3 on
error.

It also populates a session variable 'CommentApprovalMessage' with
a text message of what occurred.

## Usage

~~~~~
// basic usage
$string = $commentList->renderCheckActions();

// usage with all arguments
$string = $commentList->renderCheckActions(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array`

## Return value

- `string`
