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
})();
