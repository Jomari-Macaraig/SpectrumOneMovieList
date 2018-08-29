(function() {
  function getCookie(name) {
    var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
    return cookieValue;
  }
  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
  var csrftoken = getCookie('csrftoken');
  var movieId = null;
  $(".deleteButtons").click(function () {
    movieId = $(this).attr("data-id");
  });

  $("#deleteButton").click(function () {
    $.post("/movie/" + movieId + "/delete",
      function (data, status) {
        location.reload();
      }
    )
  });

  $(".likeButtons").click(function () {
    var element = $(this)
    var likes = parseInt(element.attr("data-like")) + 1
    $.ajax({
      url: "/movie/api/" + element.attr("data-id") + "/update",
      type: "PATCH",
      data: {"like": likes},
      success: function (result) {
        element.attr("data-like", likes);
        element.find("span").find("span").text(likes)
      }
    })
  });
})();
