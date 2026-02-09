# Modules

Source: `wire/core/Modules.php`

ProcessWire Modules

Loads and manages all runtime modules for ProcessWire


Loads and manages all modules in ProcessWire.
The `$modules` API variable is most commonly used for getting individual modules to use their API.
~~~~~
// Getting a module by name
$m = $modules->get('MarkupPagerNav');

// Getting a module by name (alternate)
$m = $modules->MarkupPagerNav;
~~~~~


Note that when iterating, find(), or calling any other method that returns module(s), excepting get(), a ModulePlaceholder may be
returned rather than a real Module. ModulePlaceholders are used in instances when the module may or may not be needed at runtime
in order to save resources. As a result, anything iterating through these Modules should check to make sure it's not a ModulePlaceholder
before using it. If it's a ModulePlaceholder, then the real Module can be instantiated/retrieved by $modules->get($className).

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [isValidItem()](method-isvaliditem.md)
Method: [get()](method-get.md)
Method: [get()](method-get.md)
Method: [getModule()](method-getmodule.md)
Method: [findByPrefix()](method-findbyprefix.md)
Method: [findByPrefix()](method-findbyprefix.md)
Method: [findByInfo()](method-findbyinfo.md)
Method: [getInstallable()](method-getinstallable.md)
Method: [isInstalled()](method-isinstalled.md)
Method: [install()](method-___install.md) (hookable)
Method: [delete()](method-___delete.md) (hookable)
Method: [uninstall()](method-___uninstall.md) (hookable)
Method: [getFlags()](method-getflags.md)
Method: [moduleInfoCache()](method-moduleinfocache.md)
Method: [getModuleID()](method-getmoduleid.md)
Method: [getModuleInfo()](method-getmoduleinfo.md)
Method: [getModuleInfoVerbose()](method-getmoduleinfoverbose.md)
Method: [getModuleInfoProperty()](method-getmoduleinfoproperty.md)
Method: [getConfig()](method-getconfig.md)
Method: [getConfig()](method-getconfig.md)
Method: [saveConfig()](method-___saveconfig.md) (hookable)
Method: [isConfigurable()](method-isconfigurable.md)
Method: [getModuleEditUrl()](method-getmoduleediturl.md)
Method: [getModuleInstallUrl()](method-getmoduleinstallurl.md)
Method: [isSingular()](method-issingular.md)
Method: [refresh()](method-___refresh.md) (hookable)
Method: [getRequiredBy()](method-getrequiredby.md)
Method: [setSubstitute()](method-setsubstitute.md)
Method: [getModuleFile()](method-getmodulefile.md)
Method: [getModuleFile()](method-getmodulefile.md)
Method: [getModuleLanguageFiles()](method-getmodulelanguagefiles.md)
Method: [__invoke()](method-__invoke.md)
Method: [__invoke()](method-__invoke.md)
Method: [memcache()](method-memcache.md)
Method: [memcache()](method-memcache.md)
Method: [__get()](method-__get.md)

Constants:
Const: [flagsSingular](const-flagssingular.md)
Const: [flagsAutoload](const-flagsautoload.md)
Const: [flagsDuplicate](const-flagsduplicate.md)
Const: [flagsConditional](const-flagsconditional.md)
Const: [flagsDisabled](const-flagsdisabled.md)
Const: [flagsNoUserConfig](const-flagsnouserconfig.md)
Const: [flagsNoFile](const-flagsnofile.md)
Const: [flagsSystemCache](const-flagssystemcache.md)
