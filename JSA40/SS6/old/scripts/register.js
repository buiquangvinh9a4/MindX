const btn_submit = document.getElementById("btn_submit");

btn_submit.onclick = function() {
    const email = document.getElementById("email").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    let accounts = localStorage.getItem("accounts");
    accounts = accounts ? JSON.parse(accounts) : [];
    let isExits = accounts.some(acc => acc.username === username || acc.email === email); 
    if (isExits) {
        alert("Tài khoản đã tồn tại");
        
    } else {
        let account = {
            "username" : username,
            "password" : password,
            "email" : email
        }
        accounts.push(account)
        localStorage.setItem("accounts", JSON.stringify(accounts));
        alert("Đăng ký thành công!");
        
    }


}