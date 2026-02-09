# ProcessWire 3.0.54 and Uikit 3 admin theme

Source: https://processwire.com/blog/posts/processwire-3.0.54-and-adminthemeuikit/

## Sections


## ProcessWire 3.0.54 and Uikit 3 admin theme

3 March 2017 by Ryan Cramer [ 10 Comments](/blog/posts/processwire-3.0.54-and-adminthemeuikit/#comments)

Last week's post indicated we may have the first [beta] version of the Uikit admin theme ready, and I’m glad to report that is the case. In this post, we’ll describe what’s new, how to install it, and how to develop with it.


## Introduction

If you’ve been following the last couple weeks of blog posts, you may already be familiar with some of what’s in this admin theme. This is a framework for a Uikit-based admin theme, and not what we’d consider a fully designed admin theme at this point. Unlike previous admin themes, the goal with this one is to put something together that others can build from and collaborate on. However, the admin theme is still quite nice to use even in its stock-Uikit themed state. And as minimal as it is, in several ways I think it’s a nice upgrade from the current default admin theme. If you are interested in testing in a non-production environment, it’s worth the download, even if you have no interest in contributing to the development of it at this stage.

Like last week, several core updates this week were related to supporting this new admin theme framework. As a result, if you want to take this Uikit admin theme for a spin, you’ll need [ProcessWire dev](https://github.com/processwire/processwire/tree/dev) version 3.0.54. Once you’ve got that, you can install the [AdminThemeUikit](https://github.com/ryancramerdesign/AdminThemeUikit) module. You install this module in much the same way you would install any other module, but we’ll quickly cover it here too.


### Installing AdminThemeUikit

Don’t attempt to install AdminThemeUikit on ProcessWire versions prior to 3.0.54 or you will get a fatal error that won’t go away until you physically remove the module files. This is because this admin theme extends a class that is new to ProcessWire 3.0.54.

The module is currently hosted in the [AdminThemeUikit GitHub repository](https://github.com/ryancramerdesign/AdminThemeUikit), and not in the PW modules directory. You’ll want to download or clone it and place the contents in /site/modules/AdminThemeUikit/. Following that, you’ll want to click Modules > Refresh in your admin, and then click Install for this module.

Upon installation, you’ll have a configuration screen for various settings of the module. I recommend leaving them alone for now, and coming back to it later once you get a feel for the theme. So the first thing you should do is click over to your user profile and change the admin theme to “Uikit admin theme”.


## What’s new

This week a lot of pre-beta-release finishing touches went in place. Many of which make the theme something that you can use quite effectively, rather than just preview or look at. Most of the work was small stuff, like styling specific Inputfield modules and fixing various issues. But here’s a few highlights on what’s been added this week:


### Upgraded sidebar

While this theme uses a top primary navigation, it uses an off canvas sidebar navigation when used at mobile sizes. A lot of work was put into making the sidebar navigation every bit as capable as the masthead navigation. Meaning, it now supports the module actions and ajax-loaded item lists (templates, fields, modules, etc.) that the masthead-based primary navigation does. But rather than using dropdown menus like the masthead does, it uses nested and ajax-loaded Uikit uk-nav elements. Granted, the styling needs some work, but the functionality is now built in.

Part of the intention with supporting all this in the offcanvas sidebar is to provide a good solution for admin themes that opt to use a sidebar (rather than masthead) for primary navigation. So now we've got a sidebar solution that is ready-to-use and style, whether just used as a mobile offcanvas navigation, or for an actual sidebar navigation.


### Theme configuration

You can now configure a few of the Inputfield style options directly in the AdminThemeUikit module settings. In doing this, you can affect all Inputfields of a specific type. For instance, the default configuration has all *InputfieldCKEditor* fields at 100% width using the borderless style. These settings, as well as colors, can also be configured on a field-by-field basis under Setup > Fields > [any field] > Input > Visibility > Uikit admin theme settings.


### Setting which admin theme is used for the login screen

One of the features added to our new [AdminThemeFramework](https://github.com/processwire/processwire/blob/dev/wire/core/AdminThemeFramework.php) class in ProcessWire is a configuration setting that lets you specify an admin theme should be used for the login page. This setting is automatically available to any admin themes extending the *AdminThemeFramework* class (as *AdminThemeUikit* does). See also the first setting in the module configuration screenshot before this one.


## What’s left

While I think most of the core elements are accounted for by this admin theme at this point, I have no doubt there will be some things that don’t translate yet. Meaning, there’s still more work to do. For example, I’ve not yet started working with this admin theme and the *SystemNotifications* module, and there’s a couple core *Inputfield* types (like *PageTable* and *Options*) that I’ve not yet spent much time testing with. Though Repeaters and File fields *are* well accounted for at this point, and these are perhaps the most complex, so it's good to have them working well already.

Lots of testing is also a big part of what’s left. Currently I’ve focused exclusively just on testing with core modules, so one of the next steps is to see how everything works with various 3rd party modules, including Pro modules. It may be that we need to make many adjustments to support the broader context of modules. Browser testing is another aspect that remains, as I’ve worked exclusively in Chrome thus far. I don’t yet know how well our admin theme framework will fare in some of the other browsers, though am cautiously optimistic that we likely won’t have many challenges there. Using a framework like Uikit can help a lot in abstracting away browser-specific issues.

There have been several suggestions and requests for features in the comments to previous blog posts on this topic. There are lots of good ideas, and we appreciate all the interest and feedback. In the short term, rather than get into new feature development, we’re trying to focus more on the foundations of the framework and getting things right there. The hope is that with a strong admin theme framework, others will be able to participate in helping to develop ground breaking new features in the admin theme. While there are certainly some nice new features available in the framework already, for the most part we’re focused on eventually replacing the Default admin theme, and thus focusing on a feature set that is familiar to that context.


## Development

In the [README file](https://github.com/ryancramerdesign/AdminThemeUikit/blob/master/README.md) for this admin theme, we’ve covered some details on how you can work with development of this admin theme. Rather than repeat what was said there, we encourage you to read that file if you are interested in the development side of this. I’ll be adding more to it as we go too. It’s also good to look at the PHP files that come with this admin theme, particularly the [AdminThemeUikit.module](https://github.com/ryancramerdesign/AdminThemeUikit/blob/master/AdminThemeUikit.module) file, [init.php](https://github.com/ryancramerdesign/AdminThemeUikit/blob/master/init.php), [default.php](https://github.com/ryancramerdesign/AdminThemeUikit/blob/master/default.php) and the files included from default.php. If you ever looked at or worked with past admin themes, you’ll see things have come a long way and should be a lot more clear and organized than before.

I imagine that some admin themes will be completely front-end CSS focused, leaving all the PHP files essentially as they are, and focusing instead on theming via the Uikit theme located in .less files in [/uikit/custom/pw/](https://github.com/ryancramerdesign/AdminThemeUikit/tree/master/uikit/custom/pw). As you want to go further outside Uikit’s default styles, you’ll add more .less files that correspond to the [Uikit component files](https://github.com/ryancramerdesign/AdminThemeUikit/tree/master/uikit/src/less/components). For that side of it you’ll want to refer to [Uikit’s instructions](https://getuikit.com/docs/less).

For admin themes that pursue a different layout, such as a sidebar-based theme like Reno, you’ll likely get into some markup changes in the default.php file (and files included from it), and perhaps more. I’m here to help and answer any questions that come up.

I’m excited about the potential of collaboration here and what results we may come up with. Thanks for reading, have a great weekend and enjoy reading the [ProcessWire Weekly](http://weekly.pw) too!
