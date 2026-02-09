# ProcessWire 3.0.56 and Uikit admin theme updates

Source: https://processwire.com/blog/posts/processwire-3.0.56-and-uikit-admin-theme-updates/

## Sections


## Core updates and Uikit admin theme additions

17 March 2017 by Ryan Cramer [ 25 Comments](/blog/posts/processwire-3.0.56-and-uikit-admin-theme-updates/#comments)


## ProcessWire 3.0.56

**[Download ProcessWire 3.0.56 at GitHub](https://github.com/processwire/processwire/tree/dev) ** (March 17, 2017)


### Core updates

This week we have a new version of ProcessWire on the dev branch that contains several additions and fixes. Here are a few highlights:


### Uikit admin theme updates

Work on the Uikit admin theme continues this week with the addition of sidebar support. For those that prefer most of the navigation to be in the sidebar rather than the masthead, you can now enable it as the default setting in the module configuration. You can also enable (or disable) it as a toggle in the user navigation.

The sidebars added this week are different from the offcanvas sidebar you may have seen in previous posts. Technically the navigation sidebar looks identical, but it's completely different in terms of how it works. I felt that sidebar navigation is more useful if it stays in the same place across page edits and other actions. To see what I mean, check out the screencast video below:

Something you'll also notice in that screencast is that there are actually two sidebars that can be revealed or hidden. These include the navigation sidebar and the page tree sidebar. By default, the navigation sidebar is visible, and the page tree sidebar is collapsed. Toggles can open or collapse either sidebar, and both are resizable. Notice that whatever you click in the sidebars loads in the main editor area, but the sidebars remain as they are. Meaning, you'll never lose your spot. Hopefully this will be a handy addition for many.

If you'd like to take it for a spin, this version of the Uikit admin theme can be downloaded from the [GitHub repo](https://github.com/ryancramerdesign/AdminThemeUikit) now, and you'll want to make sure you are running the latest core dev version as well (3.0.56).


### Live demo

You can also try out this update on our [Regular demo site](http://demo.processwire.com/regular/processwire/). Use the [admin login](http://demo.processwire.com/regular/processwire/) with username bloguser and password processwire3. Though before you go there, read the instructions below.

We don't have the sidebars enabled by default at present, so after logging in, hover the "bloguser" user menu and click the "Enable sidebars" link. After doing that you'll see the navigation sidebar appear on the left.

To enable the page tree sidebar, click the toggle that appears on the right side of the screen OR hover the "bloguser" user menu again and click "tree toggle". Please note that I've not yet tested out these admin theme updates in anything but Chrome so far, but let me know if you run into any trouble using it. If you've logged into this demo before, you may need to clear your browser cache (or use incognito mode) to ensure older assets aren't getting loaded.

That's it for this week. Have a great weekend and enjoy March 18 edition of the ProcessWire Weekly at [weekly.pw](http://weekly.pw).
