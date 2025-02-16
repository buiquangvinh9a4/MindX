let array = ["Messi", "Nguyễn Văn A",
            "Trần Thị B",
            "Hoàng Thanh C",
            "Messi"]

array.push("Messi")
array.splice(3, 1)

// for (let i = 0; i < array.length; i++) {
//     if (array[i] == "Messi") {
//         array[i] = "Ronaldo";
//     }
// }
viTriMessi = array.indexOf("Messi", 2)
console.log(viTriMessi)


for (let i = 0; i < array.length; i++) {
    console.log(array[i])
}

/*
    1 tài khoản ngân hàng:
    Thuộc tính:
    -  Số dư tài khoản
    -  Số tài khoản
    -  Tên chủ tài khoản

    Phương thức (hành động):
    -  Vay vốn
    -  Rút tiền
    -  Nạp tiền

*/

let account1 = {
    soDu : 150000,
    soTK :  "012345678",
    ten :  "Nguyễn Văn A"
}
let account2 = {
    soDu : 300000,
    soTK :  "112231223",
    ten :  "Trần Thị B"
}

let lstAccount = [account1, account2]

// Hiển thị ra tên của các chủ tài khoản trong ngân hàng
for (let i = 0; i < lstAccount.length; i++)
{
    console.log(lstAccount[i]["ten"])
}

