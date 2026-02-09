# ProcessWire core updates (2.5.24)

Source: https://processwire.com/blog/posts/processwire-core-updates-2.5.24/

## Sections


## ProcessWire core updates (2.5.24)

27 March 2015 by Ryan Cramer [ 9 Comments](/blog/posts/processwire-core-updates-2.5.24/#comments)


### Minification

This week I saw the [Optical Circuit demo by 0x4015](http://www.pouet.net/prod.php?which=65125) and my mind was blown. This is a 4k demo… no, not a demo for 4k screens, an actual self executing demo (.exe file) that takes up just 4096 bytes (soundtrack included), and runs in real-time (if you download it rather than watching it on YouTube). But for your convenience, here it is on YouTube:

Just for comparison sake, the small ProcessWire logo that you see in the ProcessWire admin (or the one you see on this page in the upper left corner, *not* including the P mark) takes up about 4k. And those are already compressed images.

Seeing what could be done with 4096 bytes in that demo made me think the least we could do was to slim down our JS and CSS assets. This week support was added for all modules to have alternate minified assets in addition to the current non-minified assets. When the minified JS or CSS files are present, and debug mode is off, the minified versions get used instead of the non-minified versions.

For example, a file like [inputfields.js](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/templates-admin/scripts/inputfields.js) was getting well above 30k, and the [minified version](https://github.com/ryancramerdesign/ProcessWire/blob/dev/wire/templates-admin/scripts/inputfields.min.js) runs at about 13k. Similar results appear in dozens of JS files used throughout the system.

Minified versions of CSS files are also supported, but many are already minified (those that come from Sass origins at least), and there aren't many large CSS files in the system outside of the admin theme.

If you are a module developer, you may find it useful to include YourModule.min.js and YourModule.min.css files in addition to your YourModule.js and YourModule.css files. The core now recognizes and uses them when appropriate.


### Field dependencies upgrades

Field dependencies now support OR values, thanks to a PR from LostKobrakai. Where you could previously only specify `field=foo`, now you can specify `field=foo|bar` to say that "field" can contain "foo" or "bar" (or more OR conditions if you'd like). While we were in there, we went ahead and upgraded it so that you could also specify OR conditions for the field portion. Meaning, you could do: `this_field|that_field=value`. You can combine them too, though we're guessing not many will need to go that far.

Something else you can now do is match checkbox and radio button fields by their label. Previously you had to specify the page ID, and perhaps it's best that you still do that… But for quick needs or FormBuilder use, you may find it more convenient to say `page_field=Something` rather than `page_field=123`.

These field dependencies work in both the ProcessWire core and FormBuilder. They can be specified globally for a field, and/or contextually for a field in a specific template.


### Shift-click with multi-checkbox fields

Multi-checkbox fields now support shift-click to select a group of checkboxes at once, thanks to a PR from awt2542. In addition to working with InputfieldCheckboxes, it also works for checkboxes in any table (that uses MarkupAdminDataTable).


### More options for modal windows

We've had a couple of requests to provide more options for modal window configuration, beyond just the width/height offset for the 4 different modal sizes (small, medium, large, full). As a result, we've added the ability to specify additional configuration settings for each of those modal window sizes, including: draggable, resizable, time to reveal (show), time to close (hide), modal behavior, and more. See the [commit to config.php comments](https://github.com/ryancramerdesign/ProcessWire/commit/a0948b110941df53f7d823f3aeaa48498c875bc8) for more.


### ProcessUser dropdown upgrade

When you've got 100+ users in your system, the current dropdown menu for Access > Users isn't particularly useful, because you'll only see the first 100 users in alpha order. We've updated it so that when you've got more than 50 (or 100) users, it now defaults to showing a list of roles and a count of how many users are in that role. Click it and it takes you to a Lister showing those users. If you have fewer than that threshold number of users and still want that behavior, you can set the threshold quantity of users in the ProcessUser module settings.


### More PRs on the way

Special thanks this week to those that submitted pull requests and/or helped update the core: LostKobrakai, esrch, teppokoivula, diogo, boundaryfunctions, adrianbj, awt2542, and anyone else I've forgotten to mention here. We've also got many more pull requests to get through in the coming weeks, thank you coding with PW!
