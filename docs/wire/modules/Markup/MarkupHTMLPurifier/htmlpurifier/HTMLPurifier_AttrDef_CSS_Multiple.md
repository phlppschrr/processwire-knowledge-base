# HTMLPurifier_AttrDef_CSS_Multiple

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Framework class for strings that involve multiple values.

Certain CSS properties such as border-width and margin allow multiple
lengths to be specified.  This class can take a vanilla border-width
definition and multiply it, usually into a max of four.

@note Even though the CSS specification isn't clear about it, inherit
      can only be used alone: it will never manifest as part of a multi
      shorthand declaration.  Thus, this class does not allow inherit.

## validate()

@param string $string
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
