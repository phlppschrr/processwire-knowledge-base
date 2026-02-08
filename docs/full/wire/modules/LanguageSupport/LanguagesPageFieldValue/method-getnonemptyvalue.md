# LanguagesPageFieldValue::getNonEmptyValue()

Source: `wire/modules/LanguageSupport/LanguagesPageFieldValue.php`

Get non-empty value in this order: current lang, default lang, other lang, failValue

@param string $failValue Value to use if we cannot find a non-empty value

@return string

@since 3.0.147
