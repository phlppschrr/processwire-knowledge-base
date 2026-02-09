# ProcessWire 3.0.84 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.84-core-updates/

## Sections


## ProcessWire 3.0.84 core updates

17 November 2017 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-3.0.84-core-updates/#comments)


## ProcessWire 3.0.84

This week we've got a newly updated ProcessWire installer, some nice upgrades to our user profile editor, along with more updates to the new Uikit admin theme that was recently added to the core.

*Please note that there may not be a blog post next week or the following week due to travel schedule here. *


### Updated ProcessWire installer

ProcessWire 3.0.84 comes with a newly updated installer. It's now using AdminThemeUikit styles so that it looks more up-to-date and consistent. A few other updates are also present:

Below is a short screencast demonstrating the updated installer.

Note the black bars at the top and bottom of the video are coming from the YouTube video player, and aren't part of the installer layout.


### AdminThemeUikit updates

With AdminThemeUikit added to the core [last week](/blog/posts/processwire-3.0.83-core-updates/), we've been fixing minor issues as they come up and adding enhancements to it.

By default this admin theme shows a user icon and your user name in the masthead, where you can access you profile among other navigation options. But now you can configure it to use various other icons, a user-specified image (avatar, like with AdminThemeReno) or use the Gravatar image.

You can also now configure the user label to show whatever you'd like, whether that be the user name, a predefined label, or some combination of fields available on the user template (like first and last name).

For those with very large screens, AdminThemeUikit has also been updated to support a maximum layout width setting, with the default value being 1600 pixels. That's still pretty large, so if you want to use a different max width setting, you can configure it in the AdminThemeUikit module settings, under the "Layout" fieldset.


### User profile updates

Last week we told you about some updates to our password field, as you'll see it in the user profile editor. This week we expanded upon that a bit and added some more security to it. Now, if you want to change your email address or your user name (from your user profile), it will require that you enter your current password, before it'll let you save the change. This adds yet more security.

In the paragraph above, I mentioned the ability to change your user name. This capability has not been available in the user profile screen before, but now it is available as an option, should you want it. Simply add it to your fields the user is allowed to edit in their user profile.

Speaking of fields in the user profile, you've always had to configure this from the ProcessProfile module settings. It was kind of a pain when you would have to add fields to the user template, then visit the ProcessProfile module settings to add them there too. Well now we've simplified that a bit. When you edit the "user" template, you now have a new field where you can simply check boxes next to which fields you want to be editable from the user profile screen.

That's all for this week. I'm going to be traveling part of next week and part of the week after, meaning I likely won't have a blog post (or core version update) for next week or the following week. Though we might have a guest post during that time. I hope that you all have a great weekend and week ahead. Be sure to keep in touch with the [ProcessWire Weekly](http://weekly.pw) for the latest ProcessWire news.
