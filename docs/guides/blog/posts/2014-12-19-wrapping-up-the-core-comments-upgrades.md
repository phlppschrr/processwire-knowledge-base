# Wrapping up the comments upgrades

Source: https://processwire.com/blog/posts/wrapping-up-the-core-comments-upgrades/

## Sections


## Wrapping up the comments upgrades

19 December 2014 by Ryan Cramer [ 7 Comments](/blog/posts/wrapping-up-the-core-comments-upgrades/#comments)


## ProcessWire 2.5.11

Now in week 3 of the core comments upgrades, almost all the planned functionality is now in place and available for use on the dev branch. Here is what was added this week:


### Comment Upvoting and Downvoting

Take a look at [last week's](/blog/posts/more-new-comments-upgrades/) post and you'll see in the comments section that each comment now includes a quantity of upvotes and downvotes. Upvotes/downvotes are fairly common in commenting systems now, and they enable people to express likes and dislikes without themselves writing a comment. They are also helpful for other visitors to see what's been liked and not liked by other users. Here's a screenshot below. Note our season-appropriate color scheme for upvotes and downvotes.

**How does it work?** When you click the up or down arrows (for upvotes or downvotes) it fires off an ajax request to the server and saves your vote with the comment. You do not need to be logged in. The vote is tied to your IP address for 1-hour, thus preventing more of the same vote for the same comment, for a short while. After one hour, the IP address connection is deleted, but the vote remains.

This upvoting/downvoting feature is not turned on by default. To enable it, you'll want to do so from your comments field settings (Setup > Fields > [comments field] > Details). You can also choose to just use upvotes (with no downvotes) if that is your preference.


### New Comments Manager Module (ProcessCommentsManager)

Also added to the core this week is the Comments Manager module. You might have used the [ProcessLatestComments](http://modules.processwire.com/modules/process-latest-comments/) module sometime in the past, and the Comments Manager is the newest version of that. I decided to bundle this module into the core because if you are using comments field(s) on your site, then there's a 99% chance you'll also want to use the Comments Manager. Since the feature set available in the Comments Manager is now closely tied into the feature set of the Comments Fieldtype, it makes a lot more sense for the two to be distributed and installed together. They will also be updated together from this point forward.

If you've used ProcessLatestComments in the past, you'll already be familiar with Comments Manager. The main differences are that the interface has been improved quite a bit, and that it supports the new ProcessWire 2.5.10+ comments features we've been building for the last 3 weeks. Meaning, the Comments Manager has been largely re-written.

To install, make sure you are running the latest PW dev branch (2.5.11+) and go to Modules > Refresh. Then go to Modules > Core > Process > Comments, and click Install. You should see the new Comments option on your admin Setup menu. If you've already got ProcessLatestComments installed, you'll want to uninstall it, since you won't need it anymore.

Here's a screenshot from the new Comments Manager module (I blurred out IP addresss and some names and emails):


### Other Updates

There were actually several other updates both in the core and to FieldtypeComments–some major and some not so major–but none that are likely to be interesting enough to capture your attention here. But if you are still interested, follow our [dev branch commit log](https://github.com/ryancramerdesign/ProcessWire/commits/dev).

If you are using the new comments features that were pushed last week, be sure to grab the latest version of the dev branch as there have been several tweaks and bug fixes that you'll want in your comments system.

Next week we'll be getting back to the bigger picture of the core and working on our ProcessWire 2.6+ and ProcessWire 3.0 roadmap planning for next year. 2015 is going to be a great year for ProcessWire!
