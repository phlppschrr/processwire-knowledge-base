# $commentFormCustom->getFormMarkup(): string

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentFormCustom.php`

Get form markup

To set form markup use the markup in this method as your starting point and set your custom markup with this:

## Example

~~~~~
$markup = "...your custom form markup...";
$commentForm->markup('form', $markup);
~~~~~

## Usage

~~~~~
// basic usage
$string = $commentFormCustom->getFormMarkup();
~~~~~

## Return value

- `string`
