# HTMLPurifier_AttrDef_CSS_URI

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates a URI in CSS syntax, which uses url('http://example.com')
@note While theoretically speaking a URI in a CSS document could
      be non-embedded, as of CSS2 there is no such usage so we're
      generalizing it. This may need to be changed in the future.
@warning Since HTMLPurifier_AttrDef_CSS blindly uses semicolons as
         the separator, you cannot put a literal semicolon in
         in the URI. Try percent encoding it, in that case.
