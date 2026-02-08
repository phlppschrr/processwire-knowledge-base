# HTMLPurifier_Injector_AutoParagraph

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Injector that auto paragraphs text in the root node based on
double-spacing.
@todo Ensure all states are unit tested, including variations as well.
@todo Make a graph of the flow control for this Injector.

## handleText()

@param HTMLPurifier_Token_Text $token

## handleElement()

@param HTMLPurifier_Token $token

## _splitText()

Splits up a text in paragraph tokens and appends them
to the result stream that will replace the original
@param string $data String text data that will be processed
   into paragraphs
@param HTMLPurifier_Token[] $result Reference to array of tokens that the
   tags will be appended onto

## _isInline()

Returns true if passed token is inline (and, ergo, allowed in
paragraph tags)
@param HTMLPurifier_Token $token
@return bool

## _pLookAhead()

Looks ahead in the token list and determines whether or not we need
to insert a <p> tag.
@return bool

## _checkNeedsP()

Determines if a particular token requires an earlier inline token
to get a paragraph. This should be used with _forwardUntilEndToken
@param HTMLPurifier_Token $current
@return bool
