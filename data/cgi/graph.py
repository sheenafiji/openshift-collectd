#!/usr/bin/env python

import os
import re

print "Content-type: text/html"

print """
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
  <html>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.0/jquery.min.js"></script>
    <script src="../js/javascriptrrd.wlibs.js" language="javascript"></script>
    <body>
      <form>
        <select id="graphs" name="graph"></select>
      </form>

      <div id="mygraph"></div>
 
    </body>
    <script>
      var rrdFiles=[];
"""

for root, subFolders, files in os.walk(".",topdown=True):
  for file in files:
    if re.search('rrd',file):
      print "rrdFiles.push('"+root+"/"+file+"');"

print """

      rrdFiles.forEach(function(file){
        $("#graphs").append("<option value='"+file+"'>"+file+"</option>");
      }); 


      $("#graphs").change(function(){
        var graph  =($('#graphs').find(":selected").text());
        var f = new rrdFlotAsync("mygraph","../"+graph);
      });


    </script>
  </html>
""" 
