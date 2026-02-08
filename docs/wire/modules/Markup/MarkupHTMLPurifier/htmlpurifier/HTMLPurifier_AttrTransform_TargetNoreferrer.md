# HTMLPurifier_AttrTransform_TargetNoreferrer

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Adds rel="noreferrer" to any links which target a different window
than the current one.  This is used to prevent malicious websites
from silently replacing the original window, which could be used
to do phishing.
This transform is controlled by %HTML.TargetNoreferrer.
