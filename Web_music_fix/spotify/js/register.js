const btn_submit1 = document.getElementById('btn_submit');

btn_submit1.onclick = function () {
    const username = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    let account = {
        "username": username, 
        "email": email,
        "password": password,
    };

    let listAccounts = localStorage.getItem("accounts");
    try {
        listAccounts = listAccounts ? JSON.parse(listAccounts) : [];
    } catch (error) {
        listAccounts = [];
    }

    listAccounts.push(account);
    localStorage.setItem("accounts", JSON.stringify(listAccounts));

    console.log("Danh sách tài khoản sau khi thêm:", listAccounts);
    console.log("Dữ liệu trong localStorage:", localStorage.getItem("accounts"));

    alert('Đăng ký thành công!');
};
