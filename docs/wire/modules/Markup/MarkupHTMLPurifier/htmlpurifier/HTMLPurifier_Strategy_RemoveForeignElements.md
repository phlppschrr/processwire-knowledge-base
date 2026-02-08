# HTMLPurifier_Strategy_RemoveForeignElements

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Removes all unrecognized tags from the list of tokens.

This strategy iterates through all the tokens and removes unrecognized
tokens. If a token is not recognized but a TagTransform is defined for
that element, the element will be transformed accordingly.
