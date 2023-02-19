function submitComment() {
  // Get user inputs
  let name = document.getElementById("name").value;
  let comment = document.getElementById("comment").value;
  
  // Create new comment element
  let newComment = document.createElement("li");
  newComment.innerHTML = "<strong>" + name + ":</strong> " + comment;
  
  // Append new comment to comment list
  let commentList = document.getElementById("comment-list");
  commentList.appendChild(newComment);
  
  // Clear form inputs
  document.getElementById("name").value = "";
  document.getElementById("comment").value = "";
}