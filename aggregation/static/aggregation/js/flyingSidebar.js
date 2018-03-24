
$(document).ready(function(){
          //ф-я offset возвращает координаты отн-но начала страницы
var sidebartop = $('#sidebar').offset().top;

$(window).scroll(function(){

if( $(window).scrollTop() > sidebartop )
       { // ф-я scrollTop() возвращает величину вертикального скроллинга
         $('#sidebar').css({position: 'fixed', top: '30px'});
       }
   else
   {
           $('#sidebar').css({position: 'static'});
       }
   });

  })
