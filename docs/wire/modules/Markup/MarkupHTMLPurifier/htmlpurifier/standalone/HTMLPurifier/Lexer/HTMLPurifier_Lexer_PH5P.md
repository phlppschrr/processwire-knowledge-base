# HTMLPurifier_Lexer_PH5P

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/Lexer/PH5P.php`

Experimental HTML5-based parser using Jeroen van der Meer's PH5P library.
Occupies space in the HTML5 pseudo-namespace, which may cause conflicts.

@note
   Recent changes to PHP's DOM extension have resulted in some fatal
   error conditions with the original version of PH5P. Pending changes,
   this lexer will punt to DirectLex if DOM throws an exception.
