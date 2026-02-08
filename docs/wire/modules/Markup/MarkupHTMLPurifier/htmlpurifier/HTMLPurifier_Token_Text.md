# HTMLPurifier_Token_Text

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Concrete text token class.

Text tokens comprise of regular parsed character data (PCDATA) and raw
character data (from the CDATA sections). Internally, their
data is parsed with all entities expanded. Surprisingly, the text token
does have a "tag name" called #PCDATA, which is how the DTD represents it
in permissible child nodes.
