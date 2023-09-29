//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex2_9{
    bool a = true && true; // true
    bool b = true && false; // false
    bool c = false && false; // false
    bool d = true || true; // true
    bool e = true || false; // true
    bool f = false || false; // false
    bool g = !false; // true

    function logical() public view returns (bool, bool, bool, bool, bool, bool, bool){
        return(a, b, c, d, e, f, g);
    }
}