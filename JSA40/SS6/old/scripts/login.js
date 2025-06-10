

document.getElementById("btn_signin").onclick = (event) => {
    event.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    
    let accounts = JSON.parse(localStorage.getItem("accounts"));

    let isExist = false, isCorrectPassword = false;
    for(const acc of accounts) {
        if (acc.email == email) {
            isExist = true;
            if (acc.password == password) {
                isCorrectPassword = true;
            }
            else {
                isCorrectPassword = false;
            }
            break;
        }
    }
    if (!isExist) {
        alert("Tài khoản không tồn tại")
    } else {
        if (isCorrectPassword) {
            alert("Đăng nhập thành công")
            window.location.href = "/index.html";

        } else {
            alert("Mật khẩu sai")
        }
    }
}
