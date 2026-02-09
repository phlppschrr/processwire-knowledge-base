# ConfigurableModule

Source: `wire/core/ConfigurableModule.php`

ProcessWire ConfigurableModule and ConfigModule Interfaces

Provides the base interfaces required by modules.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/



About the ConfigurableModule interface
======================================
ConfigurableModule is an interface that indicates the module is configurable by providing
`__get()` and `__set()` methods for getting and setting config values. Modules implementing
this interface are assumed to also implement the `Module` interface.

The module must also provide one (1) of the following:

1. A `getModuleConfigInputfields([$data])` method (static or non-static); OR
2. A separate `ModuleName.config.php` file that just populates $config array; OR
3. A separate `ModuleNameConfig.php` file that contains a ModuleConfig class.

For more details about the above options, see the commented methods within
the interface.

When you use this as an interface, you MUST also use `Module` as an interface,
i.e. `class Something implements Module, ConfigurableModule`

Hint: Make your ConfigurableModule classes inherit from `WireData`, which already has
the get/set required methods.

You may optionally specify a handler method for configuration data: `setConfigData()`.
If present, it will be used. See commented function reference in the interface below.


About the ConfigModule interface (3.0.179+)
===========================================
This interface indicates the module can receive config settings, but is not
interactively configurable. Use this for modules where configuration will
only be managed from the API/code side. Config settings must be saved using
`$modules->saveConfig()`. Settings will be automatically populated to the module
when it is loaded, or may be retrieved with `$modules->getConfig()`.

Beyond the difference mentioned above, this interface is identical to the
ConfigurableModule interface except that it needs no getModuleConfigInputfields()
method nor will it use a configuration php or json file.

A module *must not* contain both the ConfigModule and ConfigurableModule interfaces
in their implements definition at the same time, so choose just one.

Methods:
Method: [__get()](method-__get.md)
Method: [__get()](method-__get.md)
Method: [__get()](method-__get.md)
Method: [__set()](method-__set.md)
