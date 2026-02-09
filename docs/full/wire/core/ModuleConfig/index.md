# ModuleConfig

Source: `wire/core/ModuleConfig.php`

Inherits: `WireData`

ModuleConfig class

Serves as the base for classes dedicated to configuring modules.

Descending class name should follow the format: [ModuleName]Config and file [ModuleName]Config.php
located in the same directory as the module it is configuring.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct()`](method-__construct.md) Use the construct method if you are defining your module config fields as an array
- [`getDefaults(): array`](method-getdefaults.md) Return associative array of property name => default value
- [`getInputfields(): InputfieldWrapper`](method-getinputfields.md) Return an InputfieldWrapper of Inputfields necessary to configure this module
- [`add(array $a): self`](method-add.md) Set an array that defines Inputfields
- [`identifyDefaults(array $a): array`](method-identifydefaults.md) Identify defaults from the given Inputfield definition array (internal use)
