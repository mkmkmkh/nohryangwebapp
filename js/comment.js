function submitComment() {
  // Get user inputs
  let my_id = document.getElementById("my_id").value;
  let friend_id = document.getElementById("friend_id").value;
  let sns_name = document.getElementById("sns_name").value;
  // Create new comment element
  let newComment = document.createElement("li");
  newComment.innerHTML = "<h3><strong>" + sns_name + ":</strong> " + '내ID: ' +my_id+',친구ID: ' + friend_id + '</h3>';
  
  // Append new comment to comment list
  let commentList = document.getElementById("comment-list");
  commentList.appendChild(newComment);
  
  let my_idLabel
  let friend_idLabel
  let sns_nameLabel

  my_idLabel.innerHTML = "Enter your id:";
  friend_idLabel.innerHTML = "Enter friend's id:";
  sns_nameLabel.innerHTML = "Enter SNS name:";

  // Clear form inputs
  document.getElementById("my_id").value = "";
  document.getElementById("friend_id").value = "";
  document.getElementById("sns_name").value = "";
}

// Get a reference to the button element
