//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex3_1{
    // internal
    uint a = 5;
    // public
    uint public b = 5;
    // 누구나 볼 수 있지만 바꿀 수 없다.
    uint public constant c = 5;
}