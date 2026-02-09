# ProcessWire 3.0.83 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.83-core-updates/

## Sections


## ProcessWire 3.0.83 core updates

10 November 2017 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-3.0.83-core-updates/#comments)


## ProcessWire 3.0.83


### Password field updates

ProcessWire 3.0.83 improves the Password field by adding an option that requires the user to enter their existing password before they can change their password. This option is now enabled by default on the User Profile screen, though can be disabled by editing the settings for the "pass" field. By default, it is not enabled for other usages of the InputfieldPassword module, but you can enable it in the field settings, should you happen to be using this anywhere else.

Asking the user to enter their existing password before they can change their password increases security in some environments. For instance, lets say you work in an office and step away from your desk while you are logged in. This update ensures that another visitor to your desk can't change your password. There are plenty of other situations too, like forgetting to logout at someone else's computer. While not everyone necessarily needs this, I think it's a good thing to have enabled by default for our password field.


## UIkit 3 admin theme now in core

This week we added the [AdminThemeUikit](https://github.com/ryancramerdesign/AdminThemeUikit) module to the core. While we're still considering it beta (as is Uikit 3), I've felt for the last few weeks that it's every bit as solid as our other core admin themes in day-to-day use. In addition, the versions of AdminThemeUikit are lately tied to core versions. All in all, it seemed like a good time to merge it into the core!


### Installation

To start using it, grab the latest dev branch version (3.0.83) and click to Modules > Wire > Admin Theme. There you should see "Uikit 3" as an installable option. Click "install" and then review the options available on the configuration screen. Initially, the only one you may want to configure might be the "Use this admin theme for login screen?" option, and I recommend checking the box.

Once the module is installed, to start using it, you'll need to select it from your user profile (the same place where you would change your password). Choose Uikit 3 as your admin theme, and you are all set.


### Already have AdminThemeUikit installed?

If you've already been using this admin theme, then that's okay—ProcessWire can have two copies of the same module installed, no problem. But it does need to know which one you want to use. Click to Modules > Refresh. ProcessWire will tell you that it sees two copies of AdminThemeUikit, and gives you a link you can click on to configure which one of them you want to use. If you are making customizations to the admin theme (or planning on it), you may want to stick with your existing copy in /site/modules/. Otherwise, chances are you'll want to use the core version in /wire/modules/.


### AdminThemeUikit repository

The version of AdminThemeUikit included with the core is actually a little different than the one in the [AdminThemeUikit GitHub repository](https://github.com/ryancramerdesign/AdminThemeUikit). The core version is stripped down to remove a lot of things that aren't needed for production. Whereas the GitHub repo version has everything needed for development included. This is one case where we're going to continue to use the existing repository for ongoing development of this admin theme, and changes are migrated to the core once tested. If you want to submit an issue report for AdminThemeUikit, feel free to use either the dedicated [repository](https://github.com/ryancramerdesign/AdminThemeUikit), or the [processwire-issues](https://github.com/processwire/processwire-issues) repository.


### Uikit3-beta-30 to Uikit3-beta-34

The latest version of this admin theme upgrades from Uikit3 beta 30 to beta 34, and this update unexpectedly broke a lot of little things. I spent quite a bit of time this week going through and fixing them. They aren't bugs in Uikit, but rather changes in the way things like click events are watched. For instance, uk-tab in beta 34 seems to trigger from a click event on the `<li>` element, whereas beta 30 was from the `<a>` element. Little things that required some code adjustment on this side. I think it's all working now, but please keep an eye out for any issues and let us know if you spot anything that's not working.

Beyond upgrading the Uikit version to the latest beta, the latest AdminThemeUikit also contains continued optimizations and adjustments, taking care of increasingly smaller details and ensuring everything looks and works well.


### AdminThemeUikit and the ProcessWire installer

I'm currently working on an update to our installer that will use AdminThemeUikit for the installation, as well as make it the default selection for admin theme on new ProcessWire installations. I was hoping to have that in this week's version, but need a little more time to get it right.


### ProFields Table version updated for AdminThemeUikit support

With AdminThemeUikit now in the core, a new version of ProFields Table has also been released that plays (and looks) nice with the new admin theme. This was one of the few modules that initially didn't work all that well when it came to things like language tabs, but all that has been fixed. So if you are using both the AdminThemeUikit and FieldtypeTable modules together, you'll want to grab this update from the ProFields support board [download thread](/talk/topic/6413-profields-download/) (login required). Please note that AdminThemeUikit support requires that you are running ProcessWire core 3.0.83 (today's version) or newer.

A simple multi-language Table field now fully functional in AdminThemeUikit.
