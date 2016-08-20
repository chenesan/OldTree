var msg = document.getElementById("type");
var client = document.getElementById("example");
// var thinking_items = [];
// var thinking_count = 0;
function sendxhr(value) {
  var xhttp = new XMLHttpRequest();
  var csrftoken = Cookies.get('csrftoken');
  xhttp.open('POST', '/send_message/', true);
  xhttp.setRequestHeader('X-CSRFToken', csrftoken);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send('content=' + value + '&csrfmiddlewaretoken=' + csrftoken);
}

msg.addEventListener("keypress", function(event){
  console.log('event')
    if(event.keyCode === 13){
      var thinking_item = document.createElement('div');
      client.innerHTML = msg.value;
      client.className = "box";
      msg.value = '';
    }
})
