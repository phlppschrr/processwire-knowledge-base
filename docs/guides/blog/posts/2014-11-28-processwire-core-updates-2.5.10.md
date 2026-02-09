# ProcessWire core updates (2.5.10)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.10/

## Sections


## ProcessWire core updates (2.5.10)

28 November 2014 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-core-updates-2.5.10/#comments)


### Introducing the ProcessWire Config Admin Module

This week a new configuration method was added that enables you to modify most of ProcessWire's configuration settings directly in the admin, rather than manually editing the /site/config.php file. This includes more than 30 configuration properties. The module that does this is called [ProcessWireConfig](https://github.com/ryancramerdesign/ProcessWireConfig). The core has been updated to support it with version 2.5.10.

There are a lot of situations where this module could be useful. Quickly enabling (or disabling) debug mode for example, or modifying your admin thumbnail image settings as another. But you can modify nearly any configuration setting. Further, you can also use the tool to define your own (more on that later).

The actual ProcessWireConfig module has not yet been merged into the core, though likely will be soon (if ProcessWire users think it will be useful on most sites). If you'd like to give it a try now, just grab ProcessWire 2.5.10 and install the module directly from the [ZIP](https://github.com/ryancramerdesign/ProcessWireConfig/archive/master.zip). Your feedback is appreciated.

The module works by parsing the /wire/config.php file directly to determine what properties are configurable. As a result, if a new configurable property is added to /wire/config.php, then ProcessWireConfig will also pick it up as editable.


### Define custom config properties

The module also parses your site's custom /site/config.php file looking for configurable properties. If it finds any, then you'll have a new "Site" tab appear when using this module. Each `$config` property has to be commented in phpdoc format in order to be recognized (with at least a `@var` line). There are also several custom attributes that can be added to provide more information about the configuration property to ProcessWireConfig. See the current [/wire/config.php](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/config.php) for several examples. Most of the custom attributes identified by ProcessWireConfig start with a `#` within the phpdoc.

**However, you don't have to use your /site/config.php file to define custom properties if you don't want to.** You can actually define them right on the ProcessWireConfig module configuration screen. Currently it's just limited to defining basic text and checkbox fields here, but we'll add more options if there's interest.
