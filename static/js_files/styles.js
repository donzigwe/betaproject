
function popitup(url) {
    newwindow=window.open(url,'{{title}}','height=500,width=700');
    if (window.focus) {newwindow.focus()}
    return false;
}
$(function(){
  $('.js-popup-link').click(function(e){
    e.preventDefault()
    $('#popup').dialog({modal: true}).dialog('open').load(this.href)
  })
})

//var = continent new 
$(function(){
  var $searchlink = $('#searchtoggl i');
  var $searchbar  = $('#searchbar');
  
  $(function(){
  var $searchlink = $('#searchtoggl i');
  var $searchbar  = $('#searchbar');
  
  $('#searchtoggl').on('click', function(e){
    e.preventDefault();
    
    if($(this).attr('id') == 'searchtoggl') {
      if(!$searchbar.is(":visible")) { 
        // if invisible we switch the icon to appear collapsable
        $searchlink.removeClass('fa-search').addClass('fa-search-minus');
      } else {
        // if visible we switch the icon to appear as a toggle
        $searchlink.removeClass('fa-search-minus').addClass('fa-search');
      }
      
      $searchbar.slideToggle(300, function(){
        // callback after search bar animation
      });
    }
  });
  });
});

$('#searchform').submit(function(e){
    e.preventDefault(); // stop form submission
  });
