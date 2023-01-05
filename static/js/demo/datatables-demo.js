// Call the dataTables jQuery plugin
//$(document).ready(function() {
//  $('#dataTable').DataTable();
//});


$('#dataTable').dataTable({
//your normal options
  "lengthMenu": [ [25, 50, -1], [25, 50, "All"] ],

  "oLanguage": { "sSearch": "" }

});
