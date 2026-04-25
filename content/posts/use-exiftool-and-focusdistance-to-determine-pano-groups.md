---
title: Use ExifTool and FocusDistance to determine pano groups
date: 2015-01-07T13:03:38-08:00
draft: false
categories:
  - ScaleIndependent
---

When I take portraits I sometimes forget to keep track of where I am starting...

I can make several attempts, starting over at the eyes, or chin, or wherever. So looking at the resulting images is just a jumble!

Can I use focus distance to group the results?
<!--more-->


Answer: Maybe.
exiftools
exiftool -ApproximateFocusDistance *

That provides the approximate focus distances (I think in Feet). So if I make 'major' changes in camera position (more than 1 inch?) I should be able to group the images based on focus distances breaks.

Probably easier is to take a throwaway image of a blank subject to separate the images!	