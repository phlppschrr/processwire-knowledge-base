# HTMLPurifier_AttrValidator

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates the attributes of a token. Doesn't manage required attributes
very well. The only reason we factored this out was because RemoveForeignElements
also needed it besides ValidateAttributes.
