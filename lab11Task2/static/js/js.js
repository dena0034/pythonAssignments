$(document).ready(function() {
    $('#example').DataTable( {
        "order": [[ 0, "asc"  ]],
        "paging": false
    } );

} );


$(document).ready(function() {
          $('#studentList').change(function() {
            console.log(this.value);
            window.open(this.value);
          })
          console.log( "ready!" );
});