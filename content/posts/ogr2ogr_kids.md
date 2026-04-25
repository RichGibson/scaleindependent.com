---
title: OGR2OGR is still awesome
date: 2024-07-19
draft: false
categories:
  - Maps
tags:
  - maps
---

I downloaded the Sonoma County Parcel information. [From](https://gis-sonomacounty.hub.arcgis.com/datasets/sonomacounty::parcels-public-1) 

But it is too large to be useful, so let's use ogr2ogr to zoom in on their property.

lower left
 38.39
 -122.85

lower right 
 38.39
 -122.84

upper left
 38.39
 -122.85

upper right
 38.41
 -122.84

From the docs:



    ogr2ogr -clipsrc -122.85 38.39 -122.84 38.41 foo.geojson -f "GeoJSON" Sonoma_Parcels.geojson CDR_PARCEL_PUB_vw

Lookup...
https://socogis.sonomacounty.ca.gov/image/rest/services/Rasters/Ortho_SoCo_Pictometry_2021/ImageServer/exportImage??image?-13675284.022228574%2C4635749.148509143%2C-13675228.512076164%2C4635788.6800382435?102100?102100?10070%2C762?jpgpng?%7B%22ascending%22%3Atrue%2C%22mosaicMethod%22%3A%22esriMosaicNorthwest%22%2C%22mosaicOperation%22%3A%22MT_FIRST%22%7D
