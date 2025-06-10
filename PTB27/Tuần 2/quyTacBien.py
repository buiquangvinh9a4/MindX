# đặt tên biến đúng
"""
    name, name_23, 23name, _name -> Đúng 
    @name, name!!, name 23    -> Sai 

    23name  1name -> Sai 
    _name   name_  -> Đúng 

    name vs NAME  -> hai biến khác nhau
    name vs Name   -> hai biến khác nhau
    a   vs  A      -> hai biến khác nhau 

    with, pass, for, if   -> sai 
    with_01,  pass_02,  for_   -> đúng 
"""
name = "Vinh"
name@ = "Vinh"