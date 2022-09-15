var form = document.getElementById("team_form");

form.addEventListener("submit", function (event) {
    event.preventDefault();
    var msg = "";
    msg += "Name: " + form.elements.namedItem("m_name").value + "\n";
    msg += "Email: " + form.elements.namedItem("g_email").value + "\n";
    msg += "Username: " + form.elements.namedItem("s_usrname").value + "\n";
    msg += "Tead Lead: " + form.elements.namedItem("team_lead").value + "\n";
    window.alert(msg);
});

document.addEventListener("keypress", function (event) {
    if (event.ctrlKey && event.key == "m") {
        document.body.classList.toggle("dark-mode");
    }
});

document.getElementById("c_pwd").addEventListener("focusout", function () {
    var pwd = form.elements.namedItem("pwd");
    var c_pwd = form.elements.namedItem("c_pwd");
    if (c_pwd.value != pwd.value) {
        window.alert("Confirm Password does not match");
        c_pwd.value = "";
    }
})