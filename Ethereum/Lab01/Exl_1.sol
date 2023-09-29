//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract el_1{
    bool public d = true && false || true;
    bool public e = false && (true || false);
    bool public f = !true || !(false && true);

    bool public a = true||true||false;
    bool public b = true&&true&&false;
    bool public c = true||true&&false;

    bool public g = !(true && false) || (false || !true);

    bool public k = (true && !false) && !(false || true);

    function logical() public view returns (bool, bool, bool, bool, bool, bool, bool, bool){
        return(d, e, f, a, b, c, g, k);
    }
}