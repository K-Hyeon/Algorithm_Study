//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex4_7{
    function fun1() public pure returns(uint){
        uint result = 0;
        uint a = 3;
        // 3+2+1
        while(a>0){
            result += a;
            --a;
        }
        return result;
    }
}