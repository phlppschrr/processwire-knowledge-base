# HTMLPurifier_AttrTransform_TargetBlank

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Adds target="blank" to all outbound links.  This transform is
only attached if Attr.TargetBlank is TRUE.  This works regardless
of whether or not Attr.AllowedFrameTargets
