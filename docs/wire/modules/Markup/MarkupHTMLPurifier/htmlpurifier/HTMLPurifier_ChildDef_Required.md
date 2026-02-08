# HTMLPurifier_ChildDef_Required

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Definition that allows a set of elements, but disallows empty children.

## validateChildren()

@type bool
/
public $allow_empty = false;

/**
@type string
/
public $type = 'required';

/**
@param array $children
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return array
