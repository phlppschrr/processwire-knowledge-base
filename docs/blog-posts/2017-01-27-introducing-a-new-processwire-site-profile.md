# Introducing a new ProcessWire site profile

Source: https://processwire.com/blog/posts/introducing-a-new-processwire-site-profile/

## Sections


## Introducing a new ProcessWire site profile

27 January 2017 by Ryan Cramer [ 9 Comments](/blog/posts/introducing-a-new-processwire-site-profile/#comments)


## Regular blog site profile

Consistent with the plans of introducing new site profiles this year, we've started work on the new site profile, and have the first version ready this week. This profile has a little bit in common with the default site profiles (included with the ProcessWire core) but aims to go quite a bit further in demonstrating various features of ProcessWire, several of which are version 3.x specific. It also aims to be a more useful starting point to build a site from.

The front-end of this profile uses the [Uikit 3](https://getuikit.com) library and includes a library of time-saving functions for working with Uikit 3. It stays with the default Uikit styles and we've tried to keep it as generic “Uikit” look as possible. That way, when someone wants to use it to build a site, there is very little they have to reverse engineer or remove. It also means that you should be able to plug in any Uikit 3 theme and have everything adjust perfectly to that theme. We currently have no theme being applied, so you just see the generic Uikit output.

- [Site profile live example](http://demo.processwire.com/regular/)
- [Site profile code at GitHub](https://github.com/ryancramerdesign/regular)


### Site profile highlights

This new site profile can be seen at [demo.processwire.com/regular/](http://demo.processwire.com/regular/). However, it's going to be more interesting if you grab a copy yourself and play with it. Right now it has its own [GitHub repo](https://github.com/ryancramerdesign/regular) where can download it. You'll also need a copy of ProcessWire 3.0.51 (the latest dev branch version). When this profile is fully complete, it will likely replace the “Classic” profile currently included in the PW core.


### Uikit 3 PHP function library

This new site profile also includes a [Uikit 3 PHP function library](https://github.com/ryancramerdesign/regular/blob/master/site-regular/templates/_uikit.php) that simplifies some of the more verbose bits of markup you might need when using Uikit 3 with ProcessWire. For instance, creating a recursive navigation tree using [uk-nav](https://getuikit.com/docs/nav), generating a [uk-navbar](https://getuikit.com/docs/navbar) with dropdowns, rendering [uk-pagination](https://getuikit.com/docs/pagination), or any number of other things. We find it helpful to have a few helper functions to avoid markup redundancy in multiple template files.

You'll see this library included with the new site profile, even though it doesn't itself need to use all of the functions that are included. But we're planning to continue to build upon and maintain this library of Uikit 3 helper functions, since we've already used many on a lot of other client projects. We've done the same with other CSS frameworks as well, though haven't released them as part of a site profile before. But since this site profile uses Uikit, I thought it made sense.

If you get a chance to check out this new site profile, please let us know what you think and if there's anything we can do to improve it or make it more useful. An important thing is to keep it basic enough that new users can understand it easily, and build from it easily. But the more we can find the balance between “simple”, “educational” and “useful”, the better.

I hope that you all have a great weekend and enjoy reading the ProcessWire Weekly. Thanks for reading!
