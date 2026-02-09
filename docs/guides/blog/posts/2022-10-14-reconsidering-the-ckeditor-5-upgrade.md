# Considering the CKEditor 4 to 5 upgrade

Source: https://processwire.com/blog/posts/reconsidering-the-ckeditor-5-upgrade/

## Sections


## Considering the CKEditor 4 to 5 upgrade

14 October 2022 by Ryan Cramer [ 1 Comment](/blog/posts/reconsidering-the-ckeditor-5-upgrade/#comments)

With 2023 fast approaching, and CKEditor 4 having an EOL in 2023, I'm starting to feel a little pressure to get a plan in place. But is the replacement (CKEditor 5) the best path forward?

This week I spent time experimenting more in-depth with CKEditor 5 and absorbing the [Migration from CKEditor 5 to CKEditor 4 guide](https://ckeditor.com/docs/ckeditor5/latest/installation/getting-started/migration-from-ckeditor-4.html) as well as other docs on their site.

As mentioned in a [previous weekly update](https://processwire.com/talk/topic/27376-weekly-update-%E2%80%93%C2%A022-july-2022/), CKEditor 5 seems like the most logical path forward, as we've been using CKEditor 4 since [ProcessWire 2.4.9](https://processwire.com/blog/posts/switch-to-ckeditor-new-default-site-profile-and-api-additions/) (July 2014), and we're all really familiar with it by now. Plus I have a lot of confidence in the company behind it. Since that time, CKEditor 4 has been a great fit for ProcessWire, and it's logical to assume the same would be true of version 5.

But the more I spend time learning about CKEditor 5, the more I begin to question if it's the best path forward for ProcessWire. You'll get a sense of that when you read the upgrade guide (linked above). No doubt it's a great editor, but is it a great editor for ProcessWire?


### Upgrade from CKEditor 4 to 5

CKEditor 5 is not an upgrade path for CKEditor 4... it's a completely different software. They have thrown out everything about CKEditor 4 and started over from scratch. So it's a rather tedious and difficult upgrade, because it's not really an upgrade, it's changing to another software. It means everyone using CKEditor 4 is also starting over with CKEditor 5. Statements like these (in their upgrade guide) also give me pause, though I appreciate their honesty:

An extremely important aspect to be remembered is that — because of the difference in features — the data produced with CKEditor 4 may not be compatible with CKEditor 5 (which may lead to data loss).

If we are forced to stop using CKEditor 4 due to it being EOL'd then what ProcessWire really needs is a drop-in replacement for CKEditor 4.

There is no “drop in” solution for migrating.

Oops, that's not very encouraging. Well, if we can't drop-in a replacement then we at least want something that is compatible with the output from CKEditor 4, so there's no potential for data loss or conversion of existing data. But alas, it wasn't mean to be.

Extensive analysis, data verification and tests should be performed on existing data. If necessary, you will need to develop conversion procedures to avoid data loss.

When ProcessWire someday migrates to another RTE, we don't want data loss or conversion to be something that you or your clients even need to think about during a ProcessWire upgrade. So that's a definite concern with CKEditor 5—that it's not making an attempt at being compatible with its previous version (or apparently even the output of its previous version).


### Benefits of version 5 for ProcessWire users

The next concern is whether version 5 provides any significant benefits to ProcessWire users, relative to version 4. I understand it's a necessary upgrade (due to the EOL) but what makes it also feel like a worthwhile one for ProcessWire users? I haven't found a clear answer.

Experimenting with the CKEditor 5 demos, they are very nice, but so is CKEditor 4, and I don't see anything that would really motivate the amount of work required for this upgrade on its own. When it comes to ProcessWire's context, CKE 5 seems to provide exactly what CKE 4 did, perhaps with a little bit nicer skin. So the main reason to upgrade seems to be that CKEditor 4 will no longer be developed. It kind of feels like a tax bill. Though I have to assume that in other contexts the CKEditor 5 upgrade is a welcome one, but I'm not sure it is for us.


### CKEditor has a stable business model

It appears that CKEditor 5 is an excellent platform for the company's commercial add-ons and services, and perhaps this is part of why they started over. In any case, I like that the company has a stable business model that enables them to maintain and support their open source project for the long term, and that's important. Beyond that, I don't see much crossover with ProcessWire's audience and the audience for those commercial add-ons/services. At least, I'm not aware of any ProcessWire users that need or use the commercial aspects of CKEditor. But it's a benefit either way.


### Separate builds in CKEditor 5

The next concern I ran into is that the Classic and Inline editors appear to be completely separate editors (separate builds) with their own [separate files/downloads](https://ckeditor.com/ckeditor-5/download/). So in order to maintain our existing Regular and Inline editors (both important for different reasons) we'd have to have 2 full copies of CKEditor... 10 megabytes rather than 5 megabytes. Though someone please let me know if I'm mistaken on this point (maybe their "superbuild" solves this?).

CKEditor 5 also has some other interesting editor modes (Balloon and Document) but I don't think we'd have much use for these in ProcessWire. And they too also appear to need separate copies of the source files, though I hope I'm wrong.


### Other considerations

The trickiest migration challenge to be faced may be related to custom plugins you have developed for CKEditor 4. Although their concept may stay the same, their implementation will certainly be different and will require rewriting them from scratch.

I consider long term consistency, compatibility and upgradeability to be sacred in PW. I don't fault CKEditor's approach, but it's just not compatible with PW's approach. You won't ever have to "rewrite from scratch" anything in or for ProcessWire, unless you want to.

For reasons mentioned here, I'm not sure that CKEditor 5 is the right replacement for CKEditor 4 in ProcessWire. I think it may still have a place in ProcessWire, but just not in the place that CKEditor 4 currently resides. Though I know for certain that CKEditor 5 is a great tool by a great company, and perhaps it would be a good choice if we were a brand new project without an existing installation base. But we have a large installation base that is used to simple and seamless upgrades, and I value that a lot.


### Is there a drop-in replacement for CKEditor 4?

So is there a drop-in replacement for CKEditor 4 that's on the level of CKEditor 5, has the same upsides, and feels like a real upgrade/improvement, but without any of the downsides mentioned above? Maybe that's not realistic, but that's what I'm hunting for. Actually, I'm not hunting for it anymore... I'm already using it as an Inputfield in ProcessWire here locally (both regular and inline), putting it through its paces, stress testing it with hundreds of instances, and throwing everything I can at it, and so far at least, it is putting a big smile on my face. It's not CKEditor, though has a lot in common with it. If testing continues to be a success, I think you'll be able to start using it in ProcessWire this month. Stay tuned.
