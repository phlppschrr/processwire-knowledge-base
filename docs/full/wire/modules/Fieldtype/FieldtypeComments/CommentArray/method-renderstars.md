# $commentArray->renderStars($showCount = false, $options = array()): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentArray.php`

Render combined star rating for all comments in this CommentsArray

## Usage

~~~~~
// basic usage
$string = $commentArray->renderStars();

// usage with all arguments
$string = $commentArray->renderStars($showCount = false, $options = array());
~~~~~

## Arguments

- `$showCount` (optional) `bool` Specify true to include how many ratings the average is based on
- `$options` (optional) `array` Overrides of stars and/or count, see $defaults in method

## Return value

- `string`
