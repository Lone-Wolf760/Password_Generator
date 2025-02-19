// Function to copy password
function copyPassword() {
    var passwordField = document.getElementById("password");
    passwordField.select();
    document.execCommand("copy");
    alert("Password copied!");
}
