var groupTitle; 
var groupDesc;
var groupCont;
var groupTag;

groupTitle = '"Group name here"';
groupDesc = '"Group description here"';
groupCont = '"Group blog writing here"';
groupTag = 'Content by "group names here"';

$(document).ready(function () {
  groupTitle = $("#title").text(groupTitle);
  groupDesc = $("#desc").text(groupDesc);
  groupCont = $("#cont").text(groupCont);
  groupTag = $("#tag").text(groupTag);
  $('body').fadeIn(1000);
});
