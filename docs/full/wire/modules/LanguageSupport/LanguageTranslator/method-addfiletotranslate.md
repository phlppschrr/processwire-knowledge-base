# LanguageTranslator::addFileToTranslate()

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Given a source file to translate, create a new textdomain

@param string $filename Filename or textdomain that we will be translating, relative to site root.

@param bool $filenameIsTextdomain Specify true if $filename is a textdomain instead.

@param bool $save Whether to save the language

@return string|bool Returns textdomain string if successful, or false if not.
