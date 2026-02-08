# HTMLPurifier_ChildDef_Chameleon

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Definition that uses different definitions depending on context.

The del and ins tags are notable because they allow different types of
elements depending on whether or not they're in a block or inline context.
Chameleon allows this behavior to happen by using two different
definitions depending on context.  While this somewhat generalized,
it is specifically intended for those two tags.

## validateChildren()

@param HTMLPurifier_Node[] $children
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool
