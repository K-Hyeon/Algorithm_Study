//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex2_12{
    uint a = 2 + 3 * 2; // 8
    uint b = (2 + 3) * 2; // 10
    bool c = !true == false; // true

    function results() public view returns(uint, uint, bool){
        return (a, b, c);
    }
}