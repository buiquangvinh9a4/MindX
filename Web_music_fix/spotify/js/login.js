const btn_submit = document.getElementById("btn_submit")
    btn_submit.onclick = function() {
        const email = document.getElementById("email").value//Ctr+D x3
        const password = document.getElementById("password").value

        let listAccounts = localStorage.getItem("accounts");
        listAccounts = listAccounts ? JSON.parse(listAccounts) :[];
        console.log(listAccounts)

        let isEmailExist = false;//ktra su ton tai Email
        let isCorrectPassword = false;//ktra su hop le password

        for (const account of listAccounts) {
            if(account.email == email){
                isEmailExist = true;
                if(account.password == password)
                    isCorrectPassword = true;
                else{
                    isCorrectPassword = false;
                }
                break;
            }
        }
        console.log(isEmailExist, isCorrectPassword);
        if(isEmailExist==false){
            alert("Tai khoan ko ton tai")
        } else {
            if(isCorrectPassword==False){
                alert("Mat khau khong dung")
            } else {
                alert("Dang nhap thanh cong")
                window.location.href("index.html")
                
                

    
    
        }


    }
}