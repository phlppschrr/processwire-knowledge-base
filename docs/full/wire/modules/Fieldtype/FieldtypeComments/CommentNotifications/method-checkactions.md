# $commentNotifications->checkActions(): array(

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentNotifications.php`

Check for a GET variable comment approval code and take action is valid

## Usage

~~~~~
// basic usage
$result = $commentNotifications->checkActions();
~~~~~

## Return value

- `array(` 'success' => true|false, whether or not comment was updated 'valid' => true|false, whether or not the request was valid 'action' => approve|spam|pending|unknown 'message' => 'string', 'pageID' => id of page or 0 if not known 'fieldName' => 'name of field or blank if not known' 'commentID' => id of comment or 0 if not applicable, )
