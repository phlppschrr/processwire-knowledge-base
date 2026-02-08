# HTMLPurifier_AttrTransform_ImgRequired

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Transform that supplies default values for the src and alt attributes
in img tags, as well as prevents the img tag from being removed
because of a missing alt tag. This needs to be registered as both
a pre and post attribute transform.
