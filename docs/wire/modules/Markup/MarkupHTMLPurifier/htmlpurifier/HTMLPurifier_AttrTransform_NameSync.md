# HTMLPurifier_AttrTransform_NameSync

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Post-transform that performs validation to the name attribute; if
it is present with an equivalent id attribute, it is passed through;
otherwise validation is performed.
