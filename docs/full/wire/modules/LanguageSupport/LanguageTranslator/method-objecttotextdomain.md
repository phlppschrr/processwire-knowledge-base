# LanguageTranslator::objectToTextdomain()

Source: `wire/modules/LanguageSupport/LanguageTranslator.php`

Given an object instance, return the resulting textdomain string

This is accomplished with PHP's ReflectionClass to determine the file where the class lives
and then convert that to a textdomain string. Once determined, we cache it so that we
don't have to do this again.

@param Wire|object $o

@return string
