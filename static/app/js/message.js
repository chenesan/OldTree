var msg = document.getElementById("type");
var client = document.getElementById("example");
// var thinking_items = [];
// var thinking_count = 0;
function sendCB(result) {

}
msg.addEventListener("keypress", function(event){
  console.log('event')
    if(event.keyCode === 13){
      var thinking_item = document.createElement('div');
      client.innerHTML = msg.value;
      client.className = "box";
      var xhttp = new XMLHttpRequest();
      var csrftoken = Cookies.get('csrftoken');
      xhttp.open('POST', '/send_message/', true);
      xhttp.setRequestHeader('X-CSRFToken', csrftoken);
      xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
      xhttp.send('content=' + msg.value + '&csrfmiddlewaretoken=' + csrftoken);
      msg.value = '';
    }
})
