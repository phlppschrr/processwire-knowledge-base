# Uikit 3 admin theme updates

Source: https://processwire.com/blog/posts/uikit-3-admin-theme-updates/

## Sections


## Uikit 3 admin theme updates

29 September 2017 by Ryan Cramer [ 7 Comments](/blog/posts/uikit-3-admin-theme-updates/#comments)


## ProcessWire 3.0.77

While there's a new version on the dev branch this week, it contains mostly minor updates that corresponded to some updates in the *AdminThemeUikit* module. In last week's post, I mentioned the following with regard to that admin theme module:

Now we're going to start with building a version that feels like part of the AdminThemeReno family.

…and that's how things went. This week I've got another update to the *AdminThemeUikit* admin theme that inherits the colors and several design details from Tom Reno's fantastic *AdminThemeReno*. Though so far it's just an interpretation of his theme, and we're looking forward to hopefully getting Tom involved in designing/developing the new admin themes too. In this post we'll take a closer look at several screenshots. *AdminThemeUikit* is starting to look more like ProcessWire and less like Uikit 3. The folks building Uikit 3 have really done a nice job in making it themeable and flexible.

While we've still got more work to do, it is getting to the point where it's starting to feel like home and nice to use. I'm now using it instead of *AdminThemeDefault*, in part because I just like using it (now that it's got some color), but also because it helps me to spot little issues or things left to cover in development. I'd encourage you to [download](https://github.com/ryancramerdesign/AdminThemeUikit) and try it out too, and let us know how it works for you. I've already got a list of things to cover, so expect to see lots more detail work over the next week as well.

One of the biggest differences between *AdminThemeReno* and *AdminThemeDefault* has been that *AdminThemeReno* has always been sidebar-navigation based, and *AdminThemeDefault* has always been dropdown-navigation based. While *AdminThemeUikit* supports sidebars for page tree and offcanvas navigation, I'd say it's more of a masthead-based navigation theme, as I think this covers the capabilities of multi-level nested navigation in Process modules a little better. When it comes to navigation, *AdminThemeUikit* is kind of a hybrid between *AdminThemeReno* and *AdminThemeDefault*.

Part of the intention with developing this Reno-color-based theme was to show how one could theme the stock *AdminThemeUikit*, as I know there are others interested in working with this admin theme. The entirety of what differentiates the stock Uikit admin theme from the RenoKit theme is all in this file: [pw-theme-reno.less](https://github.com/ryancramerdesign/AdminThemeUikit/blob/master/uikit/custom/pw/pw-theme-reno.less). If you remove that file from the bottom of the [_import.less](https://github.com/ryancramerdesign/AdminThemeUikit/blob/master/uikit/custom/pw/_import.less) file, then it returns to the stock Uikit theme. That's all there is to it.


### Screenshots

The login screen:

The main page list (tree) screen, with a dropdown menu open:

Results from the admin search feature:

Example from the page editor, editing a blog post from a few weeks ago:

Same thing as above, but this time demonstrating the datepicker (style from AdminThemeReno):

This screenshot shows the offcanvas sidebar, which can be opened by clicking the ProcessWire logo. This offcanvas sidebar is capable of doing everything that the top/primary navigation dropdowns can do, as they both use the same ajax-driven source for data. In this screenshot, just the user “Ryan” navigation item is open:

This screenshot demonstrates the page editor with language tabs active. Note that unpopulated languages appear in a muted text, like RU and NL in the Headline field below.

The admin theme also supports a 2-column mode where the page tree is in the left column, and everything else in the right.

Example of a 3rd party module in the admin theme (ProCache). Note how the active tab color mirrors the color of the active tab content:

Another example of a 3rd party module in this admin theme. This is the one I use to distribute the ProcessWire Weekly to our email subscribers every week:

Below you'll see an example of message, warning and error notifications:

This is what the page editor looks like when using ProDrafts and editing a draft:
