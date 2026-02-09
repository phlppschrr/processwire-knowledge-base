# $commentArray->getCommentList(array $options = array()): CommentList

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Return instance of CommentList object

## Usage

~~~~~
// basic usage
$commentList = $commentArray->getCommentList();

// usage with all arguments
$commentList = $commentArray->getCommentList(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` See CommentList::$options for details, plus: - `className` (string): PHP class name to use for CommentList (default='CommentList')

## Return value

- `CommentList`
