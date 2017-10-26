$(function () {
  
  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-organization").modal("show");
      },
      success: function (data) {
        $("#modal-organization .modal-content").html(data.html_form);
      }
    });
  };


  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#organization-table tbody").html(data.html_organization_list);
          $("#modal-organization").modal("hide");
        }
        else {
          $("#modal-organization .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create organization
  $(".js-create-organization").click(loadForm);
  $("#modal-organization").on("submit", ".js-organization-create-form", saveForm);

  // Update organization
  $("#organization-table").on("click", ".js-update-organization", loadForm);
  $("#modal-organization").on("submit", ".js-organization-update-form", saveForm);
  

});
