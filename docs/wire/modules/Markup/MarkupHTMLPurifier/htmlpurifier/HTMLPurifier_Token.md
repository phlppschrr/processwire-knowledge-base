# HTMLPurifier_Token

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Abstract base token class that all others inherit from.

## position()

Sets the position of the token in the source document.
@param int $l
@param int $c

## rawPosition()

Convenience function for DirectLex settings line/col position.
@param int $l
@param int $c

## __construct()

Converts a token into its corresponding node.
/
abstract public function toNode();
}





/**
Factory for token generation.

@note Doing some benchmarking indicates that the new operator is much
      slower than the clone operator (even discounting the cost of the
      constructor).  This class is for that optimization.
      Other then that, there's not much point as we don't
      maintain parallel HTMLPurifier_Token hierarchies (the main reason why
      you'd want to use an abstract factory).
@todo Port DirectLex to use this
/
class HTMLPurifier_TokenFactory
{
// p stands for prototype

/**
@type HTMLPurifier_Token_Start
/
private $p_start;

/**
@type HTMLPurifier_Token_End
/
private $p_end;

/**
@type HTMLPurifier_Token_Empty
/
private $p_empty;

/**
@type HTMLPurifier_Token_Text
/
private $p_text;

/**
@type HTMLPurifier_Token_Comment
/
private $p_comment;

/**
Generates blank prototypes for cloning.
