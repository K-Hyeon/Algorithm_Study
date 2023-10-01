//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex3_3{
    uint public a = 3;
    uint public c = 7;
    function myFun(uint b) public{
        a = b;
    }
}