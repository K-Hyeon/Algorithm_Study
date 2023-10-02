//SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 < 0.9.0;

contract Ex4_13{
    function fun1() public pure returns(uint){
        uint result = 0;
        // 1+2+3+4+5+6+7+8+9
        for(uint a = 0; a < 10; ++a){
            if (a==0){
                break;
            }
            result += a;
        }
        return result;
    }
}