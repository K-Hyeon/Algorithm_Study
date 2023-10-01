// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 < 0.9.0;



contract quiz5{    
    uint public a = 89;
    function multiplyValues() public view returns(uint) {
        uint b = a + 5;
        return b;
    }

}