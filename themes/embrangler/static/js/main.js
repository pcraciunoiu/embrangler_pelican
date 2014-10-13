(function() {
  function scrollEvent() {
    var $p = document.getElementById('promo');
    if (window && window.pageYOffset !== 0) {
      $p.className = 'notop';
    } else {
      $p.className = '';
    }
  }

  window.onscroll = scrollEvent;

  // Cross-browser addEventListener to a list of elements
  function addEventListenerList(list, event, fn) {
    for (var i = 0, len = list.length; i < len; i++) {
      list[i].addEventListener(event, fn, false);
  	  if (list[i].attachEvent) {
  	    list[i].attachEvent('onclick', promoClose);
  	  }
  	  if (list[i].addEventListener) {
  	    list[i].addEventListener('click', promoClose, false);
  	  }
    }
  }

  // Close button for the promo, in raw JavaScript
  var promo = document.getElementById('promo');
  var promoClose = function(e) {
  	if (e && e.preventDefault) {
  		e.preventDefault();
  	}
  	promo.style.display = 'none';
  };
  var closeButtons = document.querySelectorAll('#promo .close');
  addEventListenerList(closeButtons, 'click', promoClose);
})();
