# Amazon AWS now powering processwire.com sites

Source: https://processwire.com/blog/posts/amazon-aws-now-powering-processwire.com-sites/

## Sections


## Amazon AWS now powering processwire.com sites

28 April 2017 by Ryan Cramer [ 2 Comments](/blog/posts/amazon-aws-now-powering-processwire.com-sites/#comments)


### ProcessWire Core status

Last week we released [ProcessWire 3.0.61 master](/blog/posts/processwire-3.0.61-master/) and so far there have been no major reports of any issues that I'm aware of. If you haven't yet upgraded to it, we recommend it as a nice upgrade from previous versions. For those wanting to use 2.8, we should soon have 2.8.61 ready to go as well. While there's no new core version of ProcessWire this week, we are back again working on the dev branch and we'll likely have a dev version ready next week.


### ProDrafts module status

I wanted to update those of you waiting for repeater support in [ProDrafts](/blog/categories/prodrafts/). I've been working on this for at least 2 hours every day for the last two weeks, and am continuing to make progress. The fundamentals of draft repeater support were in place months ago, but getting all the little details working, across all the different configurable settings, is taking awhile. This week I focused on the drafting of publish/un-publish and delete/undelete actions in repeaters, and now have that working. Repeaters and ProDrafts are the two most challenging modules I've built, so making them collaborate is perhaps one of the most challenging tasks I've worked on to date, but we're getting very close!


### ProcessWire.com hosting has moved to Amazon AWS

Last year about this time, we told you about our server [hosting move from ServInt to IBM Softlayer](/blog/posts/web-hosting-changes-and-server-upgrades/). Our experience with IBM Softlayer has been fantastic, the dedicated server is incredibly fast, and Softlayer has had zero outages. But with our 1-year sponsorship from them ending next month, it was time to find another hosting solution. The costs of paying for a top of the line dedicated server at IBM are beyond our resources as an open source project. However, for a business that needs enterprise level hardware and hosting, I can't think of a better place than Softlayer. They will no doubt remain first on my list for recommending to my clients.

As of this week, our hosting is now 100% powered by [AWS](https://aws.amazon.com/) (Amazon Web Services). This is all thanks to the skills of Jan VandenHengel of [Perago Solutions](http://peragosolutions.com). If you [remember](/blog/posts/web-hosting-changes-and-server-upgrades/), he's the guy who also managed our ServInt-to-Softlayer migration last year. This week he migrated us from Softlayer to Amazon, with zero downtime. Technically there was 10 minutes of forum downtime, but that was my fault–I plugged the wrong database host into IP.Board!

I'm happy to report that our new environment appears to be every bit as fast and reliable as our previous one. No longer are we on a dedicated server. Instead, we are now fully in the cloud, which is quite a change behind-the-scenes, even if completely invisible from the front-end. Here's an overview of what all of the processwire.com sites are running on now:

- [Amazon EC2](https://aws.amazon.com/ec2/) (Elastic Compute Cloud) using a t2 medium instance for the web servers.
- [Amazon RDS](https://aws.amazon.com/rds/) (Relational Database Service) t2 small instance, using MariaDB for database.
- [Amazon EBS](https://aws.amazon.com/ebs/) (Elastic Block Store) for backups with rolling daily volume snapshots.
- [Amazon Cloudfront CDN](https://aws.amazon.com/cloudfront/) (Content Delivery Network) for delivery of all static assets.*
- [Amazon Route53](https://aws.amazon.com/route53/) for all DNS services.*
- The latest stable versions of all server-side software, PHP (7), MariaDB, etc.

*We were already using Cloudfront CDN and Route53 DNS for the last year or so as well. But they served us so well that moving the rest to Amazon was an easy choice.

While that sounds like a lot of different services, this was all a relatively simple migration. Jan has moved hundreds of servers like this, and our environment was already his home, since he set it up last year. So we got on the phone yesterday and had everything moved a few hours later, a very smooth migration. Big thanks again to Jan VandenHengel for all that he's done to support the ProcessWire project. Also be sure to visit the ProcessWire-powered bike tours site that he runs called [Tripsite](https://www.tripsite.com).

I've also been working with Jan on a much larger scale, more complex migration for a client running a team of ProcessWire sites that talk to each other. In that case, we're using [Amazon ELB](https://aws.amazon.com/elasticloadbalancing/) (Elastic Load Balancing) which distributes traffic among multiple EC2 mirrored instances of the same site, providing pretty crazy redundancy, plus enabling it to scale to pretty much any traffic level easily. This setup also includes separate staging/development and production sites, separate ProcessWire content provider feeds and consumer instances, and much more. It really is fascinating seeing how all this works. It's especially satisfying to see all of our work in making ProcessWire so scalable being put to good use.

That's all for this week. Be sure to read the [ProcessWire Weekly](http://weekly.pw) tomorrow, and have a great weekend!
