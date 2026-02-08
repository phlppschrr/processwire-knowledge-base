# HTMLPurifier_VarParser_Native

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

This variable parser uses PHP's internal code engine. Because it does
this, it can represent all inputs; however, it is dangerous and cannot
be used by users.

## evalExpression()

@param string $expr
@return mixed
@throws HTMLPurifier_VarParserException
