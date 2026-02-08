# LanguageSupportInstall

Source: `wire/modules/LanguageSupport/LanguageSupportInstall.php`

Installer and uninstaller for LanguageSupport module

Split off into a seprate class/file because it's only needed once and
didn't want to keep all this code in the main module that's loaded every request.

ProcessWire 3.x, Copyright 2016 by Ryan Cramer
https://processwire.com

Groups:
Group: [other](group-other.md)

Methods:
Method: [install()](method-___install.md) (hookable)
Method: [addFilesFields()](method-addfilesfields.md)
Method: [uninstall()](method-___uninstall.md) (hookable)
Method: [getModuleConfigInputfields()](method-getmoduleconfiginputfields.md)
