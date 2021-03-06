// Generated by CoffeeScript 1.4.0
(function() {
  var $cur_input, display_results, list_of_names, list_of_pics, search, search_old, setupInputHandlers;

  $cur_input = "";

  list_of_names = ["Justin Northworth", "Justin North", "Justice Northwood", "Justyn Northwerth", "Dustin Waldo", "Dustin Waldron", "Dusty Waldy", "Dustin Waldro"];

  list_of_pics = ["/media/interceptee_photos/doge.png", "/media/interceptee_photos/doge.png", "/media/interceptee_photos/doge.png", "/media/interceptee_photos/doge.png", "/media/interceptee_photos/38503_1144682394791_1729508_n.jpg", "/media/interceptee_photos/38503_1144682394791_1729508_n.jpg", "/media/interceptee_photos/38503_1144682394791_1729508_n.jpg", "/media/interceptee_photos/38503_1144682394791_1729508_n.jpg"];

  $(function() {
    var $items, $ui;
    $ui = $("#fuzzymatching-ui");
    setupInputHandlers($ui);
    $items = $ui.find('li');
    $ui.on("click", "li", function() {
      var $button, $this, name;
      $this = $(this);
      name = $this.children(".name").text();
      console.log(name);
      $cur_input.val(name);
      $button = $cur_input.parent().parent().find(".photo-upload-button");
      $button.prop("disabled", true);
      return $button.children().css("color", "grey");
    });
    return $ui.on("mouseover", "li", function() {
      return $ui.find("img").attr("src", list_of_pics[this.id]);
    });
  });

  setupInputHandlers = function($ui) {
    var $fuzzy_ui_eles;
    $fuzzy_ui_eles = $("[data-fuzzy-ui]");
    $fuzzy_ui_eles.focus(function() {
      var $this;
      $this = $(this);
      $cur_input = $this;
      $ui.css({
        top: $this.offset().top + $this.outerHeight() + 15,
        left: $this.offset().left
      });
      search($this.val(), $ui);
      $ui.find("img").attr("src", "");
      return $ui.show();
    });
    $(document).click(function(e) {
      if (!$(e.target).attr("data-fuzzy-ui")) {
        return $ui.hide();
      }
    });
    return $fuzzy_ui_eles.keyup(function(e) {
      var _ref;
      if ((_ref = e.which) !== 16 && _ref !== 17 && _ref !== 37 && _ref !== 38 && _ref !== 39 && _ref !== 40) {
        return search($(this).val(), $ui);
      }
    });
  };

  search = function(input, $ui) {
    return $.get($ui.data("ajax"), {
      name: input
    }, function(data) {
      var results;
      results = [];
      data.forEach(function(item) {
        return results.push({
          id: 1,
          name: item[0],
          score: item[1]
        });
      });
      return display_results(results, $ui);
    });
  };

  search_old = function(input, $ui) {
    var $button, f, item, result, results;
    $button = $cur_input.parent().parent().find(".photo-upload-button");
    $button.prop("disabled", false);
    $button.children().css("color", "");
    f = new Fuse(list_of_names, {
      includeScore: true
    });
    result = f.search(input);
    results = (function() {
      var _i, _len, _results;
      _results = [];
      for (_i = 0, _len = result.length; _i < _len; _i++) {
        item = result[_i];
        _results.push({
          id: item.item,
          name: list_of_names[item.item],
          score: item.score
        });
      }
      return _results;
    })();
    console.log(results);
    return display_results(results, $ui);
  };

  display_results = function(results, $ui) {
    var $li, $span, $ul, item, _i, _len, _ref, _results, _reslen;
    $ul = $ui.find("ul");
    $ul.children().remove();
    _reslen = results.length
    if (_reslen > 0) {
      _ref = results.slice(0, 100);
      _results = [];
      // calculate height of fuzzymatching div
      document.getElementById("fuzzymatching-ui").style.height = (parseInt(_reslen*20 + 25) + 'px');

      console.log("Length:", _ref.length);
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        item = _ref[_i];
        $span = $("<span>").addClass("name").text(item.name);
        $li = $("<li>").attr("id", item.id).text("(" + item.score + ")").append($span);
        _results.push($ul.append($li));
      }
      return _results;
    } else {
      $li = $("<li>").text("Type to search for matches");
      return $ul.append($li);
    }
  };

}).call(this);
