# HTMLPurifier_AttrTransform_SafeParam

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates name/value pairs in param tags to be used in safe objects. This
will only allow name values it recognizes, and pre-fill certain attributes
with required values.

@note
     This class only supports Flash. In the future, Quicktime support
     may be added.

@warning
     This class expects an injector to add the necessary parameters tags.
