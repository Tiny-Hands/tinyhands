// Generated by CoffeeScript 1.4.0
(function() {
  var checkForCanon, toggleState;

  toggleState = function(ele) {
    return ele.toggleClass('btn-default btn-success disabled');
  };

  checkForCanon = function() {
    var form_age, form_name, form_phone;
    form_name = $('#form_name')[0];
    form_age = $('#form_age')[0];
    form_phone = $('#form_phone')[0];
    if (form_name.firstElementChild.innerHTML === window.person.name) {
      toggleState($(form_name.lastElementChild).children());
    }
    if (form_age.firstElementChild.innerHTML === window.person.age) {
      toggleState($(form_age.lastElementChild).children());
    }
    if (form_phone.firstElementChild.innerHTML === window.person.phone) {
      return toggleState($(form_phone.lastElementChild).children());
    }
  };

  $(function() {
    var $buttons;
    checkForCanon();
    $buttons = $('.input-group button');
    return $buttons.click(function() {
      var $button_to_uncheck, $matching_spans, $text, $text_span, $this;
      $this = $(this);
      $button_to_uncheck = $this.parents('.attribute').find('button.btn-success');
      toggleState($button_to_uncheck);
      $text_span = $this.parent().siblings().eq(0);
      $text = $text_span.text();
      $matching_spans = $this.parents('.attribute').find("span:contains(" + $text + ")");
      return toggleState($matching_spans.siblings().children('button'));
    });
  });

}).call(this);
