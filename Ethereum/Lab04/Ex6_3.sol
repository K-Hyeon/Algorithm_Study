//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex6_3{
    //uint[] public immutable arr;
    uint public constant num1 = 5;
    uint public immutable num2;

    constructor(uint _num){
        num2 = _num;
    }

    /*
    fuction change() public pure returns(uint){
        num2 = 10;
    }
    */
}