//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex2_8{
    bool a = 3 > 4; // false
    bool b = 3 < 4; // true
    bool c = 5 >= 2; // true
    bool d = 5 <=5; // true
    bool e = 3 == 2; // false
    bool f = 3 != 2; // true

    function comparison() public view returns (bool, bool, bool, bool, bool, bool){
        return(a, b, c, d, e, f);
    }
}