//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex2_13{
    uint constant a = 13;
    string constant b = "Hi";

    function plusA() public pure returns(uint){
        return a + 10;
    }

    /*
    function changeB() public{
        b = "Hello";  //에러 발생
    }
    */
}