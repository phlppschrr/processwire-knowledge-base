# HTMLPurifier_TokenFactory

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Factory for token generation.

@note Doing some benchmarking indicates that the new operator is much
      slower than the clone operator (even discounting the cost of the
      constructor).  This class is for that optimization.
      Other then that, there's not much point as we don't
      maintain parallel HTMLPurifier_Token hierarchies (the main reason why
      you'd want to use an abstract factory).
@todo Port DirectLex to use this

## createStart()

Creates a HTMLPurifier_Token_Start.
@param string $name Tag name
@param array $attr Associative array of attributes
@return HTMLPurifier_Token_Start Generated HTMLPurifier_Token_Start

## createEnd()

Creates a HTMLPurifier_Token_End.
@param string $name Tag name
@return HTMLPurifier_Token_End Generated HTMLPurifier_Token_End

## createEmpty()

Creates a HTMLPurifier_Token_Empty.
@param string $name Tag name
@param array $attr Associative array of attributes
@return HTMLPurifier_Token_Empty Generated HTMLPurifier_Token_Empty

## createText()

Creates a HTMLPurifier_Token_Text.
@param string $data Data of text token
@return HTMLPurifier_Token_Text Generated HTMLPurifier_Token_Text

## createComment()

Creates a HTMLPurifier_Token_Comment.
@param string $data Data of comment token
@return HTMLPurifier_Token_Comment Generated HTMLPurifier_Token_Comment
