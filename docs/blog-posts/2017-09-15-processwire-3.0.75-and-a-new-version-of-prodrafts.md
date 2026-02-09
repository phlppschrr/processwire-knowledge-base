# ProcessWire 3.0.75 and a new version of ProDrafts

Source: https://processwire.com/blog/posts/processwire-3.0.75-and-a-new-version-of-prodrafts/

## Sections


## ProcessWire 3.0.75 and a new version of ProDrafts

15 September 2017 by Ryan Cramer [ 6 Comments](/blog/posts/processwire-3.0.75-and-a-new-version-of-prodrafts/#comments)


### ProcessWire 3.0.75

A new version has been posted on the ProcessWire dev branch this week. Version 3.0.75 focuses mostly on covering GitHub issue reports, small bug fixes and tweaks. It is a recommended upgrade if you are currently using the ProcessWire dev branch. For more details on what's new in this version, see the [dev branch commit log](https://github.com/processwire/processwire/commits/dev) for September 1–15, 2017.

**It's been kind of a crazy week here.** On Monday the remains of Hurricane Irma went through here and brought some really crazy winds. It knocked down some trees, and with them all the electricity. As a result, we've had no power in our city this past week. Today (Friday) is the first day that things are finally back up and running and getting back into the office. The schools didn't have power either, so no school for the kids. It's been a nice week with the kids, but a challenging week to get work done.

I work off a notebook computer, so still managed to cover some ground, but don't have the new module I alluded to last week. So long as another hurricane doesn't roll through, that should be ready next week instead. However, we do have a new version of ProcessWire on the dev branch, and a new version of ProDrafts released! The rest of this post will cover the latest updates to ProDrafts.


## New version of ProDrafts

ProDrafts version 6 was released today in the ProDrafts board. This version contains a whole lot of updates, but the most notable are the addition of repeaters support and basic workflow support. We'll cover each in more detail below. (If you aren't yet familiar with ProDrafts, you can read [about ProDrafts here](/blog/categories/prodrafts/)).


### Repeaters in ProDrafts

This update has been a work in progress for quite a long time. Implementing repeater support in ProDrafts was a pretty challenging task. But I've spent a lot of time working with repeaters lately, building the repeaters page export/import functions in the core, and newly added Repeater derivative module (also in the core): [FieldtypeFieldsetPage](/blog/posts/processwire-3.0.74-adds-new-fieldsetpage-field-type/). Which is to say Repeaters are fresh on the mind, and it was a good time to finally finish the repeater support in ProDrafts.

Repeater support is enabled automatically if the core module FieldtypeRepeater is installed. Nested repeaters are also supported. Repeater support in ProDrafts includes support for these Fieldtypes:

- FieldtypeRepeater (core)
- FieldtypeFieldsetPage (core)
- FieldtypeRepeaterMatrix (ProFields)

The only caveats are that the Automatic Save feature of ProDrafts (and thus Live Preview feature) are not supported with repeaters. I've done a lot of testing here, but because there are a lot of potential combinations when it comes to repeaters, nesting and such, repeater support is considered beta at this point in time. If you are using ProDrafts and have wanted to use it with repeaters, please give it a try and let me know how it works for you. Because it's in beta, you'll want to test in non-production environments thoroughly before using in production environments.


### Workflow support in ProDrafts

Workflow support enables users without publish permission to submit their drafts for approval. Likewise it enables users with publish permission to approve or reject drafts that have been submitted for approval. It also includes notifications and messages for communication between parties.

This workflow support in ProDrafts was proposed by ProcessWire user Nikolaus Rademacher (wheelmaker24 in the forums) and is built largely to specifications he came up with. His experience is with large ProcessWire installations with sometimes thousands of users. His ideas and support were essential to this feature in ProDrafts.

To enable workflow support in ProDrafts v6, the [page-publish permission](/processwire/access/permissions/#page-publish) must be installed. This is a core permission that is not installed by default, but very simple to install. To install this permission, go to Access > Permissions > Add New, and check the box for the page-publish permission. Once installed, visit the ProDrafts module configuration page in the ProcessWire admin and click "Save". This will enable basic workflow support.

When drafts are submitted or rejected, the user can optionally add notes for the person that receives the request or rejection. These notes appear in a notification when the page is edited, and also appear in email notifications that ProDrafts sends.

After submitting a draft for approval, another user with page-publish permission to the submitted page can approve or reject the draft.

If a publisher decides to reject a draft, they also have the opportunity to provide notes on why the draft was rejected. The original submitter is notified and given the opportunity to make edits and re-submit or abandon the draft.

Note: this screenshot above shows the editor for a newly created page that has not yet been published. If it were a draft for an already published page, then it would look the same but with a little bit different button labels and options to compare to live version or abandon the draft.

Notifications can be sent automatically by email if the user has opted-in to receive them. This is done with checkbox fields when a user edits their profile. Three separate email templates are provided for these actions:

- Request publish of draft: sent to user(s) with publish permission to page.
- Approval of draft: sent to the user that requested publish and had their draft approved.
- Rejection of draft: sent to the user that requested publish and had their draft rejected.

Drafts awaiting approval/publish can also be reviewed from the Drafts page in the admin (Pages > Drafts). When there are pending drafts awaiting approval there is an "Awaiting Approval" tab that appears. It contains a list of all drafts awaiting approval.

This version of ProDrafts is now ready for download in the [ProDrafts board](/talk/topic/12195-prodrafts-download/) (subscriber login required). This is a beta version, so we do expect that there may be some bugs or issues to resolve. As a result, stick to using it only in a non-production environment until you've tested thoroughly that there aren't any issues for your installation and environment.

**Next week **we'll be back with a new module and a new version of ProcessWire on the dev branch. For the latest ProcessWire news and updates, read the [ProcessWire Weekly](http://weekly.pw). For me at least, there's nothing better than reading the ProcessWire Weekly with a cup of coffee first thing on a Saturday morning.
