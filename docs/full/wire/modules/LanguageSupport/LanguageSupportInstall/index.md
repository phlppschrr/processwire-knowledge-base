# LanguageSupportInstall

Source: `wire/modules/LanguageSupport/LanguageSupportInstall.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

Installer and uninstaller for LanguageSupport module

Split off into a seprate class/file because it's only needed once and
didn't want to keep all this code in the main module that's loaded every request.

Methods:
Method: [install()](method-___install.md) (hookable)
Method: [addFilesFields()](method-addfilesfields.md)
Method: [uninstall()](method-___uninstall.md) (hookable)
Method: [getModuleConfigInputfields()](method-getmoduleconfiginputfields.md)
