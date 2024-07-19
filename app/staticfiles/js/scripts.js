// Set a timeout to remove the messages after 15 seconds
setTimeout(function () {
  var messages = document.getElementById("messages");
  if (messages) {
    messages.remove();
  }
}, 15000);
