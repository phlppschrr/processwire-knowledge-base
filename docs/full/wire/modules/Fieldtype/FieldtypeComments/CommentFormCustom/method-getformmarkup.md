# CommentFormCustom::getFormMarkup()

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentFormCustom.php`

Get form markup

To set form markup use the markup in this method as your starting point and set your custom markup with this:
~~~~~
$markup = "...your custom form markup...";
$commentForm->markup('form', $markup);
~~~~~

@return string
