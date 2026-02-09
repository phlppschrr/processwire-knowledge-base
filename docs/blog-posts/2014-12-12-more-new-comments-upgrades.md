# More New Comments Upgrades

Source: https://processwire.com/blog/posts/more-new-comments-upgrades/

## Sections


## More New Comments Upgrades

12 December 2014 by Ryan Cramer [ 15 Comments](/blog/posts/more-new-comments-upgrades/#comments)

Last week [we told you about major upgrades](/blog/posts/core-comments-upgrades/) we're making to ProcessWire's comments system thanks to the support of [update AG](http://update.ch/). This week we continued those upgrades (on the dev branch) and have added the following:


### Admin approval of comments from email

Previously whenever a new comment was posted the administrator would get an email notification. But it wasn't anything more than a notification. If the comment needed action, such as approval or deletion, then they would have to go and login to the site and take care of it. That was kind of a hassle.

Now the admin notification emails actually let you approve comments directly from a link in the email. Further, you don't have to be logged in to the site to make it happen. Each comment now incudes a very long random password/code of sorts that makes this possible, and that code is bundled into the URL in the email so that the action can be performed without doing anything more than clicking on it. Note that it's a one-time action– once used, the comment can no longer be modified without being logged-in.

This also makes it easy to approve comments on-the-go, as you could do it from your mobile device as easily as from your desktop. When a notification email arrives, it indicates the current status of the comment. If the status is pending then you'll have an action link to approve the comment. Once approved, the comment appears on the site. If the status is approved already, then you'll have an action link to label the comment as spam, which removes it from the site.


### New admin notification email options

Previously the comments field settings let you defined one or more email addresses that could receive notifications of new comments. Typically this would be the administrator email. With the latest update, you can now specify not only emails, but user names or page fields (where it should pull an email address from). This enables it to determine what email the notification should go to at the time the comment is posted.

An example of where this is useful is in our modules directory. Module authors previously had no way of knowing when a new comment was posted short of regularly checking back in on the page. The result is that a lot of questions/comments posted on a module page go unanswered. But with the latest core update, I can specify that I want it to pull the admin notification email from the page it was submitted on. This sends the notification email to the module author, rather than me. It also enables the module author to approve (or label as spam) comments for their own module page. *Note: I haven't actually installed this on the modules directory just yet, but will be shortly.*


### New user notification emails

Any visitors that post comments can now opt-in to receive email notifications when someone has replied to their comment, or when any new comment is posted on the page. This should help greatly with keeping conversations active. For an example, take a look at the comments on this page. You'll see a new select box that lets you choose your notification preference.

Note that notifications don't get sent out until the comment is approved. This ensures your server won't be spamming people. Each notification email also includes a "disable notifications" link that lets the user later opt-out of receiving comments if they want to.

Something that I think we need, but isn't yet there is a double opt-in for this. While it may not be technically necessary, given that a new visitor typically has to go through an approval before any notifications are sent, I still think it's a good idea. So that's something I've setup locally, but just haven't yet pushed to dev. When the visitor indicates they want to receive notifications, they get sent an opt-in email asking them to confirm it, and notifications don't get sent until they do.

Currently the notification emails do not include the actual comment itself for a few reasons. First is just a matter of security and spam protection. If a user's first comment is approved, then their later comments are auto-approved (a config option you have in your field settings, which is the most common option). That means email notifications go out immediately. It works the same way in WordPress, and spammers are aware of this. They will usually post some comment that says something like "thank you for this helpful information" or something friendly to get you to approve it (don't do it!). Following that approval, they can post their spam. If we're sending comments in email, then at that point the email notifications would themselves be spam. That's something I'd like to avoid. Next is the issue of users replying to the emails rather than going to the page where the comment exists. Replying to the email doesn't make it appear in the comments, so we want to prevent the chance that the user will do that. Lastly, we want people to interact with your site (increasing your pageviews), not absorb everything in their email. I recognize there may still be value in bundling the comment directly in the email, so if need be we can always make it a setting.

*Note that user notifications are disabled by default. You have to enable these in your comments field settings. *


### Other comments updates

- Re-do of the comments field settings screen (Settings > Fields > comments).
- You can now set the notification "from" email address from the comments field settings.
- Remembering a user's name/email from request-to-request is now handled fully in javascript with cookies, rather than with PHP sessions. This is much more cache friendly if you are using ProCache or template cache.
- Notification emails are now HTML rather than plain text. Though a plain text version is still bundled in.

Next week we'll be adding support for up/down votes for each comment. We'll also be adding double opt-in for email notifications.

There are a lot of updates here to the comments system, and they may not be fully ready for a production environment. As a result, if you are using comments on your site, you may want to give it another week or two before upgrading to the latest version of FieldtypeComments present on the dev branch. Or if you want to run the latest dev branch, you can give it a try (and let us know how it works for you) or just replace /wire/modules/Fieldtype/FieldtypeComments/ with the FieldtypeComments from the stable branch.
