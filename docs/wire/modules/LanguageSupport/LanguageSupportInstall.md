# LanguageSupportInstall

Source: `wire/modules/LanguageSupport/LanguageSupportInstall.php`

Installer and uninstaller for LanguageSupport module

Split off into a seprate class/file because it's only needed once and
didn't want to keep all this code in the main module that's loaded every request.

ProcessWire 3.x, Copyright 2016 by Ryan Cramer
https://processwire.com

## other

@method void install()

@method void uninstall()

## ___install()

Install the module and related modules

## addFilesFields()

@param Fieldgroup $fieldgroup

## ___uninstall()

Uninstall the module and related modules

## getModuleConfigInputfields()

@return InputfieldWrapper
