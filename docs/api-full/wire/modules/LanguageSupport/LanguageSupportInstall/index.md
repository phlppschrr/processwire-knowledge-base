# LanguageSupportInstall

Source: `wire/modules/LanguageSupport/LanguageSupportInstall.php`

Inherits: `Wire`

## Summary

Installer and uninstaller for LanguageSupport module

Common methods:
- [`install()`](method-___install.md)
- [`addFilesFields()`](method-addfilesfields.md)
- [`uninstall()`](method-___uninstall.md)
- [`getModuleConfigInputfields()`](method-getmoduleconfiginputfields.md)

Groups:
Group: [other](group-other.md)

Split off into a seprate class/file because it's only needed once and
didn't want to keep all this code in the main module that's loaded every request.

## Methods
- [`install()`](method-___install.md) (hookable) Install the module and related modules
- [`addFilesFields(Fieldgroup $fieldgroup)`](method-addfilesfields.md)
- [`uninstall()`](method-___uninstall.md) (hookable) Uninstall the module and related modules
- [`getModuleConfigInputfields(): InputfieldWrapper`](method-getmoduleconfiginputfields.md)
