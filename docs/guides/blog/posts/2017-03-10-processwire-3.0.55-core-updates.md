# ProcessWire 3.0.55 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.55-core-updates/

## Sections


## ProcessWire 3.0.55 core updates

10 March 2017 by Ryan Cramer [ 5 Comments](/blog/posts/processwire-3.0.55-core-updates/#comments)


## ProcessWire 3.0.55

This week we’ve got a new core version on the dev branch (3.0.55). This version has a whole bunch of fixes and adjustments, and is recommended if you’ve been running a prior dev branch version. For full details see the [commit log](https://github.com/processwire/processwire/commits/dev) for this week.


### Dropdown page tree

This new version also contains a handy new page tree integrated into the drop down navigation. This provides a useful shortcut for editing pages. It is something I’ve wanted there since the beginning, but never really was sure how to implement it. But after doing a lot of re-writing of navigation code along with the Uikit admin theme, it became fairly straightforward.

This dropdown page tree works with either the Default admin theme, or the new Uikit admin theme. It doesn’t work in the Reno admin theme at present because it is sidebar based and doesn’t use dropdown menus. Though we may still yet find a way to implement it there too.

These dropdown menus are a little better suited to the Uikit admin theme than the Default admin theme, mostly because the top navigation lives on the left rather than the right. This leaves more room for drilling down through the page tree. In either case, there are limitations to how far you can take it, though those limitations have to do with screen real estate rather than a technical limitation. While we are just showing 3 levels in the screenshots above, you can navigate as deep into the tree as your screen space will allow. The dropdown page tree is not a replacement for the main page tree, but it’s definitely a handy alternative for many cases.

Note that if you are trying to use it in a narrow window using the Default admin theme, you may run out of space easily, at which point jQuery UI starts rendering menus on top of one another. This is less likely to occur in the Uikit admin theme due to the navigation placement. So that’s just something to be aware of. Since a derivative of the Uikit admin theme will eventually be replacing the Default admin theme, I’m not too worried about that for the short term.

This navigable page tree is also implemented in the sidebar navigation of the Uikit admin theme. This one uses ajax-rendered uk-nav elements rather than ajax dropdowns:

If you’d like to try these new features out, grab the latest version of ProcessWire core (3.0.55) and optionally the latest [AdminThemeUikit](https://github.com/ryancramerdesign/AdminThemeUikit) (0.0.2). You can also try out the [live demo](http://demo.processwire.com/regular/processwire/), which is running these latest versions as well. Login with username “bloguser” and password “processwire3”.

In AdminThemeUikit, clicking the ProcessWire logo/mark now opens the off-canvas sidebar navigation, regardless of whether you are at the mobile responsive size or not. So if you want to test out that part of it, no need to make your browser window narrow anymore.

Thanks for reading. I hope that you all have a great weekend and enjoy reading the ProcessWire Weekly!
