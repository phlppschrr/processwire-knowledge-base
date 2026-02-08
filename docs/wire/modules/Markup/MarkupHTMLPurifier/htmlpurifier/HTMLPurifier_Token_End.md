# HTMLPurifier_Token_End

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Concrete end token class.

@warning This class accepts attributes even though end tags cannot. This
is for optimization reasons, as under normal circumstances, the Lexers
do not pass attributes.
